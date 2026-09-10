---
title: "Omeka S"
slug: "omeka-s"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "acervos e publicação"

tags:
  - publicação de coleções
  - open source
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: GPL-3.0
access_model: gratuito

systems:
  - Web
  - Linux
curva_aprendizado: "moderada a alta"
integrations:
  - IIIF

concepts: []
alternatives:
  - Omeka.net
  - Tainacan
  - WordPress

official_site: "https://omeka.org/s/"
documentation: "https://omeka.org/s/docs/"
forum: "https://forum.omeka.org/"
repository: "https://github.com/omeka/omeka-s"

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

Omeka S é uma plataforma gratuita e de código aberto para publicar coleções digitais e criar exposições online, voltada a bibliotecas, arquivos, museus e universidades. É mantida pela Corporation for Digital Scholarship, organização que também mantém o [Tropy](tropy.md), e é a sucessora do Omeka Classic — a versão original do software, que ainda existe separadamente e é a base do serviço hospedado [Omeka.net](omeka-net.md). Diferente do Omeka Classic, o Omeka S foi desenhado para que uma instituição gerencie múltiplos sites a partir de um único acervo compartilhado de itens e metadados.

## Para que serve

- Publicar coleções digitais (imagens, documentos, objetos catalogados) com metadados estruturados, usando por padrão o esquema Dublin Core
- Criar múltiplos sites independentes (exposições, portais temáticos) a partir de um mesmo repositório de itens, sem duplicar dados
- Associar itens a ontologias de dados vinculados (linked data), publicando os metadados também como JSON-LD
- Exibir imagens compatíveis com o padrão IIIF, permitindo zoom profundo e comparação lado a lado de imagens de alta resolução
- Ampliar funcionalidades com módulos desenvolvidos pela comunidade (importação em lote, exportação, integração com outros padrões de metadados)

## Exemplo de uso

Uma universidade tem um acervo de fotografias históricas do campus e quer publicá-lo tanto num portal geral da biblioteca quanto numa exposição temática específica sobre um evento histórico. A equipe técnica instala o Omeka S em um servidor próprio, cataloga o acervo uma única vez com metadados Dublin Core, e cria dois sites diferentes — o portal geral e a exposição temática — que reaproveitam os mesmos itens sem precisar recatalogar nada.

## Quando pode não ser a melhor opção

- Se você não tem equipe técnica para instalar e manter um servidor: o Omeka S exige instalação própria (Linux, Apache, MySQL, PHP) — o [Omeka.net](omeka-net.md) (hospedado, mas rodando o Omeka Classic, não o S) ou serviços de hospedagem gerenciada da própria Corporation for Digital Scholarship são alternativas para quem não quer lidar com infraestrutura
- Se você só precisa de um único site simples, sem múltiplas exposições compartilhando o mesmo acervo: o Omeka Classic é mais direto para esse caso
- Se sua prioridade for descrição arquivística formal (normas como ISAD(G), fundos e séries documentais): ferramentas especializadas em arquivos, como o [AtoM](atom.md), são mais adequadas para esse tipo de estrutura
- Se o foco for patrimônio cultural indígena ou tradicional, com protocolos de acesso diferenciados por comunidade: o [Mukurtu](mukurtu.md) foi desenhado especificamente para esse contexto

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GPL v3). A Corporation for Digital Scholarship também oferece hospedagem gerenciada e suporte técnico pagos ("Omeka Services"), como alternativa opcional a instalar e manter o servidor por conta própria.

## Sistemas em que roda

Acessado pelo navegador. A instalação requer um servidor Linux com Apache, MySQL e PHP.

## Integrações

- IIIF (International Image Interoperability Framework): exibição de imagens em alta resolução com zoom e anotação, via módulo específico

## Alternativas

- [Omeka.net](omeka-net.md) (versão hospedada, mas do Omeka Classic — mais simples, sem servidor próprio)
- [Tainacan](tainacan.md) (também open source, plugin de WordPress, com forte adoção em instituições brasileiras)
- [WordPress](wordpress.md) (CMS generalista; pode ser adaptado para acervos com plugins como o [Tainacan](tainacan.md), mas não foi desenhado especificamente para isso)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://omeka.org/s/](https://omeka.org/s/)
- Documentação: [https://omeka.org/s/docs/](https://omeka.org/s/docs/)
- Repositório: [https://github.com/omeka/omeka-s](https://github.com/omeka/omeka-s)
- Fórum da comunidade: [https://forum.omeka.org/](https://forum.omeka.org/)

## Observações

É comum confundir Omeka S, Omeka Classic e Omeka.net — são três coisas diferentes: Omeka Classic é o software original (um site por instalação); Omeka.net é o serviço hospedado que roda o Omeka Classic; e Omeka S é a versão mais recente e tecnicamente distinta, pensada para redes de múltiplos sites compartilhando um mesmo acervo. Vale sempre confirmar qual delas uma instituição está de fato usando antes de dar suporte ou recomendar a ferramenta.

