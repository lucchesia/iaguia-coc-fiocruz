---
title: "Palladio"
slug: "palladio"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "visualização"

tags:
  - visualização
  - análise de redes
  - mapas e análise espacial
  - open source
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: BSD-3-Clause
access_model: gratuito

systems:
  - Web
curva_aprendizado: "baixa a moderada"
integrations:
  - Dropbox

concepts: []
alternatives:
  - Gephi
  - Kepler.gl
  - RAWGraphs

official_site: "https://hdlab.stanford.edu/palladio/"
documentation: "https://hdlab.stanford.edu/palladio/help/"
forum: "não disponível"
repository: "https://github.com/humanitiesplusdesign/palladio-app"

caveats: []
learning_resources: []
academic_use: []
tool_status: legada
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Palladio é uma ferramenta gratuita e de código aberto para visualizar dados históricos complexos, criada pelo laboratório Humanities + Design da Universidade Stanford. Diferente de ferramentas especializadas como o [Gephi](gephi.md) (redes) ou o [Kepler.gl](kepler-gl.md) (mapas), o Palladio combina os dois tipos de visualização — mapa e rede — na mesma ferramenta simples, pensada especificamente para o tipo de dado tabular comum em pesquisa histórica (pessoas, lugares, eventos, relações entre eles).

## Para que serve

- Visualizar dados com coordenadas geográficas num mapa interativo, mostrando conexões entre pontos
- Visualizar relações entre dimensões dos dados como uma rede de nós conectados (grafo)
- Explorar os dados numa galeria em grade, com opções de ordenação
- Criar listas personalizadas dos dados, exportáveis em CSV
- Carregar dados colando de uma planilha, arrastando um arquivo (CSV, TAB, TSV) ou vinculando a uma pasta pública do Dropbox

## Exemplo de uso

Uma pesquisadora tem uma planilha com registros de correspondência entre membros de uma rede de ativistas do século XIX, incluindo remetente, destinatário, data e cidade de envio de cada carta. Ela carrega os dados no Palladio e alterna entre duas visualizações da mesma informação: um mapa mostrando de onde as cartas foram enviadas, e uma rede mostrando quem se correspondia com quem — sem precisar aprender duas ferramentas diferentes ou reformatar os dados para cada uma.

## Quando pode não ser a melhor opção

- Se você precisa de recursos avançados de análise de redes (métricas de centralidade, detecção de comunidades): o Gephi é mais completo para essa tarefa específica
- Se você precisa de mapas com muitas camadas de dados ou grandes volumes de pontos: o Kepler.gl ou o [QGIS](qgis.md) lidam melhor com esse cenário
- Se você quer uma ferramenta com atualizações e manutenção frequentes: o ritmo de desenvolvimento do Palladio é lento atualmente — o projeto continua funcional, mas não recebe novidades com a mesma frequência de outras ferramentas mencionadas neste glossário
- Se os dados forem muito sensíveis: como é uma ferramenta web, vale verificar como os dados são processados antes de usar com informações confidenciais

## Tipo de acesso

Totalmente gratuito e de código aberto (licença BSD 3-Clause, Stanford University).

## Sistemas em que roda

Funciona em qualquer navegador moderno — não há instalação necessária.

## Integrações

- Dropbox (é possível vincular um arquivo de dados hospedado numa pasta pública do Dropbox, em vez de fazer upload direto)

## Alternativas

- [Gephi](gephi.md) (mais completo para análise de redes, com mais recursos de métricas)
- [Kepler.gl](kepler-gl.md) (mais completo para mapas com grandes volumes de dados)
- [RAWGraphs](rawgraphs.md) (mais tipos de gráfico, sem foco específico em mapas ou redes)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://hdlab.stanford.edu/palladio/](https://hdlab.stanford.edu/palladio/)
- Tutoriais e FAQ: [https://hdlab.stanford.edu/palladio/help/](https://hdlab.stanford.edu/palladio/help/)
- Repositório: [https://github.com/humanitiesplusdesign/palladio-app](https://github.com/humanitiesplusdesign/palladio-app)

## Observações

O Palladio é uma referência histórica em humanidades digitais — foi uma das primeiras ferramentas a combinar visualização de mapas e redes numa interface simples, pensada especificamente para pesquisadores sem formação técnica. Vale ter em mente que o ritmo de manutenção do projeto diminuiu nos últimos anos (poucos commits recentes e issues em aberto no repositório), embora a ferramenta continue disponível e funcional — não se trata de um projeto formalmente descontinuado, mas de desenvolvimento mais lento do que o de ferramentas mantidas por equipes maiores ou empresas.

