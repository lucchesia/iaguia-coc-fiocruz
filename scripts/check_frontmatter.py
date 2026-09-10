#!/usr/bin/env python3
"""
Valida o frontmatter YAML dos verbetes de ferramentas (docs/ferramentas/*.md).

Verifica presenca de campos obrigatorios e, para os campos que tem vocabulario
fechado, se o valor esta dentro dele. Nao corrige nada: so mede e relata.

Uso: python scripts/check_frontmatter.py
"""
import glob
import os
import re
import sys

import yaml

DOCS_DIR = "docs/ferramentas"
IGNORE = {"_template.md", "index.md"}

REQUIRED_FIELDS = [
    "title", "slug", "entry_type", "tool_type", "category", "tags",
    "systems", "curva_aprendizado", "integrations", "alternatives",
    "official_site", "documentation", "status", "reviewed", "last_reviewed",
]

VOCAB = {
    "entry_type": {"ferramenta"},
    "tool_type": {"aplicativo", "serviço web", "biblioteca", "modelo",
                  "extensão", "protocolo"},
    "curva_aprendizado": {"baixa", "baixa a moderada", "moderada",
                          "moderada a alta", "alta"},
    "status": {"publicado", "rascunho"},
    "source_model": {"aberto", "proprietário", "misto", "não identificado"},
    "access_model": {"gratuito", "gratuito com limites", "freemium", "pago",
                     "licença acadêmica", "acesso institucional"},
    "tool_status": {"ativa", "estável", "em desenvolvimento", "legada"},
    "software_license": {"MIT", "GPL-2.0", "GPL-3.0", "LGPL-2.1", "LGPL-3.0",
                         "AGPL-3.0", "Apache-2.0", "BSD-3-Clause", "EUPL-1.2",
                         "MPL-2.0", "proprietária"},
}
CAVEATS = {"documentação de uso limitada", "manutenção reduzida",
           "licença não identificada", "requer infraestrutura própria",
           "requer conhecimentos técnicos", "envia dados para serviço externo"}

# Opcionais nesta versão: ausência não é erro, presença é validada. Isso é o
# que permite rodar o validador antes e depois da migração da tarefa 4.
# Documenta o contrato dos campos; a validação em si vem de REQUIRED_FIELDS,
# VOCAB, LIST_FIELDS e EMPTY_ALLOWED — este conjunto não é lido pelo código.
OPTIONAL_FIELDS = {
    "source_model", "access_model", "tool_status", "software_license",
    "caveats", "learning_resources", "academic_use",
}
LIST_FIELDS = {"caveats", "learning_resources", "academic_use"}

# Campo de curadoria que pode estar presente e vazio: vazio é deliberado e
# significa "ainda não classificado". O vocabulário só é cobrado quando há valor.
# software_license fica de fora de propósito: quando a licença não é conhecida o
# campo fica AUSENTE, nunca vazio — placeholder vazio ali contradiz o caveat
# "licença não identificada", que só vale quando a ausência foi verificada.
EMPTY_ALLOWED = {"tool_status"}

LAST_REVIEWED_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def iter_files():
    for path in sorted(glob.glob(os.path.join(DOCS_DIR, "*.md"))):
        if os.path.basename(path) in IGNORE:
            continue
        yield path.replace(os.sep, "/")


def load_frontmatter(path):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    m = FRONTMATTER_RE.match(content)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def is_empty(value):
    return value is None or (isinstance(value, str) and not value.strip())


def check_file(path, problems):
    data = load_frontmatter(path)
    if not isinstance(data, dict):
        problems.append(f"{path}: frontmatter: ausente ou YAML inválido")
        return None

    for field in REQUIRED_FIELDS:
        if field not in data:
            problems.append(f"{path}: {field}: campo obrigatório ausente")

    for field, allowed in VOCAB.items():
        if field not in data:
            continue
        if field in EMPTY_ALLOWED and is_empty(data[field]):
            continue
        if data[field] not in allowed:
            problems.append(
                f"{path}: {field}: valor {data[field]!r} fora do vocabulário {sorted(allowed)}"
            )

    for field in LIST_FIELDS:
        if field not in data:
            continue
        value = data[field]
        if not isinstance(value, list):
            problems.append(
                f"{path}: {field}: deveria ser lista, veio {type(value).__name__}"
            )
            continue
        if field == "caveats":
            for item in value:
                if item not in CAVEATS:
                    problems.append(
                        f"{path}: caveats: item {item!r} fora do vocabulário fechado"
                    )

    if "last_reviewed" in data and data["last_reviewed"] not in (None, ""):
        value = str(data["last_reviewed"])
        if not LAST_REVIEWED_RE.match(value):
            problems.append(
                f"{path}: last_reviewed: valor {value!r} não casa com AAAA-MM-DD"
            )

    return data


def main():
    problems = []
    total = 0
    sem_tool_status = 0
    for path in iter_files():
        total += 1
        data = check_file(path, problems)
        if not isinstance(data, dict) or is_empty(data.get("tool_status")):
            sem_tool_status += 1

    for line in problems:
        print(line)

    # Informativo: mede o avanço da curadoria, não é problema e não afeta o
    # código de saída.
    print(f">> curadoria: {sem_tool_status} de {total} verbetes ainda sem tool_status")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
