---
title: "Cytoscape"
slug: "cytoscape"

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
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada a alta"
integrations:
  - WikiPathways
  - Reactome
  - KEGG

concepts: []
alternatives:
  - Gephi
  - VOSviewer
  - Palladio

official_site: "https://cytoscape.org/"
documentation: "https://manual.cytoscape.org/en/stable/"
forum: "https://groups.google.com/g/cytoscape-helpdesk"
repository: "https://github.com/cytoscape/cytoscape"

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

Cytoscape é um programa gratuito e de código aberto para visualizar e analisar redes complexas, mantido pelo Cytoscape Consortium. Foi criado originalmente para biologia molecular — análise de redes de interação entre genes e proteínas —, mas hoje é uma plataforma independente de domínio, usada também em análise de redes sociais e de relações interpessoais. Assim como o [Gephi](gephi.md), permite explorar visualmente estruturas de nós e conexões, mas mantém um ecossistema de recursos voltado à origem biológica da ferramenta.

## Para que serve

- Visualizar redes complexas e integrar os dados da rede com qualquer tipo de informação adicional (atributos)
- Calcular estatísticas de rede, encontrar caminhos mais curtos entre nós e identificar clusters (agrupamentos)
- Carregar dados de interação em múltiplos formatos e mapear conjuntos de dados diferentes sobre a mesma rede
- Ampliar funcionalidades por meio de "apps" (plugins), incluindo integração direta com bases de dados biológicas como WikiPathways, Reactome e KEGG
- Aplicar a mesma lógica de visualização a redes de qualquer natureza, não só biológicas — incluindo redes sociais e de correspondência

## Exemplo de uso

Um pesquisador de história da ciência quer mapear a rede de colaboração entre cientistas de um instituto de pesquisa ao longo de décadas, a partir de coautorias em publicações. Ele organiza os dados como uma rede (cada cientista é um nó, cada coautoria uma conexão) e usa o Cytoscape para visualizar a estrutura, calcular quais pesquisadores ocupam posições mais centrais na rede de colaboração e identificar grupos que trabalharam mais próximos entre si ao longo do tempo.

## Quando pode não ser a melhor opção

- Se sua pesquisa não tem relação com dados biológicos e você quer uma ferramenta pensada desde o início para humanidades e ciências sociais: o [Gephi](gephi.md) tem uma comunidade maior nessa área e recursos de layout mais imediatos para esse uso
- Se você não tem familiaridade com conceitos de análise de redes: a curva de aprendizado é real, como em qualquer ferramenta desse tipo
- Se você só precisa de uma visualização pontual e simples: ferramentas mais leves e baseadas em navegador podem ser mais rápidas de usar
- A instalação exige Java (versão 17 nas versões mais recentes) configurado corretamente no computador

## Tipo de acesso

Totalmente gratuito e de código aberto (licença LGPL).

## Sistemas em que roda

Windows, macOS e Linux, com Java (JRE 17 recomendado) instalado.

## Integrações

- WikiPathways, Reactome e KEGG (bases de dados biológicas, integração nativa relevante principalmente para pesquisa em biologia)
- Ecossistema de "apps" (plugins) desenvolvidos pela comunidade, para funcionalidades adicionais de análise e visualização

## Alternativas

- [Gephi](gephi.md) (também gratuito e de código aberto, com comunidade mais forte em humanidades digitais)
- [VOSviewer](vosviewer.md) (gratuito, mais focado em redes bibliométricas — citações, coautoria)
- [Palladio](palladio.md) (ferramenta web mais simples, pensada para humanidades digitais)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://cytoscape.org/](https://cytoscape.org/)
- Documentação: [https://manual.cytoscape.org/en/stable/](https://manual.cytoscape.org/en/stable/)
- Repositório: [https://github.com/cytoscape/cytoscape](https://github.com/cytoscape/cytoscape)
- Fórum da comunidade: [https://groups.google.com/g/cytoscape-helpdesk](https://groups.google.com/g/cytoscape-helpdesk)

## Observações

Embora tenha nascido na biologia molecular, o Cytoscape é tecnicamente capaz de lidar com qualquer tipo de rede, incluindo as usadas em pesquisa histórica (correspondência, parentesco, redes comerciais). Na prática, porém, a maior parte de sua documentação, tutoriais e "apps" da comunidade ainda giram em torno de aplicações biológicas — por isso, para quem está começando em humanidades digitais, o Gephi tende a ter uma curva de entrada mais direta, com mais exemplos e tutoriais voltados a esse público.

