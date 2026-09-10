---
title: "Temperature"
title_pt: "Temperatura"
slug: "temperatura"

entry_type: "conceito"
concept_type: "conceito"

category: "modelos generativos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "temperature"

related_terms:
  - modelo-de-linguagem-grande
prerequisites:
  - modelo-de-linguagem-grande

references:
  - title: "temperature — Machine Learning Glossary: Generative AI | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary/generative#temperature"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Temperatura

## O que é

Temperatura é um parâmetro configurável que controla o grau de aleatoriedade das respostas geradas por um [modelo de linguagem](modelo-de-linguagem-grande.md). Segundo o glossário técnico do Google for Developers, temperatura é "um hiperparâmetro que controla o grau de aleatoriedade da saída de um modelo. Temperaturas mais altas resultam em saídas mais aleatórias, enquanto temperaturas mais baixas resultam em saídas menos aleatórias". Na prática, a cada token gerado, o modelo calcula várias possibilidades de continuação com diferentes probabilidades; a temperatura ajusta o quanto o modelo tende a escolher sempre a opção mais provável (temperatura baixa) ou a variar mais entre opções menos prováveis (temperatura alta).

## Por que isso importa?

Entender a temperatura ajuda a interpretar por que a mesma pergunta feita duas vezes a uma ferramenta de IA generativa pode gerar respostas diferentes, e por que algumas ferramentas produzem respostas mais previsíveis e outras, mais criativas ou variadas. Em tarefas de pesquisa que exigem precisão e consistência — como extrair informações factuais de um documento —, uma temperatura mais baixa tende a ser mais adequada; já em tarefas que envolvem geração de ideias ou variações de texto, uma temperatura mais alta pode ser útil.

## Exemplo

Algumas ferramentas de IA generativa, incluindo interfaces voltadas a programadores que usam modelos como o GPT ou o [Claude](../ferramentas/claude.md) por meio de API, permitem ajustar diretamente o valor da temperatura. Um valor baixo (próximo de 0) faz o modelo repetir quase sempre a mesma resposta para uma mesma pergunta; um valor mais alto introduz mais variação entre execuções diferentes da mesma tarefa.

## Não confunda com

Temperatura (o parâmetro de IA generativa) não tem relação com temperatura no sentido físico (grau de calor), nem com o "temperature sensor" do vocabulário técnico do NIST, usado em contextos de hardware e sensores industriais. Também não é sinônimo de qualidade da resposta: uma temperatura mais alta não torna a resposta "melhor" ou "mais inteligente" — apenas mais variada; dependendo da tarefa, uma temperatura mais alta pode até prejudicar a precisão do resultado.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary: Generative AI* (entrada "temperature").
  [developers.google.com/machine-learning/glossary/generative](https://developers.google.com/machine-learning/glossary/generative#temperature)
