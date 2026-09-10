---
title: "Explainable AI"
title_pt: "Explicabilidade"
slug: "explicabilidade"

entry_type: "conceito"
concept_type: "conceito"

category: "limitações e letramento crítico"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "XAI"
  - "IA explicável"
  - "explainability"

related_terms:
  - vies-algoritmico
prerequisites:
  - modelo

references:
  - title: "NISTIR 8312: Four Principles of Explainable Artificial Intelligence"
    url: "https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8312.pdf"
    type: "padrão técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Explicabilidade

## O que é

Explicabilidade é a capacidade de um sistema de IA fornecer razões ou evidências compreensíveis sobre como chegou a um determinado resultado, recomendação ou decisão. Segundo o documento NISTIR 8312 ("Four Principles of Explainable Artificial Intelligence"), um sistema de IA explicável deve seguir quatro princípios: fornecer evidências ou razões que acompanhem os resultados e processos; oferecer explicações compreensíveis para cada pessoa usuária específica; garantir que a explicação reflita corretamente o processo real usado pelo sistema; e operar apenas dentro das condições para as quais foi projetado, reconhecendo os limites da própria confiança em sua saída. A área de pesquisa dedicada a esse tema é frequentemente chamada de XAI (do inglês *Explainable AI*).

## Por que isso importa?

Muitos sistemas de IA — especialmente os baseados em redes neurais profundas, como os modelos de linguagem — funcionam como "caixas-pretas": produzem resultados sofisticados sem que seja simples entender exatamente por que chegaram àquela resposta específica. Para pesquisa, isso é relevante ao avaliar ferramentas de IA usadas em tarefas com impacto real — por exemplo, a classificação automática de documentos de arquivo por tema —, já que a falta de explicabilidade dificulta auditar decisões, identificar vieses ou corrigir erros sistemáticos.

## Exemplo

Uma ferramenta de análise que usa reconhecimento de entidades nomeadas para identificar automaticamente pessoas mencionadas num conjunto de cartas históricas pode cometer erros de identificação sem indicar claramente por que interpretou um determinado nome de uma forma específica — a falta de explicabilidade nesse tipo de sistema dificulta que uma pesquisadora entenda e corrija sistematicamente os erros do processo.

## Não confunda com

Explicabilidade não é sinônimo de transparência: transparência normalmente se refere à abertura sobre como um sistema foi construído (dados usados, código, decisões de design); explicabilidade se refere especificamente à capacidade de explicar por que um resultado específico foi produzido. Também não é sinônimo de interpretabilidade, embora os termos às vezes sejam usados de forma intercambiável: interpretabilidade costuma se referir à possibilidade de compreender diretamente o funcionamento interno de um modelo, enquanto explicabilidade abrange também técnicas que geram explicações a posteriori para modelos complexos e opacos.

## Termos relacionados

## Referências

- NIST. *NISTIR 8312: Four Principles of Explainable Artificial Intelligence*.
  [nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8312.pdf](https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8312.pdf)
