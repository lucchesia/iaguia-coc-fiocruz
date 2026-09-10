---
title: "AtoM"
slug: "atom"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "acervos e publicação"

tags:
  - descrição arquivística
  - open source
  - gratuito para pesquisa
aliases:
  - "Access to Memory"

source_model: aberto
software_license: AGPL-3.0
access_model: gratuito

systems:
  - Web
  - Linux
curva_aprendizado: "moderada a alta"
integrations:
  - Archivematica

concepts: []
alternatives:
  - Omeka S
  - Tainacan
  - ArchivesSpace

official_site: "https://www.accesstomemory.org/"
documentation: "https://www.accesstomemory.org/en/docs/"
forum: "https://groups.google.com/g/ica-atom-users"
repository: "https://github.com/artefactual/atom"

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

AtoM (Access to Memory) é uma aplicação web gratuita e de código aberto para descrição arquivística e acesso público a acervos, seguindo normas internacionais de arquivologia. Foi originalmente encomendada pelo International Council on Archives (ICA) e hoje é mantida pela Artefactual Systems — a mesma empresa por trás do [Archivematica](archivematica.md), voltado à preservação digital. AtoM e Archivematica são ferramentas complementares, não equivalentes: o Archivematica cuida da preservação técnica dos arquivos digitais, enquanto o AtoM cuida da descrição arquivística e do acesso público a esses registros.

## Para que serve

- Descrever acervos arquivísticos seguindo normas internacionais e nacionais: ISAD(G) e ISAAR (padrões do ICA), RAD (Canadá), DACS (Estados Unidos), além de Dublin Core e MODS
- Organizar a descrição em níveis hierárquicos próprios de arquivos — fundos, séries, dossiês, itens — em vez de tratar cada documento como um item isolado
- Publicar o acervo com busca pública, acessível por qualquer pessoa com navegador
- Importar e exportar dados nos formatos EAD, EAC-CPF, CSV e SKOS, compatíveis com outros sistemas arquivísticos
- Gerenciar múltiplos repositórios/instituições numa mesma instalação, com interface multilíngue

## Exemplo de uso

Um arquivo público está organizando a descrição de um fundo documental de uma antiga instituição estadual, estruturado em várias séries (correspondência, processos administrativos, relatórios) ao longo de décadas. A equipe usa o AtoM para descrever o fundo seguindo a norma ISAD(G), respeitando a hierarquia arquivística original (fundo → série → dossiê → item), e publica a descrição com busca pública — permitindo que pesquisadores encontrem os documentos sem precisar visitar o arquivo fisicamente para consultar o instrumento de pesquisa.

## Quando pode não ser a melhor opção

- Se seu acervo não é organizado com lógica arquivística (fundos, proveniência, hierarquia documental), mas sim uma coleção de itens individuais (fotografias, objetos de museu): o [Omeka S](omeka-s.md) ou o [Tainacan](tainacan.md) são mais adequados para esse tipo de publicação de coleções
- Se você precisa de preservação digital técnica dos arquivos (checagem de integridade, formatos de preservação): isso é função do [Archivematica](archivematica.md), não do AtoM — os dois são complementares, geridos pela mesma empresa, mas resolvem problemas diferentes
- Se o foco for patrimônio cultural indígena com protocolos de acesso comunitário: o [Mukurtu](mukurtu.md) foi desenhado especificamente para esse contexto
- Se você não tem formação ou apoio de profissionais de arquivologia: aproveitar bem as normas de descrição do AtoM pressupõe algum conhecimento arquivístico prévio

## Tipo de acesso

Totalmente gratuito e de código aberto (licença AGPL v3). A documentação é licenciada separadamente sob Creative Commons Atribuição-CompartilhaIgual.

## Sistemas em que roda

Acessado pelo navegador. A instalação requer um servidor (tipicamente Linux).

## Integrações

- [Archivematica](archivematica.md) (mesma empresa mantenedora, Artefactual; fluxo de trabalho complementar entre preservação e descrição/acesso)

## Alternativas

- [Omeka S](omeka-s.md) (publicação de coleções em geral, não descrição arquivística formal)
- [Tainacan](tainacan.md) (também publicação de coleções, plugin de WordPress)
- ArchivesSpace (outra ferramenta open source de descrição arquivística, mais usada em arquivos universitários dos EUA)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.accesstomemory.org/](https://www.accesstomemory.org/)
- Documentação: [https://www.accesstomemory.org/en/docs/](https://www.accesstomemory.org/en/docs/)
- Repositório: [https://github.com/artefactual/atom](https://github.com/artefactual/atom)
- Fórum da comunidade: [https://groups.google.com/g/ica-atom-users](https://groups.google.com/g/ica-atom-users)

## Observações

O AtoM é uma referência internacional em descrição arquivística de código aberto, com adoção em arquivos nacionais, universitários e municipais em diversos países. É importante não confundi-lo com ferramentas de publicação de coleções generalistas (Omeka S, Tainacan): a diferença não é só técnica, mas conceitual — arquivologia trabalha com a lógica de proveniência e hierarquia documental (fundos, séries), diferente da lógica de "itens de coleção" usada em bibliotecas e museus.

