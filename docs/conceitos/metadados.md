---
title: "Metadata"
title_pt: "Metadados"
slug: "metadados"

entry_type: "conceito"
concept_type: "conceito"

category: "fundamentos"

tags:
  - fundamentos de computação

aliases:
  - "metadata"

related_terms: []
prerequisites:
  - dados

references:
  - title: "Understanding Metadata: What Is Metadata, and What Is It For? — NISO"
    url: "https://www.fidgeo.de/fileadmin/user_upload/2016/07/2017_01-NISO-understanding-metadata.pdf"
    type: "documento técnico de referência (NISO)"
  - title: "ANSI/NISO Z39.85 — The Dublin Core Metadata Element Set"
    url: "https://www.niso.org/publications/ansiniso-z3985-2012-dublin-core-metadata-element-set"
    type: "padrão técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Metadados

## O que é

Metadados são [dados](dados.md) estruturados que descrevem, explicam, localizam ou tornam mais fácil recuperar, usar ou gerenciar outro recurso — em outras palavras, "dados sobre dados". Segundo o guia de referência do NISO (National Information Standards Organization), metadados são justamente essa camada de informação estruturada que acompanha um dado ou recurso para torná-lo compreensível e localizável. Um padrão amplamente usado para organizar metadados é o Dublin Core, com 15 campos básicos (título, autor, data, formato, entre outros), reconhecido internacionalmente (ISO 15836, ANSI/NISO Z39.85).

## Por que isso importa?

Metadados são a espinha dorsal de qualquer sistema de organização de acervos digitais — sem eles, seria praticamente impossível buscar, filtrar ou entender a proveniência de um item numa coleção grande. Ferramentas usadas em pesquisa histórica para organizar coleções, como [Omeka S](../ferramentas/omeka-s.md), [Tainacan](../ferramentas/tainacan.md), [AtoM](../ferramentas/atom.md), [Zotero](../ferramentas/zotero.md) e [Tropy](../ferramentas/tropy.md), dependem fundamentalmente de metadados bem estruturados para funcionar. Padrões como o Dublin Core existem justamente para que sistemas diferentes "conversem" entre si, usando os mesmos campos padronizados — o que permite, por exemplo, que um acervo migre de uma plataforma para outra sem perder a estrutura da informação.

## Exemplo

Numa entrevista de história oral, o arquivo de áudio da entrevista é o dado; a data da gravação, o nome da pessoa entrevistada (com consentimento registrado), o local e a duração são metadados sobre essa entrevista. É esse tipo de metadado que uma ferramenta como o [SayMore](../ferramentas/saymore.md) ajuda a organizar sistematicamente no momento da coleta em campo — e que, depois, pode ser usado por uma ferramenta de acervo como o Omeka S para tornar a entrevista pesquisável dentro de uma coleção maior.

## Não confunda com

Metadados não são sinônimo de [dados](dados.md): metadados descrevem um dado ou recurso, mas não são o conteúdo em si — o áudio da entrevista é o dado; a ficha com informações sobre ele são os metadados. Também não são sinônimo de tags ou palavras-chave livres: metadados costumam seguir um padrão estruturado, com campos definidos (como os do Dublin Core: autor, data, formato), enquanto tags livres não seguem necessariamente nenhuma estrutura formal — embora uma tag possa, em certos sistemas, funcionar como um tipo específico de metadado.

## Termos relacionados

## Referências

- Riley, Jenn. *Understanding Metadata: What Is Metadata, and What Is It For?*. NISO, 2017.
  [fidgeo.de/.../2017_01-NISO-understanding-metadata.pdf](https://www.fidgeo.de/fileadmin/user_upload/2016/07/2017_01-NISO-understanding-metadata.pdf)
- NISO. *ANSI/NISO Z39.85 — The Dublin Core Metadata Element Set*.
  [niso.org/publications/ansiniso-z3985-2012-dublin-core-metadata-element-set](https://www.niso.org/publications/ansiniso-z3985-2012-dublin-core-metadata-element-set)
