---
title: "ELAN"
slug: "elan"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "anotação e marcação"

tags:
  - anotação de fontes
  - história oral
  - documentação linguística
  - transcrição manual
  - open source
  - uso offline
aliases:
  - "EUDICO Linguistic Annotator"

source_model: aberto
software_license: GPL-3.0
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada a alta"
integrations:
  - Praat
  - Toolbox
  - FLEx
  - CLAN
  - SayMore
  - Lameta

concepts: []
alternatives:
  - SayMore
  - Praat
  - CLAN

official_site: "https://archive.mpi.nl/tla/elan"
documentation: "https://archive.mpi.nl/tla/elan/documentation"
forum: "https://archive.mpi.nl/forums/c/elan"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

ELAN (EUDICO Linguistic Annotator) é um programa gratuito e de código aberto para criar anotações detalhadas e sincronizadas no tempo sobre arquivos de áudio e vídeo. É desenvolvido pelo The Language Archive, do Max Planck Institute for Psycholinguistics (Nijmegen, Países Baixos), e é uma das ferramentas mais usadas em linguística, documentação de línguas e pesquisa sobre interação multimodal.

## Para que serve

- Adicionar um número ilimitado de anotações textuais a um arquivo de áudio ou vídeo, cada uma vinculada a um intervalo de tempo específico
- Organizar as anotações em camadas chamadas "tiers" (por exemplo, uma tier por participante, ou tiers separadas para fala, gesto e expressão facial), com relações hierárquicas entre elas
- Transcrever, traduzir, glosar ou comentar qualquer trecho da gravação
- Importar e exportar dados em formatos usados por outras ferramentas de pesquisa linguística: Praat (TextGrid), Toolbox, FLEx (.flextext) e CLAN/CHAT
- Abrir diretamente arquivos .eaf produzidos pelo [SayMore](saymore.md) ou pelo [Lameta](lameta.md), continuando a anotação de onde a organização de sessão parou

## Exemplo de uso

Uma pesquisadora de história oral gravou entrevistas em vídeo com um grupo de trabalhadores rurais. Depois de organizar as sessões e os metadados de consentimento no SayMore, ela abre o mesmo arquivo diretamente no ELAN para fazer uma anotação detalhada: cria uma tier para a transcrição da fala, outra para tradução e uma terceira para observações sobre gestos e pausas, tudo sincronizado com o tempo exato do vídeo — o que facilita tanto a análise quanto a citação de trechos específicos em publicações futuras.

## Quando pode não ser a melhor opção

- Se você só precisa organizar sessões de gravação e metadados de campo, sem fazer anotação temporal detalhada: o [SayMore](saymore.md) ou o [Lameta](lameta.md) são mais diretos para isso
- Se você precisa de transcrição automática gerada por IA: o ELAN não faz reconhecimento de fala — é uma ferramenta de anotação manual (a transcrição em si tem que ser feita por uma pessoa)
- Se você está começando agora e só precisa de algo simples: a curva de aprendizado é considerada íngreme — a interface tem uma lógica própria, incomum em relação a outros programas, e usar os recursos mais avançados (tiers hierárquicas, vocabulários controlados) exige consultar a documentação

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GPL 3).

## Sistemas em que roda

Windows, macOS e Linux.

## Integrações

Importa e exporta dados de/para Praat, Toolbox, FLEx e CLAN/CHAT. Abre diretamente arquivos .eaf gerados pelo SayMore e pelo Lameta, sem precisar reorganizar nada.

## Alternativas

- [SayMore](saymore.md) (foco em gestão de sessões e metadados de campo, não em anotação temporal detalhada)
- Praat (foco em análise acústica/fonética, com anotação temporal mais simples)
- CLAN (ferramenta do projeto CHILDES, mais usada em aquisição de linguagem infantil, com formato próprio CHAT)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://archive.mpi.nl/tla/elan](https://archive.mpi.nl/tla/elan)
- Documentação: [https://archive.mpi.nl/tla/elan/documentation](https://archive.mpi.nl/tla/elan/documentation)
- Fórum da comunidade: [https://archive.mpi.nl/forums/c/elan](https://archive.mpi.nl/forums/c/elan)

## Observações

O ELAN é considerado um padrão de fato para anotação de dados multimodais em linguística — é amplamente citado em publicações acadêmicas da área, e o próprio site pede que o programa seja citado em trabalhos que o utilizem. Por ser mantido por uma instituição de pesquisa (Max Planck Institute), tem forte compromisso com formatos abertos e interoperabilidade, mas isso também significa uma interface menos "amigável" que a de ferramentas comerciais — vale avisar quem está começando sobre essa curva de aprendizado antes de recomendar o programa como primeira ferramenta.

