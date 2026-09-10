---
title: "Training Data"
title_pt: "Dados de Treinamento"
slug: "dados-de-treinamento"

entry_type: "conceito"
concept_type: "conceito"

category: "aprendizado de máquina"

tags:
  - aprendizado de máquina
  - inteligência artificial

aliases:
  - "training data"
  - "conjunto de treinamento"
  - "dataset de treinamento"

related_terms:
  - treinamento
prerequisites:
  - aprendizado-de-maquina
  - dados

references:
  - title: "training set / training — Machine Learning Glossary | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary#training-set"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Dados de Treinamento

## O que é

Dados de treinamento são o conjunto de [dados](dados.md) usado para "ensinar" um sistema de [aprendizado de máquina](aprendizado-de-maquina.md) a reconhecer padrões, antes de ele ser testado ou usado em situações novas. Segundo o glossário técnico do Google for Developers, o "training set" é o subconjunto de um conjunto de dados usado para treinar um modelo — geralmente dividido em três partes: o conjunto de treinamento propriamente dito, um conjunto de validação (usado para ajustes durante o desenvolvimento) e um conjunto de teste (usado para avaliar o desempenho final em exemplos que o modelo nunca viu). Durante o treinamento, o sistema examina repetidamente os exemplos do conjunto de treinamento e ajusta gradualmente seus parâmetros internos para reduzir a diferença entre suas previsões e o resultado esperado.

## Por que isso importa?

A qualidade, o volume e a representatividade dos dados de treinamento determinam diretamente a qualidade e os limites de uma ferramenta de IA. Se um sistema de reconhecimento de fala foi treinado majoritariamente com um sotaque ou variante linguística específica, ele tende a ter desempenho pior com falas de grupos pouco representados nesse conjunto — uma questão especialmente relevante para projetos de história oral com comunidades sub-representadas nas bases usadas para treinar essas ferramentas. Entender isso ajuda a interpretar criticamente erros e vieses recorrentes nos resultados de ferramentas de IA.

## Exemplo

O [Whisper](../ferramentas/whisper.md) foi treinado com centenas de milhares de horas de áudio transcrito em várias línguas — esses áudios (e suas transcrições) são os dados de treinamento do modelo. Uma pesquisadora que usa o Whisper para transcrever entrevistas de história oral num dialeto regional pouco frequente nesse conjunto deve esperar mais erros de transcrição do que em falas semelhantes às que predominam nos dados de treinamento — e revisar o resultado com atenção redobrada.

## Não confunda com

Dados de treinamento não são sinônimo de dados em geral: são especificamente o subconjunto usado durante o processo de treinamento de um modelo — distinto do conjunto de teste (usado só para avaliar o modelo já pronto, sem influenciar seus parâmetros) e do conjunto de validação (usado para ajustes durante o desenvolvimento). Também não é sinônimo do processo de [treinamento](treinamento.md) em si: dados de treinamento são a matéria-prima; treinamento é o processo que usa esses dados para ajustar o modelo.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary* (entradas "training set" / "training").
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary#training-set)
