---
title: "Resource Description Framework"
title_pt: "RDF"
slug: "rdf"

entry_type: "conceito"
concept_type: "padrão"

category: "acervos, patrimônio e infraestrutura digital"

tags:
  - fundamentos de computação

aliases:
  - "Resource Description Framework"

related_terms:
  - dados-vinculados
  - json
prerequisites:
  - uri
  - dados

references:
  - title: "RDF — W3C"
    url: "https://www.w3.org/RDF/"
    type: "padrão institucional de referência (W3C)"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# RDF

## O que é

RDF (*Resource Description Framework* — Framework de Descrição de Recursos) é um padrão do W3C para representar informação na forma de afirmações simples, compostas por três partes: sujeito, predicado e objeto (conhecidas como "triplas"). Segundo o próprio W3C, "RDF é um modelo padrão para intercâmbio de dados na web". Uma tripla RDF típica poderia afirmar, por exemplo, que "um manuscrito" (sujeito) "tem como autor" (predicado) "uma pessoa específica" (objeto) — cada elemento costuma ser identificado por uma URI, o que torna a afirmação legível e conectável por máquinas.

## Por que isso importa?

RDF é a base técnica sobre a qual dados vinculados são construídos — é o formato que permite representar relações entre entidades de forma padronizada e legível por máquina, essencial para conectar acervos de instituições diferentes. Para quem trabalha com infraestrutura de dados de pesquisa, entender RDF ajuda a compreender como plataformas como a Wikidata organizam e conectam milhões de afirmações sobre pessoas, lugares e eventos.

## Exemplo

Uma base de dados histórica que representa a afirmação "Napoleão Bonaparte nasceu em Ajácio" como uma tripla RDF permite que sistemas automatizados relacionem essa informação com outras triplas sobre Ajácio ou sobre Napoleão, construindo uma rede de conhecimento conectada e consultável.

## Não confunda com

RDF não é sinônimo de JSON ou XML: JSON e XML são formatos de arquivo genéricos que podem, entre outros usos, servir para representar dados RDF (nas variantes JSON-LD e RDF/XML); RDF é o modelo abstrato de dados, independente de qual formato de arquivo é usado para escrevê-lo. Também não é sinônimo de dados vinculados: RDF é o formato técnico usado para representar afirmações; dados vinculados é o método e os princípios mais amplos sobre como publicar e conectar esses dados na web.

## Termos relacionados

## Referências

- W3C. *RDF*.
  [w3.org/RDF](https://www.w3.org/RDF/)
