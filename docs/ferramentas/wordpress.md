---
title: "WordPress"
slug: "wordpress"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "acervos e publicação"

tags:
  - CMS generalista
  - open source
  - gratuito para pesquisa
aliases:
  - "WordPress.org"

source_model: aberto
software_license: GPL-2.0
access_model: gratuito

systems:
  - Web
  - Linux
curva_aprendizado: "baixa a moderada"
integrations:
  - Tainacan

concepts: []
alternatives:
  - Omeka S
  - Drupal
  - Joomla

official_site: "https://wordpress.org/"
documentation: "https://wordpress.org/documentation/"
forum: "https://wordpress.org/support/forums/"
repository: "https://github.com/WordPress/wordpress-develop"

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

WordPress é um sistema de gestão de conteúdo (CMS) gratuito e de código aberto, usado para criar qualquer tipo de site — blogs, portais institucionais, lojas virtuais, portfólios. É mantido por uma comunidade global sob a Fundação WordPress, e é hoje o CMS mais usado do mundo. É importante situá-lo nesta lista ao lado de ferramentas como o [Omeka S](omeka-s.md): diferente delas, o WordPress **não foi desenhado para gestão de acervos ou coleções** — ele se torna uma ferramenta de acervo apenas quando combinado com plugins especializados, como o [Tainacan](tainacan.md).

## Para que serve

- Publicar e gerenciar conteúdo de qualquer tipo de site, com editor de blocos visual, sem exigir programação
- Personalizar a aparência com milhares de temas prontos, gratuitos ou pagos
- Ampliar funcionalidades com dezenas de milhares de plugins — incluindo, no caso de instituições culturais, o Tainacan, que transforma um site WordPress numa plataforma de coleções digitais
- Gerenciar múltiplos usuários com diferentes níveis de permissão de edição

## Exemplo de uso

Uma instituição cultural já mantém um site institucional em WordPress e quer, sem migrar para outra plataforma, adicionar uma seção com seu acervo de fotografias históricas. Em vez de adotar uma ferramenta de acervo dedicada, a equipe instala o plugin Tainacan no WordPress já existente, o que permite publicar a coleção com metadados estruturados e busca facetada, aproveitando a infraestrutura e o design que o site já tinha.

## Quando pode não ser a melhor opção

- Se o objetivo principal é publicar e gerenciar um acervo ou coleção digital: o WordPress sozinho não tem essa função — é preciso combiná-lo com um plugin como o Tainacan, ou considerar diretamente uma plataforma dedicada, como o [Omeka S](omeka-s.md)
- Se você precisa de descrição arquivística formal (ISAD(G), RAD, DACS): o [AtoM](atom.md) é especializado para isso, e o WordPress não tem essa estrutura nativamente
- Se o foco for patrimônio cultural indígena com protocolos de acesso comunitário: o [Mukurtu](mukurtu.md) foi desenhado especificamente para esse contexto
- Se você não quer lidar com hospedagem, atualizações e manutenção de segurança: existe a versão gerenciada WordPress.com, que resolve isso — de forma parecida com a relação entre Omeka S e Omeka.net

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GPL v2 ou posterior). A hospedagem gerenciada (WordPress.com) tem planos gratuitos e pagos separados, mas é um produto distinto do software WordPress em si.

## Sistemas em que roda

Acessado pelo navegador. A instalação autogerenciada (WordPress.org) requer um servidor com PHP e MySQL, tipicamente Linux.

## Integrações

- Tainacan: plugin que transforma um site WordPress numa plataforma de publicação de coleções digitais, com metadados estruturados e busca facetada

## Alternativas

- [Omeka S](omeka-s.md) (plataforma dedicada a acervos, não um CMS generalista)
- Drupal (outro CMS de código aberto, base do Mukurtu)
- Joomla (outro CMS generalista de código aberto)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://wordpress.org/](https://wordpress.org/)
- Documentação: [https://wordpress.org/documentation/](https://wordpress.org/documentation/)
- Repositório (espelho no GitHub; o desenvolvimento oficial usa Subversion): [https://github.com/WordPress/wordpress-develop](https://github.com/WordPress/wordpress-develop)
- Fórum da comunidade: [https://wordpress.org/support/forums/](https://wordpress.org/support/forums/)

### Material de apoio

O WordPress tem muitos tutoriais, boa parte comercial. Os dois materiais abaixo são da
própria comunidade que mantém o programa. A documentação de instalação percorre os
cinco passos até o site no ar. O curso para iniciantes cobre o uso cotidiano, do painel
administrativo à publicação, com temas, plugins e segurança, e pede cadastro gratuito para
abrir as aulas.

- "How to Install WordPress", documentação oficial:
  [https://developer.wordpress.org/advanced-administration/before-install/howto-install/](https://developer.wordpress.org/advanced-administration/before-install/howto-install/)
- Curso "Beginner WordPress User", da plataforma oficial Learn WordPress:
  [https://learn.wordpress.org/course/beginner-wordpress-user/](https://learn.wordpress.org/course/beginner-wordpress-user/)

## Uso em pesquisa e ensino

Por ser um sistema de uso geral, o WordPress aparece com frequência como base técnica de
projetos de humanidades digitais. O CERES Exhibit Toolkit, do Digital Scholarship Group da
biblioteca da Northeastern University, é um caso documentado: a ferramenta de exposições
digitais do grupo foi construída sobre uma instância customizada do WordPress.

- CERES Exhibit Toolkit, Digital Scholarship Group, Northeastern University Library:
  [https://cerestoolkit.dsg.northeastern.edu/credit/](https://cerestoolkit.dsg.northeastern.edu/credit/)

## Observações

O WordPress aparece nesta lista não porque seja uma ferramenta de acervo, mas porque, na prática, muitas instituições pequenas e médias acabam usando-o para esse fim — geralmente por já ter um site na plataforma e adicionar um plugin como o Tainacan, em vez de adotar uma solução dedicada desde o início. Vale sempre perguntar, antes de recomendar essa combinação, se as necessidades específicas de descrição e organização do acervo não seriam mais bem atendidas por uma ferramenta pensada para isso desde a origem.

