---
title: "Linked Open Data"
title_pt: "Dados Abertos Vinculados"
slug: "linked-open-data"

entry_type: "conceito"
concept_type: "conceito"

category: "acervos, patrimônio e infraestrutura digital"

tags:
  - fundamentos de computação

aliases:
  - "LOD"
  - "linked open data"
  - "dados abertos interligados"

related_terms:
  - dados-vinculados
prerequisites:
  - dados-vinculados
  - codigo-aberto

references:
  - title: "Linked Data (5-star scheme) — W3C Design Issues (Tim Berners-Lee)"
    url: "https://www.w3.org/DesignIssues/LinkedData.html"
    type: "padrão institucional de referência (W3C)"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Dados Abertos Vinculados

## O que é

Linked Open Data (LOD) é dados vinculados disponibilizados sob uma licença aberta, que não impede seu reuso livre. Segundo Tim Berners-Lee, "Linked Open Data é Dados Vinculados publicados sob uma licença aberta, que não impede seu reuso gratuito". Berners-Lee também propôs um sistema de "cinco estrelas" para avaliar o grau de abertura de um conjunto de dados: uma estrela para dados disponíveis na web sob licença aberta, em qualquer formato; duas se também forem estruturados e legíveis por máquina; três se usarem um formato não proprietário; quatro se também usarem padrões abertos do W3C (como RDF); e cinco se, além de tudo isso, estiverem conectados aos dados de outras pessoas.

## Por que isso importa?

Projetos de acervos digitais e infraestrutura de pesquisa em Humanidades cada vez mais adotam princípios de Linked Open Data para tornar seus dados reutilizáveis por outras instituições, sem depender de acordos formais de compartilhamento — a Wikidata é um dos exemplos mais conhecidos dessa abordagem. Entender o sistema de cinco estrelas ajuda a avaliar, na prática, o grau de abertura de um conjunto de dados publicado por uma instituição de pesquisa.

## Exemplo

Um museu que publica o catálogo de sua coleção como Linked Open Data, identificando cada obra e artista com URIs conectadas à Wikidata, permite que pesquisadoras de outras instituições relacionem automaticamente essas obras a outras informações históricas já disponíveis, sem precisar reconstruir manualmente essas conexões.

## Não confunda com

Linked Open Data não é sinônimo de dados vinculados em geral: todo Linked Open Data é dados vinculados, mas nem todo dado vinculado é aberto — dados vinculados podem estar disponíveis sob licenças restritivas, sem deixar de seguir os princípios técnicos de Linked Data. Também não é sinônimo de código aberto: código aberto se refere à licença de software; Linked Open Data se refere à licença e à estrutura técnica de dados, não de programas.

## Termos relacionados

## Referências

- Berners-Lee, T. *Linked Data* (esquema de cinco estrelas, W3C Design Issues).
  [w3.org/DesignIssues/LinkedData.html](https://www.w3.org/DesignIssues/LinkedData.html)
