---
title: "Large Language Model"
title_pt: "Modelo de Linguagem Grande"
slug: "modelo-de-linguagem-grande"

entry_type: "conceito"
concept_type: "conceito"

category: "modelos generativos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "LLM"
  - "large language model"
  - "grande modelo de linguagem"

related_terms:
  - modelo-fundamental
  - multimodalidade
  - transformador
  - modelo-de-linguagem
prerequisites:
  - modelo
  - ia-generativa

references:
  - title: "large language model (LLM) — Machine Learning Glossary: Generative AI | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary/generative#large-language-model-llm"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Modelo de Linguagem Grande

## O que é

Modelo de linguagem grande (LLM, do inglês *large language model*) é um tipo de [modelo](modelo.md) de [IA generativa](ia-generativa.md) treinado com volumes muito grandes de texto, capaz de prever, gerar e manipular linguagem humana com fluência. Segundo o glossário técnico do Google for Developers, um LLM é, no mínimo, "um modelo de linguagem com um número muito alto de parâmetros" — e, de forma mais informal, "qualquer modelo de linguagem baseado em [Transformer](transformador.md), como o Gemini ou o GPT". Na prática, um LLM funciona prevendo, fragmento por fragmento, qual é a continuação mais provável de um texto, com base em padrões aprendidos durante o pré-treinamento com enormes quantidades de texto.

## Por que isso importa?

A maioria das ferramentas de IA generativa voltadas a texto usadas em pesquisa e ensino — [ChatGPT](../ferramentas/chatgpt.md), [Claude](../ferramentas/claude.md), [Gemini](../ferramentas/gemini.md), [Mistral Vibe](../ferramentas/mistral-vibe.md) — é construída sobre um LLM. Entender que um LLM funciona prevendo a continuação mais provável de um texto, e não "sabendo" fatos da mesma forma que uma pessoa, ajuda a interpretar criticamente por que essas ferramentas podem produzir informações erradas com aparência de certeza (alucinações), por que seu desempenho varia conforme o idioma e o domínio de conhecimento, e por que não substituem a verificação em fontes primárias e na literatura acadêmica.

## Exemplo

Uma pesquisadora que usa o Claude para resumir um conjunto de artigos está, na prática, usando um LLM para prever qual sequência de palavras resume melhor o conteúdo enviado — por isso é importante conferir o resumo em relação aos textos originais.

## Não confunda com

LLM não é sinônimo de IA generativa: IA generativa é a categoria mais ampla, que inclui também modelos que geram imagem, áudio ou vídeo; LLM é especificamente o tipo de modelo voltado à geração de texto (embora LLMs também sirvam de base para alguns modelos com [multimodalidade](multimodalidade.md), capazes de lidar com mais de um tipo de conteúdo). Também não é sinônimo de [modelo de linguagem](modelo-de-linguagem.md) em geral: todo LLM é um modelo de linguagem, mas nem todo modelo de linguagem é "grande" — modelos de linguagem menores e mais simples existem há décadas em processamento de linguagem natural, antes do surgimento dos LLMs atuais.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary: Generative AI* (entrada "large language model (LLM)").
  [developers.google.com/machine-learning/glossary/generative](https://developers.google.com/machine-learning/glossary/generative#large-language-model-llm)
