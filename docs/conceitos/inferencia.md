---
title: "Inference"
title_pt: "Inferência"
slug: "inferencia"

entry_type: "conceito"
concept_type: "conceito"

category: "aprendizado de máquina"

tags:
  - aprendizado de máquina
  - inteligência artificial

aliases:
  - "inference"

related_terms:
  - treinamento
prerequisites:
  - treinamento

references:
  - title: "inference — Machine Learning Glossary: ML Fundamentals | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary/fundamentals#inference"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Inferência

## O que é

Inferência é a etapa em que um modelo de IA já [treinado](treinamento.md) é usado para produzir um resultado sobre dados novos, que ele nunca viu antes. Segundo o glossário do Google for Developers, em aprendizado de máquina tradicional, inferência é "o processo de fazer previsões aplicando um modelo treinado a exemplos sem rótulo"; em modelos de linguagem, inferência é "o processo de usar um modelo treinado para gerar uma resposta a um prompt de entrada". Em ambos os casos, é a etapa em que o modelo é efetivamente usado — em contraste com o treinamento, etapa anterior em que os parâmetros do modelo são ajustados a partir de exemplos.

## Por que isso importa?

Para quem usa ferramentas prontas de IA em pesquisa ([Whisper](../ferramentas/whisper.md), [ChatGPT](../ferramentas/chatgpt.md), [Transkribus](../ferramentas/transkribus.md) etc.), inferência é o que acontece a cada vez que se envia um áudio, um prompt ou uma imagem para a ferramenta processar. Diferentemente do treinamento — caro, demorado e feito uma vez por uma empresa ou equipe de pesquisa —, a inferência é rápida e acontece a cada novo uso da ferramenta. Saber que o resultado de uma ferramenta de IA vem de inferência sobre um modelo já treinado — não de um raciocínio dedutivo caso a caso — ajuda a entender por que erros sistemáticos aprendidos durante o treinamento tendem a se repetir de forma consistente durante o uso.

## Exemplo

Toda vez que uma pesquisadora envia uma gravação de entrevista de história oral para o Whisper transcrever, o modelo realiza uma inferência: aplica os parâmetros que aprendeu durante o treinamento para prever, a partir do áudio recebido, qual sequência de palavras corresponde à fala. Nenhum novo aprendizado acontece nesse momento — o modelo apenas usa o que já "aprendeu" durante o treinamento para produzir uma resposta sobre um dado que nunca tinha visto antes.

## Não confunda com

Inferência (no sentido de IA) não é o mesmo que inferência no sentido de privacidade de dados: nesse outro contexto — usado, por exemplo, no glossário técnico do NIST (SP 800-188) —, "inferência" se refere à capacidade de deduzir a identidade de uma pessoa a partir de pistas presentes em dados que tiveram identificadores diretos removidos (como nome e CPF). É um risco de reidentificação relevante para quem anonimiza dados de pesquisa (entrevistas, questionários), mas é um conceito diferente do usado aqui. Inferência também não é sinônimo de treinamento: treinamento é a etapa em que o modelo aprende a partir de exemplos; inferência é a etapa seguinte, em que o modelo já treinado é usado.

## Termos relacionados

## Referências

- Google for Developers. *Machine Learning Glossary: ML Fundamentals* (entrada "inference").
  [developers.google.com/machine-learning/glossary/fundamentals](https://developers.google.com/machine-learning/glossary/fundamentals#inference)
