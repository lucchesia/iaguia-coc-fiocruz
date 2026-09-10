---
title: "Open Model"
title_pt: "Modelo Aberto"
slug: "modelo-aberto"

entry_type: "conceito"
concept_type: "conceito"

category: "abertura e infraestrutura"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "open model"
  - "open source AI"

related_terms:
  - pesos-abertos
prerequisites:
  - modelo
  - codigo-aberto

references:
  - title: "The Open Source AI Definition – 1.0 — Open Source Initiative (OSI)"
    url: "https://opensource.org/ai/open-source-ai-definition"
    type: "padrão institucional de referência"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Modelo Aberto

## O que é

Modelo aberto é um termo usado, com graus variados de precisão, para descrever modelos de IA disponibilizados publicamente com algum nível de abertura — o que pode significar desde apenas os pesos do modelo disponíveis para download até, no sentido mais completo, tudo o que seria necessário para reproduzir o modelo do zero. A Open Source Initiative (OSI), organização que também define [código aberto](codigo-aberto.md) para software tradicional, publicou em 2024 a "Open Source AI Definition", que exige que um modelo verdadeiramente aberto forneça "acesso à forma preferencial de fazer modificações no sistema" — incluindo informação detalhada sobre os dados de treinamento, o código-fonte completo usado para treinar e executar o modelo, e os parâmetros do modelo (os pesos). Nem todo "modelo aberto", no uso corrente do termo, atende a esse padrão mais rigoroso.

## Por que isso importa?

O uso impreciso do termo "modelo aberto" pode levar a uma falsa impressão de transparência total: muitos modelos anunciados como "abertos" disponibilizam apenas os pesos, sem os dados de treinamento ou o código usado para treiná-los — o que impede verificar de fato como o modelo foi construído ou reproduzir o processo de treinamento de forma independente. Para pesquisa, essa distinção importa na hora de avaliar reivindicações de "abertura" feitas por ferramentas de IA: um modelo verdadeiramente aberto, no sentido da definição da OSI, permite um nível de escrutínio muito maior do que um modelo que apenas libera seus pesos.

## Exemplo

Modelos como os da família Llama (Meta) costumam ser descritos como "modelos abertos", mas na prática disponibilizam apenas os pesos treinados, sob uma licença com algumas restrições de uso — sem tornar públicos os dados de treinamento nem o código de treinamento completo, o que os diferencia de um modelo de IA verdadeiramente aberto segundo a definição da OSI.

## Não confunda com

Modelo aberto não é sinônimo de pesos abertos: pesos abertos descreve especificamente a disponibilização dos parâmetros treinados do modelo para download; modelo aberto é um termo mais amplo, que pode incluir apenas os pesos ou, no sentido mais completo, também os dados e o código de treinamento. Também não é sinônimo de código aberto no sentido tradicional de software: modelos de IA envolvem dados de treinamento e parâmetros numéricos, elementos sem equivalente direto no conceito clássico de código-fonte de um programa.

## Termos relacionados

## Referências

- Open Source Initiative. *The Open Source AI Definition – 1.0*.
  [opensource.org/ai/open-source-ai-definition](https://opensource.org/ai/open-source-ai-definition)
