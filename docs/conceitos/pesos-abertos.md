---
title: "Open Weights"
title_pt: "Pesos Abertos"
slug: "pesos-abertos"

entry_type: "conceito"
concept_type: "conceito"

category: "abertura e infraestrutura"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "open weights"
  - "open-weight"

related_terms:
  - modelo-aberto
prerequisites:
  - modelo-de-linguagem-grande
  - modelo-aberto

references:
  - title: "International AI Safety Report"
    url: "https://arxiv.org/abs/2501.17805"
    type: "relatório internacional de especialistas"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Pesos Abertos

## O que é

Pesos abertos é a prática de disponibilizar publicamente, para download, os parâmetros treinados de um modelo de IA — sem necessariamente disponibilizar também os dados usados para treiná-lo ou o código do processo de treinamento. Segundo o *International AI Safety Report* — relatório elaborado por uma rede internacional de especialistas, a pedido de dezenas de governos —, "os chamados 'modelos de pesos abertos' são modelos de IA cujos componentes centrais, chamados 'pesos', são compartilhados publicamente para download"; pesos são "os parâmetros matemáticos que permitem que modelos de IA processem entradas e gerem saídas". Um modelo de pesos abertos pode ser executado e ajustado por qualquer pessoa com os recursos computacionais necessários, mesmo sem acesso aos dados ou ao código originais de treinamento.

## Por que isso importa?

Pesos abertos ocupam um meio-termo entre um modelo totalmente fechado (acessível só por API, sem nenhum detalhe técnico público) e um [modelo aberto](modelo-aberto.md) no sentido mais completo. Para pesquisa, essa distinção é relevante porque pesos abertos permitem rodar um modelo localmente — o que pode ser importante para preservar a privacidade de dados sensíveis, como entrevistas de história oral —, mas não permitem verificar de forma independente quais dados foram usados para treinar o modelo.

## Exemplo

Modelos usados em ferramentas de execução local, como o [Ollama](../ferramentas/ollama.md) e o [LM Studio](../ferramentas/lm-studio.md), costumam ser modelos de pesos abertos — os arquivos com os parâmetros treinados são baixados e executados no computador da pessoa usuária, sem depender de um servidor externo, mesmo sem acesso aos dados originais usados para treinar esses modelos.

## Não confunda com

Pesos abertos não é sinônimo de modelo aberto no sentido mais completo: pesos abertos garante apenas acesso aos parâmetros treinados; um modelo aberto, no sentido da definição mais rigorosa da OSI, exige também informação sobre os dados de treinamento e o código-fonte usado para treinar o modelo. Também não é sinônimo de código aberto: pesos não são código-fonte no sentido tradicional — são valores numéricos resultantes de um processo de treinamento, e sua disponibilização não implica, por si só, que o processo que os gerou seja transparente ou reprodutível.

## Termos relacionados

## Referências

- International AI Safety Report.
  [arxiv.org/abs/2501.17805](https://arxiv.org/abs/2501.17805)
