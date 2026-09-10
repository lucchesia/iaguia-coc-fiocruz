---
title: "eScriptorium"
slug: "escriptorium"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "transcrição"

tags:
  - transcrição automática
  - transcrição manual
  - OCR
  - anotação de fontes
  - open source
aliases: []

source_model: aberto
software_license: MIT
access_model: gratuito

systems:
  - Web
  - Linux
  - macOS
curva_aprendizado: "moderada a alta"
integrations:
  - Kraken
  - IIIF
  - ALTO XML

concepts:
  - reconhecimento-optico-de-caracteres
  - reconhecimento-de-texto-manuscrito
alternatives:
  - Transkribus
  - Arkindex
  - Kraken

official_site: "https://escriptorium.eu/"
documentation: "https://escriptorium.readthedocs.io/"
forum: "não disponível"
repository: "https://gitlab.com/scripta/escriptorium"

caveats:
  - requer infraestrutura própria
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

eScriptorium é uma plataforma gratuita e de código aberto para segmentação e transcrição de manuscritos, livros impressos históricos e documentos de arquivo. Combina [OCR](../conceitos/reconhecimento-optico-de-caracteres.md) (texto impresso) e [HTR](../conceitos/reconhecimento-de-texto-manuscrito.md) — reconhecimento de texto manuscrito —, usando por baixo dos panos o motor Kraken. Foi criada em 2018 no âmbito do programa de pesquisa Scripta PSL, na Université PSL (Paris), e hoje é mantida em parceria entre a École Pratique des Hautes Études (EPHE) e o projeto ALMAnaCH do Inria (ambos franceses).

## Para que serve

- Segmentar e transcrever manuscritos e documentos impressos históricos, incluindo escritas em árabe, hebraico, grego, copta e outros sistemas de escrita
- Treinar modelos de reconhecimento próprios para uma caligrafia, período ou coleção específica, num fluxo "humano no circuito": a pessoa transcreve algumas páginas manualmente, o sistema treina um [modelo](../conceitos/modelo.md), gera previsões no restante e a pessoa revisa
- Importar imagens compatíveis com o padrão IIIF, comum em bibliotecas e acervos digitais
- Exportar dados estruturados nos formatos ALTO XML e PAGE XML, usados em projetos de edição digital e preservação

## Exemplo de uso

Uma equipe de pesquisa em história medieval tem acesso a uma instância do eScriptorium mantida pela biblioteca da própria universidade. Eles fazem upload de imagens de um cartulário do século XIII (importadas diretamente via IIIF do acervo digital da instituição), transcrevem manualmente as primeiras páginas para treinar um modelo específico para aquela caligrafia, e usam o modelo treinado para acelerar a transcrição do restante do documento, revisando o resultado depois.

## Quando pode não ser a melhor opção

- Se você é uma pessoa pesquisadora individual sem acesso a uma instância institucional: diferente do [Transkribus](transkribus.md), o eScriptorium não tem uma plataforma pública única de acesso imediato — é preciso instalar em servidor próprio (requer Linux ou macOS, Docker e, idealmente, placa de vídeo Nvidia) ou encontrar uma instância já mantida por uma biblioteca ou departamento de humanidades digitais
- Se o documento for impresso e não manuscrito: ferramentas de OCR mais simples, como o [Tesseract](tesseract.md), podem ser suficientes e mais fáceis de configurar
- Se você precisa de suporte comercial dedicado ou uma plataforma hospedada com um único login: o [Transkribus](transkribus.md) ou o [Arkindex](arkindex.md) (versão comercial hospedada) resolvem isso de forma mais direta

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MIT). Não há custo de licença, mas o acesso depende de auto-hospedagem (requer infraestrutura própria) ou de uma instância mantida por uma instituição parceira.

## Sistemas em que roda

Acessado por navegador web. A hospedagem própria requer um servidor Linux ou macOS, com pelo menos 8 GB de RAM (16 GB ou mais recomendado para treinar modelos) e, opcionalmente, uma GPU Nvidia para acelerar o treinamento.

## Integrações

- Kraken (motor de OCR/HTR usado internamente)
- IIIF (International Image Interoperability Framework): importação de imagens de acervos digitais compatíveis
- ALTO XML e PAGE XML: formatos de exportação para projetos de edição digital

## Alternativas

- [Transkribus](transkribus.md) (plataforma com login único e créditos, mais acessível para uso individual imediato)
- [Arkindex](arkindex.md) (também da família de plataformas HTR de nível institucional, com versão comercial hospedada)
- Kraken (o motor por trás do eScriptorium, usável isoladamente por linha de comando)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://escriptorium.eu/](https://escriptorium.eu/)
- Documentação: [https://escriptorium.readthedocs.io/](https://escriptorium.readthedocs.io/)
- Repositório: [https://gitlab.com/scripta/escriptorium](https://gitlab.com/scripta/escriptorium)

### Material de apoio

Os dois materiais abaixo são abertos e detalhados. Praticar o que eles ensinam exige acesso a
uma instância, seja institucional, seja instalada por você, condição que este verbete
registra em "Quando pode não ser a melhor opção". O guia rápido oficial percorre o fluxo
inteiro, da criação do projeto à correção da transcrição. O guia da Universidade de Mannheim cobre o ciclo de
treinamento de um modelo, em passos numerados.

- "Quick-start", documentação oficial:
  [https://escriptorium.readthedocs.io/en/latest/quick-start/](https://escriptorium.readthedocs.io/en/latest/quick-start/)
- KAMLAH, Jan; SCHMIDT, Thomas. "Training with eScriptorium (a step-by-step guide)",
  Universitätsbibliothek Mannheim, v. 1.0, 2024:
  [https://ub-mannheim.github.io/eScriptorium_Dokumentation/Training-with-eScriptorium-EN.html](https://ub-mannheim.github.io/eScriptorium_Dokumentation/Training-with-eScriptorium-EN.html)

## Uso em pesquisa e ensino

A ferramenta nasceu dentro de um projeto de pesquisa e é usada em projetos de edição de fontes
manuscritas. O artigo dos criadores descreve o eScriptorium como ambiente virtual de pesquisa
para culturas manuscritas. O projeto DAHN documenta o uso concreto: segmentação, transcrição e
correção pós-OCR do corpus de correspondência de Paul d'Estournelles de Constant.

- STOKES, Peter A. et al. The eScriptorium VRE for manuscript cultures. *Classics@ Journal*,
  v. 18, n. 1, 2021:
  [https://classics-at.chs.harvard.edu/classics18-stokes-kiessling-stokl-ben-ezra-tissot-gargem/](https://classics-at.chs.harvard.edu/classics18-stokes-kiessling-stokl-ben-ezra-tissot-gargem/)
- Projeto DAHN (Universidade de Le Mans, EHESS e Inria), documentação de metodologia "How to
  do a transcription (with eScriptorium)":
  [https://github.com/FloChiff/DAHNProject/blob/master/Project%20development/Documentation/How%20to%20do%20a%20transcription%20(with%20eScriptorium).md](https://github.com/FloChiff/DAHNProject/blob/master/Project%20development/Documentation/How%20to%20do%20a%20transcription%20(with%20eScriptorium).md)

## Observações

O eScriptorium é referência acadêmica em HTR de código aberto, especialmente em projetos de humanidades digitais europeus ligados a manuscritos medievais e escritas não latinas. Por ser descentralizado — sem uma única plataforma pública central —, o primeiro passo prático para uma pessoa pesquisadora interessada costuma ser verificar se a própria universidade, biblioteca ou departamento de humanidades digitais já mantém uma instância, antes de considerar hospedar uma própria.

