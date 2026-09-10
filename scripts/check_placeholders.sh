#!/usr/bin/env bash
# Falha (exit 1) se encontrar tokens editoriais de bastidor em docs/.
# Uso: bash scripts/check_placeholders.sh
set -uo pipefail
# Os marcadores REF, VERIFICAR e CONFIRMAR são pegos tanto puros, "[REF]", quanto com
# indicação depois dos dois-pontos, "[REF: manuais da Fiocruz]". Os dois tokens da citação
# bibliográfica, "[inserir ...]" e "[data de acesso]", entram no mesmo conjunto.
PATTERN='\[(REF|VERIFICAR|CONFIRMAR)(:[^]]*)?\]|\[inserir [^]]*\]|\[data de acesso\]|A redigir'
if grep -rnE "$PATTERN" docs/ --include='*.md'; then
  echo ">> Tokens editoriais encontrados acima. Corrigir antes de publicar."
  exit 1
else
  echo ">> OK: nenhum token editorial em docs/."
fi
