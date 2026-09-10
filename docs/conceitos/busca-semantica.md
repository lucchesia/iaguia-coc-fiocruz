---
title: "Semantic Search"
title_pt: "Busca Semântica"
slug: "busca-semantica"

entry_type: "conceito"
concept_type: "técnica"

category: "representação, busca e recuperação"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "semantic search"

related_terms:
  - embedding
prerequisites:
  - embedding
  - representacao-vetorial

references:
  - title: "Semantic search — Wikipédia"
    url: "https://en.wikipedia.org/wiki/Semantic_search"
    type: "enciclopédia colaborativa (apoio)"
  - title: "Introduction to embeddings and vector search — BigQuery | Google Cloud Documentation"
    url: "https://docs.cloud.google.com/bigquery/docs/vector-search-intro"
    type: "documentação técnica"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Busca Semântica

## O que é

Busca semântica é uma forma de busca que localiza resultados com base no significado de uma consulta, e não apenas na presença literal das mesmas palavras. Segundo a Wikipédia, "busca semântica designa a busca com significado, diferenciando-se da busca lexical, em que o motor de busca procura correspondências literais das palavras da consulta — ou suas variações — sem compreender o sentido geral da consulta". Tecnicamente, ferramentas de busca semântica costumam funcionar convertendo a consulta e os documentos de uma coleção em [embeddings](embedding.md), e depois comparando a proximidade numérica entre esses vetores — segundo a documentação técnica do Google Cloud, "quanto mais próximos os objetos estão no espaço de embedding, mais semanticamente semelhantes eles são".

## Por que isso importa?

Para pesquisa acadêmica, busca semântica é especialmente útil porque encontra textos relevantes mesmo quando o vocabulário exato da busca não aparece no documento — um problema comum em buscas tradicionais por palavra-chave, principalmente quando um mesmo conceito histórico é descrito com termos diferentes em épocas, regiões ou tradições historiográficas distintas. Ferramentas de revisão de literatura acadêmica costumam usar busca semântica, em vez de busca por palavra-chave, para ajudar pesquisadoras a encontrar artigos relacionados a um tema mesmo com vocabulário diferente.

## Exemplo

Uma busca por "trabalho compulsório no período colonial" numa ferramenta de busca semântica pode retornar artigos que usam termos como "mão de obra forçada" ou "sistema de trabalho obrigatório", mesmo que a frase exata da busca não apareça em nenhum desses textos — porque a ferramenta compara o significado da consulta com o significado dos documentos, não apenas as palavras usadas.

## Não confunda com

Busca semântica não é sinônimo de busca por palavra-chave (busca lexical): busca por palavra-chave procura correspondências exatas — ou quase exatas — de termos; busca semântica busca por significado, mesmo quando as palavras usadas são diferentes. Também não é sinônimo de embedding: embedding é a representação numérica usada internamente para calcular semelhança de significado; busca semântica é a aplicação prática dessa técnica a um sistema de busca.

## Termos relacionados

## Referências

- Wikipédia. *Semantic search*.
  [en.wikipedia.org/wiki/Semantic_search](https://en.wikipedia.org/wiki/Semantic_search)
- Google Cloud. *Introduction to embeddings and vector search* (documentação BigQuery).
  [docs.cloud.google.com/bigquery/docs/vector-search-intro](https://docs.cloud.google.com/bigquery/docs/vector-search-intro)
