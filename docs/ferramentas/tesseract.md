---
title: "Tesseract"
slug: "tesseract"

entry_type: "ferramenta"
tool_type: "biblioteca"

category: "transcrição"

tags:
  - OCR
  - linha de comando
  - open source
  - uso offline
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: Apache-2.0
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada"
integrations:
  - Python
  - OCRmyPDF
  - Leptonica

concepts:
  - reconhecimento-optico-de-caracteres
alternatives:
  - Gamera
  - ABBYY FineReader
  - Google Document AI

official_site: "https://github.com/tesseract-ocr/tesseract"
documentation: "https://tesseract-ocr.github.io/tessdoc/"
forum: "não disponível"
repository: "https://github.com/tesseract-ocr/tesseract"

caveats:
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Tesseract é um motor de [reconhecimento óptico de caracteres (OCR)](../conceitos/reconhecimento-optico-de-caracteres.md) gratuito e de código aberto, que funciona tanto como programa de linha de comando quanto como biblioteca (`libtesseract`) para ser usado dentro de outros programas. Foi desenvolvido originalmente pela HP em 1985, disponibilizado como código aberto em 2005 e recebeu grandes melhorias sob a Google entre 2006 e 2017. Hoje é mantido pela comunidade, com suporte a mais de 100 idiomas.

## Para que serve

- Extrair texto de imagens de documentos digitalizados (páginas escaneadas, fotos de documentos, PDFs de imagem)
- Reconhecer texto impresso em mais de 100 idiomas, incluindo português
- Servir de base para outras ferramentas de OCR, como o [OCRmyPDF](ocrmypdf.md) (que usa o Tesseract para adicionar uma camada de texto pesquisável a PDFs escaneados)
- Ser incorporado como biblioteca dentro de programas escritos em Python, C++ e outras linguagens, via wrappers como o pytesseract

## Exemplo de uso

Um grupo de pesquisa digitalizou centenas de páginas de jornais impressos do início do século XX e quer torná-las pesquisáveis por palavra-chave. Um membro da equipe com alguma familiaridade técnica instala o Tesseract e, usando um script simples em Python com o pytesseract, processa o lote de imagens em sequência, gerando um arquivo de texto para cada página — texto que depois é usado para indexar o acervo digital.

## Quando pode não ser a melhor opção

- Se você não tem nenhuma familiaridade com linha de comando ou programação: o Tesseract não tem interface gráfica própria; existem programas de terceiros que usam o Tesseract por trás de uma interface mais simples, mas o motor em si exige algum conforto técnico
- Se o material for manuscrito: o Tesseract foi desenhado para texto impresso — para manuscritos (HTR), ferramentas como o [Transkribus](transkribus.md) ou o [eScriptorium](escriptorium.md) são mais adequadas
- Se o documento tiver layout complexo (colunas, tabelas, texto sobreposto a imagens) sem pré-processamento: a qualidade do reconhecimento pode cair bastante
- Se você precisa de uma solução pronta, sem instalação, para poucos documentos: serviços web ou aplicativos com interface gráfica podem ser mais práticos

## Tipo de acesso

Totalmente gratuito e de código aberto (licença Apache 2.0).

## Sistemas em que roda

Windows, macOS e Linux — via pacotes pré-compilados ou compilação a partir do código-fonte.

## Integrações

- Python, por meio do wrapper pytesseract, entre outras linguagens com wrappers disponíveis (C/C++ nativamente)
- [OCRmyPDF](ocrmypdf.md) (ferramenta que usa o Tesseract para gerar PDFs pesquisáveis a partir de digitalizações)
- Leptonica (biblioteca de processamento de imagens usada internamente pelo Tesseract)

## Alternativas

- [Gamera](gamera.md) (arcabouço mais flexível e mais difícil de usar, voltado a documentos com características visuais muito específicas)
- ABBYY FineReader (proprietário, pago, referência em OCR de textos impressos)
- Google Document AI (serviço pago por uso, alta capacidade, requer configuração técnica)

## Aprenda a usar

### Onde encontrar

- Site oficial / repositório: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Documentação: [https://tesseract-ocr.github.io/tessdoc/](https://tesseract-ocr.github.io/tessdoc/)

### Material de apoio

O Tesseract é maduro e tem ciclo de desenvolvimento lento, então material antigo continua
válido. A documentação oficial cobre o comando básico e as opções de idioma e de segmentação
de página. A lição do Programming Historian é revisada por pares e aplica o programa a um
documento de arquivo real, antes de comparar a abordagem com a do Google Vision.

- "Command Line Usage", documentação oficial:
  [https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html)
- GRIBOMONT, Isabelle. "OCR with Google Vision API and Tesseract", *Programming Historian*,
  2023:
  [https://programminghistorian.org/en/lessons/ocr-with-google-vision-and-tesseract](https://programminghistorian.org/en/lessons/ocr-with-google-vision-and-tesseract)

## Uso em pesquisa e ensino

Bibliotecárias da Western University compararam o desempenho de vários programas de OCR sobre
documentos históricos digitalizados, entre eles o jornal *The Voice of the Bondsman* e
relatórios institucionais da própria universidade. O Tesseract saiu bem no reconhecimento de
tabelas, um ponto em que os concorrentes falharam. O artigo serve como referência de decisão
para quem precisa escolher um programa de OCR para um acervo específico.

- OLSON, Leanne; BERRY, Veronica. Digitization decisions: comparing OCR software for librarian
  and archivist use. *The Code4Lib Journal*, n. 52, 2021:
  [https://journal.code4lib.org/articles/16132](https://journal.code4lib.org/articles/16132)

## Observações

O Tesseract é considerado um dos motores de OCR de código aberto mais usados no mundo, e serve de base técnica para diversas outras ferramentas mencionadas neste glossário (Arkindex e [OCRmyPDF](ocrmypdf.md), por exemplo, dependem dele ou de motores comparáveis). É voltado principalmente a texto impresso — para manuscritos históricos, a família de ferramentas de HTR (Transkribus, [eScriptorium](escriptorium.md), Gamera) é mais indicada.

