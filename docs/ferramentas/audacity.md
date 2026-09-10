---
title: "Audacity"
slug: "audacity"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "edição de áudio"

tags:
  - edição de áudio
  - história oral
  - open source
  - uso offline
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: GPL-3.0
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "baixa a moderada"
integrations:
  - SayMore
  - VST3
  - Nyquist

concepts: []
alternatives:
  - Adobe Audition
  - Ocenaudio
  - GarageBand

official_site: "https://www.audacityteam.org/"
documentation: "https://manual.audacityteam.org/"
forum: "https://forum.audacityteam.org/"
repository: "https://github.com/audacity/audacity"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Audacity é um programa gratuito e de código aberto para gravar e editar áudio, com edição multipista. É um dos editores de áudio mais usados no mundo, mantido pelo Muse Group com contribuições da comunidade. Diferente de ferramentas de transcrição ou anotação, o Audacity não lida com texto — sua função é trabalhar diretamente no som: cortar, limpar, converter e melhorar arquivos de áudio.

## Para que serve

- Gravar áudio diretamente do microfone ou de outra fonte de entrada
- Editar arquivos existentes: cortar trechos, unir gravações, ajustar volume
- Reduzir ruído de fundo e melhorar a inteligibilidade de gravações de campo
- Ajustar velocidade e tom (pitch) de uma gravação, ou remover uma faixa vocal
- Converter entre formatos de áudio (WAV, MP3, FLAC, Ogg e outros)
- Estender funcionalidades com plugins no formato VST3 ou scripts Nyquist

## Exemplo de uso

Um pesquisador gravou uma entrevista de história oral em um ambiente com bastante ruído de fundo (ventilador, trânsito). Antes de enviar o arquivo para transcrição — manual no [oTranscribe](otranscribe.md) ou automática no [Whisper](whisper.md) — ele abre o áudio no Audacity, aplica redução de ruído, corta os trechos sem conteúdo relevante no início e no fim, e exporta um MP3 limpo, mais fácil de transcrever e de arquivar.

## Quando pode não ser a melhor opção

- Se você precisa transcrever ou anotar o conteúdo, não editar o áudio em si: o Audacity não faz isso — ferramentas como Whisper, MacWhisper, Buzz, oTranscribe ou ELAN são mais adequadas para essa etapa
- Se você precisa gerenciar sessões de gravação e metadados de um projeto de campo: SayMore ou Lameta cobrem essa necessidade, não o Audacity
- Se você só precisa de um corte simples e rápido, sem instalar nada: existem editores mais leves ou baseados em navegador para tarefas pontuais

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GPL v3, com partes sob GPL v2).

## Sistemas em que roda

Windows, macOS e Linux.

## Integrações

- Exporta áudio compatível com o fluxo de trabalho do [SayMore](saymore.md) (que também consegue abrir e extrair áudio diretamente)
- Plugins no formato VST3
- Scripts e plugins Nyquist, para automatizar tarefas de edição

## Alternativas

- Adobe Audition (pago, parte do pacote Adobe Creative Cloud)
- Ocenaudio (gratuito, interface mais simples, sem edição multipista)
- GarageBand (gratuito, mas só para macOS/iOS, com foco em produção musical)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.audacityteam.org/](https://www.audacityteam.org/)
- Documentação: [https://manual.audacityteam.org/](https://manual.audacityteam.org/)
- Fórum da comunidade: [https://forum.audacityteam.org/](https://forum.audacityteam.org/)
- Repositório: [https://github.com/audacity/audacity](https://github.com/audacity/audacity)

## Observações

O Audacity passou por uma controvérsia pública em 2021, quando o Muse Group (que administra o projeto desde então) propôs coletar dados de telemetria dos usuários. A reação da comunidade foi forte o suficiente para que a empresa recuasse e revisasse a política de privacidade — hoje o envio de relatórios de erro é opcional e controlado pela pessoa usuária. Vale ter esse histórico em mente, embora o programa continue sendo gratuito, de código aberto e sem coleta de dados obrigatória.

