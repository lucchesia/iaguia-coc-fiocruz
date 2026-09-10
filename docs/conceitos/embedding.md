---
title: "Embedding"
title_pt: "Embedding"
slug: "embedding"

entry_type: "conceito"
concept_type: "conceito"

category: "representação, busca e recuperação"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "vetor de embedding"
  - "embedding vector"

related_terms:
  - representacao-vetorial
prerequisites:
  - modelo-de-linguagem-grande
  - token

references:
  - title: "embedding vector — Machine Learning Glossary | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary#embedding-vector"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Embedding

## O que é

Embedding é uma representação numérica de uma palavra, frase, imagem ou outro tipo de dado, na forma de uma lista de números decimais (um vetor). Segundo o glossário técnico do Google for Developers, um vetor de embedding é "uma representação de uma palavra ou frase como uma lista de números de ponto flutuante. Cada dimensão do embedding captura alguma propriedade latente da palavra, melhorando a capacidade dos modelos de aprendizado de máquina de reconhecer padrões". Palavras ou trechos de texto com significados parecidos tendem a ter embeddings numericamente próximos entre si — é essa proximidade numérica que permite a um modelo "entender" relações de significado entre diferentes palavras ou textos.

## Por que isso importa?

Embeddings são a base técnica que permite a ferramentas de IA comparar o significado de textos diferentes de forma automática — por exemplo, encontrar documentos parecidos com um documento de referência, mesmo que não compartilhem as mesmas palavras exatas. Isso é especialmente relevante para pesquisa: ferramentas de busca e recuperação de literatura acadêmica usam embeddings para encontrar artigos relacionados a um tema, mesmo quando o vocabulário usado nos textos é diferente do vocabulário da busca original.

## Exemplo

Ao buscar artigos relacionados a "escravidão urbana no Brasil" numa ferramenta como o [Semantic Scholar](../ferramentas/semantic-scholar.md), o sistema não procura apenas essas palavras exatas — ele compara o embedding da busca com os embeddings de milhões de artigos, encontrando textos semanticamente próximos, mesmo que usem termos como "cativeiro nas cidades" ou "trabalho escravo urbano".

## Não confunda com

Embedding não é sinônimo de [token](token.md): token é a unidade de texto processada por um modelo; embedding é a representação numérica (o vetor) associada a essa unidade — ou a um trecho maior de texto. Também não é sinônimo de [representação vetorial](representacao-vetorial.md) em geral: embedding é um tipo específico de representação vetorial, produzido por um modelo treinado para capturar significado semântico — nem toda representação vetorial de dados é um embedding.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary* (entrada "embedding vector").
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary#embedding-vector)
