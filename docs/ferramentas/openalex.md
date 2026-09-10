---
title: OpenAlex
slug: openalex
entry_type: ferramenta
tool_type: serviço web
category: revisão de literatura
tags:
  - revisão de literatura
  - open source
  - sem código
  - gratuito para pesquisa
aliases: []
source_model: aberto
access_model: gratuito com limites
systems:
  - Web
curva_aprendizado: baixa a moderada
integrations:
  - VOSviewer
concepts: []
alternatives:
  - Semantic Scholar
  - Google Scholar
  - Web of Science
  - Scopus
official_site: https://openalex.org
documentation: https://docs.openalex.org
forum: https://groups.google.com/g/openalex-community
repository: https://github.com/ourresearch
caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: '2026-08-19'
---

## O que é

OpenAlex é um catálogo aberto e gratuito de todo o sistema de pesquisa científica mundial — artigos, autores, instituições, periódicos e áreas de conhecimento — mantido pela organização sem fins lucrativos OurResearch. Funciona como uma base de dados bibliográfica de acesso livre, sucessora do Microsoft Academic Graph, com interface de busca web, API e possibilidade de download completo dos dados.

## Para que serve

- Buscar artigos, autores, instituições e periódicos por tema, com uma interface web de busca gratuita
- Explorar redes de citação: ver quais trabalhos um artigo cita e quais trabalhos o citam
- Acompanhar tendências de colaboração entre instituições e áreas de pesquisa ao longo do tempo
- Consultar e baixar dados em grande volume, por meio de uma API gratuita (para uso típico) ou de um snapshot completo da base
- Alimentar outras ferramentas de pesquisa e bibliometria (como o [VOSviewer](vosviewer.md)) com dados abertos de citação

## Exemplo de uso

Um pesquisador está fazendo uma revisão de literatura sobre historiografia digital e quer mapear como o campo mudou ao longo dos últimos vinte anos. Ele usa a interface web do OpenAlex para buscar o tema, filtra os resultados por ano e instituição, e explora a rede de citações entre os artigos mais relevantes — sem precisar de acesso pago a nenhuma base bibliográfica comercial.

## Quando pode não ser a melhor opção

- Se você precisa de análises automatizadas em grande volume (milhares de consultas via API): a partir de fevereiro de 2026, o uso intenso da API pode gerar cobrança — o modelo é "dados gratuitos, serviço pago"; o uso típico individual continua dentro do orçamento diário gratuito
- Se você não tem familiaridade com bases de dados bibliográficas: a interface é funcional, mas menos refinada visualmente do que a de ferramentas comerciais como Web of Science ou Scopus
- Se você precisa de curadoria editorial da mesma qualidade de bases pagas tradicionais: por ser construído automaticamente a partir de múltiplas fontes, o OpenAlex pode conter duplicações ou desambiguações imperfeitas de autores e instituições

## Tipo de acesso

Gratuito com limites de uso na API. Os dados são de domínio público (licença CC0) e podem ser baixados integralmente sem custo. A interface web de busca e o uso típico da API são gratuitos (orçamento diário gratuito de US$ 1 por chave de API, suficiente para a maioria dos usos individuais e de pesquisa). Uso institucional intenso ou em grande escala pode exigir um plano pago (a partir de US$ 5.000/ano). O código-fonte da plataforma é aberto.

## Sistemas em que roda

Funciona inteiramente pela web — interface de busca em navegador e API. Não há aplicativo de desktop; qualquer sistema operacional com acesso à internet pode usá-lo.

## Integrações

- [VOSviewer](vosviewer.md) (consulta diretamente a API do OpenAlex para construir redes bibliométricas, sem precisar baixar arquivos)
- Existem plugins não oficiais, mantidos pela comunidade, para conectar o OpenAlex a gerenciadores de referências como o Zotero

## Alternativas

- [Semantic Scholar](semantic-scholar.md) (também gratuito, com recursos de IA para resumo e recomendação)
- Google Scholar (mais conhecido, mas sem API aberta e sem dados para download)
- Web of Science e Scopus (bases comerciais, pagas, com curadoria editorial mais rigorosa)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://openalex.org](https://openalex.org)
- Documentação: [https://docs.openalex.org](https://docs.openalex.org)
- Fórum da comunidade: [https://groups.google.com/g/openalex-community](https://groups.google.com/g/openalex-community)

## Observações

O OpenAlex nasceu em 2022 como sucessor do Microsoft Academic Graph, descontinuado pela Microsoft. É mantido pela OurResearch, a mesma organização sem fins lucrativos por trás do Unpaywall. Por reunir dados de múltiplas fontes automaticamente (Crossref, PubMed, repositórios institucionais, entre outras), tem cobertura maior que muitas bases comerciais — inclusive de produção científica em português e de outras regiões historicamente sub-representadas —, mas isso também significa que pode conter inconsistências que uma curadoria manual evitaria.

