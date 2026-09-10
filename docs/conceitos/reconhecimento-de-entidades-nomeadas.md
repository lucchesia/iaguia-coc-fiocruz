---
title: "Named Entity Recognition"
title_pt: "Reconhecimento de Entidades Nomeadas"
slug: "reconhecimento-de-entidades-nomeadas"

entry_type: "conceito"
concept_type: "técnica"

category: "linguagem, documentos, imagem e áudio"

tags:
  - inteligência artificial
  - aprendizado de máquina

aliases:
  - "NER"
  - "named entity recognition"

related_terms:
  - processamento-de-linguagem-natural
prerequisites:
  - processamento-de-linguagem-natural

references:
  - title: "Named-entity recognition — Wikipédia"
    url: "https://en.wikipedia.org/wiki/Named-entity_recognition"
    type: "enciclopédia colaborativa (apoio)"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Reconhecimento de Entidades Nomeadas

## O que é

NER (Reconhecimento de Entidades Nomeadas, do inglês *Named Entity Recognition*) é uma tarefa de [processamento de linguagem natural](processamento-de-linguagem-natural.md) que identifica e classifica, dentro de um texto, menções a entidades específicas — como nomes de pessoas, lugares, organizações, datas ou valores monetários. Segundo a Wikipédia, reconhecimento de entidades nomeadas "é uma subtarefa de extração de informação que busca localizar e classificar entidades nomeadas mencionadas em texto não estruturado em categorias pré-definidas, como nomes de pessoas, organizações, locais, entidades geopolíticas, códigos médicos, expressões temporais, quantidades, valores monetários, percentuais, entre outras".

## Por que isso importa?

NER é útil para pesquisa em Humanidades porque permite extrair automaticamente, de grandes coleções de texto, listas de pessoas, lugares e datas mencionados — uma etapa que, feita manualmente, levaria muito tempo em corpora extensos, como coleções de correspondência, processos judiciais históricos ou jornais digitalizados. Entender que o NER depende de categorias pré-definidas e de um modelo treinado ajuda a interpretar por que nomes incomuns, grafias antigas ou entidades específicas de um contexto histórico podem não ser reconhecidos corretamente por ferramentas genéricas.

## Exemplo

Ao processar um conjunto de cartas do século XIX com uma ferramenta de análise textual que usa NER, uma pesquisadora pode extrair automaticamente uma lista de todos os nomes de pessoas e lugares mencionados na coleção, para depois construir uma rede de relações entre essas entidades — uma etapa preparatória comum em projetos de análise de redes históricas.

## Não confunda com

NER não é sinônimo de PLN: PLN é o campo mais amplo de processamento de linguagem; NER é uma tarefa específica dentro desse campo. Também não é sinônimo de controle de autoridade (usado em descrição arquivística): NER é um processo automatizado de extração a partir do texto; controle de autoridade é um processo de descrição e normalização de nomes, geralmente feito com curadoria humana, dentro de um padrão como os usados em arquivos e bibliotecas.

## Termos relacionados

## Referências

- Wikipédia. *Named-entity recognition*.
  [en.wikipedia.org/wiki/Named-entity_recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)
