---
title: "Vector Representation"
title_pt: "Representação Vetorial"
slug: "representacao-vetorial"

entry_type: "conceito"
concept_type: "conceito"

category: "representação, busca e recuperação"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "vector representation"
  - "feature vector"
  - "vetor de características"

related_terms:
  - embedding
prerequisites:
  - dados
  - modelo

references:
  - title: "feature vector — Machine Learning Glossary: ML Fundamentals | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary/fundamentals#feature-vector"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Representação Vetorial

## O que é

Representação vetorial é a prática de transformar um dado — uma palavra, uma imagem, uma medição, um documento inteiro — numa lista ordenada de números (um vetor), de forma que um sistema computacional consiga processá-lo matematicamente. Segundo o glossário técnico do Google for Developers, um "vetor de características" (*feature vector*) é "o conjunto de valores de características que compõem um exemplo" — em outras palavras, os valores numéricos que compõem um exemplo usado por um [modelo](modelo.md). Modelos de aprendizado de máquina não processam texto, imagens ou som diretamente: precisam primeiro que esses dados sejam convertidos em vetores numéricos.

## Por que isso importa?

Entender que qualquer tipo de dado processado por um modelo de IA precisa antes ser convertido em números ajuda a compreender por que a forma como esses números são calculados — quais características são capturadas, quais são ignoradas — influencia diretamente o que o modelo consegue "perceber" sobre um dado. Isso é relevante para avaliar criticamente ferramentas de IA que processam fontes de pesquisa: uma imagem de documento histórico, por exemplo, é representada por um vetor que captura certas características visuais, mas não necessariamente o contexto histórico ou arquivístico daquele documento.

## Exemplo

Ao processar uma coleção de fotografias históricas digitalizadas, uma ferramenta de IA converte cada imagem numa representação vetorial — uma lista de números que descreve características visuais como cores, formas e texturas presentes na imagem. É a partir dessa representação numérica, e não da imagem "em si", que a ferramenta consegue comparar fotografias entre si ou agrupá-las por semelhança visual.

## Não confunda com

Representação vetorial não é sinônimo de [embedding](embedding.md): embedding é um tipo específico de representação vetorial, produzido por um modelo treinado especificamente para capturar significado semântico — representação vetorial é o conceito mais amplo, que também inclui vetores construídos de outras formas (por exemplo, contando a frequência de palavras num texto, sem nenhum aprendizado envolvido). Todo embedding é uma representação vetorial, mas nem toda representação vetorial é um embedding.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary: ML Fundamentals* (entrada "feature vector").
  [developers.google.com/machine-learning/glossary/fundamentals](https://developers.google.com/machine-learning/glossary/fundamentals#feature-vector)
