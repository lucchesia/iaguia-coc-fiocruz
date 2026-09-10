---
title: "Language Model"
title_pt: "Modelo de Linguagem"
slug: "modelo-de-linguagem"

entry_type: "conceito"
concept_type: "conceito"

category: "aprendizado de máquina"

tags:
  - inteligência artificial
  - aprendizado de máquina

aliases:
  - "language model"
  - "LM"

related_terms:
  - modelo-de-linguagem-grande
  - processamento-de-linguagem-natural
prerequisites:
  - modelo
  - aprendizado-de-maquina

references:
  - title: "Speech and Language Processing (3ª edição, rascunho online) — Jurafsky & Martin, Stanford University"
    url: "https://web.stanford.edu/~jurafsky/slp3/3.pdf"
    type: "referência acadêmica de PLN"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-27"
---

# Modelo de Linguagem

## O que é

Modelo de linguagem é um [modelo](modelo.md) que estima a probabilidade de sequências de palavras — calcula quão provável é uma palavra aparecer depois de outras, com base em padrões estatísticos aprendidos a partir de grandes quantidades de texto. Segundo Daniel Jurafsky e James Martin, autores do livro de referência *Speech and Language Processing* (Universidade Stanford), "um modelo de linguagem atribui probabilidades a sequências de palavras". A ideia é bem anterior à IA generativa atual: modelos de linguagem estatísticos simples, baseados em contagem de palavras vizinhas (os chamados "n-gramas"), já eram usados décadas antes do surgimento dos [modelos de linguagem grande (LLMs)](modelo-de-linguagem-grande.md) baseados em redes neurais.

## Por que isso importa?

"Modelo de linguagem" é um termo mais amplo e mais antigo do que costuma parecer no debate atual sobre IA: corretores ortográficos, sugestões de autocompletar em teclados de celular e ferramentas clássicas de [PLN](processamento-de-linguagem-natural.md) já usam (ou usavam) modelos de linguagem estatísticos simples, bem menos sofisticados que um [LLM](modelo-de-linguagem-grande.md). Entender essa distinção evita tratar "modelo de linguagem" e "modelo de linguagem grande" como sinônimos, quando na verdade um é um caso específico — e muito mais recente — do outro.

## Exemplo

Um verificador ortográfico clássico de processador de texto, que sugere a próxima palavra mais provável com base nas palavras já digitadas, é um exemplo simples de modelo de linguagem — décadas mais simples e mais antigo do que ferramentas como o [ChatGPT](../ferramentas/chatgpt.md) ou o [Claude](../ferramentas/claude.md), construídas sobre modelos de linguagem grande, uma categoria específica e muito mais recente de modelo de linguagem.

## Não confunda com

Modelo de linguagem não é sinônimo de [modelo de linguagem grande (LLM)](modelo-de-linguagem-grande.md): todo LLM é um modelo de linguagem, mas nem todo modelo de linguagem é "grande" — modelos estatísticos simples (como os baseados em n-gramas) existem desde muito antes dos LLMs atuais, treinados com volumes de dados e número de parâmetros ordens de grandeza menores. Também não é sinônimo de [processamento de linguagem natural (PLN)](processamento-de-linguagem-natural.md): PLN é o campo de pesquisa mais amplo que estuda como computadores processam linguagem humana; um modelo de linguagem é um tipo específico de modelo usado dentro desse campo, não o campo inteiro.

## Termos relacionados

## Referências

- Jurafsky, Daniel; Martin, James H. *Speech and Language Processing* (3ª edição, rascunho online), Stanford University.
  [web.stanford.edu/~jurafsky/slp3/3.pdf](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
