---
title: "Prompt Engineering"
title_pt: "Engenharia de Prompt"
slug: "engenharia-de-prompt"

entry_type: "conceito"
concept_type: "técnica"

category: "interação com modelos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "prompt engineering"

related_terms:
  - prompt
prerequisites:
  - prompt

references:
  - title: "prompt engineering — Machine Learning Glossary: Generative AI | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary/generative#prompt-engineering"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Engenharia de Prompt

## O que é

Engenharia de prompt é a prática de elaborar e ajustar [prompts](prompt.md) de forma deliberada para obter respostas melhores ou mais precisas de um modelo de linguagem. Segundo o glossário técnico do Google for Developers, engenharia de prompt é "a arte de criar prompts que provocam as respostas desejadas de um modelo de linguagem grande". Isso envolve escolhas como o nível de detalhe do pedido, o formato de resposta solicitado, o fornecimento de exemplos do resultado esperado, ou instruções sobre o papel que o modelo deve assumir ao responder.

## Por que isso importa?

Para quem usa ferramentas de IA generativa em pesquisa e ensino, dominar noções básicas de engenharia de prompt costuma fazer diferença real na qualidade dos resultados obtidos — sem exigir conhecimento técnico de programação. Saber, por exemplo, dividir uma tarefa complexa em pedidos menores, fornecer contexto suficiente ou pedir explicitamente que o modelo justifique sua resposta são técnicas de engenharia de prompt que podem melhorar significativamente a utilidade de uma ferramenta como o [ChatGPT](../ferramentas/chatgpt.md) ou o [Claude](../ferramentas/claude.md) para tarefas de pesquisa.

## Exemplo

Em vez de pedir simplesmente "traduza este trecho de uma carta do século XIX", uma pesquisadora pratica engenharia de prompt ao especificar: "traduza este trecho de uma carta do século XIX preservando o registro formal da época, mantendo entre colchetes qualquer palavra cujo sentido seja ambíguo no original". Esse tipo de instrução mais elaborada tende a produzir um resultado mais adequado ao uso acadêmico do que um pedido genérico.

## Não confunda com

Engenharia de prompt não é sinônimo de prompt: prompt é o texto de entrada em si; engenharia de prompt é a prática — e o conjunto de técnicas — de elaborar prompts de forma eficaz. Também não é sinônimo de [ajuste fino](ajuste-fino.md): engenharia de prompt não altera o modelo em si — atua apenas na forma como a pessoa usuária se comunica com um modelo já pronto, sem exigir treinamento adicional nem acesso técnico ao modelo.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary: Generative AI* (entrada "prompt engineering").
  [developers.google.com/machine-learning/glossary/generative](https://developers.google.com/machine-learning/glossary/generative#prompt-engineering)
