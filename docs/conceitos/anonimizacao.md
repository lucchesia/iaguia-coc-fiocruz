---
title: "Anonymization"
title_pt: "Anonimização"
slug: "anonimizacao"

entry_type: "conceito"
concept_type: "conceito"

category: "limitações e letramento crítico"

tags:
  - dados de pesquisa
  - privacidade

aliases:
  - "anonymization"
  - "dado anonimizado"

related_terms:
  - pseudonimizacao
  - lgpd
prerequisites:
  - dados

references:
  - title: "Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais)"
    url: "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm"
    type: "legislação"
  - title: "ANPD. Documentos técnicos e orientativos"
    url: "https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos"
    type: "documento técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-09-10"
---

# Anonimização

## O que é

Anonimização é o conjunto de técnicas que retira de um dado a possibilidade de associação a uma pessoa, direta ou indireta, considerando os meios técnicos razoáveis e disponíveis no momento do tratamento. Um dado efetivamente anonimizado deixa de ser dado pessoal e sai do alcance da [LGPD](lgpd.md). A condição é exigente: se o processo puder ser revertido com esforço razoável, o dado continua pessoal e a lei continua valendo.

## Por que isso importa?

Trocar nomes por códigos costuma ser chamado de anonimizar, e quase nunca é. Numa entrevista de história oral, o cargo, a instituição, a data de admissão e a doença mencionada podem identificar a pessoa sem que o nome apareça uma única vez. Tratar um material como anônimo quando ele não é leva a decisões erradas sobre o que publicar, o que depositar em repositório e o que enviar a um serviço de IA.

## Exemplo

Um corpus de entrevistas tem os nomes substituídos por E1, E2 e E3. Uma delas menciona "a única enfermeira do turno da noite do pavilhão em 1987". A troca do nome não impediu a identificação, porque a combinação de cargo, turno, local e ano é única naquele contexto. O material continua sendo dado pessoal.

## Não confunda com

Anonimização não é [pseudonimização](pseudonimizacao.md). Na pseudonimização existe uma chave que liga o código à pessoa, guardada em separado, e o dado segue sendo dado pessoal. Na anonimização não há chave e não há caminho de volta. Anonimização também não é sigilo nem embargo: esses restringem quem acessa, e o dado permanece identificável para quem tem acesso.

## Termos relacionados

- [Pseudonimização](pseudonimizacao.md)
- [LGPD](lgpd.md)

## Referências

- BRASIL. *Lei nº 13.709, de 14 de agosto de 2018*. Lei Geral de Proteção de Dados Pessoais (LGPD).
  [planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- ANPD. *Documentos técnicos e orientativos*.
  [gov.br/anpd](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos)
