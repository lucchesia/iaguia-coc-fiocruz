---
title: "Uniform Resource Identifier"
title_pt: "URI"
slug: "uri"

entry_type: "conceito"
concept_type: "padrão"

category: "acervos, patrimônio e infraestrutura digital"

tags:
  - fundamentos de computação

aliases:
  - "Uniform Resource Identifier"

related_terms:
  - rdf
prerequisites: []

references:
  - title: "RFC 3986 — Uniform Resource Identifier (URI): Generic Syntax | IETF"
    url: "https://www.rfc-editor.org/rfc/rfc3986"
    type: "padrão técnico institucional (IETF)"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# URI

## O que é

URI (Identificador Uniforme de Recurso, do inglês *Uniform Resource Identifier*) é uma sequência padronizada de caracteres usada para identificar de forma única um recurso — que pode ser uma página web, um documento, uma pessoa ou qualquer outra entidade, física ou abstrata. Segundo a norma técnica RFC 3986, que define o padrão, "um Identificador Uniforme de Recurso (URI) é uma sequência compacta de caracteres que identifica um recurso abstrato ou físico". Um endereço de página web comum é um tipo específico de URI, chamado URL (Localizador Uniforme de Recurso).

## Por que isso importa?

URIs são a base técnica que permite identificar, de forma única e sem ambiguidade, qualquer entidade referenciada em dados vinculados — uma pessoa histórica, um lugar, um conceito — de forma que sistemas diferentes possam apontar exatamente para a mesma coisa. Para projetos de pesquisa que constroem ou usam bases de dados conectadas, entender URIs ajuda a compreender por que "identificar" uma entidade da forma correta é tão importante quanto descrevê-la.

## Exemplo

Ao mencionar a cidade do Rio de Janeiro num conjunto de dados vinculados, uma pesquisadora usa a URI específica da Wikidata para essa cidade — em vez de apenas escrever o nome como texto livre —, o que evita ambiguidade com outras cidades de mesmo nome e permite que qualquer sistema que reconheça aquela URI saiba exatamente a qual lugar a pesquisa se refere.

## Não confunda com

URI não é sinônimo de URL: todo URL é um tipo de URI (aquele que indica como localizar e acessar o recurso, geralmente por HTTP), mas nem todo URI é um URL. Também não é sinônimo de nome ou rótulo comum: uma URI é projetada para ser única globalmente, diferente de um nome em linguagem natural, que pode se referir a várias coisas diferentes.

## Termos relacionados

## Referências

- IETF. *RFC 3986 — Uniform Resource Identifier (URI): Generic Syntax*.
  [rfc-editor.org/rfc/rfc3986](https://www.rfc-editor.org/rfc/rfc3986)
