---
title: "Training"
title_pt: "Treinamento"
slug: "treinamento"

entry_type: "conceito"
concept_type: "conceito"

category: "aprendizado de máquina"

tags:
  - aprendizado de máquina
  - inteligência artificial

aliases:
  - "training"
  - "treino"

related_terms:
  - inferencia
prerequisites:
  - aprendizado-de-maquina
  - dados-de-treinamento

references:
  - title: "training — Machine Learning Glossary | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary#training"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Treinamento

## O que é

Treinamento é o processo pelo qual um sistema de [aprendizado de máquina](aprendizado-de-maquina.md) ajusta seus parâmetros internos a partir de exemplos, para melhorar seu desempenho numa tarefa. Segundo o glossário do Google for Developers, treinamento é "o processo de determinar os parâmetros ideais que compõem um modelo, examinando exemplos e ajustando gradualmente pesos e vieses". De forma simplificada, esse processo costuma seguir os seguintes passos: o modelo recebe um lote de exemplos dos [dados de treinamento](dados-de-treinamento.md); faz previsões sobre esses exemplos; essas previsões são comparadas com o resultado esperado (conhecido de antemão); os parâmetros internos do modelo são ajustados de acordo com a diferença entre a previsão e o resultado esperado; e o processo se repete muitas vezes, até que o desempenho do modelo pare de melhorar significativamente.

## Por que isso importa?

O treinamento é a etapa em que um modelo de IA "aprende" — e também a etapa mais cara computacionalmente e mais dependente da qualidade dos dados de treinamento usados. Para quem usa ferramentas prontas (como Whisper ou ChatGPT), entender o que é treinamento ajuda a diferenciar duas situações bem diferentes: usar um modelo já treinado (o caso mais comum em pesquisa e ensino) e treinar ou ajustar um modelo com dados próprios — o que exige recursos técnicos e computacionais bem maiores.

## Exemplo

O [eScriptorium](../ferramentas/escriptorium.md) permite treinar modelos de HTR (reconhecimento de escrita manuscrita) específicos para uma caligrafia, período ou coleção. Nesse processo de treinamento, a pesquisadora transcreve manualmente algumas páginas de um documento; o sistema ajusta repetidamente os parâmetros do modelo comparando suas previsões de transcrição com as transcrições corretas fornecidas, até conseguir reconhecer bem aquele tipo específico de caligrafia.

## Não confunda com

Treinamento não é sinônimo de [dados de treinamento](dados-de-treinamento.md): dados de treinamento são a matéria-prima (os exemplos usados); treinamento é o processo que usa esses dados para ajustar o modelo. Também não é sinônimo de [inferência](inferencia.md): treinamento é a etapa em que o modelo "aprende" a partir de exemplos; inferência é a etapa seguinte, em que o modelo já treinado é usado para produzir resultados sobre dados novos.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary* (entrada "training").
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary#training)
