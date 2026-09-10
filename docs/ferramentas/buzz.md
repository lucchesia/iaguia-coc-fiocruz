---
title: "Buzz"
slug: "buzz"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "transcrição"

tags:
  - transcrição automática
  - reconhecimento de fala
  - open source
  - uso offline
  - linha de comando
aliases:
  - "Buzz Captions"

source_model: aberto
software_license: MIT
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "baixa a moderada"
integrations:
  - Hugging Face
  - OpenAI

concepts:
  - aprendizado-de-maquina
  - reconhecimento-automatico-de-fala
alternatives:
  - Whisper
  - MacWhisper
  - oTranscribe

official_site: "https://chidiwilliams.github.io/buzz/"
documentation: "https://chidiwilliams.github.io/buzz/docs/installation"
forum: "https://github.com/chidiwilliams/buzz/discussions"
repository: "https://github.com/chidiwilliams/buzz"

caveats:
  - manutenção reduzida
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Buzz é um aplicativo gratuito e de código aberto que transcreve e traduz áudio localmente no computador, usando o [Whisper](whisper.md), da OpenAI. É mantido por um desenvolvedor independente (Chidi Williams) e funciona como uma interface gráfica multiplataforma para o Whisper e variantes dele (Whisper.cpp, Faster Whisper), sem exigir linha de comando — embora também ofereça uma interface de linha de comando para quem quiser automatizar tarefas.

## Para que serve

- Transcrever arquivos de áudio e vídeo já gravados, ou a partir de um link do YouTube
- Transcrever em tempo real a partir do microfone, com uma janela de apresentação pensada para uso durante eventos ao vivo
- Traduzir a transcrição para outros idiomas usando os próprios modelos de [aprendizado de máquina](../conceitos/aprendizado-de-maquina.md) do Whisper
- Separar e identificar falantes diferentes na gravação, o que ajuda a precisão em áudios com várias vozes
- Exportar em TXT, SRT ou VTT, com um visualizador de transcrição com busca e controle de reprodução
- Acelerar o processamento usando GPU (Nvidia CUDA, Apple Silicon ou Vulkan, dependendo do sistema)

## Exemplo de uso

Uma pesquisadora está organizando um evento de história oral com depoimentos ao vivo e quer gerar uma transcrição em tempo real para exibir em tela, além de transcrever depois os áudios já gravados de entrevistas anteriores. Como não usa Mac, o MacWhisper não é uma opção — ela instala o Buzz no Windows, usa a transcrição ao vivo durante o evento e, depois, processa em lote os arquivos de áudio já gravados, tudo rodando localmente no próprio computador.

## Quando pode não ser a melhor opção

- Se você usa Mac e não se importa em pagar por uma experiência mais polida: o MacWhisper tem interface mais refinada e recursos adicionais (como integração com apps de reunião), mas é pago
- Se você só precisa transcrever um arquivo simples, sem interface gráfica: o Whisper por linha de comando é mais direto
- No Windows, o instalador não é assinado digitalmente, então o sistema pode exibir um aviso de segurança antes de permitir a instalação
- Como qualquer ferramenta baseada no Whisper, a precisão pode cair em áudios com muito ruído de fundo, sobreposição de vozes ou sotaques muito regionais

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MIT).

## Sistemas em que roda

Windows, macOS (Intel e Apple Silicon) e Linux (via Flatpak ou Snap). Também pode ser instalado como pacote Python (`pip install buzz-captions`), exigindo Python 3.12 e FFmpeg.

## Integrações

- Hugging Face (modelos Whisper-compatíveis hospedados na plataforma)
- OpenAI (API do Whisper, como alternativa a rodar o [modelo](../conceitos/modelo.md) localmente)
- Sistema de plugins, incluindo um plugin de resumo automático por IA

## Alternativas

- [Whisper](whisper.md) (o modelo em si, sem interface gráfica própria)
- [MacWhisper](macwhisper.md) (interface paga e exclusiva para Mac, com recursos adicionais)
- [oTranscribe](otranscribe.md) (transcrição manual, sem IA, funciona no navegador)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://chidiwilliams.github.io/buzz/](https://chidiwilliams.github.io/buzz/)
- Documentação: [https://chidiwilliams.github.io/buzz/docs/installation](https://chidiwilliams.github.io/buzz/docs/installation)
- Repositório: [https://github.com/chidiwilliams/buzz](https://github.com/chidiwilliams/buzz)
- Fórum da comunidade: [https://github.com/chidiwilliams/buzz/discussions](https://github.com/chidiwilliams/buzz/discussions)

## Observações

O Buzz é uma opção relevante para quem quer os benefícios do Whisper (transcrição local, sem enviar áudio a terceiros) com uma interface gráfica, mas sem pagar por uma ferramenta proprietária como o MacWhisper — e com a vantagem de rodar em Windows e Linux, não só em Mac. Por ser mantido por um único desenvolvedor independente, vale considerar isso ao avaliar a continuidade do projeto a longo prazo, embora o repositório mostre desenvolvimento ativo.

