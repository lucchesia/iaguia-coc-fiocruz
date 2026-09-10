---
title: "Few-shot Prompting"
title_pt: "Few-shot"
slug: "few-shot"

entry_type: "conceito"
concept_type: "técnica"

category: "interação com modelos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "few-shot prompting"
  - "few-shot learning"

related_terms:
  - zero-shot
prerequisites:
  - prompt
  - zero-shot

references:
  - title: "few-shot prompting — Machine Learning Glossary: Generative AI | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary/generative#few-shot-prompting"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Few-shot

## O que é

Few-shot é uma forma de usar um modelo de linguagem em que o [prompt](prompt.md) inclui um ou mais exemplos de como a resposta deve ser, antes de pedir a tarefa em si. Segundo o glossário técnico do Google for Developers, um prompt few-shot é "um prompt que contém mais de um exemplo (uns 'poucos' exemplos) demonstrando como o modelo de linguagem grande deve responder". Essa técnica costuma produzir resultados melhores do que um pedido [zero-shot](zero-shot.md) (sem nenhum exemplo), embora exija um prompt mais longo.

## Por que isso importa?

Fornecer exemplos dentro do prompt é uma das técnicas mais simples e eficazes de engenharia de prompt para tarefas que exigem um formato específico — por exemplo, aplicar uma convenção particular de transcrição, seguir um estilo de citação específico, ou classificar textos segundo categorias definidas pela própria pesquisadora. Em vez de tentar descrever em palavras exatamente o que se espera, mostrar um ou dois exemplos do resultado desejado costuma comunicar a tarefa de forma mais clara ao modelo.

## Exemplo

Em vez de pedir simplesmente "classifique estes trechos de cartas históricas por tema" (um pedido zero-shot), uma pesquisadora usa few-shot ao incluir no prompt dois ou três exemplos já classificados por ela mesma — mostrando o formato exato de categoria que deseja — antes de pedir para o modelo classificar o restante das cartas seguindo o mesmo padrão.

## Não confunda com

Few-shot não é sinônimo de zero-shot: zero-shot é um prompt sem nenhum exemplo; few-shot é um prompt com um ou mais exemplos. Também não é sinônimo de [ajuste fino](ajuste-fino.md): fornecer exemplos num prompt (few-shot) não altera o modelo em si nem exige treinamento adicional — é apenas uma forma de comunicar a tarefa dentro de uma única interação; ajuste fino, por outro lado, modifica de fato os parâmetros internos do modelo.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary: Generative AI* (entrada "few-shot prompting").
  [developers.google.com/machine-learning/glossary/generative](https://developers.google.com/machine-learning/glossary/generative#few-shot-prompting)
