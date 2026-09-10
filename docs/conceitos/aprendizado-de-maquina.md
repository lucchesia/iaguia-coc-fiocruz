---
title: Machine Learning
title_pt: Aprendizado de Máquina
slug: aprendizado-de-maquina

entry_type: conceito
concept_type: conceito

category: aprendizado de máquina

tags:
  - aprendizado de máquina
  - inteligência artificial

aliases:
  - ML
  - machine learning
  - aprendizagem de máquina

related_terms: []
prerequisites:
  - algoritmo

references:
  - title: "Machine Learning — Glossary | NIST Computer Security Resource Center"
    url: "https://csrc.nist.gov/glossary/term/machine_learning"
    type: "glossário técnico institucional"
  - title: "Glossário de Termos Relacionados à IA — Governo Federal do Brasil"
    url: "https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/glossario-de-termos-relacionados-a-ia"
    type: "glossário institucional"
  - title: "Machine Learning Glossary — Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary"
    type: "glossário técnico"

status: publicado
reviewed: true
last_reviewed: '2026-08-19'
---

# Aprendizado de Máquina

## O que é

Aprendizado de máquina (do inglês *machine learning*) é o subcampo da [inteligência artificial](inteligencia-artificial.md) que desenvolve algoritmos e modelos capazes de melhorar seu desempenho em uma tarefa a partir de experiência — ou seja, a partir de dados —, em vez de seguir apenas instruções explicitamente programadas por uma pessoa para cada situação possível. O sistema "aprende" padrões nos dados que recebe, e usa esses padrões para lidar com casos novos.

## Por que isso importa?

Muitas ferramentas digitais usadas em pesquisa e ensino — de reconhecimento automático de fala a recomendação de artigos relacionados — funcionam com aprendizado de máquina por trás da interface. Entender essa diferença ajuda a interpretar criticamente os resultados dessas ferramentas: um sistema de aprendizado de máquina não segue regras fixas escritas por um programador para cada caso, mas generaliza a partir de exemplos vistos durante o treinamento — o que explica por que ele pode acertar em situações parecidas com as que "aprendeu" e errar em situações muito diferentes, incomuns ou mal representadas nos dados de treinamento.

## Exemplo

O [Whisper](../ferramentas/whisper.md), modelo de reconhecimento automático de fala usado para transcrever entrevistas de história oral, não tem uma lista de regras escritas manualmente para cada palavra e sotaque possível. Em vez disso, foi treinado com milhares de horas de áudio já transcrito, e "aprendeu" a associar padrões sonoros a palavras. É por isso que esse tipo de ferramenta tende a transcrever melhor sotaques e vocabulários semelhantes aos que apareceram nos dados de treinamento, e pode ter mais dificuldade com falas de grupos ou regiões pouco representados nesses dados — uma limitação relevante para projetos de história oral com comunidades sub-representadas.

## Não confunda com

Aprendizado de máquina não é sinônimo de [algoritmo](algoritmo.md): todo sistema de aprendizado de máquina usa algoritmos, mas nem todo algoritmo envolve aprendizado de máquina (um algoritmo de ordenação alfabética, por exemplo, não "aprende" nada — apenas segue passos fixos). Também não é sinônimo de "inteligência artificial": aprendizado de máquina é uma abordagem específica dentro do campo mais amplo da IA, que inclui outras técnicas que não envolvem aprendizado a partir de dados.

## Referências

- NIST Computer Security Resource Center. *Machine Learning — Glossary*.
  [csrc.nist.gov/glossary/term/machine_learning](https://csrc.nist.gov/glossary/term/machine_learning)
- Governo Federal do Brasil. *Glossário de Termos Relacionados à IA* (Estratégia Brasileira de Inteligência Artificial).
  [gov.br/governodigital](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/glossario-de-termos-relacionados-a-ia)
- Google for Developers. *Machine Learning Glossary*.
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary)
