"""MkDocs build hook: gera docs/assets/data/entries.json a partir do frontmatter
de docs/ferramentas/*.md e docs/conceitos/*.md, para alimentar o buscador por
facetas em docs/encontrar.md (docs/javascripts/facet-finder.js).

Não altera nenhum verbete — só lê os campos já existentes no YAML e no corpo.
"""

import json
import os
import re

import yaml

SKIP_FILES = {"_template.md", "index.md"}
EXCERPT_LIMIT = 160


def _read_frontmatter(path):
    text = open(path, encoding="utf-8").read()
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}, ""
    fm = yaml.safe_load(parts[1]) or {}
    return fm, parts[2]


def _excerpt(body):
    match = re.search(r"^## O que é\s*\n+(.+?)(\n##|\Z)", body, re.S | re.M)
    if not match:
        return ""
    paragraph = match.group(1).strip().split("\n\n")[0]
    paragraph = re.sub(r"\s+", " ", paragraph).strip()
    paragraph = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", paragraph)
    if len(paragraph) > EXCERPT_LIMIT:
        paragraph = paragraph[:EXCERPT_LIMIT].rsplit(" ", 1)[0] + "…"
    return paragraph


def _collect(docs_dir, subdir, entry_type):
    entries = []
    folder = os.path.join(docs_dir, subdir)
    if not os.path.isdir(folder):
        return entries
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith(".md") or fname in SKIP_FILES:
            continue
        fm, body = _read_frontmatter(os.path.join(folder, fname))
        slug = fm.get("slug")
        if not slug:
            continue
        entries.append(
            {
                "slug": slug,
                "title": fm.get("title_pt") or fm.get("title"),
                "entry_type": entry_type,
                "url": f"{subdir}/{slug}/",
                "category": fm.get("category"),
                "tags": fm.get("tags") or [],
                "subtype": fm.get("tool_type") or fm.get("concept_type"),
                "license": fm.get("license"),
                "cost": fm.get("cost"),
                "excerpt": _excerpt(body),
            }
        )
    return entries


def on_post_build(config, **kwargs):
    docs_dir = config["docs_dir"]
    site_dir = config["site_dir"]
    entries = _collect(docs_dir, "ferramentas", "ferramenta") + _collect(
        docs_dir, "conceitos", "conceito"
    )
    out_dir = os.path.join(site_dir, "assets", "data")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entries.json"), "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False)
