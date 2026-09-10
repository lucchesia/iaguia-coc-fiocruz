---
title: "RAWGraphs"
slug: "rawgraphs"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "visualização"

tags:
  - visualização
  - open source
  - sem código
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: Apache-2.0
access_model: gratuito

systems:
  - Web
curva_aprendizado: "baixa a moderada"
integrations:
  - OpenRefine
  - Illustrator
  - Inkscape

concepts: []
alternatives:
  - Datawrapper
  - Flourish
  - Tableau

official_site: "https://www.rawgraphs.io/"
documentation: "https://www.rawgraphs.io/learning"
forum: "https://github.com/rawgraphs/rawgraphs-app/discussions"
repository: "https://github.com/rawgraphs/rawgraphs-app"

caveats: []
learning_resources: []
academic_use: []
tool_status: estável
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

RAWGraphs é uma ferramenta gratuita e de código aberto para transformar planilhas de dados em visualizações, direto no navegador. Foi criada em 2013 pelo DensityDesign Research Lab (Politecnico di Milano), em parceria com os estúdios Calibro e INMAGIK, com a proposta de ser "o elo perdido" entre programas de planilha (como Excel ou o [OpenRefine](openrefine.md)) e editores de gráficos vetoriais (como Illustrator ou Inkscape).

## Para que serve

- Transformar dados de uma planilha em quase 30 tipos de visualização diferentes: gráficos de quantidade, hierarquia, série temporal, redes, entre outros
- Colar dados diretamente de uma planilha, enviar arquivos (CSV, TSV, JSON) ou buscar dados de uma URL ou endpoint SPARQL
- Ajustar a visualização mapeando colunas dos dados a variáveis visuais (cor, tamanho, posição), sem escrever código
- Exportar o resultado como imagem vetorial (SVG) editável em programas como Illustrator ou Inkscape, ou como imagem raster (PNG)

## Exemplo de uso

Um pesquisador tem uma planilha com o número de processos judiciais por tipo de crime e por década, ao longo de um século, e quer visualizar como essa distribuição mudou ao longo do tempo. Ele cola os dados diretamente no RAWGraphs, escolhe um gráfico de fluxo (streamgraph) e mapeia as colunas de década, tipo de crime e quantidade às variáveis visuais correspondentes. Em seguida, exporta o resultado como SVG e faz ajustes finais de estilo no Illustrator antes de incluir a imagem no artigo.

## Quando pode não ser a melhor opção

- Se você precisa de mapas geográficos interativos: o RAWGraphs não é feito para dados espaciais — o [Kepler.gl](kepler-gl.md) ou o [QGIS](qgis.md) são mais adequados
- Se você quer publicar um gráfico interativo direto na web (não uma imagem estática): o [Datawrapper](datawrapper.md) ou o Flourish são mais indicados, já que o RAWGraphs gera imagens fixas, não widgets interativos incorporáveis
- Se seus dados forem muito sensíveis e você preferir não usar nenhuma ferramenta baseada em navegador: embora o processamento seja só local (nada é enviado a servidores), algumas instituições preferem soluções instaladas localmente
- Se você não tem nenhuma familiaridade com os conceitos de cada tipo de gráfico (o que é um streamgraph, um diagrama Sankey, etc.): escolher a visualização certa exige algum conhecimento prévio de visualização de dados

## Tipo de acesso

Totalmente gratuito e de código aberto (licença Apache 2.0).

## Sistemas em que roda

Funciona em qualquer navegador moderno — não há instalação necessária. Todo o processamento dos dados acontece localmente no navegador, sem envio a servidores.

## Integrações

- OpenRefine (fonte comum de dados já limpos, antes de visualizar no RAWGraphs)
- Illustrator e Inkscape (editores vetoriais usados para refinar o SVG exportado)

## Alternativas

- [Datawrapper](datawrapper.md) (mais focado em gráficos e mapas interativos para publicação editorial/jornalística)
- Flourish (proposta parecida, com mais recursos de interatividade e narrativa)
- Tableau (proprietário, pago, referência comercial em visualização e dashboards)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.rawgraphs.io/](https://www.rawgraphs.io/)
- Documentação/tutoriais: [https://www.rawgraphs.io/learning](https://www.rawgraphs.io/learning)
- Repositório: [https://github.com/rawgraphs/rawgraphs-app](https://github.com/rawgraphs/rawgraphs-app)
- Discussões da comunidade: [https://github.com/rawgraphs/rawgraphs-app/discussions](https://github.com/rawgraphs/rawgraphs-app/discussions)

## Observações

O RAWGraphs é bastante usado em cursos de visualização de dados e design de informação, justamente por servir de ponte entre planilhas comuns e visualizações mais sofisticadas, sem exigir programação — mas ainda assim produzindo resultados editáveis e refináveis em ferramentas de design vetorial, o que o distingue de geradores de gráfico mais "engessados".

