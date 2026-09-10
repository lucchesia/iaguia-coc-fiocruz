---
title: "Mukurtu"
slug: "mukurtu"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "acervos e publicação"

tags:
  - publicação de coleções
  - patrimônio cultural
  - open source
  - gratuito para pesquisa
aliases:
  - "Mukurtu CMS"

source_model: aberto
software_license: GPL-3.0
access_model: gratuito

systems:
  - Web
  - Linux
curva_aprendizado: "moderada a alta"
integrations:
  - Drupal

concepts: []
alternatives:
  - Omeka S
  - Tainacan
  - AtoM

official_site: "https://mukurtu.org/"
documentation: "https://mukurtu.org/support/"
forum: "não disponível"
repository: "https://github.com/MukurtuCMS/mukurtucms"

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

Mukurtu é uma plataforma gratuita e de código aberto para gerenciar e compartilhar patrimônio cultural digital, criada e mantida em colaboração com comunidades indígenas pelo Center for Digital Scholarship and Curation da Washington State University. É uma distribuição do Drupal (sistema de gestão de conteúdo), mas se diferencia de plataformas de acervo genéricas como o [Omeka S](omeka-s.md) ou o [Tainacan](tainacan.md) por um recurso central: protocolos culturais que permitem que a própria comunidade defina quem pode acessar cada item, de acordo com seus próprios valores e regras — não apenas um controle técnico de permissões, mas uma estrutura pensada para respeitar formas indígenas e tradicionais de conhecimento.

## Para que serve

- Definir protocolos culturais de acesso a cada item do acervo, de totalmente aberto a estritamente restrito, de acordo com regras definidas pela própria comunidade
- Adicionar Traditional Knowledge (TK) Labels — etiquetas que informam como um material deve ser usado, circulado ou atribuído, complementando (não substituindo) o direito autoral convencional
- Registrar múltiplas narrativas sobre um mesmo item ("community records"), permitindo que diferentes vozes e sistemas de conhecimento coexistam na descrição de um mesmo objeto
- Preservar a integridade dos metadados na importação e exportação de dados ("roundtrip")

## Exemplo de uso

Uma equipe de pesquisa está trabalhando em parceria com uma comunidade indígena para digitalizar gravações de narrativas orais e objetos culturais. Em vez de publicar tudo com acesso público irrestrito, a comunidade define, junto com a equipe, quais materiais podem ser vistos por qualquer pessoa, quais só por membros da comunidade, e quais exigem autorização específica — tudo configurado no Mukurtu por meio dos protocolos culturais, com TK Labels explicando o contexto de uso apropriado de cada item.

## Quando pode não ser a melhor opção

- Se o projeto não envolve patrimônio cultural indígena ou tradicional com necessidades de protocolo comunitário: ferramentas mais genéricas, como o Omeka S ou o Tainacan, tendem a ser mais diretas
- Se você precisa de preservação digital de longo prazo (com verificação de integridade de arquivos, formatos de preservação): o Mukurtu não é uma solução de preservação digital — ele mesmo se posiciona como parte de um ecossistema maior de curadoria digital, não como substituto de ferramentas como o Archivematica
- Se você não tem equipe técnica para administrar um site Drupal: a instalação e manutenção exigem conhecimento técnico; há opções de hospedagem paga (Reclaim Hosting, Mukurtu Hosting) para quem prefere não lidar com isso
- Se a decisão de usar protocolos culturais não envolveu a comunidade detentora do patrimônio: o valor da ferramenta depende de um processo real de consulta e colaboração, não apenas da configuração técnica

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GPL v3). A hospedagem pode ser feita por conta própria ou contratada separadamente (por exemplo, com a Reclaim Hosting ou o serviço Mukurtu Hosting, mantido pela própria equipe da WSU).

## Sistemas em que roda

Acessado pelo navegador. A instalação requer um servidor compatível com Drupal (tipicamente Linux, com PHP e banco de dados).

## Integrações

- Drupal (o Mukurtu é construído como uma distribuição do Drupal, aproveitando seu ecossistema de módulos)

## Alternativas

- [Omeka S](omeka-s.md) (plataforma genérica de publicação de coleções, sem protocolos culturais dedicados)
- [Tainacan](tainacan.md) (também genérico, plugin de WordPress)
- [AtoM](atom.md) (focado em descrição arquivística formal, normas ISAD(G))

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://mukurtu.org/](https://mukurtu.org/)
- Documentação e suporte: [https://mukurtu.org/support/](https://mukurtu.org/support/)
- Repositório: [https://github.com/MukurtuCMS/mukurtucms](https://github.com/MukurtuCMS/mukurtucms)

## Observações

O Mukurtu é referência internacional em ferramentas digitais desenvolvidas em colaboração direta com comunidades indígenas, e não apenas para elas — o processo de design envolveu consulta contínua com organizações indígenas. Para pesquisa histórica ou antropológica em parceria com comunidades tradicionais no Brasil, vale considerar o Mukurtu como modelo de como equilibrar acesso digital e protocolos de conhecimento tradicional, ainda que a adoção local possa exigir adaptação de contexto.

