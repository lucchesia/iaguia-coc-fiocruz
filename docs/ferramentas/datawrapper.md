---
title: "Datawrapper"
slug: "datawrapper"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "visualização"

tags:
  - visualização
  - sem código
  - gratuito para pesquisa
aliases: []

source_model: proprietário
software_license: proprietária
access_model: freemium

systems:
  - Web
curva_aprendizado: "baixa"
integrations:
  - Google Sheets

concepts: []
alternatives:
  - RAWGraphs
  - Flourish
  - Kepler.gl

official_site: "https://www.datawrapper.de/"
documentation: "https://academy.datawrapper.de/"
forum: "não disponível"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Datawrapper é uma ferramenta web para criar gráficos, mapas e tabelas prontos para publicação, sem precisar programar. É desenvolvida pela empresa alemã Datawrapper GmbH e é amplamente usada por redações jornalísticas — mas, diferente do [RAWGraphs](rawgraphs.md), que exporta imagens estáticas editáveis em programas de design, o Datawrapper gera visualizações interativas prontas para incorporar diretamente numa página web.

## Para que serve

- Criar gráficos (barras, linhas, dispersão, entre outros), mapas e tabelas interativas a partir de uma planilha
- Conectar diretamente a uma planilha do Google Sheets, com opção de atualização automática — o gráfico se atualiza sozinho quando os dados na planilha mudam
- Personalizar tipografia, cores e layout, com controle sobre acessibilidade (rótulos que não se sobrepõem, por exemplo)
- Incorporar (embed) a visualização final diretamente numa página web, com o código de incorporação gerado automaticamente
- Exportar como imagem (PNG no plano gratuito; PDF e SVG exigem plano pago)

## Exemplo de uso

Uma pesquisadora está escrevendo um texto de divulgação científica para o site do seu departamento e quer incluir um gráfico interativo mostrando a evolução do número de teses defendidas em história ao longo de vinte anos. Ela conecta uma planilha do Google Sheets com os dados diretamente ao Datawrapper, escolhe um gráfico de linhas, ajusta cores e rótulos, e gera o código de incorporação para colar na página do site — sem precisar de conhecimento de design gráfico ou programação.

## Quando pode não ser a melhor opção

- Se você precisa de código-fonte auditável ou quer rodar a ferramenta localmente: o Datawrapper é proprietário — o [RAWGraphs](rawgraphs.md) é uma alternativa de código aberto
- Se você quer editar o resultado num programa de design vetorial (Illustrator, Inkscape): o Datawrapper não gera SVG editável no plano gratuito; o RAWGraphs é mais indicado para esse fluxo
- Se você precisa de mapas geográficos mais avançados, com muitas camadas de dados: o [Kepler.gl](kepler-gl.md) ou o [QGIS](qgis.md) oferecem mais recursos espaciais
- Se a marca d'água "Created with Datawrapper" for um problema: removê-la exige o plano pago (Pro)

## Tipo de acesso

Freemium: o plano gratuito permite criar, publicar e incorporar gráficos, mapas e tabelas sem limite de quantidade, mas com uma atribuição "Created with Datawrapper" no rodapé e exportação só em PNG. Planos pagos (Pro, Custom/Enterprise) liberam exportação em PDF/SVG, remoção da atribuição, histórico de edições e recursos de equipe.

## Sistemas em que roda

Funciona em qualquer navegador moderno — não há instalação necessária.

## Integrações

- Google Sheets (conexão direta, com opção de atualização automática dos dados)
- Também aceita arquivos Excel, OpenOffice/LibreOffice (XLSX, XLS, ODS), CSV, TSV, TXT e DBF

## Alternativas

- [RAWGraphs](rawgraphs.md) (código aberto, gera imagens estáticas editáveis em vez de widgets interativos)
- Flourish (proposta parecida, também freemium, com mais recursos de narrativa)
- [Kepler.gl](kepler-gl.md) (código aberto, mais indicado para mapas com grandes volumes de dados geográficos)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.datawrapper.de/](https://www.datawrapper.de/)
- Documentação (Datawrapper Academy): [https://academy.datawrapper.de/](https://academy.datawrapper.de/)

## Observações

O Datawrapper é uma referência no jornalismo de dados, mas também é bastante usado por pesquisadores e comunicadores científicos que precisam publicar visualizações interativas em sites e blogs, sem depender de uma equipe técnica. A conexão com Google Sheets e a atualização automática são especialmente úteis para dados de pesquisa que mudam ao longo do tempo, como séries históricas em atualização contínua.

