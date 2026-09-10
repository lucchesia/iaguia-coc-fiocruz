---
title: "Zero-shot Prompting"
title_pt: "Zero-shot"
slug: "zero-shot"

entry_type: "conceito"
concept_type: "técnica"

category: "interação com modelos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "zero-shot prompting"
  - "zero-shot learning"

related_terms:
  - prompt
  - few-shot
prerequisites:
  - prompt

references:
  - title: "zero-shot prompting — Machine Learning Glossary: Generative AI | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary/generative#zero-shot-prompting"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Zero-shot

## O que é

Zero-shot é uma forma de usar um modelo de linguagem em que o [prompt](prompt.md) não inclui nenhum exemplo de como a resposta deve ser — pede-se diretamente a tarefa, confiando que o modelo já "sabe" como realizá-la a partir do que aprendeu durante o treinamento. Segundo o glossário técnico do Google for Developers, um prompt zero-shot é "um prompt que não fornece um exemplo de como você quer que o modelo de linguagem grande responda". A tarefa é pedida sem nenhuma demonstração prévia do formato esperado — em contraste com abordagens que fornecem um ou mais exemplos antes do pedido ([few-shot](few-shot.md)).

## Por que isso importa?

A maioria das interações cotidianas com ferramentas de IA generativa é, na prática, zero-shot: a pessoa simplesmente pede algo ("traduza este parágrafo", "resuma este artigo") sem mostrar um exemplo do resultado esperado. Entender essa distinção ajuda a interpretar por que, em tarefas mais específicas ou incomuns — como aplicar uma convenção particular de transcrição paleográfica —, um pedido zero-shot pode produzir um resultado menos preciso do que um pedido acompanhado de um exemplo do formato desejado.

## Exemplo

Ao pedir para o [Claude](../ferramentas/claude.md) "classifique estes trechos de cartas históricas por tema", sem fornecer nenhum exemplo de como as categorias devem ser nomeadas ou organizadas, uma pesquisadora está fazendo um pedido zero-shot. O modelo decide sozinho, com base no que aprendeu durante o treinamento, como interpretar e executar essa tarefa — o que pode gerar categorias diferentes das que a pesquisadora imaginava.

## Não confunda com

Zero-shot não é sinônimo de prompt em geral: prompt é qualquer entrada de texto enviada a um modelo; zero-shot é uma característica específica de um prompt — a ausência de exemplos. Também não é sinônimo de [few-shot](few-shot.md): few-shot é o oposto — um prompt que inclui um ou mais exemplos do resultado esperado antes de pedir a tarefa.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary: Generative AI* (entrada "zero-shot prompting").
  [developers.google.com/machine-learning/glossary/generative](https://developers.google.com/machine-learning/glossary/generative#zero-shot-prompting)
