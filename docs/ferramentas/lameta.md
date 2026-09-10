---
title: "Lameta"
slug: "lameta"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "gestão de sessões e metadados"

tags:
  - gestão de sessões e metadados
  - história oral
  - documentação linguística
  - open source
  - uso offline
aliases:
  - "SayMoreX"

source_model: aberto
software_license: MIT
access_model: gratuito

systems:
  - Windows
  - macOS
curva_aprendizado: "baixa a moderada"
integrations:
  - nenhuma conhecida

concepts: []
alternatives:
  - SayMore
  - ELAN
  - oTranscribe

official_site: "https://www.lameta.org/"
documentation: "http://hdl.handle.net/2196/07dd468f-0199-42d8-a02a-ae6f0ccbcfff"
forum: "não disponível"
repository: "https://github.com/onset/lameta"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Lameta é um programa gratuito e de código aberto para organizar metadados de coleções de arquivos, voltado sobretudo a projetos de documentação linguística, musical e de expressões culturais. Foi inspirado no [SayMore](saymore.md) e criado em grande parte pelo mesmo desenvolvedor principal (John Hatton), mas hoje é mantido por um consórcio de instituições acadêmicas de arquivamento (com pesquisadores da Universidade do Havaí, Universidade de Melbourne e SOAS), com financiamento da NSF, ELDP e CoEDL. Diferente do SayMore, não é um projeto da SIL International.

## Para que serve

- Organizar projetos de documentação em três níveis: Projeto, Pessoas e Sessões (cada sessão reúne os arquivos e metadados de um evento de gravação/coleta)
- Vincular registros de metadados aos arquivos de áudio, vídeo, imagem ou texto correspondentes, sem alterar os arquivos originais
- Acompanhar o andamento do trabalho de gestão de dados de um projeto de campo
- Empacotar e exportar os dados no formato IMDI, prontos para depósito em arquivos digitais como o ELAR (Endangered Languages Archive)
- Preencher campos de metadados com apoio de guias interativos, com interface disponível em vários idiomas (projeto de tradução colaborativa no Crowdin)

## Exemplo de uso

Um pesquisador está documentando uma língua em risco de extinção durante trabalho de campo. Ele cria um projeto no Lameta, registra os metadados de cada participante entrevistado e organiza cada gravação de áudio ou vídeo como uma sessão, com informações sobre data, local, tema e consentimento. O programa não transcreve nem anota os arquivos — apenas organiza os metadados. Ao final do trabalho de campo, ele empacota tudo no formato IMDI, pronto para ser depositado em um arquivo digital como o ELAR.

## Quando pode não ser a melhor opção

- Se você precisa transcrever, segmentar ou anotar os arquivos de áudio/vídeo dentro do próprio programa: o Lameta cuida só dos metadados, não tem essas ferramentas — nesse caso, o [SayMore](saymore.md) (Windows) ou o [ELAN](elan.md) são mais indicados
- Se você usa Linux e precisa de um instalador oficial: os instaladores oficiais cobrem apenas Windows e macOS; para Linux existe apenas um pacote não oficial via Snap Store, mantido por terceiros
- Se você só precisa transcrever um único áudio, sem organizar metadados de um projeto de campo: ferramentas mais simples como o [oTranscribe](otranscribe.md) podem bastar

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MIT), disponível no GitHub.

## Sistemas em que roda

Windows e macOS (instaladores oficiais). Há também um pacote não oficial para Linux via Snap Store, mantido por terceiros.

## Integrações

Não integra diretamente com outros programas de anotação ou transcrição — sua função é vincular metadados aos arquivos, não editá-los. Exporta pacotes no formato IMDI, compatíveis com arquivos digitais como o ELAR.

## Alternativas

- [SayMore](saymore.md) (mesma proposta de organização de sessões e metadados, mas com ferramentas adicionais de transcrição inicial e edição de mídia; disponível só para Windows)
- [ELAN](elan.md) (foco em anotação temporal detalhada, não em gestão de metadados de projeto)
- [oTranscribe](otranscribe.md) (transcrição manual simples, sem gestão de metadados)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.lameta.org/](https://www.lameta.org/)
- Documentação: [http://hdl.handle.net/2196/07dd468f-0199-42d8-a02a-ae6f0ccbcfff](http://hdl.handle.net/2196/07dd468f-0199-42d8-a02a-ae6f0ccbcfff)
- Repositório: [https://github.com/onset/lameta](https://github.com/onset/lameta)

## Observações

O Lameta costuma ser descrito como um "spin-off" do SayMore: foi inspirado nele e parte da equipe de desenvolvimento é a mesma, mas não é mantido pela SIL International — é mantido por um consórcio de instituições acadêmicas de arquivamento linguístico. Também é conhecido pelo nome anterior "SayMoreX", antes de adotar marca própria. É uma ferramenta bem estabelecida entre arquivos de línguas em risco (como o ELAR), por isso vale considerá-la quando o objetivo final do projeto de campo é depositar os dados nesse tipo de repositório.

