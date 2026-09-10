---
title: "Token"
title_pt: "Token"
slug: "token"

entry_type: "conceito"
concept_type: "conceito"

category: "modelos generativos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "tokens"

related_terms:
  - janela-de-contexto
prerequisites:
  - modelo-de-linguagem-grande

references:
  - title: "What is a token? — Introduction to Large Language Models | Google for Developers (Machine Learning Crash Course)"
    url: "https://developers.google.com/machine-learning/crash-course/llm"
    type: "documentação técnica"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Token

## O que é

Token é a menor unidade de texto que um [modelo de linguagem](modelo-de-linguagem-grande.md) processa — pode ser uma palavra inteira, parte de uma palavra (uma "subpalavra") ou até um único caractere. Segundo o curso técnico do Google for Developers sobre LLMs, "um token pode ser uma palavra, uma subpalavra... ou até um único caractere", e "tokens são a unidade atômica, a menor unidade do processamento de linguagem". Modelos de linguagem atuais costumam dividir o texto em subpalavras com algum significado: a palavra "unwatched" (em inglês), por exemplo, pode ser dividida em três tokens ("un", "watch" e "ed"). Em português, de forma aproximada, um token corresponde a cerca de 3/4 de uma palavra.

## Por que isso importa?

Ferramentas de IA generativa baseadas em LLM costumam cobrar (ou limitar o uso gratuito) por token processado, não por palavra ou por caractere — entender essa unidade ajuda a interpretar limites de uso e custos de ferramentas como o [ChatGPT](../ferramentas/chatgpt.md) ou o [Claude](../ferramentas/claude.md). Além disso, o tamanho máximo de texto que um modelo consegue processar de uma vez também é medido em tokens, não em páginas ou palavras — o que é relevante, por exemplo, ao enviar um documento longo de pesquisa para uma ferramenta de IA resumir.

## Exemplo

Ao enviar a transcrição de uma entrevista de história oral para o Claude resumir, o texto inteiro é primeiro dividido em tokens antes de ser processado pelo modelo — um documento de dez páginas pode se transformar em alguns milhares de tokens. Se o documento ultrapassar o limite de tokens que o modelo consegue processar de uma vez, pode ser necessário dividir o texto em partes menores.

## Não confunda com

"Token" tem outro significado bastante comum em segurança da informação — um dispositivo físico ou digital usado para autenticar a identidade de uma pessoa (como o segundo fator de autenticação de um login). É esse o sentido presente em praticamente todas as definições do glossário técnico do NIST. O sentido usado neste verbete — unidade de texto processada por um modelo de linguagem — é específico do campo de processamento de linguagem natural e IA, sem relação com aquele outro uso.

## Termos relacionados

## Referências

- Google for Developers. *Introduction to Large Language Models* (Machine Learning Crash Course).
  [developers.google.com/machine-learning/crash-course/llm](https://developers.google.com/machine-learning/crash-course/llm)
