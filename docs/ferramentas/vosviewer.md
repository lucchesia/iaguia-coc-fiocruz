---
title: "VOSviewer"
slug: "vosviewer"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "análise de redes"

tags:
  - análise de redes
  - revisão de literatura
  - uso offline
  - gratuito para pesquisa
aliases: []

source_model: proprietário
software_license: proprietária
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
  - Web
curva_aprendizado: "moderada"
integrations:
  - OpenAlex
  - Semantic Scholar
  - Scopus
  - Web of Science

concepts: []
alternatives:
  - Gephi
  - Cytoscape
  - CitNetExplorer

official_site: "https://www.vosviewer.com/"
documentation: "https://www.vosviewer.com/getting-started"
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

VOSviewer é um programa gratuito para construir e visualizar redes bibliométricas — mapas de citação, coautoria e coocorrência de termos entre publicações acadêmicas. Foi criado por Nees Jan van Eck e Ludo Waltman, do Centre for Science and Technology Studies (CWTS) da Universidade de Leiden (Países Baixos), e é a ferramenta de mapeamento bibliométrico mais usada em artigos publicados sobre o tema. Diferente do [Gephi](gephi.md) e do [Cytoscape](cytoscape.md), que são ferramentas gerais de análise de redes, o VOSviewer foi desenhado especificamente para redes construídas a partir de dados bibliográficos.

## Para que serve

- Construir e visualizar redes de citação, coautoria e acoplamento bibliográfico entre publicações, autores, periódicos ou instituições
- Gerar mapas de coocorrência de termos e palavras-chave a partir de mineração de texto em títulos e resumos
- Importar dados diretamente de bases como Web of Science, Scopus, [OpenAlex](openalex.md), [Semantic Scholar](semantic-scholar.md), Crossref, Europe PMC, Lens e Dimensions
- Compartilhar mapas interativos pela web, usando a versão VOSviewer Online, sem precisar instalar nada

## Exemplo de uso

Um pesquisador está fazendo uma revisão de literatura sobre um tema histórico específico e quer entender como o campo se organiza: quais autores publicam mais, quais trabalhos são mais citados entre si e quais termos aparecem com mais frequência nos resumos. Ele exporta os dados bibliográficos de uma busca no OpenAlex e importa no VOSviewer, que gera um mapa visual mostrando clusters de autores que se citam mutuamente e os principais termos que caracterizam cada subárea do campo.

## Quando pode não ser a melhor opção

- Se sua rede não vem de dados bibliográficos (por exemplo, redes de correspondência ou parentesco): o [Gephi](gephi.md) é mais flexível para esse tipo de dado
- Se você precisa de código-fonte auditável: a versão desktop do VOSviewer é gratuita, mas de código fechado — só a versão online mais recente (VOSviewer Online) é de código aberto
- Se você quer aplicar algoritmos de análise de redes mais avançados e customizáveis (detecção de comunidades com múltiplos métodos, scripts próprios): o Gephi ou o Cytoscape, com seus ecossistemas de plugins, oferecem mais controle
- A instalação da versão desktop também depende de Java, como Gephi e Cytoscape

## Tipo de acesso

Totalmente gratuito, mas de código fechado (freeware) na versão desktop principal. A versão mais recente, VOSviewer Online, é de código aberto (licença MIT), mas é um produto complementar, não um substituto direto do desktop.

## Sistemas em que roda

Windows, macOS e Linux (versão desktop, requer Java), além de acesso via navegador na versão VOSviewer Online.

## Integrações

- [OpenAlex](openalex.md) e [Semantic Scholar](semantic-scholar.md): consulta direta às APIs para montar redes bibliométricas sem precisar baixar arquivos manualmente
- Web of Science e Scopus: importação de dados exportados dessas bases (as mais usadas em bibliometria tradicional)
- Crossref, Europe PMC, Lens e Dimensions: outras fontes de dados bibliográficos suportadas

## Alternativas

- [Gephi](gephi.md) (ferramenta geral de análise de redes, não limitada a dados bibliográficos)
- [Cytoscape](cytoscape.md) (também geral, com origem em biologia molecular)
- CitNetExplorer (outra ferramenta do mesmo grupo de pesquisa da CWTS, focada especificamente em redes de citação)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.vosviewer.com/](https://www.vosviewer.com/)
- Guia de início / manual: [https://www.vosviewer.com/getting-started](https://www.vosviewer.com/getting-started)

## Observações

O VOSviewer é uma referência amplamente citada em estudos bibliométricos e em revisões sistemáticas de literatura que incluem mapeamento visual do campo — é comum aparecer em artigos ao lado de ferramentas de descoberta de literatura como Semantic Scholar, OpenAlex ou Connected Papers. Por ser mantido por um centro de pesquisa acadêmico (CWTS/Leiden) e não por uma empresa, tem atualizações constantes acompanhando mudanças nas APIs das bases de dados que suporta.

