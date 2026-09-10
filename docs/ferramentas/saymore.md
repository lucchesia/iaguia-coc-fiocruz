---
title: SayMore
slug: saymore
entry_type: ferramenta
tool_type: aplicativo
category: gestão de sessões e metadados
tags:
  - gestão de sessões e metadados
  - história oral
  - documentação linguística
  - open source
  - uso offline
aliases: []
source_model: aberto
software_license: MIT
access_model: gratuito
systems:
  - Windows
curva_aprendizado: baixa a moderada
integrations:
  - ELAN
  - Audacity
concepts: []
alternatives:
  - Lameta
  - ELAN
  - oTranscribe
official_site: https://software.sil.org/saymore/
documentation: https://software.sil.org/saymore/help/
forum: https://community.software.sil.org/c/saymore/8
repository: https://github.com/sillsdev/saymore
caveats: []
learning_resources: []
academic_use: []
tool_status: estável
status: publicado
reviewed: true
last_reviewed: '2026-08-19'
---

## O que é

SayMore é um programa gratuito e de código aberto para gestão de sessões de gravação e metadados em projetos de documentação linguística e história oral. É desenvolvido pela SIL International (organização sem fins lucrativos voltada a pesquisa e desenvolvimento de línguas) e ajuda pesquisadores a organizar arquivos de áudio/vídeo, informações de consentimento e metadados de participantes desde o momento da coleta em campo.

## Para que serve

- Organizar cada evento de gravação (sessão) junto com todos os arquivos e metadados associados, na aba "Sessions"
- Gerenciar informações e consentimento informado de participantes da pesquisa, na aba "People"
- Fazer transcrição inicial e tradução oral básica diretamente no programa (ferramentas de Documentação Oral Básica, ou BOLD)
- Extrair áudio (MP3) de arquivos de vídeo e nomear arquivos automaticamente, seguindo convenções consistentes
- Exportar dados para o [ELAN](elan.md) (usando o mesmo formato .eaf, com um clique para abrir e continuar a anotação), [Audacity](audacity.md), FLEx ou Toolbox
- Empacotar arquivos e metadados para envio a um arquivo digital, seguindo o padrão IMDI ou o Language & Culture Archive da SIL

## Exemplo de uso

Uma pesquisadora está fazendo trabalho de campo para um projeto de história oral com uma comunidade indígena. A cada entrevista gravada, ela cria uma nova sessão no SayMore, registra os metadados do participante (com consentimento informado) e faz uma transcrição inicial e tradução ali mesmo. Depois, para uma anotação linguística mais detalhada, ela abre o mesmo arquivo diretamente no ELAN — sem precisar reorganizar nada manualmente — e, ao final do projeto, empacota tudo no formato IMDI para depositar no acervo da instituição.

## Quando pode não ser a melhor opção

- Se você usa Mac: o SayMore só está disponível para Windows; para Mac, a SIL recomenda o [Lameta](lameta.md), criado pelo mesmo desenvolvedor principal do SayMore, com proposta semelhante mas sem as ferramentas de edição de mídia (o Lameta também tem um pacote não oficial para Linux, via Snap Store, mantido por terceiros)
- Se você só precisa transcrever um único áudio, sem gerenciar sessões de campo, metadados ou consentimento: ferramentas mais simples como o [oTranscribe](otranscribe.md) podem ser suficientes
- Se você precisa de reconhecimento automático de fala (transcrição gerada por IA): o SayMore não faz isso — é uma ferramenta de organização e transcrição manual assistida, não de ASR
- O projeto recebe manutenção contínua, mas a SIL informa que não há planos atuais de grandes novos recursos

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MIT), mantido pela SIL International.

## Sistemas em que roda

Apenas Windows (qualquer versão suportada, 64 bits a partir da versão 3.8).

## Integrações

- [ELAN](elan.md) (mesmo formato de arquivo .eaf; abre diretamente no ELAN para anotação mais avançada)
- [Audacity](audacity.md), FLEx e Toolbox (exportação de dados)
- Arquivos digitais compatíveis com o padrão IMDI, incluindo o Language & Culture Archive da SIL

## Alternativas

- [Lameta](lameta.md) (do mesmo desenvolvedor principal, para Mac/Linux, sem ferramentas de edição de mídia)
- [ELAN](elan.md) (foco em anotação temporal detalhada, não em gestão de sessões e metadados de campo)
- [oTranscribe](otranscribe.md) (transcrição manual simples, sem gestão de sessões ou metadados)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://software.sil.org/saymore/](https://software.sil.org/saymore/)
- Documentação: [https://software.sil.org/saymore/help/](https://software.sil.org/saymore/help/)
- Fórum da comunidade: [https://community.software.sil.org/c/saymore/8](https://community.software.sil.org/c/saymore/8)

## Observações

O SayMore é mantido pela SIL International, organização de base religiosa (cristã) sem fins lucrativos historicamente dedicada à documentação e desenvolvimento de línguas — incluindo línguas minoritárias e em risco de extinção — ao redor do mundo. É uma ferramenta bem estabelecida no campo da documentação linguística e da história oral acadêmica, com forte integração ao ELAN. Vale mencionar essa origem institucional ao indicar a ferramenta, especialmente em contextos de pesquisa com comunidades indígenas ou tradicionais, para que a equipe de pesquisa possa considerar esse contexto.

