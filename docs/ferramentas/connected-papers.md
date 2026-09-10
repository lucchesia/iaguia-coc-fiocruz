---
title: Connected Papers
slug: connected-papers
entry_type: ferramenta
tool_type: serviço web
category: revisão de literatura
tags:
  - revisão de literatura
  - gratuito para pesquisa
  - sem código
aliases: []
source_model: proprietário
software_license: proprietária
access_model: freemium
systems:
  - Web
curva_aprendizado: baixa a moderada
integrations:
  - Paperpile
  - Zotero
  - Mendeley
concepts:
  - algoritmo
alternatives:
  - Semantic Scholar
  - ResearchRabbit
  - Litmaps
official_site: https://www.connectedpapers.com
documentation: https://www.connectedpapers.com/about
forum: não disponível
caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: '2026-08-19'
---

## O que é

Connected Papers é uma ferramenta de descoberta de literatura acadêmica que gera mapas visuais de artigos relacionados a partir de um único artigo de referência. Foi criada em 2019 por uma startup israelense (Alex Tarnavsky Eitan, Itay Knaan Harpaz e Eddie Smolyansky) e usa os dados abertos do Semantic Scholar como base para construir os grafos, por meio de um [algoritmo](../conceitos/algoritmo.md) que mede o quão semelhantes dois artigos são entre si.

## Para que serve

- Gerar um grafo visual interativo de artigos relacionados a um artigo de origem, com base em similaridade de conteúdo (não apenas citações diretas)
- Identificar rapidamente os trabalhos mais influentes de uma área, pelo tamanho dos nós no grafo (que reflete o número de citações)
- Perceber a evolução temporal de um campo de pesquisa, pela cor dos nós (que reflete a data de publicação)
- Explorar listas de "trabalhos anteriores" (Prior Works) e "trabalhos derivados" (Derivative Works) de um artigo
- Exportar referências encontradas para o Zotero, Mendeley ou EndNote, ou salvar diretamente no Paperpile

## Exemplo de uso

Um pesquisador quer entender rapidamente o "estado da arte" de um tema específico dentro da história da tecnologia, a partir de um único artigo de referência que já conhece. Ele insere esse artigo no Connected Papers e recebe um grafo visual com dezenas de trabalhos relacionados, agrupados por similaridade — o que ajuda a identificar tanto os trabalhos fundacionais da área quanto os mais recentes, sem precisar ler cada resumo manualmente antes de decidir o que priorizar.

## Quando pode não ser a melhor opção

- Se você precisa de mais de 5 grafos por mês: o plano gratuito tem esse limite; usos mais frequentes exigem o plano Academic (uso individual/acadêmico) ou Business
- Se você está conduzindo uma revisão sistemática formal: como o grafo é gerado por um algoritmo de similaridade, seu uso como parte da estratégia de busca documentada deve ser declarado explicitamente (ferramenta, data de uso e como as sugestões foram verificadas), da mesma forma que outras ferramentas de descoberta automatizada
- Se você precisa de dados de todas as áreas do conhecimento com a mesma profundidade: como depende da cobertura do Semantic Scholar, a qualidade dos grafos pode variar conforme a área

## Tipo de acesso

Freemium, e a ferramenta funciona sem criar conta. O plano gratuito limita a 5 grafos novos por mês. Os planos Academic (uso individual, acadêmico ou sem fins lucrativos) e Business removem esse limite, com valores que variam conforme o ciclo de cobrança, anual ou trimestral, publicados em [connectedpapers.com/pricing](https://www.connectedpapers.com/pricing). O software é proprietário.

## Sistemas em que roda

Funciona inteiramente pela web, por meio do navegador. Não há aplicativo de desktop ou mobile dedicado.

## Integrações

- Paperpile (extensão de navegador com botão "salvar" direto nos grafos)
- Exportação de referências para Zotero, Mendeley e EndNote

## Alternativas

- [Semantic Scholar](semantic-scholar.md) (base de dados que o Connected Papers usa; oferece busca e resumos por IA, mas não mapas visuais de similaridade)
- [ResearchRabbit](researchrabbit.md) (proposta semelhante de mapeamento visual, com integração direta ao Zotero)
- [Litmaps](litmaps.md) (também focado em mapas visuais de citação)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.connectedpapers.com](https://www.connectedpapers.com)
- Documentação: [https://www.connectedpapers.com/about](https://www.connectedpapers.com/about)

### Material de apoio

O artigo de Behera, Jain e Kumar funciona como tutorial completo, com capturas de tela de cada
etapa. Ele parte de um tema de exemplo e percorre a construção do grafo, a leitura dos nós, a
exportação das referências e as seções de trabalhos anteriores e derivados. Está publicado em
periódico de biblioteconomia, com licença aberta e sem exigência de cadastro.

- BEHERA, Prashanta Kumar; JAIN, Sanmati Jinendran; KUMAR, Ashok. Visual exploration of
  literature using Connected Papers: a practical approach. *Issues in Science and Technology
  Librarianship*, n. 104, 2023:
  [https://journals.library.ualberta.ca/istl/index.php/istl/article/view/2760](https://journals.library.ualberta.ca/istl/index.php/istl/article/view/2760)

## Uso em pesquisa e ensino

Na data de preparação deste verbete não foi localizada pesquisa que declare ter usado o
Connected Papers como parte da estratégia de busca. A procura incluiu SciELO, BDTD e Google
Scholar. A ferramenta é descrita com frequência em guias de biblioteca e em textos de
divulgação, e o registro do seu uso dentro do método de um trabalho é raro. Para revisões
sistemáticas, isso reforça o que este verbete já recomenda: se você usar a ferramenta, declare
o uso explicitamente na descrição da busca. Este verbete será revisto quando houver uso
documentado.

## Observações

O Connected Papers é construído sobre os dados abertos do Semantic Scholar — ou seja, depende da cobertura e qualidade dessa base para gerar seus grafos. É uma ferramenta bastante popular entre pesquisadores para uma primeira exploração visual de um tema, mas, por ser baseada em um algoritmo de similaridade (não em curadoria humana), os resultados devem ser tratados como ponto de partida, não como levantamento bibliográfico completo — especialmente em revisões sistemáticas formais, nas quais seu uso deve ser declarado como parte do método.

