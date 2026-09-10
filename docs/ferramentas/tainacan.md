---
title: "Tainacan"
slug: "tainacan"

entry_type: "ferramenta"
tool_type: "extensão"

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
curva_aprendizado: "moderada"
integrations:
  - WordPress

concepts: []
alternatives:
  - Omeka S
  - Mukurtu
  - AtoM

official_site: "https://tainacan.org/"
documentation: "https://tainacan.org/en/documentation/"
forum: "https://tainacan.discourse.group/"
repository: "https://github.com/tainacan/tainacan"

caveats:
  - requer infraestrutura própria
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Tainacan é um plugin gratuito e de código aberto que transforma um site [WordPress](wordpress.md) numa plataforma de repositório digital para publicar e gerenciar coleções. É desenvolvido pela Universidade de Brasília (UnB), com apoio da UFG, do IBICT e do Ibram (Instituto Brasileiro de Museus), e tem forte adoção em instituições culturais brasileiras — mais de trinta museus do Ibram, além do Museu do Índio e do Museu Paulista, entre outras instituições, usam a ferramenta.

## Para que serve

- Publicar coleções digitais dentro de um site WordPress já existente, com a mesma facilidade de publicar um post de blog
- Criar estruturas de metadados personalizadas, com vocabulários controlados e taxonomias próprias para cada tipo de coleção
- Oferecer busca facetada, permitindo que visitantes filtrem itens por categoria, data, tema ou autor
- Importar dados em lote a partir de planilhas, e exportar coleções em CSV ou XLSX
- Disponibilizar uma API REST com suporte ao padrão de metadados Dublin Core, para integração com outros sistemas

## Exemplo de uso

Um museu histórico municipal já tem um site em WordPress e quer publicar seu acervo de objetos catalogados sem precisar migrar para outra plataforma. A equipe instala o plugin Tainacan no site existente, define os campos de metadados relevantes para o tipo de acervo (data, proveniência, material, condição de conservação) e começa a publicar os itens com busca facetada, permitindo que o público filtre a coleção por período ou categoria.

## Quando pode não ser a melhor opção

- Se sua instituição não usa WordPress e não quer adotá-lo: o Tainacan depende do WordPress como base — o [Omeka S](omeka-s.md), que é uma plataforma independente, pode ser mais direto nesse caso
- Se você precisa de descrição arquivística formal, com normas como ISAD(G): o [AtoM](atom.md) é mais especializado para esse tipo de estrutura
- Se o foco for patrimônio cultural indígena com protocolos de acesso diferenciados por comunidade: o [Mukurtu](mukurtu.md) foi desenhado especificamente para esse contexto
- Se você não tem nenhuma familiaridade com WordPress: ainda que a publicação em si seja simples, configurar a estrutura de metadados exige algum aprendizado prévio

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GPL v3).

## Sistemas em que roda

Funciona como plugin dentro de uma instalação WordPress, que por sua vez requer um servidor com PHP e MySQL (tipicamente Linux).

## Integrações

- [WordPress](wordpress.md) (é a base sobre a qual o Tainacan funciona — não é opcional, é um plugin desse CMS)

## Alternativas

- [Omeka S](omeka-s.md) (plataforma independente, não depende do WordPress)
- [Mukurtu](mukurtu.md) (focado especificamente em patrimônio cultural indígena e protocolos comunitários de acesso)
- [AtoM](atom.md) (focado em descrição arquivística formal, normas ISAD(G))

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://tainacan.org/](https://tainacan.org/)
- Documentação: [https://tainacan.org/en/documentation/](https://tainacan.org/en/documentation/)
- Repositório: [https://github.com/tainacan/tainacan](https://github.com/tainacan/tainacan)
- Fórum da comunidade: [https://tainacan.discourse.group/](https://tainacan.discourse.group/)

### Material de apoio

O guia inicial do wiki oficial monta uma coleção de exemplo do começo ao fim, passando pela
configuração dos metadados e pela criação de taxonomias. É o caminho mais curto para entender
a lógica do sistema antes de instalar.

- "Getting Started", wiki oficial:
  [https://tainacan.github.io/tainacan-wiki/#/getting-started](https://tainacan.github.io/tainacan-wiki/#/getting-started)

## Uso em pesquisa e ensino

O Tainacan tem adoção institucional ampla no Brasil, registrada em outra parte deste verbete,
e tem também um estudo de caso publicado. Estudantes de Museologia da UFPA relataram a
implementação do repositório digital do Museu do Instituto Evandro Chagas em projeto de
extensão, com a metodologia, os resultados e as dificuldades encontradas. Adotar a ferramenta e
documentar o que aconteceu ao usá-la são coisas diferentes, e é a segunda que interessa a
quem planeja um projeto parecido.

- LIMA, Jessica Tarine Moitinho de et al. O repositório digital do Museu do Instituto Evandro
  Chagas: resultados da implementação com o Tainacan. *Revista Ibero-Americana de Ciência da
  Informação*, v. 17, n. 3, 2024:
  [https://doi.org/10.26512/rici.v17.n3.2024.51660](https://doi.org/10.26512/rici.v17.n3.2024.51660)

## Observações

O Tainacan é um projeto brasileiro com adoção consolidada em museus e instituições culturais do Brasil — um diferencial relevante para pesquisadores e instituições nacionais, tanto pela proximidade institucional quanto pela documentação e suporte em português. Por rodar sobre o WordPress, também é uma opção prática para instituições que já mantêm um site nessa plataforma e querem adicionar um repositório de coleções sem trocar de sistema.

