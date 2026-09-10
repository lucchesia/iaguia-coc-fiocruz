---
title: "Artificial Neural Network"
title_pt: "Rede Neural Artificial"
slug: "rede-neural-artificial"

entry_type: "conceito"
concept_type: "conceito"

category: "aprendizado de máquina"

tags:
  - aprendizado de máquina
  - inteligência artificial

aliases:
  - "artificial neural network"
  - "ANN"
  - "rede neural"
  - "neural network"

related_terms:
  - aprendizado-profundo
prerequisites:
  - aprendizado-de-maquina

references:
  - title: "feedforward neural networks — Glossary | NIST Computer Security Resource Center (citando NIST AI 100-2e2025)"
    url: "https://csrc.nist.gov/glossary/term/feedforward_neural_networks"
    type: "glossário técnico institucional"
  - title: "neural network / hidden layer / weight — Machine Learning Glossary | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary#neural-network"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Rede Neural Artificial

## O que é

Rede neural artificial é um tipo de modelo de [aprendizado de máquina](aprendizado-de-maquina.md) organizado em camadas de unidades de processamento interconectadas — chamadas de "neurônios" ou "nós" — vagamente inspirado na estrutura de neurônios biológicos. Segundo o glossário técnico do Google for Developers, uma rede neural é "um modelo composto por camadas; cada camada é formada por um ou mais neurônios". Cada neurônio recebe valores de entrada, aplica um peso a cada um (a importância atribuída a cada entrada, ajustada durante o treinamento) e repassa o resultado adiante por meio de uma função de ativação, que permite à rede aprender relações complexas entre os dados de entrada e o resultado desejado. Segundo o NIST (documento NIST AI 100-2e2025), redes do tipo "feedforward" — um dos arranjos mais comuns — são aquelas em que as conexões entre os nós vão sempre de uma camada para a próxima, sem formar ciclos.

## Por que isso importa?

Redes neurais artificiais são a base técnica da maior parte das ferramentas de IA usadas hoje em pesquisa e ensino — de reconhecimento de fala a geração de texto e imagens. Entender sua estrutura básica (camadas, pesos ajustados durante o treinamento a partir de exemplos) ajuda a interpretar por que essas ferramentas "aprendem" padrões em vez de seguir regras escritas manualmente por uma pessoa, e por que a quantidade e a qualidade dos dados de treinamento influenciam diretamente a qualidade do resultado.

## Exemplo

Ferramentas como o [Whisper](../ferramentas/whisper.md) (transcrição automática de fala) e o [Transkribus](../ferramentas/transkribus.md) (reconhecimento de escrita manuscrita) usam redes neurais artificiais para transformar um sinal de entrada — áudio ou imagem — em texto. Nas camadas iniciais da rede, os neurônios captam padrões simples (um som isolado, um traço de caligrafia); nas camadas seguintes, esses padrões são combinados em unidades mais complexas, até chegar a uma palavra ou frase reconhecida como saída.

## Não confunda com

Rede neural artificial não é sinônimo de [aprendizado profundo](aprendizado-profundo.md): toda rede de aprendizado profundo é uma rede neural artificial, mas nem toda rede neural artificial é "profunda" — uma rede sem camadas ocultas, por exemplo, não é considerada aprendizado profundo. Também não é sinônimo de "cérebro" ou "neurônio biológico": a inspiração em neurônios biológicos orientou o design original desse tipo de modelo, mas não é uma reprodução literal do funcionamento do cérebro humano.

## Termos relacionados

## Referências

- NIST Computer Security Resource Center. *feedforward neural networks — Glossary* (citando NIST AI 100-2e2025).
  [csrc.nist.gov/glossary/term/feedforward_neural_networks](https://csrc.nist.gov/glossary/term/feedforward_neural_networks)
- Google for Developers. *Machine Learning Glossary* (entradas "neural network" / "hidden layer" / "weight").
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary#neural-network)
