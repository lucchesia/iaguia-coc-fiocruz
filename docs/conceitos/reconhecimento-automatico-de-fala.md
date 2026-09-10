---
title: "Automatic Speech Recognition"
title_pt: "Reconhecimento Automático de Fala"
slug: "reconhecimento-automatico-de-fala"

entry_type: "conceito"
concept_type: "técnica"

category: "linguagem, documentos, imagem e áudio"

tags:
  - inteligência artificial
  - aprendizado de máquina

aliases:
  - "ASR"
  - "automatic speech recognition"
  - "reconhecimento de fala"

related_terms: []
prerequisites:
  - aprendizado-profundo

references:
  - title: "Speech recognition — Wikipédia"
    url: "https://en.wikipedia.org/wiki/Speech_recognition"
    type: "enciclopédia colaborativa (apoio)"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Reconhecimento Automático de Fala

## O que é

ASR (Reconhecimento Automático de Fala, do inglês *Automatic Speech Recognition*) é a tecnologia que converte um sinal de áudio de fala humana em texto escrito. Segundo a Wikipédia, reconhecimento de fala "é um subcampo da linguística computacional dedicado a métodos e tecnologias que traduzem linguagem falada em texto ou outras formas interpretáveis". Modelos atuais de ASR costumam ser treinados com grandes volumes de áudio transcrito, usando arquiteturas de aprendizado profundo, para aprender a associar padrões sonoros a palavras.

## Por que isso importa?

ASR é a tecnologia por trás de ferramentas de transcrição automática cada vez mais usadas em projetos de história oral e pesquisa qualitativa. Entender que a qualidade do ASR depende diretamente dos dados de treinamento do modelo ajuda a interpretar por que certos sotaques, dialetos ou vocabulários técnicos são transcritos com mais erros do que outros — uma limitação especialmente relevante para projetos de história oral com comunidades linguisticamente sub-representadas nos conjuntos de dados usados para treinar esses modelos.

## Exemplo

O Whisper é um modelo de ASR usado por ferramentas como o [MacWhisper](../ferramentas/macwhisper.md) e o [Buzz](../ferramentas/buzz.md) para transcrever automaticamente entrevistas de história oral gravadas em áudio, convertendo a fala em texto que depois pode ser revisado e corrigido manualmente por uma pesquisadora.

## Não confunda com

ASR não é sinônimo de transcrição manual: ASR é o processo automatizado de conversão de fala em texto; transcrição manual é feita por uma pessoa, sem uso de reconhecimento automático (embora o resultado do ASR quase sempre precise de revisão manual). Também não é sinônimo de reconhecimento de locutor (*speaker recognition*): ASR identifica o que foi dito; reconhecimento de locutor identifica quem falou — são tarefas relacionadas, mas distintas.

## Termos relacionados

## Referências

- Wikipédia. *Speech recognition*.
  [en.wikipedia.org/wiki/Speech_recognition](https://en.wikipedia.org/wiki/Speech_recognition)
