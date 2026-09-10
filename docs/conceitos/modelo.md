---
title: "Model"
title_pt: "Modelo"
slug: "modelo"

entry_type: "conceito"
concept_type: "conceito"

category: "fundamentos"

tags:
  - fundamentos de computação

aliases:
  - "model"

related_terms:
  - aprendizado-de-maquina
  - ia-generativa
prerequisites:
  - algoritmo

references:
  - title: "Scientific modeling — Encyclopedia Britannica"
    url: "https://www.britannica.com/science/scientific-modeling"
    type: "referência enciclopédica"
  - title: "artificial intelligence model — Glossary | NIST CSRC"
    url: "https://csrc.nist.gov/glossary/term/artificial_intelligence_model"
    type: "glossário técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Modelo

## O que é

Um modelo é uma representação simplificada de algo — um objeto, um processo, um sistema — construída para entender ou prever esse algo sem precisar lidar com toda a sua complexidade real. A ideia vem da ciência em geral, não só da computação: um modelo pode ser físico, conceitual ou matemático. Em [inteligência artificial](inteligencia-artificial.md), um modelo tem um sentido mais específico: é o resultado do treinamento de um [algoritmo](algoritmo.md) sobre um conjunto de dados — um componente que recebe uma entrada e produz uma saída (uma previsão, uma classificação, um texto gerado), com base em padrões capturados durante esse treinamento.

## Por que isso importa?

Quando uma ferramenta diz que "usa um modelo de IA", isso significa algo bem específico: não é o algoritmo em si, mas o resultado de um processo de treinamento sobre dados — e a qualidade desse resultado depende diretamente de quais dados foram usados nesse treinamento. Um modelo treinado majoritariamente com dados em inglês, por exemplo, tende a ter desempenho pior em português. Entender "modelo" como um produto de treinamento, e não como uma regra fixa escrita por uma pessoa, ajuda a interpretar por que ferramentas de IA erram de formas específicas — geralmente relacionadas a lacunas ou vieses nos dados usados para treiná-las.

## Exemplo

O [Whisper](../ferramentas/whisper.md), usado para transcrever entrevistas de história oral, é um modelo: foi treinado com milhares de horas de áudio já transcrito, e o resultado desse treinamento — os padrões capturados — é o que permite a ele transformar novos áudios em texto. Fora do contexto de IA, um exemplo mais tradicional de "modelo" em pesquisa histórica seria um modelo demográfico usado para estimar a população de uma região no passado a partir de registros fragmentários — uma representação simplificada da realidade, construída para permitir inferências que os dados brutos, sozinhos, não permitiriam.

## Não confunda com

Modelo não é sinônimo de [algoritmo](algoritmo.md): o algoritmo é o processo usado para treinar (ou para usar) um modelo; o modelo é o resultado desse processo — os padrões capturados, prontos para gerar novas saídas. Também não é sinônimo dos dados usados para treiná-lo: os dados de treinamento são a matéria-prima; o modelo é o que resulta de processá-los por meio de um algoritmo de aprendizado. Um mesmo algoritmo de treinamento, aplicado a dados diferentes, produz modelos diferentes.

## Termos relacionados

## Referências

- Encyclopedia Britannica. *Scientific modeling*.
  [britannica.com/science/scientific-modeling](https://www.britannica.com/science/scientific-modeling)
- NIST Computer Security Resource Center. *artificial intelligence model — Glossary*.
  [csrc.nist.gov/glossary/term/artificial_intelligence_model](https://csrc.nist.gov/glossary/term/artificial_intelligence_model)
