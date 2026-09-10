---
title: "Gephi"
slug: "gephi"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "análise de redes"

tags:
  - análise de redes
  - open source
  - uso offline
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: GPL-3.0
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada a alta"
integrations:
  - nenhuma conhecida

concepts: []
alternatives:
  - Cytoscape
  - VOSviewer
  - Palladio

official_site: "https://gephi.org/"
documentation: "https://docs.gephi.org/"
forum: "https://github.com/gephi/gephi/discussions"
repository: "https://github.com/gephi/gephi"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Gephi é um programa gratuito e de código aberto para visualizar e analisar redes — estruturas de dados formadas por nós (pontos) e arestas (conexões entre eles). É usado em disciplinas como sociologia, biologia e humanidades digitais para explorar visualmente dados conectados, como redes de correspondência, relações de parentesco, citações entre autores ou vínculos entre instituições. É mantido por uma comunidade de colaboradores, sem fins lucrativos, e é citado em dezenas de milhares de publicações acadêmicas.

## Para que serve

- Visualizar redes de até milhões de nós e conexões, com algoritmos de disposição espacial (layout) como Force Atlas 2
- Aplicar métricas e algoritmos de análise de redes: detecção de comunidades, medidas de centralidade, agrupamento (clustering)
- Manipular os dados da rede diretamente numa interface de planilha, sem precisar editar arquivos externos
- Filtrar e transformar a rede de forma interativa, explorando diferentes recortes dos dados
- Exportar visualizações em PNG, PDF ou SVG, prontas para uso em artigos e apresentações
- Ler e gravar arquivos no formato GEXF (formato próprio do Gephi) e em outros formatos comuns de dados de rede

## Exemplo de uso

Um pesquisador está estudando a correspondência trocada entre intelectuais de um movimento político do século XIX, a partir de um acervo de cartas catalogadas. Ele organiza os dados como uma rede — cada pessoa é um nó, e cada carta trocada entre duas pessoas é uma conexão — e importa esses dados no Gephi. Usando o algoritmo de detecção de comunidades, identifica grupos de correspondência mais densos (possíveis alianças ou círculos de influência) e gera uma visualização para ilustrar essas relações no artigo que está escrevendo.

## Quando pode não ser a melhor opção

- Se você não tem familiaridade com conceitos de análise de redes (nós, arestas, centralidade, comunidades): a curva de aprendizado é real, tanto pelos conceitos quanto pela interface do programa
- Se você só precisa de uma visualização simples e rápida, sem instalar nada: existe o Gephi Lite, uma versão mais leve que roda direto no navegador, com menos recursos
- Se sua rede for pequena e simples: ferramentas mais focadas em biologia (como o [Cytoscape](cytoscape.md)) ou em bibliometria (como o [VOSviewer](vosviewer.md)) podem se ajustar melhor a propósitos específicos
- Redes muito grandes (na casa dos milhões de nós) podem exigir bastante memória RAM do computador

## Tipo de acesso

Totalmente gratuito e de código aberto (licença dupla GPL v3 / CDDL v1.1), mantido como projeto sem fins lucrativos.

## Sistemas em que roda

Windows, macOS e Linux. Desde a versão 0.9.3, o Java necessário já vem embutido no instalador — não é preciso instalar separadamente.

## Integrações

Não tem integrações formais com outras ferramentas específicas, mas conta com um ecossistema de plugins desenvolvidos pela comunidade (novos algoritmos de layout, métricas, formatos de arquivo, entre outros).

## Alternativas

- [Cytoscape](cytoscape.md) (também gratuito e de código aberto, com foco mais forte em biologia/bioinformática)
- [VOSviewer](vosviewer.md) (gratuito, mais focado em redes bibliométricas — citações, coautoria)
- [Palladio](palladio.md) (ferramenta web mais simples, pensada para humanidades digitais)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://gephi.org/](https://gephi.org/)
- Documentação: [https://docs.gephi.org/](https://docs.gephi.org/)
- Repositório: [https://github.com/gephi/gephi](https://github.com/gephi/gephi)
- Discussões da comunidade: [https://github.com/gephi/gephi/discussions](https://github.com/gephi/gephi/discussions)

## Observações

O Gephi é uma das ferramentas mais citadas em humanidades digitais para "análise de redes sociais históricas" (historical social network analysis) — um campo que cresce dentro da pesquisa em história, especialmente em estudos de correspondência, parentesco, redes comerciais e círculos intelectuais. Vale considerar que interpretar uma visualização de rede exige cuidado metodológico: a disposição visual (layout) é gerada por um algoritmo e não representa, por si só, uma "verdade" sobre as relações — é preciso combinar a visualização com a análise crítica das fontes.

