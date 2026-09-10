---
title: "Kdenlive"
slug: "kdenlive"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "áudio, vídeo e produção"

tags:
  - áudio e vídeo
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
curva_aprendizado: "moderada a alta"
integrations:
  - MLT Framework
  - Glaxnimate

concepts: []
alternatives:
  - OBS Studio
  - DaVinci Resolve
  - Shotcut

official_site: "https://kdenlive.org/"
documentation: "https://docs.kdenlive.org/"
forum: "https://discuss.kde.org/tag/kdenlive"
repository: "https://invent.kde.org/multimedia/kdenlive"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Kdenlive (sigla para "KDE Non-Linear Video Editor") é um editor de vídeo gratuito e de código aberto, parte do projeto KDE. Diferente do [OBS Studio](obs-studio.md), que serve para gravar e transmitir, o Kdenlive é uma ferramenta de edição: corta, organiza, aplica efeitos e finaliza vídeos já gravados, em várias trilhas simultâneas.

## Para que serve

- Editar vídeo em múltiplas trilhas de vídeo e áudio, numa linha do tempo (timeline) não-linear
- Aplicar efeitos de vídeo e áudio (correção de cor, desfoque, ajustes de som), com controle por keyframes ao longo do tempo
- Criar títulos e legendas, incluindo conversão de fala em texto assistida por IA para gerar legendas automaticamente (recurso mais recente, ainda sujeito a revisão manual)
- Trabalhar com cópias em baixa resolução dos vídeos originais (proxy clips) durante a edição, para manter fluidez mesmo em computadores mais fracos, renderizando na resolução final só ao exportar
- Exportar o resultado final em diversos formatos de vídeo

## Exemplo de uso

Um pesquisador gravou várias entrevistas de história oral com o OBS Studio e agora precisa editar o material: cortar trechos irrelevantes, unir depoimentos de diferentes sessões numa única peça e adicionar legendas para acessibilidade. Ele importa os arquivos no Kdenlive, organiza os cortes na linha do tempo, usa o recurso de conversão de fala em texto para gerar uma legenda inicial (que revisa manualmente para corrigir erros) e exporta o vídeo final pronto para publicação.

## Quando pode não ser a melhor opção

- Se você precisa gravar tela, áudio ou fazer transmissões ao vivo: essa não é a função do Kdenlive — o [OBS Studio](obs-studio.md) é a ferramenta certa para captura e transmissão
- Se você já usa o DaVinci Resolve e não tem motivo para trocar: é outra opção robusta e gratuita (com plano pago para recursos avançados), amplamente usada em produção profissional
- Se você não tem familiaridade com conceitos de edição não-linear (trilhas, keyframes, efeitos): a curva de aprendizado é real, como em qualquer editor de vídeo profissional
- Se você só precisa de um corte muito simples e rápido: ferramentas mais leves, como o Shotcut, podem ter menos sobrecarga para tarefas pontuais

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GPL v3 ou posterior).

## Sistemas em que roda

Windows, macOS e Linux (também disponível para FreeBSD).

## Integrações

- MLT Framework (motor de processamento de vídeo/áudio usado internamente, também empregado por outras ferramentas de edição)
- Glaxnimate (editor de animação vetorial, integrado para criar títulos e elementos animados)

## Alternativas

- [OBS Studio](obs-studio.md) (gravação e transmissão, não edição)
- DaVinci Resolve (proprietário, gratuito com plano pago para recursos avançados, referência em produção profissional)
- Shotcut (também gratuito e de código aberto, interface mais simples)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://kdenlive.org/](https://kdenlive.org/)
- Documentação: [https://docs.kdenlive.org/](https://docs.kdenlive.org/)
- Repositório: [https://invent.kde.org/multimedia/kdenlive](https://invent.kde.org/multimedia/kdenlive)
- Fórum da comunidade: [https://discuss.kde.org/tag/kdenlive](https://discuss.kde.org/tag/kdenlive)

## Observações

O Kdenlive é uma opção robusta e madura para quem precisa editar vídeo sem depender de ferramentas proprietárias — bastante usado em projetos de documentação audiovisual, história oral e produção de material didático. O recurso de legendagem automática por IA é útil como ponto de partida, mas, como qualquer transcrição automática, deve ser revisado manualmente antes da publicação, especialmente para nomes próprios, termos técnicos ou trechos com áudio de baixa qualidade.

