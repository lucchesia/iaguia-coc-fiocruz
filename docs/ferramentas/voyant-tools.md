---
title: "Voyant Tools"
slug: "voyant-tools"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "análise de texto"

tags:
  - análise de texto
  - open source
  - sem código
  - uso offline
aliases: []

source_model: aberto
software_license: GPL-3.0
access_model: gratuito

systems:
  - Web
  - Windows
  - macOS
  - Linux
curva_aprendizado: "baixa a moderada"
integrations:
  - Spyral

concepts:
  - processamento-de-linguagem-natural
alternatives:
  - AntConc
  - spaCy
  - Orange Data Mining

official_site: "https://voyant-tools.info/"
documentation: "https://voyant-tools.org/docs/"
forum: "https://github.com/voyanttools/Voyant/discussions"
repository: "https://github.com/voyanttools/Voyant"

caveats:
  - envia dados para serviço externo
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Voyant Tools é um conjunto gratuito e de código aberto de ferramentas de análise textual que rodam direto no navegador, sem exigir instalação nem programação. Foi criado pelos pesquisadores Stéfan Sinclair (McGill) e Geoffrey Rockwell (Universidade de Alberta) e é mantido pelo Voyant Consortium. É uma das ferramentas mais usadas para introduzir "leitura distante" (distant reading) e análise quantitativa de texto em humanidades digitais.

## Para que serve

- Gerar nuvens de palavras (Cirrus) para visualizar rapidamente os termos mais frequentes de um texto ou corpus
- Mostrar como a frequência de termos muda ao longo de um documento ou entre documentos de um corpus (Trends)
- Explorar palavras-chave em contexto (Contexts/KWIC), vendo cada ocorrência de um termo cercada pelo trecho onde aparece
- Analisar correlações entre a frequência de diferentes termos (Correlations)
- Combinar dezenas de outras visualizações (nuvens, redes de termos, mapas de dispersão, gráficos de fluxo) num painel único e interativo
- Importar textos colando diretamente, enviando arquivos (TXT, PDF, DOCX, HTML, XML, entre outros) ou apontando para URLs

## Exemplo de uso

Uma pesquisadora quer comparar o vocabulário usado em décadas diferentes de um mesmo jornal histórico digitalizado. Ela reúne os arquivos de texto por década em um corpus e carrega tudo no Voyant Tools. Usando a ferramenta Trends, observa como certos termos ganham ou perdem frequência ao longo do tempo, e usa a ferramenta Contexts para ler rapidamente os trechos em que um termo específico aparece, sem precisar abrir cada documento manualmente.

## Quando pode não ser a melhor opção

- Se você precisa de análise linguística mais precisa (concordância com anotação gramatical detalhada, comparação estatística entre corpora): o [AntConc](antconc.md) é mais indicado para esse tipo de trabalho
- Se você precisa processar textos em português com reconhecimento de entidades, análise sintática ou outras tarefas de [PLN](../conceitos/processamento-de-linguagem-natural.md) mais avançadas: ferramentas como o [spaCy](spacy.md), que exigem programação, oferecem mais controle
- Se os documentos tiverem informação sensível: a versão web envia os textos aos servidores do Voyant Consortium; para dados sigilosos, a versão local (VoyantServer) evita esse envio
- Corpora muito grandes podem ficar lentos na versão hospedada gratuita, dependendo do volume de texto

## Tipo de acesso

Totalmente gratuito. O aplicativo web tem licença Creative Commons Atribuição 4.0, e o código-fonte é distribuído sob licença GPL 3.

## Sistemas em que roda

Funciona em qualquer navegador moderno. Também existe uma versão para rodar localmente (VoyantServer), disponível para Windows, macOS e Linux, que requer Java instalado.

## Integrações

- Spyral (ambiente de notebooks integrado ao Voyant, para combinar visualizações com texto explicativo em relatórios)

## Alternativas

- [AntConc](antconc.md) (gratuito, mais focado em concordância e linguística de corpus, também sem programação)
- [spaCy](spacy.md) (biblioteca de código aberto para PLN, exige programação, mais flexível)
- [Orange Data Mining](orange-data-mining.md) (interface visual sem código, mais voltada a mineração de dados em geral)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://voyant-tools.info/](https://voyant-tools.info/)
- Documentação: [https://voyant-tools.org/docs/](https://voyant-tools.org/docs/)
- Repositório: [https://github.com/voyanttools/Voyant](https://github.com/voyanttools/Voyant)
- Discussões da comunidade: [https://github.com/voyanttools/Voyant/discussions](https://github.com/voyanttools/Voyant/discussions)

## Observações

O Voyant Tools é amplamente adotado em cursos introdutórios de humanidades digitais justamente por não exigir programação — é possível carregar um texto e começar a explorar visualizações em poucos minutos. Isso o torna um bom primeiro contato com análise textual computacional para estudantes e docentes de história, antes de migrar (se necessário) para ferramentas que exigem programação, como o [spaCy](spacy.md).

