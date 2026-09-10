---
title: "JavaScript Object Notation"
title_pt: "JSON"
slug: "json"

entry_type: "conceito"
concept_type: "formato"

category: "acervos, patrimônio e infraestrutura digital"

tags:
  - fundamentos de computação

aliases:
  - "JavaScript Object Notation"

related_terms:
  - rdf
prerequisites: []

references:
  - title: "Introducing JSON — json.org"
    url: "https://www.json.org/json-en.html"
    type: "padrão técnico de referência"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# JSON

## O que é

JSON (*JavaScript Object Notation* — Notação de Objetos JavaScript) é um formato leve de intercâmbio de dados, amplamente usado para estruturar e trocar informação entre sistemas diferentes na web. Segundo a definição oficial do formato, em json.org, "JSON é um formato leve de intercâmbio de dados". Apesar do nome fazer referência à linguagem de programação JavaScript, o JSON é independente de linguagem: pode ser lido e escrito por praticamente qualquer linguagem de programação atual, o que o tornou um dos formatos mais usados para APIs e arquivos de configuração.

## Por que isso importa?

Muitas ferramentas digitais usadas em pesquisa — de APIs de bases de dados acadêmicas a arquivos de configuração de ferramentas de análise — armazenam ou trocam dados no formato JSON. Reconhecer minimamente a estrutura de um arquivo JSON ajuda pesquisadoras a entender, ler ou até editar manualmente arquivos de dados exportados por diferentes ferramentas, mesmo sem formação técnica em programação.

## Exemplo

Ao exportar os resultados de uma busca da API do [Semantic Scholar](../ferramentas/semantic-scholar.md), uma pesquisadora recebe os dados em formato JSON — uma lista estruturada de artigos, cada um com campos como título, autores e ano, organizados de forma consistente e legível tanto por um script de análise quanto, com alguma familiaridade, por uma pessoa lendo o arquivo diretamente.

## Não confunda com

JSON não é sinônimo de RDF: RDF é um modelo abstrato de dados baseado em afirmações sujeito-predicado-objeto; JSON é um formato de arquivo genérico, que pode (na variante JSON-LD) ser usado para representar dados RDF, mas também serve para representar qualquer outro tipo de dado estruturado. Também não é sinônimo de XML: os dois são formatos usados para estruturar dados, mas com sintaxes bem diferentes — JSON costuma ser mais compacto e é o formato preferido de muitas APIs web modernas; XML é mais verboso, mas é a base de padrões como a TEI.

## Termos relacionados

## Referências

- json.org. *Introducing JSON*.
  [json.org/json-en.html](https://www.json.org/json-en.html)
