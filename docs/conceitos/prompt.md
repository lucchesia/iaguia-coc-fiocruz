---
title: "Prompt"
title_pt: "Prompt"
slug: "prompt"

entry_type: "conceito"
concept_type: "conceito"

category: "interação com modelos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases: []

related_terms:
  - engenharia-de-prompt
  - prompt-de-sistema
prerequisites:
  - modelo-de-linguagem-grande

references:
  - title: "prompt — Machine Learning Glossary: Generative AI | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary/generative#prompt"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Prompt

## O que é

Prompt é o texto (ou outro tipo de conteúdo, como uma imagem) enviado como entrada a um [modelo de linguagem](modelo-de-linguagem-grande.md), para orientar o tipo de resposta que ele deve produzir. Segundo o glossário técnico do Google for Developers, prompt é "qualquer texto inserido como entrada em um modelo de linguagem grande para condicionar o modelo a se comportar de determinada maneira". Em outras palavras: é a instrução, pergunta ou trecho de texto que a pessoa usuária escreve para pedir algo a uma ferramenta de IA generativa — um resumo, uma tradução, uma resposta a uma pergunta.

## Por que isso importa?

Como um modelo de linguagem gera sua resposta prevendo a continuação mais provável a partir do texto recebido, a forma como um prompt é escrito influencia diretamente a qualidade e a precisão da resposta. Para pesquisa e ensino, isso significa que pedidos vagos ou ambíguos tendem a gerar respostas genéricas ou imprecisas, enquanto prompts claros, específicos e com contexto suficiente — indicando, por exemplo, a área de conhecimento, o formato desejado ou restrições relevantes — tendem a produzir resultados mais úteis.

## Exemplo

Ao pedir para o [Claude](../ferramentas/claude.md) "resuma este texto", uma pesquisadora recebe um resumo genérico; ao escrever um prompt mais específico — "resuma este texto em três parágrafos, destacando os argumentos principais sobre a historiografia da escravidão no Brasil, mantendo os termos técnicos originais" — ela tende a receber um resultado mais próximo do que precisa. A escolha das palavras, do nível de detalhe e do contexto fornecido no prompt é o que molda a resposta do modelo.

## Não confunda com

Prompt não é sinônimo de pergunta: um prompt pode ser uma pergunta, mas também pode ser uma instrução, um exemplo a seguir, ou um trecho de texto para completar — qualquer entrada que direcione o comportamento do modelo. Também não é sinônimo de [engenharia de prompt](engenharia-de-prompt.md) ou de [prompt de sistema](prompt-de-sistema.md): prompt é o texto de entrada em si; os outros dois são conceitos relacionados, mas distintos.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary: Generative AI* (entrada "prompt").
  [developers.google.com/machine-learning/glossary/generative](https://developers.google.com/machine-learning/glossary/generative#prompt)
