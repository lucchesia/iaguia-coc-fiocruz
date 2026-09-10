---
title: "Algorithmic Bias"
title_pt: "Viés Algorítmico"
slug: "vies-algoritmico"

entry_type: "conceito"
concept_type: "conceito"

category: "limitações e letramento crítico"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "algorithmic bias"
  - "viés de IA"

related_terms: []
prerequisites:
  - algoritmo
  - dados-de-treinamento

references:
  - title: "NIST Special Publication 1270: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence"
    url: "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf"
    type: "padrão técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Viés Algorítmico

## O que é

Viés algorítmico é a tendência sistemática de um sistema de IA produzir resultados que favorecem ou desfavorecem injustamente determinados grupos, categorias ou situações — geralmente refletindo desigualdades presentes nos dados usados para treinar o sistema, ou em escolhas feitas durante seu desenvolvimento. Segundo a NIST Special Publication 1270, o viés em sistemas de IA pode ser classificado em três categorias amplas: viés estatístico e computacional (erros sistemáticos que surgem quando os dados de treinamento não representam adequadamente a população real); viés sistêmico (resultante de normas, processos ou estruturas que já favorecem certos grupos sociais antes mesmo da IA entrar em cena); e viés humano (resultante de decisões e julgamentos de pessoas envolvidas no desenvolvimento e uso do sistema).

## Por que isso importa?

Ferramentas de IA usadas em pesquisa — de reconhecimento de fala a tradução automática e assistentes de escrita — podem funcionar de forma sistematicamente pior para determinados grupos linguísticos, sotaques, nomes próprios ou variantes culturais, refletindo desequilíbrios nos dados de treinamento. Para projetos de pesquisa que envolvem comunidades sub-representadas — como história oral com grupos indígenas, populações rurais ou minorias linguísticas —, entender o viés algorítmico como uma limitação estrutural, e não uma falha pontual, é essencial para avaliar criticamente os resultados dessas ferramentas.

## Exemplo

Um sistema de reconhecimento automático de fala treinado majoritariamente com gravações de falantes de uma variante linguística urbana e de classe média tende a transcrever com mais erros entrevistas de história oral com falantes de sotaques regionais, dialetos populares ou línguas indígenas pouco representadas nos dados de treinamento — um exemplo direto de viés algorítmico com impacto real na qualidade da pesquisa.

## Não confunda com

Viés algorítmico não é sinônimo de erro técnico aleatório: um erro aleatório afeta resultados de forma imprevisível e não sistemática; viés algorítmico é uma distorção sistemática e recorrente, que tende a prejudicar ou favorecer os mesmos grupos de forma consistente. Também não é sinônimo de alucinação: alucinação é a invenção de conteúdo falso apresentado com confiança; viés algorítmico é uma distorção sistemática de desempenho relacionada a grupos ou categorias — os dois podem ocorrer juntos, mas são fenômenos distintos.

## Termos relacionados

## Referências

- NIST. *Special Publication 1270: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence*.
  [nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf)
