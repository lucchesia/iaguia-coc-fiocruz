---
title: "OCRmyPDF"
slug: "ocrmypdf"

entry_type: "ferramenta"
tool_type: "biblioteca"

category: "transcrição"

tags:
  - OCR
  - organização de PDFs
  - linha de comando
  - open source
  - uso offline
aliases: []

source_model: aberto
software_license: MPL-2.0
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada"
integrations:
  - Tesseract
  - Python
  - Ghostscript

concepts:
  - reconhecimento-optico-de-caracteres
alternatives:
  - Adobe Acrobat
  - ABBYY FineReader
  - Google Document AI

official_site: "https://github.com/ocrmypdf/OCRmyPDF"
documentation: "https://ocrmypdf.readthedocs.io/"
forum: "https://github.com/ocrmypdf/OCRmyPDF/discussions"
repository: "https://github.com/ocrmypdf/OCRmyPDF"

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

OCRmyPDF é uma ferramenta gratuita e de código aberto que adiciona uma camada de texto pesquisável a arquivos PDF escaneados, sem alterar a aparência visual do documento original. Por trás dela, usa o [Tesseract](tesseract.md) para o reconhecimento de texto propriamente dito. Foi criada por James R. Barlow e é mantida pela comunidade, com uso testado em milhões de PDFs.

## Para que serve

- Transformar um PDF que é só uma sequência de imagens escaneadas em um PDF onde o texto pode ser selecionado, copiado e buscado
- Gerar PDFs no formato PDF/A-2b, adequado para preservação digital de longo prazo
- Corrigir automaticamente páginas escaneadas tortas (deskew) e limpar a imagem antes do reconhecimento
- Processar arquivos com centenas ou milhares de páginas de uma vez, por linha de comando
- Lidar com PDFs "híbridos", que já têm algum texto digital misturado com páginas de imagem

## Exemplo de uso

Uma equipe de um arquivo institucional digitalizou uma coleção de processos judiciais antigos e gerou PDFs de imagem — que não podem ser buscados por palavra-chave. Um técnico da equipe usa o OCRmyPDF em lote, processando a pasta inteira por um único comando, e gera uma nova versão dos PDFs com camada de texto pesquisável, pronta para ser indexada no sistema de busca do acervo digital.

## Quando pode não ser a melhor opção

- Se o documento for manuscrito: o OCRmyPDF depende do Tesseract, que reconhece texto impresso, não caligrafia — para manuscritos, use ferramentas de HTR como [Transkribus](transkribus.md)
- Se você não tem nenhuma familiaridade com linha de comando: não há interface gráfica própria; é preciso rodar comandos no terminal (ou usar uma versão empacotada em Docker)
- Se você só tem um ou dois arquivos para processar, sem repetição: um serviço web ou o recurso de [OCR](../conceitos/reconhecimento-optico-de-caracteres.md) embutido em leitores de PDF comerciais pode ser mais rápido de usar pontualmente
- A precisão do reconhecimento depende inteiramente da qualidade do Tesseract e da digitalização original — documentos de baixa qualidade produzem resultados piores

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MPL 2.0).

## Sistemas em que roda

Windows, macOS e Linux (Debian, Ubuntu, Fedora, Arch, entre outros), além de FreeBSD e OpenBSD. Também disponível como imagem Docker, útil para quem quer evitar instalar as dependências manualmente.

## Integrações

- [Tesseract](tesseract.md) (motor de OCR usado internamente; é uma dependência obrigatória)
- Python (linguagem em que o OCRmyPDF é escrito, também disponível como biblioteca)
- Ghostscript ou pypdfium2 (usados para processar/rasterizar as páginas do PDF)

## Alternativas

- Adobe Acrobat (proprietário, pago, tem OCR embutido com interface gráfica)
- ABBYY FineReader (proprietário, pago, referência em qualidade de OCR)
- Google Document AI (serviço pago por uso, alta capacidade, requer configuração técnica)

## Aprenda a usar

### Onde encontrar

- Repositório: [https://github.com/ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)
- Documentação: [https://ocrmypdf.readthedocs.io/](https://ocrmypdf.readthedocs.io/)
- Discussões da comunidade: [https://github.com/ocrmypdf/OCRmyPDF/discussions](https://github.com/ocrmypdf/OCRmyPDF/discussions)

## Observações

O OCRmyPDF é especialmente útil em projetos de digitalização de acervos que precisam tornar grandes volumes de PDFs escaneados pesquisáveis, sem depender de serviços comerciais pagos. Por gerar PDFs no formato PDF/A-2b (padrão de preservação digital), também é uma opção relevante para instituições preocupadas com a durabilidade dos arquivos digitais a longo prazo, não só com a busca por palavra-chave.

