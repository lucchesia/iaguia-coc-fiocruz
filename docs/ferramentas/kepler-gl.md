---
title: "Kepler.gl"
slug: "kepler-gl"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "mapas e análise espacial"

tags:
  - mapas e análise espacial
  - open source
  - sem código
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: MIT
access_model: gratuito

systems:
  - Web
curva_aprendizado: "baixa a moderada"
integrations:
  - Jupyter

concepts: []
alternatives:
  - QGIS
  - Datawrapper
  - Google My Maps

official_site: "https://kepler.gl/"
documentation: "https://docs.kepler.gl/"
forum: "https://github.com/keplergl/kepler.gl/discussions"
repository: "https://github.com/keplergl/kepler.gl"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Kepler.gl é uma ferramenta gratuita e de código aberto para visualizar dados geográficos de grande escala direto no navegador, sem precisar instalar nada nem programar. Foi criada pela Uber em 2018 e, desde 2019, é mantida como projeto hospedado pela Urban Computing Foundation (ligada à Linux Foundation). Diferente do [QGIS](qgis.md), que é um Sistema de Informação Geográfica completo para criar e editar mapas, o Kepler.gl é focado especificamente em exploração visual rápida de grandes volumes de dados de localização.

## Para que serve

- Visualizar milhões de pontos geográficos com bom desempenho, incluindo agregações espaciais em tempo real (por exemplo, agrupar pontos próximos em hexágonos coloridos por densidade)
- Detectar automaticamente colunas de latitude/longitude numa planilha, montando camadas de mapa sem configuração manual
- Criar diferentes tipos de camada: pontos, arcos (para visualizar trajetos entre origem e destino), polígonos, grades e hexágonos, em 2D ou 3D
- Compartilhar mapas interativos exportando a configuração ou publicando o mapa online
- Ser usado também dentro de notebooks [Jupyter](jupyter.md), como biblioteca Python, para quem já trabalha nesse ambiente

## Exemplo de uso

Um pesquisador tem uma planilha com milhares de registros de migração interna histórica, cada linha com o local de origem e destino de uma pessoa e o ano do deslocamento. Ele arrasta o arquivo CSV para o Kepler.gl no navegador, que detecta automaticamente as colunas de coordenadas e sugere uma camada de arcos ligando origem e destino. Em poucos minutos, ele tem um mapa interativo mostrando os principais fluxos migratórios do período, sem escrever nenhuma linha de código.

## Quando pode não ser a melhor opção

- Se você precisa editar ou criar dados geográficos (digitalizar polígonos, corrigir geometrias): o Kepler.gl é uma ferramenta de visualização, não de edição — o [QGIS](qgis.md) é mais adequado para isso
- Se você precisa georreferenciar mapas antigos ou fazer análise espacial mais avançada (buffers, interseções, projeções): essas tarefas também exigem um SIG completo como o QGIS
- Se o dataset for muito grande (acima de 250 MB): como os dados ficam só no navegador, há um limite prático de tamanho de arquivo — para volumes maiores, é preciso carregar os dados a partir de uma URL remota, em vez de fazer upload direto
- Se você precisa de um mapa estático simples para publicação: ferramentas mais simples, como o Datawrapper, podem ser mais diretas

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MIT).

## Sistemas em que roda

Funciona em qualquer navegador moderno — não há versão desktop nem instalação necessária.

## Integrações

- [Jupyter](jupyter.md): existe uma versão do Kepler.gl como biblioteca Python, para uso dentro de notebooks, aceitando dados de Pandas e GeoPandas diretamente

## Alternativas

- [QGIS](qgis.md) (Sistema de Informação Geográfica completo, com edição e análise espacial avançada)
- Datawrapper (mais focado em mapas simples para publicação jornalística/editorial)
- Google My Maps (gratuito, muito mais simples, sem recursos de análise ou grandes volumes de dados)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://kepler.gl/](https://kepler.gl/)
- Documentação: [https://docs.kepler.gl/](https://docs.kepler.gl/)
- Repositório: [https://github.com/keplergl/kepler.gl](https://github.com/keplergl/kepler.gl)
- Discussões da comunidade: [https://github.com/keplergl/kepler.gl/discussions](https://github.com/keplergl/kepler.gl/discussions)

## Observações

Um ponto relevante para pesquisa com dados sensíveis: o Kepler.gl é um aplicativo totalmente client-side — os dados carregados ficam só no navegador da pessoa usuária e nunca são enviados a um servidor. Isso o torna uma opção segura para explorar visualmente dados de localização sensíveis (por exemplo, endereços de participantes de pesquisa), desde que o volume de dados esteja dentro do limite prático do navegador.

