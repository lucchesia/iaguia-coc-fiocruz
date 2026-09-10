---
title: "Confabulation"
title_pt: "Alucinação"
slug: "alucinacao"

entry_type: "conceito"
concept_type: "conceito"

category: "limitações e letramento crítico"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "hallucination"
  - "confabulação"
  - "fabricação"

related_terms:
  - fundamentacao
prerequisites:
  - modelo-de-linguagem-grande

references:
  - title: "NIST AI 600-1: Artificial Intelligence Risk Management Framework — Generative Artificial Intelligence Profile"
    url: "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf"
    type: "padrão técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Alucinação

## O que é

Alucinação é o termo popularmente usado para descrever quando um modelo de linguagem produz uma informação incorreta ou inventada, mas apresentada com a mesma confiança de uma informação correta. O NIST prefere o termo técnico "confabulação", definido no documento AI 600-1 como "a produção de conteúdo apresentado com confiança, mas incorreto ou falso — conhecido popularmente como 'alucinações' ou 'fabricações' —, pelo qual pessoas usuárias podem ser enganadas ou levadas a erro". A mesma fonte observa que confabulações incluem tanto respostas que se desviam do que foi pedido no prompt quanto respostas que contradizem afirmações geradas anteriormente na mesma conversa — e destaca que os termos "alucinação" e "fabricação" antropomorfizam a IA generativa, o que é, em si, um risco adicional.

## Por que isso importa?

Alucinações são uma das limitações mais relevantes de ferramentas de IA generativa para uso em pesquisa: um modelo de linguagem pode inventar uma citação bibliográfica que não existe, atribuir uma frase à pessoa errada, ou descrever um evento histórico com detalhes fabricados — tudo com a mesma fluência e aparência de certeza de uma resposta correta. Entender que isso é uma característica estrutural do funcionamento desses modelos, e não uma falha ocasional e rara, reforça a necessidade de conferir qualquer informação factual gerada por IA em fontes confiáveis antes de usá-la em trabalhos acadêmicos.

## Exemplo

Uma pesquisadora que pede ao ChatGPT ou ao Claude uma lista de referências bibliográficas sobre um tema específico corre o risco de receber, entre referências reais, títulos, autores ou anos de publicação inventados, com formatação de citação impecável — só uma verificação em uma base de dados acadêmica real revela quais referências existem de fato.

## Não confunda com

Alucinação não é sinônimo de erro de fato qualquer: um modelo pode errar por limitações reais de conhecimento (informação desatualizada, por exemplo) sem "alucinar" no sentido técnico; alucinação especificamente descreve a geração de conteúdo inventado apresentado com confiança injustificada. Também não é sinônimo de viés algorítmico: viés algorítmico se refere a distorções sistemáticas relacionadas a grupos ou categorias sociais; alucinação é sobre a invenção de fatos, independentemente de qualquer grupo social envolvido.

## Termos relacionados

## Referências

- NIST. *AI 600-1: Artificial Intelligence Risk Management Framework — Generative Artificial Intelligence Profile*.
  [nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
