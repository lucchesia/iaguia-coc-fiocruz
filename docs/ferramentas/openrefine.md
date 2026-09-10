---
title: "OpenRefine"
slug: "openrefine"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "dados e transformação"

tags:
  - dados e transformação
  - open source
  - uso offline
  - gratuito para pesquisa
aliases:
  - "Google Refine"

source_model: aberto
software_license: BSD-3-Clause
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada"
integrations:
  - Wikidata
  - Wikibase

concepts: []
alternatives:
  - Orange Data Mining
  - Excel
  - Trifacta Wrangler

official_site: "https://openrefine.org/"
documentation: "https://openrefine.org/docs"
forum: "https://forum.openrefine.org/"
repository: "https://github.com/OpenRefine/OpenRefine"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

OpenRefine é um programa gratuito e de código aberto para limpar, organizar e transformar dados "bagunçados" — planilhas com inconsistências, duplicatas, grafias variadas de um mesmo nome, formatos misturados. Roda localmente no computador (usando o navegador como interface, mas sem enviar dados a servidores externos) e é bastante usado em bibliotecas, arquivos e projetos de pesquisa que lidam com grandes planilhas de dados. Originou-se como Google Refine, projeto comprado pelo Google em 2010, e se tornou um projeto de código aberto mantido pela comunidade a partir de 2012.

## Para que serve

- Limpar dados inconsistentes: corrigir grafias diferentes do mesmo valor (ex.: "São Paulo", "Sao Paulo", "SP") usando agrupamento (clustering) automático de valores parecidos
- Filtrar e explorar os dados por facetas (categorias), sem precisar escrever fórmulas
- Transformar dados de um formato para outro (CSV, TSV, Excel, JSON, XML, entre outros)
- Reconciliar dados com bases externas, como o Wikidata — vinculando, por exemplo, nomes de pessoas ou lugares de uma planilha aos itens correspondentes no Wikidata
- Desfazer e refazer qualquer alteração, com histórico completo das transformações aplicadas ao longo do projeto

## Exemplo de uso

Uma equipe de pesquisa tem uma planilha com milhares de registros de batismo digitalizados de um arquivo paroquial, e os nomes de lugares aparecem grafados de formas diferentes ao longo dos anos ("Bahia", "Bahya", "BAHIA"). Usando o recurso de clustering do OpenRefine, a equipe identifica rapidamente essas variações e as padroniza em um único valor. Em seguida, usa a reconciliação com o Wikidata para vincular cada lugar mencionado ao item correspondente na base, enriquecendo os dados com coordenadas geográficas e outras informações — sem precisar preencher isso manualmente linha por linha.

## Quando pode não ser a melhor opção

- Se você só precisa de operações simples de planilha (somar, filtrar, ordenar): um programa de planilha comum (Excel, LibreOffice Calc, Google Sheets) é mais direto
- Se você precisa de análise estatística ou visual mais avançada dos dados: ferramentas como o [Orange Data Mining](orange-data-mining.md) são mais indicadas depois que os dados já estão limpos
- Se você não tem paciência para aprender uma ferramenta nova: há uma curva de aprendizado real para usar bem os recursos de faceting, clustering e a linguagem de expressões própria (GREL) usada em transformações mais avançadas
- Datasets extremamente grandes (milhões de linhas) podem exigir mais memória do que o computador disponível tem

## Tipo de acesso

Totalmente gratuito e de código aberto (licença BSD 3-Clause).

## Sistemas em que roda

Windows, macOS e Linux. Nas versões para Windows e Mac, o Java necessário já vem incluído no instalador; no Linux, é preciso ter um Java Runtime Environment (JRE) instalado separadamente.

## Integrações

- Wikidata (serviço de reconciliação de dados: vincula valores da planilha a itens do Wikidata)
- Wikibase (mesma lógica de reconciliação, para outras instâncias que usam essa tecnologia, além do Wikidata)

## Alternativas

- [Orange Data Mining](orange-data-mining.md) (mais voltado à análise visual e mineração de dados, menos à limpeza inicial)
- Excel / LibreOffice Calc / Google Sheets (para tarefas simples de planilha, sem os recursos de limpeza avançada)
- Trifacta Wrangler (proprietário, com proposta parecida, focado em ambientes corporativos)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://openrefine.org/](https://openrefine.org/)
- Documentação: [https://openrefine.org/docs](https://openrefine.org/docs)
- Repositório: [https://github.com/OpenRefine/OpenRefine](https://github.com/OpenRefine/OpenRefine)
- Fórum da comunidade: [https://forum.openrefine.org/](https://forum.openrefine.org/)

## Observações

O recurso de reconciliação com o Wikidata torna o OpenRefine especialmente relevante para projetos de humanidades digitais que trabalham com dados vinculados (linked data) e querem conectar seus registros a identificadores estáveis e reconhecidos internacionalmente — uma prática cada vez mais valorizada em projetos de acervos e bases de dados históricas. Por processar tudo localmente, também é uma opção segura para dados de pesquisa sensíveis, já que nada é enviado a servidores de terceiros (exceto quando a própria pessoa usuária opta por usar um serviço de reconciliação externo).

