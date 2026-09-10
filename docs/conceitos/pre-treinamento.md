---
title: "Pre-training"
title_pt: "Pré-treinamento"
slug: "pre-treinamento"

entry_type: "conceito"
concept_type: "conceito"

category: "aprendizado de máquina"

tags:
  - aprendizado de máquina
  - inteligência artificial

aliases:
  - "pre-training"
  - "pretraining"

related_terms:
  - ajuste-fino
prerequisites:
  - treinamento

references:
  - title: "pre-training — Glossary | NIST Computer Security Resource Center (citando NIST SP 800-226 e NIST AI 100-2e2025)"
    url: "https://csrc.nist.gov/glossary/term/pre_training"
    type: "glossário técnico institucional"
  - title: "base model / pre-trained model — Machine Learning Glossary | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary#base-model"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Pré-treinamento

## O que é

Pré-treinamento é a primeira etapa do [treinamento](treinamento.md) de um modelo de IA, na qual o modelo é treinado com um volume muito grande e geralmente genérico de dados, para aprender padrões amplos, antes de ser adaptado para uma tarefa específica. Segundo a norma NIST SP 800-226, pré-treinamento é "uma etapa de treinamento que treina um modelo de propósito geral (às vezes chamado de modelo fundacional) com dados disponíveis publicamente" — etapa "geralmente seguida de ajuste fino, para equipar o modelo com informação específica de uma tarefa". O documento NIST AI 100-2e2025 acrescenta que, nessa etapa, "o modelo aprende padrões, características e relações gerais a partir de grandes volumes de dados sem rótulo", muitas vezes por meio de aprendizado autossupervisionado. O resultado desse processo é o que o glossário do Google for Developers chama de "modelo base" (*base model*) ou "modelo pré-treinado" (*pre-trained model*): um modelo que "pode servir de ponto de partida para o ajuste fino, voltado a tarefas ou aplicações específicas". Modelos de linguagem, por exemplo, costumam ser pré-treinados com grandes volumes de texto coletados da internet, livros e outras fontes, antes de passarem por uma etapa posterior de ajuste fino para tarefas específicas, como responder perguntas ou seguir instruções.

## Por que isso importa?

Entender a diferença entre pré-treinamento e ajuste fino ajuda a entender por que a maioria das pessoas que usa ferramentas de IA generativa não "treina" um modelo do zero — na prática, ela usa (ou, no máximo, ajusta minimamente) um modelo já pré-treinado por uma grande empresa de tecnologia, com custo computacional e volume de dados fora do alcance da maioria das instituições de pesquisa. Essa etapa costuma ser a mais custosa (em tempo, dinheiro e energia) do desenvolvimento de um modelo de IA, e também aquela em que boa parte dos vieses presentes nos dados coletados da internet acabam incorporados ao comportamento do modelo.

## Exemplo

Modelos de reconhecimento de fala como o [Whisper](../ferramentas/whisper.md) são pré-treinados com centenas de milhares de horas de áudio em várias línguas, coletadas de fontes diversas. Só depois dessa etapa de pré-treinamento é que versões do modelo podem ser ajustadas (*fine-tuned*) para tarefas mais específicas, como reconhecer melhor um dialeto ou um vocabulário técnico particular.

## Não confunda com

Pré-treinamento não é sinônimo de treinamento em geral: é especificamente a etapa inicial, com dados amplos e genéricos, que produz um modelo base; treinamento é o termo mais geral para o processo de ajuste dos parâmetros de um modelo a partir de exemplos, e pode se referir tanto ao pré-treinamento quanto a etapas posteriores. Também não é sinônimo de [ajuste fino](ajuste-fino.md): ajuste fino parte de um modelo já pré-treinado e o adapta, com um volume bem menor de dados, para uma tarefa específica.

## Termos relacionados

## Referências

- NIST. *Computer Security Resource Center Glossary*, verbete "pre-training" (citando NIST SP 800-226 e NIST AI 100-2e2025).
  [csrc.nist.gov/glossary/term/pre_training](https://csrc.nist.gov/glossary/term/pre_training)
- Google for Developers. *Machine Learning Glossary* (entradas "base model" / "pre-trained model").
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary#base-model)
