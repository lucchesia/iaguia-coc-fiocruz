---
title: "Foundation Model"
title_pt: "Modelo Fundamental"
slug: "modelo-fundamental"

entry_type: "conceito"
concept_type: "conceito"

category: "modelos generativos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "foundation model"
  - "modelo fundacional"

related_terms:
  - modelo-de-linguagem-grande
prerequisites:
  - modelo
  - pre-treinamento

references:
  - title: "foundation model — Glossary | NIST Computer Security Resource Center (citando NIST AI 100-2e2025)"
    url: "https://csrc.nist.gov/glossary/term/foundation_model"
    type: "glossário técnico institucional"
  - title: "foundation model / base model — Machine Learning Glossary | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary#foundation-model"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Modelo Fundamental

## O que é

Modelo fundamental (também chamado de "modelo fundacional", do inglês *foundation model*) é um [modelo](modelo.md) de IA treinado com um volume muito amplo e diverso de dados, de forma genérica, para depois servir de base a várias aplicações diferentes. Segundo o documento NIST AI 100-2e2025, um modelo fundamental é, em IA generativa, "um modelo treinado com dados amplos por meio de aprendizado autossupervisionado, que pode ser adaptado — por exemplo, por meio de ajuste fino — para uma variedade de tarefas subsequentes". Em vez de treinar um modelo do zero para cada tarefa específica (traduzir textos, transcrever áudio, responder perguntas), pesquisadores e empresas costumam partir de um único modelo fundamental, já [pré-treinado](pre-treinamento.md), e adaptá-lo para diferentes usos.

## Por que isso importa?

Boa parte das ferramentas de IA generativa usadas hoje em pesquisa e ensino — de assistentes de texto a sistemas de transcrição — é construída sobre um pequeno número de modelos fundamentais mantidos por grandes empresas de tecnologia, e não desenvolvida do zero por cada equipe que a utiliza. Entender isso ajuda a interpretar por que ferramentas de propósitos muito diferentes às vezes compartilham os mesmos pontos fortes e as mesmas limitações — porque, por trás delas, existe o mesmo modelo fundamental adaptado para tarefas diferentes.

## Exemplo

O Whisper é um exemplo de modelo fundamental voltado a áudio: foi pré-treinado uma única vez, pela OpenAI, com um grande volume de áudio em várias línguas, e passou a servir de base para diferentes aplicações — da transcrição automática de entrevistas de história oral em ferramentas como o [MacWhisper](../ferramentas/macwhisper.md) e o [Buzz](../ferramentas/buzz.md) a versões ajustadas por outras equipes para reconhecer melhor dialetos ou vocabulários específicos.

## Não confunda com

Modelo fundamental não é sinônimo de [modelo de linguagem grande](modelo-de-linguagem-grande.md) (LLM): todo LLM costuma ser um modelo fundamental voltado a texto, mas nem todo modelo fundamental é um LLM — existem modelos fundamentais voltados a áudio (como o Whisper), imagem ou outros tipos de dado. Também não é sinônimo de modelo pré-treinado em geral: um modelo fundamental é, além de pré-treinado, projetado especificamente para servir de base a múltiplas tarefas diferentes, e não apenas a uma única aplicação.

## Termos relacionados

## Referências

- NIST Computer Security Resource Center. *foundation model — Glossary* (citando NIST AI 100-2e2025).
  [csrc.nist.gov/glossary/term/foundation_model](https://csrc.nist.gov/glossary/term/foundation_model)
- Google for Developers. *Machine Learning Glossary* (entrada "foundation model" / "base model").
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary#foundation-model)
