---
title: "MacWhisper"
slug: "macwhisper"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "transcrição"

tags:
  - transcrição automática
  - reconhecimento de fala
  - uso offline
aliases:
  - "Whisper Transcription"

source_model: proprietário
software_license: proprietária
access_model: freemium

systems:
  - macOS
curva_aprendizado: "baixa a moderada"
integrations:
  - Zoom
  - Teams
  - Ollama
  - OpenAI
  - Anthropic
  - Google Gemini

concepts:
  - aprendizado-de-maquina
  - reconhecimento-automatico-de-fala
alternatives:
  - Whisper
  - oTranscribe
  - Buzz

official_site: "https://www.macwhisper.com/"
documentation: "https://docs.macwhisper.com/"
forum: "não disponível"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

MacWhisper é um aplicativo proprietário para macOS que transcreve áudio e vídeo usando modelos de [aprendizado de máquina](../conceitos/aprendizado-de-maquina.md) — principalmente o [Whisper](whisper.md), da OpenAI, além do Parakeet, da Nvidia. É desenvolvido por Jordi Bruin (Good Snooze, Países Baixos) e funciona como uma interface gráfica completa em volta desses modelos, sem exigir linha de comando. Também é distribuído na App Store da Apple sob o nome "Whisper Transcription", com pequenas diferenças de recursos e modelo de cobrança.

## Para que serve

- Transcrever entrevistas, aulas, vídeos e podcasts a partir de arquivos de áudio/vídeo já gravados
- Gravar e transcrever reuniões em Zoom, Teams, Webex, Skype ou Discord
- Fazer ditado em tempo real em qualquer campo de texto do Mac
- Reconhecer automaticamente diferentes falantes na gravação (diarização)
- Remover automaticamente cacoetes de fala ("é", "tipo", "uhm") da transcrição
- Transcrever vídeos do YouTube a partir do link
- Processar arquivos em lote e buscar por palavras dentro das transcrições já feitas

## Exemplo de uso

Um pesquisador de história oral tem uma pilha de entrevistas em vídeo gravadas em campo. Em vez de instalar e rodar o Whisper por linha de comando, ele abre o MacWhisper, arrasta os arquivos para a janela do programa e transcreve tudo em lote, com identificação automática de quem está falando em cada trecho. Como o processamento roda localmente no Mac, os áudios das entrevistas não saem do computador — relevante quando há informação sensível envolvida.

## Quando pode não ser a melhor opção

- Se você precisa de uma ferramenta gratuita e de código aberto: o MacWhisper é proprietário; o plano gratuito só libera os modelos menores do Whisper, e os recursos mais avançados (modelos maiores, diarização, transcrição em lote) exigem a versão Pro ou Pro Max, pagas
- Se você não usa Mac: o programa é exclusivo para macOS (a versão para iOS existe, mas é um produto à parte, "Whisper Transcription")
- Se você quer usar os provedores de IA em nuvem (OpenAI, Anthropic, Google Gemini) para pós-processar a transcrição: isso envia dados a servidores externos, o que pode não ser adequado para fontes sensíveis — nesse caso, vale manter só os modelos locais
- Se você já tem confiança com linha de comando e não se importa com a instalação: o Whisper original é gratuito e de código aberto

## Tipo de acesso

Freemium: uma versão gratuita com os modelos menores do Whisper, e uma versão Pro (compra única, ~€64, com atualizações vitalícias) que libera os modelos maiores, diarização de falantes e transcrição em lote. Há também uma versão Pro Max, com licença comercial. A versão da App Store ("Whisper Transcription") tem opções de assinatura em vez de compra única.

## Sistemas em que roda

macOS (funciona melhor em Macs com chip Apple Silicon; também roda em Macs Intel, com desempenho menor).

## Integrações

- Zoom, Teams, Webex, Skype e Discord (gravação e transcrição de reuniões)
- Ollama (modelos de IA locais adicionais)
- OpenAI, Anthropic e Google Gemini (serviços de IA em nuvem, usados para "conversar" com a transcrição ou pós-processá-la — recurso opcional, envia dados à nuvem)

## Alternativas

- [Whisper](whisper.md) (o [modelo](../conceitos/modelo.md) em si, gratuito e de código aberto, mas exige linha de comando)
- [oTranscribe](otranscribe.md) (transcrição manual, sem IA, funciona no navegador)
- Buzz (interface gráfica gratuita e de código aberto para o Whisper, multiplataforma)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.macwhisper.com/](https://www.macwhisper.com/)
- Documentação: [https://docs.macwhisper.com/](https://docs.macwhisper.com/)

### Material de apoio

A documentação oficial é gratuita, aberta e cobre os dois modos de uso do programa. O artigo
de transcrição em lote percorre a tarefa pela interface gráfica, da abertura dos arquivos à
exportação. O da ferramenta de linha de comando traz o comando real com a saída
correspondente, útil para quem processa muitos arquivos.

- "How to use the Batch Transcription feature":
  [https://docs.macwhisper.com/article/19-batch-transcription](https://docs.macwhisper.com/article/19-batch-transcription)
- "MacWhisper Command-Line Tool":
  [https://docs.macwhisper.com/article/57-macwhisper-command-line-tool](https://docs.macwhisper.com/article/57-macwhisper-command-line-tool)

## Uso em pesquisa e ensino

Na data de preparação deste verbete não foi localizada pesquisa que documente o uso do
MacWhisper. O programa aparece citado em guias de biblioteca universitária e em anúncios de
oficinas, sempre dentro de listas de opções de transcrição, sem relato do que foi feito com
ele em um projeto específico. Isso é coerente com ser produto de desenvolvedor independente,
fora do circuito de publicação acadêmica. Este verbete será revisto quando houver uso
documentado.

## Observações

O MacWhisper é um produto de desenvolvedor independente (Jordi Bruin, Good Snooze), não de uma instituição acadêmica ou de pesquisa — vale essa ressalva ao indicar a ferramenta em contexto institucional. Por rodar os modelos localmente por padrão, preserva a mesma vantagem de privacidade do Whisper original; mas os recursos mais recentes de "conversar" com a transcrição via provedores de IA em nuvem (OpenAI, Anthropic, Google Gemini) são opcionais e, se ativados, enviam dados a servidores externos — importante avisar quem for indicar a ferramenta para trabalho com fontes sensíveis.

