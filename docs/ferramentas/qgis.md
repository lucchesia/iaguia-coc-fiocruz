---
title: "QGIS"
slug: "qgis"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "mapas e análise espacial"

tags:
  - mapas e análise espacial
  - open source
  - uso offline
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: GPL-2.0
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada a alta"
integrations:
  - PostGIS
  - GDAL
  - Python

concepts: []
alternatives:
  - Kepler.gl
  - ArcGIS
  - Google Earth

official_site: "https://qgis.org/"
documentation: "https://docs.qgis.org/"
forum: "não disponível"
repository: "https://github.com/qgis/QGIS"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

QGIS é um Sistema de Informação Geográfica (SIG) gratuito e de código aberto, usado para criar, editar, analisar e publicar mapas e dados espaciais. É um projeto oficial da Open Source Geospatial Foundation (OSGeo), mantido por uma comunidade de colaboradores desde 2002, e é considerado uma das principais alternativas gratuitas a softwares SIG comerciais como o ArcGIS.

## Para que serve

- Criar mapas para impressão, tela ou publicação na web, combinando várias camadas de dados
- Editar e digitalizar dados geográficos (pontos, linhas, polígonos) diretamente na interface
- Georreferenciar mapas antigos ou plantas históricas digitalizadas — atribuir coordenadas reais a uma imagem sem informação espacial, tornando possível sobrepô-la a mapas atuais
- Analisar dados espaciais com um conjunto amplo de ferramentas (cálculo de distâncias, áreas, interseções, buffers, entre outras)
- Ler e exportar uma grande variedade de formatos: Shapefile, GeoJSON, GeoPackage, e conectar-se a bancos de dados espaciais como PostGIS

## Exemplo de uso

Um historiador tem uma planta urbana de uma cidade brasileira do início do século XX, digitalizada a partir de um arquivo público, e quer compará-la com o traçado atual da cidade. Ele usa a ferramenta de georreferenciamento do QGIS para atribuir coordenadas reais à imagem antiga, alinhando pontos de referência reconhecíveis (como igrejas ou praças) com sua localização atual. O resultado é um mapa histórico sobreposto ao mapa contemporâneo, permitindo visualizar como a malha urbana mudou ao longo do tempo.

## Quando pode não ser a melhor opção

- Se você só precisa criar um mapa simples e pontual, sem edição ou análise espacial detalhada: ferramentas como Google Earth ou Google My Maps são muito mais diretas para esse uso
- Se você quer visualizar rapidamente um grande volume de dados geográficos de forma interativa na web, sem instalar nada: o [Kepler.gl](kepler-gl.md) é mais indicado para esse cenário específico
- Se você não tem familiaridade com conceitos de SIG (sistemas de coordenadas, projeções, camadas): a curva de aprendizado é real, e a interface pode intimidar no início
- Se sua instituição já usa ArcGIS e precisa de compatibilidade total com esse ecossistema: o QGIS lê e converte muitos formatos do ArcGIS, mas não é uma cópia idêntica da interface

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GNU GPL v2 ou posterior).

## Sistemas em que roda

Windows, macOS e Linux. Também há versões para Android voltadas à coleta de dados em campo.

## Integrações

- PostGIS (extensão espacial do banco de dados PostgreSQL, para projetos com grandes volumes de dados geográficos)
- GDAL (biblioteca de conversão de formatos geoespaciais, usada internamente pelo QGIS)
- Python (linguagem usada para automatizar tarefas e criar plugins/scripts personalizados)

## Alternativas

- [Kepler.gl](kepler-gl.md) (ferramenta web mais leve, focada em visualização interativa de dados geográficos, sem edição)
- ArcGIS (proprietário, pago, referência comercial em SIG, amplamente usado em instituições)
- Google Earth (gratuito, muito mais simples, sem recursos de análise espacial avançada)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://qgis.org/](https://qgis.org/)
- Documentação: [https://docs.qgis.org/](https://docs.qgis.org/)
- Repositório: [https://github.com/qgis/QGIS](https://github.com/qgis/QGIS)

## Observações

O georreferenciamento de mapas históricos é uma das aplicações mais citadas do QGIS em pesquisa histórica — o próprio Programming Historian, referência em tutoriais de humanidades digitais, tem um guia dedicado a essa técnica. O suporte oficial é descentralizado: em vez de um único fórum, a comunidade se organiza por listas de discussão, pelo GIS Stack Exchange (marcando perguntas com a tag "qgis") e por canais de chat em tempo real.

