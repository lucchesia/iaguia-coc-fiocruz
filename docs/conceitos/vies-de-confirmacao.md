---
title: "Confirmation Bias"
title_pt: "Viés de Confirmação"
slug: "vies-de-confirmacao"

entry_type: "conceito"
concept_type: "conceito"

category: "limitações e letramento crítico"

tags:
  - ia generativa
  - método de pesquisa

aliases:
  - "confirmation bias"

related_terms:
  - vies-algoritmico
  - engenharia-de-prompt
prerequisites:
  - ia-generativa

references:
  - title: "NICKERSON, Raymond S. Confirmation bias: a ubiquitous phenomenon in many guises. Review of General Psychology, v. 2, n. 2, p. 175-220, 1998"
    url: "https://doi.org/10.1037/1089-2680.2.2.175"
    type: "artigo de revisão"

status: "publicado"
reviewed: true
last_reviewed: "2026-09-10"
---

# Viés de Confirmação

## O que é

Viés de confirmação é a tendência humana de buscar, notar e valorizar as informações que confirmam o que já se pensa, submetendo a escrutínio maior as que contrariam. É um padrão amplamente documentado na psicologia cognitiva desde os anos 1960, e opera sem que a pessoa perceba.

## Por que isso importa?

Ferramentas de [IA generativa](ia-generativa.md) são muito boas em confirmar. Elas geram a continuação mais provável do que receberam, então uma pergunta que já embute uma hipótese tende a receber uma resposta que a sustenta. Perguntar "quais evidências mostram que X causou Y" produz uma lista de evidências para X, exista ou não essa relação. O modelo não avalia a premissa, ele a desenvolve. O viés que já estava em quem pergunta volta amplificado e com aparência de levantamento.

## Exemplo

Uma pesquisadora convencida de que certa instituição resistiu a uma política pública pede ao modelo exemplos dessa resistência. Recebe uma lista convincente, e alguns itens são invenção. A [alucinação](alucinacao.md) do modelo explica parte do erro. A pergunta explica o resto: ela pedia confirmação em vez de teste. Reformulada como "que evidências existem a favor e contra a hipótese de que a instituição resistiu", a mesma ferramenta devolve os dois lados.

## Não confunda com

Viés de confirmação não é [viés algorítmico](vies-algoritmico.md). O algorítmico é distorção sistemática do sistema, herdada dos dados de treinamento e das escolhas de desenvolvimento. O de confirmação está em quem pergunta e em como pergunta. Os dois se combinam com facilidade, e a combinação é pior que cada um isolado.

## Termos relacionados

- [Viés Algorítmico](vies-algoritmico.md)
- [Alucinação](alucinacao.md)
- [Engenharia de Prompt](engenharia-de-prompt.md)

## Referências

- NICKERSON, Raymond S. Confirmation bias: a ubiquitous phenomenon in many guises. *Review of General Psychology*, v. 2, n. 2, p. 175-220, 1998.
  [doi.org/10.1037/1089-2680.2.2.175](https://doi.org/10.1037/1089-2680.2.2.175)
