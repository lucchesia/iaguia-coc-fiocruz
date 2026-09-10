---
title: "Linked Data"
title_pt: "Dados Vinculados"
slug: "dados-vinculados"

entry_type: "conceito"
concept_type: "método"

category: "acervos, patrimônio e infraestrutura digital"

tags:
  - fundamentos de computação

aliases:
  - "linked data"
  - "dados interligados"

related_terms:
  - linked-open-data
  - rdf
prerequisites:
  - rdf
  - uri

references:
  - title: "Linked Data — W3C Design Issues (Tim Berners-Lee)"
    url: "https://www.w3.org/DesignIssues/LinkedData.html"
    type: "padrão institucional de referência (W3C)"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Dados Vinculados

## O que é

Dados vinculados (*Linked Data*) é um método para publicar e conectar dados estruturados na web, de forma que diferentes conjuntos de dados possam ser interligados e explorados como uma rede, e não apenas como arquivos isolados. Segundo Tim Berners-Lee, criador da web e autor da proposta original de Linked Data, o método segue quatro regras: usar URIs como nomes para as coisas; usar URIs no formato HTTP, para que essas coisas possam ser consultadas; ao consultar uma URI, fornecer informação útil, usando padrões como RDF; e incluir links para outras URIs, para que mais coisas possam ser descobertas a partir dali.

## Por que isso importa?

Dados vinculados permitem que informações de fontes diferentes — um registro de uma pessoa histórica num arquivo, uma entrada sobre essa mesma pessoa numa enciclopédia, um mapa de um lugar associado a ela — sejam conectadas de forma explícita e legível por máquina, em vez de existirem como silos isolados. Para pesquisa em Humanidades, isso abre possibilidades de explorar relações entre acervos de instituições diferentes de forma automatizada.

## Exemplo

Um projeto de pesquisa sobre uma rede de correspondência histórica pode publicar seus dados como Linked Data, usando URIs para identificar cada pessoa, lugar e carta mencionados — permitindo que esses registros sejam conectados automaticamente a registros equivalentes em outras bases de dados históricas, como a Wikidata.

## Não confunda com

Dados vinculados não é sinônimo de dados abertos: dados vinculados descreve a forma técnica como os dados são estruturados e conectados; dados abertos se refere à licença sob a qual os dados são disponibilizados — um conjunto de dados vinculados pode ou não ser aberto. Quando os dois se combinam, o resultado é chamado especificamente de Linked Open Data. Também não é sinônimo de RDF: RDF é o formato técnico usado para representar dados vinculados; dados vinculados é o método e o conjunto de princípios mais amplos sobre como e por que publicar dados dessa forma.

## Termos relacionados

## Referências

- Berners-Lee, T. *Linked Data* (W3C Design Issues).
  [w3.org/DesignIssues/LinkedData.html](https://www.w3.org/DesignIssues/LinkedData.html)
