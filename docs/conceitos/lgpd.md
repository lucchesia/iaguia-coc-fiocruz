---
title: "Brazilian General Data Protection Law"
title_pt: "LGPD"
slug: "lgpd"

entry_type: "conceito"
concept_type: "conceito"

category: "limitações e letramento crítico"

tags:
  - dados de pesquisa
  - privacidade

aliases:
  - "Lei Geral de Proteção de Dados Pessoais"
  - "Lei nº 13.709/2018"

related_terms:
  - anonimizacao
  - pseudonimizacao
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

# LGPD

## O que é

A LGPD, Lei nº 13.709/2018, é a lei brasileira que regula o tratamento de dados pessoais por pessoa física ou jurídica, de direito público ou privado. Ela alcança a pesquisa acadêmica sempre que o trabalho envolve dados que identificam ou permitem identificar alguém: entrevistas, prontuários, fichas de acervo, cadastros, imagens de pessoas. A lei organiza o que se pode fazer com esses dados em torno de bases legais, entre elas o consentimento e a realização de estudos por órgão de pesquisa, e atribui obrigações a quem trata os dados.

## Por que isso importa?

Ferramentas de [IA generativa](ia-generativa.md) processam em servidores de terceiros o que recebem. Enviar a transcrição de uma entrevista, uma lista de pacientes ou um documento de acervo com nomes para um serviço na nuvem é uma operação de tratamento de dados pessoais, e a LGPD se aplica a ela. Isso muda decisões práticas: que ferramenta usar, o que se pode enviar, o que precisa rodar no próprio computador e o que declarar no projeto e no termo de consentimento.

## Exemplo

Uma pesquisa de história oral grava trinta entrevistas com trabalhadores da saúde. Transcrever esses áudios num serviço web significa enviar voz e nome de pessoas identificáveis a uma empresa terceira. Transcrever com um modelo instalado no próprio computador mantém o áudio na máquina. As duas rotas produzem a mesma transcrição, e só uma delas é uma transferência de dados pessoais a terceiros.

## Não confunda com

A LGPD não substitui a aprovação de um comitê de ética em pesquisa. As duas exigências convivem: o comitê avalia o desenho da pesquisa com seres humanos, e a LGPD regula o tratamento de dados pessoais em qualquer contexto, inclusive fora da pesquisa. Ela também não se confunde com sigilo: sigilo é uma restrição de acesso, e um dado pessoal pode ser de acesso público e ainda assim estar protegido pela lei.

## Termos relacionados

- [Anonimização](anonimizacao.md)
- [Pseudonimização](pseudonimizacao.md)

## Referências

- BRASIL. *Lei nº 13.709, de 14 de agosto de 2018*. Lei Geral de Proteção de Dados Pessoais (LGPD).
  [planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- ANPD. *Documentos técnicos e orientativos*.
  [gov.br/anpd](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos)
