---
title: "Optical Character Recognition"
title_pt: "Reconhecimento Óptico de Caracteres"
slug: "reconhecimento-optico-de-caracteres"

entry_type: "conceito"
concept_type: "técnica"

category: "linguagem, documentos, imagem e áudio"

tags:
  - inteligência artificial
  - aprendizado de máquina

aliases:
  - "OCR"
  - "optical character recognition"

related_terms:
  - visao-computacional
  - reconhecimento-de-texto-manuscrito
prerequisites:
  - visao-computacional

references:
  - title: "OCR — Glossary | Federal Agencies Digitization Guidelines Initiative (FADGI)"
    url: "https://www.digitizationguidelines.gov/term.php?term=OCR"
    type: "glossário institucional (agências federais dos EUA)"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Reconhecimento Óptico de Caracteres

## O que é

OCR (Reconhecimento Óptico de Caracteres, do inglês *Optical Character Recognition*) é a tecnologia que converte imagens de texto impresso ou datilografado — como a foto ou o escaneamento de uma página — em texto digital editável e pesquisável. Segundo o glossário da Federal Agencies Digitization Guidelines Initiative (iniciativa de agências federais dos Estados Unidos voltada a diretrizes de digitalização, usada como referência por arquivos e bibliotecas), OCR "é uma tecnologia que permite que pontos ou pixels representando caracteres gerados mecanicamente numa imagem raster sejam convertidos em texto digitalmente codificado".

## Por que isso importa?

OCR é uma etapa fundamental na digitalização de acervos: sem ele, documentos digitalizados permanecem como imagens — pesquisáveis apenas por metadados descritivos, não pelo próprio conteúdo do texto. Entender os limites do OCR ajuda a avaliar a qualidade de uma coleção digitalizada: fontes tipográficas incomuns, papel danificado, colunas complexas ou línguas pouco comuns podem produzir um texto reconhecido cheio de erros, exigindo revisão manual antes de qualquer análise textual automatizada.

## Exemplo

Uma pesquisadora que digitaliza um jornal histórico usa uma ferramenta como o [Tesseract](../ferramentas/tesseract.md) ou o [OCRmyPDF](../ferramentas/ocrmypdf.md) para aplicar OCR às páginas escaneadas, transformando as imagens em um PDF pesquisável — o que permite localizar rapidamente todas as menções a um nome ou termo específico ao longo de anos de edições, sem precisar ler cada página manualmente.

## Não confunda com

OCR não é sinônimo de HTR (Reconhecimento de Texto Manuscrito): OCR é voltado a texto impresso ou datilografado, com formas de caracteres relativamente padronizadas; HTR é uma tecnologia relacionada, mas distinta, voltada especificamente a caligrafia manuscrita, que varia muito mais de pessoa para pessoa. Também não é sinônimo de visão computacional em geral: OCR é uma aplicação específica de visão computacional, focada em reconhecer caracteres, não objetos ou cenas em geral.

## Termos relacionados

## Referências

- Federal Agencies Digitization Guidelines Initiative. *OCR — Glossary*.
  [digitizationguidelines.gov/term.php?term=OCR](https://www.digitizationguidelines.gov/term.php?term=OCR)
