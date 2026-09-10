---
title: "Deep Learning"
title_pt: "Aprendizado Profundo"
slug: "aprendizado-profundo"

entry_type: "conceito"
concept_type: "conceito"

category: "aprendizado de máquina"

tags:
  - aprendizado de máquina
  - inteligência artificial

aliases:
  - "deep learning"
  - "DL"
  - "aprendizagem profunda"

related_terms:
  - rede-neural-artificial
prerequisites:
  - aprendizado-de-maquina

references:
  - title: "Artificial intelligence — Methods and goals in AI | Encyclopaedia Britannica"
    url: "https://www.britannica.com/technology/artificial-intelligence/Methods-and-goals-in-AI"
    type: "enciclopédia acadêmica de referência"
  - title: "deep model / neural network — Machine Learning Glossary | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary#deep-model"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Aprendizado Profundo

## O que é

Aprendizado profundo (do inglês *deep learning*) é uma abordagem de [aprendizado de máquina](aprendizado-de-maquina.md) baseada em redes neurais artificiais com várias camadas ("profundas") entre a entrada e a saída dos dados. Segundo a Enciclopédia Britannica, é um tipo de aprendizado de máquina em que a rede neural tem quatro ou mais camadas, contando a camada de entrada e a de saída. Segundo o glossário técnico do Google for Developers, uma rede "profunda" é justamente uma rede neural com mais de uma camada oculta ("hidden layer") entre a entrada e a saída — cada camada processa os dados recebidos da camada anterior e passa padrões cada vez mais abstratos para a camada seguinte.

## Por que isso importa?

Aprendizado profundo é a técnica por trás da maioria dos avanços recentes de IA usados em pesquisa e ensino — reconhecimento automático de fala, geração de texto, tradução automática, reconhecimento de escrita manuscrita. Entender que se trata de uma técnica específica (e não sinônimo de todo aprendizado de máquina) ajuda a interpretar por que certas ferramentas exigem tanto poder computacional (GPUs) e grandes volumes de dados de treinamento para funcionar bem, e por que seu funcionamento interno costuma ser difícil de explicar em detalhe — problema conhecido informalmente como "caixa-preta" — mesmo para quem desenvolve essas ferramentas.

## Exemplo

Ferramentas como o [Transkribus](../ferramentas/transkribus.md) e o [eScriptorium](../ferramentas/escriptorium.md) usam modelos de aprendizado profundo — redes neurais artificiais com múltiplas camadas — para reconhecimento de texto manuscrito (HTR). Nas camadas iniciais da rede, o modelo reconhece traços simples de caligrafia; em camadas mais profundas, combina esses traços em padrões mais complexos, como letras, palavras e estilos de escrita típicos de um período histórico específico.

## Não confunda com

Aprendizado profundo não é sinônimo de aprendizado de máquina: é uma técnica específica dentro desse campo mais amplo, que inclui também outras abordagens (como árvores de decisão) sem redes neurais de múltiplas camadas. Também não é sinônimo de [rede neural artificial](rede-neural-artificial.md): toda rede de aprendizado profundo é uma rede neural, mas nem toda rede neural é "profunda" — uma rede com uma única camada oculta, por exemplo, não é considerada aprendizado profundo.

## Termos relacionados

## Referências

- Encyclopaedia Britannica. *Artificial intelligence — Methods and goals in AI*.
  [britannica.com/technology/artificial-intelligence/Methods-and-goals-in-AI](https://www.britannica.com/technology/artificial-intelligence/Methods-and-goals-in-AI)
- Google for Developers. *Machine Learning Glossary* (entradas "deep model" / "neural network").
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary#deep-model)
