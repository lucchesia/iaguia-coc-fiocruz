---
title: Transcritor-IA
slug: transcritor-ia
entry_type: ferramenta
tool_type: serviço web
category: transcrição
tags:
  - transcrição automática
  - transcrição manual
  - gratuito para pesquisa
aliases: []
source_model: não identificado
access_model: gratuito
systems:
  - Web
curva_aprendizado: baixa a moderada
integrations:
  - nenhuma conhecida
concepts:
  - reconhecimento-de-texto-manuscrito
alternatives:
  - Transkribus
  - eScriptorium
  - Kraken
  - Google Document AI
official_site: https://transcritor-ia.com/
documentation: não disponível
forum: não disponível
caveats:
  - licença não identificada
learning_resources: []
academic_use: []
tool_status: em desenvolvimento
status: publicado
reviewed: true
last_reviewed: '2026-09-01'
---

## O que é

Transcritor-IA é uma plataforma web brasileira para transcrição assistida de documentos históricos manuscritos, desenvolvida no Instituto Federal do Ceará (IFCE), campus Aracati. Usa [reconhecimento de texto manuscrito](../conceitos/reconhecimento-de-texto-manuscrito.md) (HTR) para converter imagens de manuscritos em texto pesquisável e ajusta seus modelos a partir das correções feitas pelo próprio usuário, apoiando-se na biblioteca de código aberto PyLaia.

## Para que serve

- Transcrever automaticamente manuscritos históricos e revisar o resultado na própria interface
- Melhorar o reconhecimento a partir das correções do usuário, ajustando o modelo a uma caligrafia ou a um acervo específico
- Trabalhar com fontes e caligrafias brasileiras, pouco cobertas por modelos treinados majoritariamente em outras línguas
- Organizar e curar coleções documentais digitalizadas

## Exemplo de uso

Uma pesquisadora com um conjunto de cartas manuscritas de um médico do início do século XX faz o upload das imagens, gera uma primeira transcrição automática e corrige os trechos falhos na interface. Cada correção realimenta o modelo, que passa a errar menos naquela caligrafia ao longo da coleção.

## Quando pode não ser a melhor opção

- É um projeto recente; estabilidade, cobertura e continuidade ainda não têm a maturidade de plataformas consolidadas
- Para textos impressos ou datilografados, uma ferramenta de OCR comum tende a resolver melhor
- Caligrafias muito danificadas seguem exigindo revisão quase integral

## Tipo de acesso

Gratuito, pela web em transcritor-ia.com, desenvolvido em contexto acadêmico e público. O motor de HTR apoia-se na biblioteca aberta PyLaia; a licença do código da própria plataforma não está declarada publicamente.

## Sistemas em que roda

Navegador web.

## Integrações

Nenhuma integração externa documentada. Internamente, usa a biblioteca PyLaia para o reconhecimento.

## Alternativas

- Transkribus
- eScriptorium
- Kraken
- Google Document AI

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://transcritor-ia.com/](https://transcritor-ia.com/)
- Artigo (SEMISH 2025, SBC): [sol.sbc.org.br](https://sol.sbc.org.br/index.php/semish/article/view/36804)
- Notícia (IFCE Aracati): [portal.ifce.edu.br](https://portal.ifce.edu.br/campus/aracati/noticias/alunos-criam-plataforma-com-ia-para-transcricao-de-documentos-historicos-manuscritos/)

## Observações

Iniciativa nacional que dialoga diretamente com o problema do viés dos modelos de HTR treinados majoritariamente fora do português e de caligrafias brasileiras. Apresentada no SEMISH 2025 (SBC). Por ser recente, convém reconferir periodicamente seu estado de manutenção e disponibilidade.

