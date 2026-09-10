---
title: Gemini Notebook
slug: gemini-notebook
entry_type: ferramenta
tool_type: serviço web
category: inteligência artificial generativa
tags:
  - ia generativa
  - revisão de literatura
  - gratuito para pesquisa
  - sem código
aliases:
  - NotebookLM
source_model: proprietário
software_license: proprietária
access_model: freemium
systems:
  - Web
curva_aprendizado: baixa
integrations:
  - Google Drive
  - Google Docs
concepts:
  - fundamentacao
  - modelo-de-linguagem-grande
  - alucinacao
alternatives:
  - Elicit
  - Consensus
  - Claude
official_site: https://notebooklm.google/
documentation: https://support.google.com/notebooklm
forum: não disponível
caveats:
  - envia dados para serviço externo
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: '2026-09-10'
---

## O que é

Gemini Notebook é um assistente de leitura e síntese do Google que responde a partir dos documentos que você mesmo carrega, e não a partir de tudo que existe na internet. Você reúne num caderno as suas fontes, PDFs, textos, apresentações, links e áudios, e passa a fazer perguntas sobre aquele conjunto. Cada resposta traz a indicação do trecho de origem, o que permite conferir de onde a afirmação saiu. A ferramenta chamava-se NotebookLM e foi renomeada pelo Google em julho de 2026.

## Para que serve

- Fazer perguntas a um conjunto fechado de fontes suas, com indicação de origem em cada resposta
- Produzir resumos, roteiros de estudo e linhas do tempo a partir do material carregado
- Comparar o que várias fontes dizem sobre o mesmo ponto
- Gerar visões gerais em áudio, em formato de conversa, sobre o material do caderno
- Retomar rapidamente um corpus de leitura que ficou parado

## Exemplo de uso

Uma estudante de mestrado reúne no mesmo caderno os quinze artigos da sua revisão de literatura e a legislação que analisa. Em vez de reler tudo para localizar uma discussão específica, pergunta ao caderno onde os autores divergem sobre determinado conceito e recebe a resposta com o apontamento de cada trecho. Ela confere os trechos nos originais antes de usar qualquer coisa no texto.

## Quando pode não ser a melhor opção

- Se as fontes contiverem dados pessoais, entrevistas ou material sob restrição de acesso: o conteúdo carregado é processado em servidores do Google, e isso é tratamento de dados por terceiro, com as implicações da [LGPD](../conceitos/lgpd.md)
- Se você precisa de descoberta bibliográfica: a ferramenta trabalha sobre o que você já tem, e não localiza literatura nova. Para isso servem o [Connected Papers](connected-papers.md), o [Semantic Scholar](semantic-scholar.md) ou o [Litmaps](litmaps.md)
- Se o trabalho exige reprodutibilidade do procedimento: as respostas variam entre execuções e o funcionamento interno não é auditável
- A indicação de origem reduz a [alucinação](../conceitos/alucinacao.md), e não a elimina. Conferir o trecho apontado continua sendo necessário

## Tipo de acesso

Freemium. Contas pessoais do Google têm acesso gratuito, com limites de quantidade de cadernos e de fontes por caderno. Planos pagos do Google e edições do Workspace ampliam esses limites. Como os limites e as condições mudam com frequência, consulte a página oficial antes de planejar um uso intensivo.

## Sistemas em que roda

Web, em navegador, sem instalação. Há aplicativos móveis para Android e iOS.

## Integrações

- Google Drive e Google Docs, para carregar fontes que já estão na conta
- Aceita PDF, texto, apresentações, endereços da web e áudio como fontes

## Alternativas

- Elicit (busca e extração de dados de artigos científicos)
- Consensus (respostas fundamentadas em literatura publicada)
- Claude e ChatGPT com documentos anexados (menos estruturados para trabalhar com um corpus fixo)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://notebooklm.google/](https://notebooklm.google/)
- Central de ajuda: [https://support.google.com/notebooklm](https://support.google.com/notebooklm)

## Observações

A ferramenta é muito procurada por estudantes, e o motivo é o desenho: responder a partir de um conjunto fechado de fontes escolhidas por quem pergunta se aproxima mais do trabalho acadêmico do que responder a partir de um modelo treinado em texto genérico. Isso reduz o problema, sem resolvê-lo. O apontamento de origem facilita a conferência e não a dispensa. E a escolha das fontes que entram no caderno continua sendo um ato de curadoria, com todas as consequências que uma seleção tem sobre o que vai ser encontrado depois.

