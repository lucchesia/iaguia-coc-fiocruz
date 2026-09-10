---
title: "OBS Studio"
slug: "obs-studio"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "áudio, vídeo e produção"

tags:
  - áudio e vídeo
  - open source
  - uso offline
  - gratuito para pesquisa
aliases:
  - "Open Broadcaster Software"

source_model: aberto
software_license: GPL-2.0
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada"
integrations:
  - VST
  - Python

concepts: []
alternatives:
  - Kdenlive
  - Camtasia
  - Zoom

official_site: "https://obsproject.com/"
documentation: "https://obsproject.com/help"
forum: "https://obsproject.com/forum/"
repository: "https://github.com/obsproject/obs-studio"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

OBS Studio (Open Broadcaster Software) é um programa gratuito e de código aberto para gravar tela, áudio e vídeo, e para transmitir ao vivo. Mantido por uma comunidade de voluntários ao redor do mundo, é uma das ferramentas mais usadas para capturar aulas, apresentações, entrevistas e transmissões, combinando diferentes fontes (webcam, tela do computador, microfone, imagens) numa única gravação ou transmissão.

## Para que serve

- Gravar a tela do computador, sozinha ou combinada com webcam e áudio do microfone
- Criar "cenas" que combinam múltiplas fontes visuais e sonoras, com transições entre elas
- Transmitir ao vivo para plataformas como YouTube ou outras, além de gravar localmente
- Aplicar filtros de áudio, como redução e supressão de ruído, sem precisar de outro programa
- Monitorar múltiplas cenas ao mesmo tempo antes de exibi-las (Modo Estúdio), útil para transmissões mais elaboradas

## Exemplo de uso

Um docente está gravando uma série de aulas para disponibilizar aos alunos, combinando slides de apresentação com sua própria webcam num canto da tela, junto com o áudio do microfone. Ele configura uma cena no OBS Studio com essas três fontes (tela do computador, webcam e áudio), aplica um filtro de redução de ruído no microfone, e grava a aula localmente, sem precisar transmitir ao vivo nem depender de nenhum serviço externo.

## Quando pode não ser a melhor opção

- Se você só precisa editar um vídeo já gravado (cortar trechos, adicionar legendas, unir clipes): o OBS Studio é uma ferramenta de captura/transmissão, não de edição — o [Kdenlive](kdenlive.md) é mais indicado para essa etapa
- Se você quer algo mais simples, só para gravar reuniões: ferramentas como o Zoom já gravam a própria chamada, sem precisar configurar cenas
- Se você não tem familiaridade nenhuma com conceitos de produção de vídeo (cenas, fontes, mixagem de áudio): a curva de aprendizado inicial pode intimidar, embora gravações simples sejam relativamente diretas depois de alguma prática
- Se o computador for muito limitado: gravar e, principalmente, transmitir ao vivo em boa qualidade exige processamento razoável, especialmente com múltiplas fontes ativas

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GPL v2 ou posterior), mantido por doações da comunidade via Open Collective e Patreon.

## Sistemas em que roda

Windows, macOS e Linux.

## Integrações

- Plugins VST (efeitos de áudio profissionais, aplicáveis diretamente no mixer do OBS)
- Scripts em Lua e Python (para automatizar e estender funcionalidades)

## Alternativas

- [Kdenlive](kdenlive.md) (edição de vídeo já gravado, não captura/transmissão ao vivo)
- Camtasia (proprietário, pago, com edição integrada mais simples)
- Zoom (gravação de chamadas/reuniões, sem os recursos de composição de cenas do OBS)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://obsproject.com/](https://obsproject.com/)
- Documentação (Help Portal): [https://obsproject.com/help](https://obsproject.com/help)
- Repositório: [https://github.com/obsproject/obs-studio](https://github.com/obsproject/obs-studio)
- Fórum da comunidade: [https://obsproject.com/forum/](https://obsproject.com/forum/)

## Observações

Embora seja mais conhecido no contexto de transmissões ao vivo (streaming), o OBS Studio é bastante usado também apenas para gravação local, sem transmitir nada — um caso de uso relevante para docência (gravação de aulas) e para pesquisa (registro de entrevistas, apresentações, eventos acadêmicos). Por ser gratuito, de código aberto e não depender de nenhum serviço externo, é uma alternativa importante a ferramentas proprietárias de gravação de tela.

