---
title: "Retrieval-Augmented Generation"
title_pt: "Geração Aumentada por Recuperação"
slug: "rag"

entry_type: "conceito"
concept_type: "técnica"

category: "representação, busca e recuperação"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "RAG"
  - "retrieval-augmented generation"

related_terms:
  - busca-semantica
prerequisites:
  - modelo-de-linguagem-grande
  - busca-semantica

references:
  - title: "retrieval-augmented generation — Glossary | NIST Computer Security Resource Center (citando NIST AI 100-2e2025)"
    url: "https://csrc.nist.gov/glossary/term/retrieval_augmented_generation"
    type: "glossário técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Geração Aumentada por Recuperação

## O que é

RAG (Geração Aumentada por Recuperação, do inglês *Retrieval-Augmented Generation*) é uma técnica que combina um modelo de linguagem com um sistema externo de busca de informação — uma "base de conhecimento" — para melhorar a qualidade e a precisão das respostas geradas. Segundo o documento NIST AI 100-2e2025, RAG é "um tipo de sistema de IA generativa em que um modelo é combinado com um sistema separado de recuperação de informação (ou 'base de conhecimento'). A partir de uma consulta da pessoa usuária, o sistema RAG identifica informações relevantes dentro da base de conhecimento e as fornece ao modelo de IA generativa, como contexto, para que o modelo as use ao formular sua resposta. Sistemas RAG permitem que o conhecimento interno de um modelo de IA generativa seja modificado sem a necessidade de um novo treinamento".

## Por que isso importa?

RAG é uma das formas mais comuns de adaptar um modelo de linguagem genérico para trabalhar com um conjunto específico de documentos — por exemplo, o acervo de uma instituição, uma coleção de fontes primárias ou a bibliografia de um projeto de pesquisa — sem precisar treinar ou ajustar o modelo em si. Isso é relevante para avaliar ferramentas de IA voltadas a pesquisa: uma ferramenta que usa RAG sobre uma base de dados confiável e bem curada tende a produzir respostas mais precisas e verificáveis do que um modelo de linguagem "puro", que responde apenas com base no que aprendeu durante o treinamento — embora RAG não elimine completamente o risco de erros ou alucinações.

## Exemplo

Ferramentas de revisão de literatura acadêmica, como o [Elicit](../ferramentas/elicit.md) e o [Scite](../ferramentas/scite.md), usam uma abordagem próxima de RAG: em vez de responder apenas com o conhecimento genérico armazenado no modelo de linguagem durante o treinamento, elas primeiro buscam artigos relevantes numa base de dados acadêmica e depois usam o modelo para resumir ou responder com base nesses artigos recuperados — o que permite que as respostas citem fontes específicas e verificáveis.

## Não confunda com

RAG não é sinônimo de [busca semântica](busca-semantica.md): busca semântica é a técnica usada para encontrar os documentos relevantes dentro da base de conhecimento; RAG é o processo mais amplo, que combina essa busca com a geração de uma resposta por um modelo de linguagem. Também não é sinônimo de [ajuste fino](ajuste-fino.md): RAG não modifica os parâmetros internos do modelo — apenas fornece informação adicional no momento da consulta; ajuste fino, por outro lado, altera de fato o modelo.

## Termos relacionados

## Referências

- NIST Computer Security Resource Center. *retrieval-augmented generation — Glossary* (citando NIST AI 100-2e2025).
  [csrc.nist.gov/glossary/term/retrieval_augmented_generation](https://csrc.nist.gov/glossary/term/retrieval_augmented_generation)
