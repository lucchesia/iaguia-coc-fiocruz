---
title: "Archivematica"
slug: "archivematica"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "preservação digital"

tags:
  - preservação digital
  - open source
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: AGPL-3.0
access_model: gratuito

systems:
  - Web
  - Linux
curva_aprendizado: "alta"
integrations:
  - AtoM

concepts: []
alternatives:
  - Preservica
  - Rosetta
  - LOCKSS

official_site: "https://www.archivematica.org/"
documentation: "https://www.archivematica.org/en/docs/latest/"
forum: "https://groups.google.com/g/archivematica"
repository: "https://github.com/artefactual/archivematica"

caveats:
  - requer infraestrutura própria
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Archivematica é um sistema gratuito e de código aberto para preservação digital de longo prazo, mantido pela Artefactual Systems — a mesma empresa por trás do [AtoM](atom.md). É importante não confundi-lo com ferramentas de publicação de coleções, como [Omeka S](omeka-s.md), [Tainacan](tainacan.md) ou [WordPress](wordpress.md): o Archivematica não publica nada para o público — sua função é garantir que arquivos digitais permaneçam íntegros, autênticos e acessíveis ao longo de décadas, seguindo o modelo de referência internacional OAIS (Open Archival Information System).

## Para que serve

- Identificar formatos de arquivo e normalizá-los para formatos mais estáveis e adequados à preservação de longo prazo
- Verificar a integridade dos arquivos ao longo do processo, gerando registros de proveniência e autenticidade
- Empacotar os arquivos preservados em Pacotes de Informação Arquivística (AIPs), seguindo padrões como METS, PREMIS, Dublin Core e a especificação BagIt
- Disponibilizar um painel web para monitorar e controlar cada etapa do processamento (ingestão, normalização, empacotamento)
- Integrar com o AtoM: depois de preservado tecnicamente pelo Archivematica, o material pode ser descrito e disponibilizado ao público através do AtoM

## Exemplo de uso

Um arquivo universitário recebeu um HD com milhares de arquivos digitais de um pesquisador aposentado — documentos em formatos antigos, planilhas, e-mails exportados, fotos digitais de diferentes épocas. Antes de disponibilizar qualquer coisa ao público, a equipe usa o Archivematica para processar o material: identificar cada formato, normalizar os arquivos para versões mais estáveis, verificar a integridade de cada um e gerar um pacote de preservação documentado. Só depois desse processo técnico é que a equipe usa o AtoM para descrever e publicar o acervo já preservado.

## Quando pode não ser a melhor opção

- Se o objetivo é publicar uma coleção para o público, não preservar tecnicamente os arquivos: o Archivematica não tem essa função — [Omeka S](omeka-s.md), [Tainacan](tainacan.md) ou o próprio [AtoM](atom.md) (para descrição arquivística) são as ferramentas certas para isso
- Se você não tem equipe técnica com conhecimento de preservação digital e administração de servidores: a curva de aprendizado é alta, tanto pelos conceitos (OAIS, formatos de preservação) quanto pela instalação e manutenção do sistema
- Se o volume de material for pequeno e não houver necessidade de processo formal de preservação: pode ser desproporcional montar toda essa infraestrutura para poucos arquivos
- Se você precisa de suporte comercial dedicado: a Artefactual oferece serviços pagos de hospedagem e suporte, mas o software em si não inclui isso por padrão

## Tipo de acesso

Totalmente gratuito e de código aberto (licença AGPL v3). A documentação segue licença Creative Commons Atribuição-CompartilhaIgual.

## Sistemas em que roda

Acessado pelo navegador. A instalação requer um servidor Linux (Ubuntu ou Rocky Linux/RHEL são oficialmente suportados), com Docker recomendado apenas para ambiente de desenvolvimento, não produção.

## Integrações

- [AtoM](atom.md): fluxo de trabalho complementar — o Archivematica preserva tecnicamente os arquivos, e o AtoM cuida da descrição arquivística e do acesso público a esse material já preservado

## Alternativas

- Preservica (proprietário, pago, referência comercial em preservação digital)
- Rosetta (proprietário, pago, da Ex Libris, usado principalmente em bibliotecas nacionais e grandes instituições)
- LOCKSS (rede comunitária de preservação distribuída, com proposta diferente — foco em redundância entre instituições)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.archivematica.org/](https://www.archivematica.org/)
- Documentação: [https://www.archivematica.org/en/docs/latest/](https://www.archivematica.org/en/docs/latest/)
- Repositório: [https://github.com/artefactual/archivematica](https://github.com/artefactual/archivematica)
- Fórum da comunidade: [https://groups.google.com/g/archivematica](https://groups.google.com/g/archivematica)

## Observações

Vale reforçar a distinção conceitual: preservação digital (garantir que um arquivo digital continue íntegro, legível e autêntico daqui a décadas) é um problema técnico diferente de publicação de coleções (tornar um acervo navegável e pesquisável pelo público). O Archivematica resolve o primeiro problema; ferramentas como Omeka S, Tainacan e o próprio AtoM (para descrição) resolvem o segundo. Instituições com acervos digitais críticos frequentemente usam o Archivematica e o AtoM em conjunto, um complementando o outro.

