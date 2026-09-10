---
title: "Context Window"
title_pt: "Janela de Contexto"
slug: "janela-de-contexto"

entry_type: "conceito"
concept_type: "conceito"

category: "modelos generativos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "context window"

related_terms:
  - token
prerequisites:
  - token
  - modelo-de-linguagem-grande

references:
  - title: "context window — Machine Learning Glossary | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary#context-window"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Janela de Contexto

## O que é

Janela de contexto é o número máximo de [tokens](token.md) que um [modelo de linguagem](modelo-de-linguagem-grande.md) consegue processar de uma vez, somando o texto de entrada (prompt) e a resposta gerada. Segundo o glossário técnico do Google for Developers, janela de contexto é "o número de tokens que um modelo consegue processar em um determinado prompt. Quanto maior a janela de contexto, mais informação o modelo pode usar para fornecer respostas coerentes e consistentes ao prompt". Uma vez ultrapassado esse limite, o modelo passa a "esquecer" as partes mais antigas do texto, ou simplesmente não consegue processar o conteúdo enviado.

## Por que isso importa?

A janela de contexto determina, na prática, quanto texto uma pesquisadora consegue enviar de uma vez para uma ferramenta de IA generativa — um documento muito longo, um conjunto grande de artigos ou uma transcrição extensa de entrevista pode ultrapassar esse limite e precisar ser dividido em partes menores. Diferentes ferramentas e diferentes versões de um mesmo modelo têm janelas de contexto de tamanhos bem diferentes, o que é um critério relevante na hora de escolher uma ferramenta para lidar com documentos longos.

## Exemplo

Ao tentar enviar a transcrição completa de várias horas de entrevistas de história oral de uma vez para o [ChatGPT](../ferramentas/chatgpt.md) ou o [Claude](../ferramentas/claude.md) resumirem, uma pesquisadora pode esbarrar no limite da janela de contexto do modelo — nesse caso, é preciso dividir o material em partes menores, resumir cada parte separadamente e depois combinar os resumos.

## Não confunda com

Janela de contexto não é sinônimo de memória de longo prazo de uma ferramenta de IA: a janela de contexto se refere apenas ao texto processado numa única interação (ou conversa); recursos como "memória" entre conversas diferentes, oferecidos por algumas ferramentas, funcionam de outra forma — geralmente resumindo ou armazenando informações fora da janela de contexto do modelo, para reintroduzi-las depois. Também não é sinônimo de token: token é a unidade de medida; janela de contexto é o limite de quantos tokens cabem numa interação.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary* (entrada "context window").
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary#context-window)
