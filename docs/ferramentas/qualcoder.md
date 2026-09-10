---
title: "QualCoder"
slug: "qualcoder"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "anotação e marcação"

tags:
  - análise qualitativa
  - anotação de fontes
  - open source
  - uso offline
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: LGPL-3.0
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada a alta"
integrations:
  - OpenAI
  - Blablador

concepts:
  - aprendizado-de-maquina
alternatives:
  - Taguette
  - NVivo
  - ATLAS.ti

official_site: "https://qualcoder.org/"
documentation: "https://qualcoder.org/doc/en/"
forum: "https://github.com/ccbogel/QualCoder/discussions"
repository: "https://github.com/ccbogel/QualCoder"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

QualCoder é um programa gratuito e de código aberto para análise qualitativa de dados, criado por Colin Curtain (Universidade da Tasmânia) e mantido por uma pequena equipe de colaboradores. Diferente do [Taguette](taguette.md), que é deliberadamente simples, o QualCoder se aproxima mais dos recursos de programas comerciais como NVivo e ATLAS.ti: codifica não só texto, mas também imagens, áudio e vídeo, permite consultas mais avançadas e, nas versões recentes, incorpora recursos assistidos por [aprendizado de máquina](../conceitos/aprendizado-de-maquina.md).

## Para que serve

- Codificar textos, imagens, áudios e vídeos com um sistema de códigos organizados hierarquicamente
- Escrever notas de diário de pesquisa e memorandos vinculados aos dados
- Fazer consultas SQL diretamente sobre o banco de dados do projeto, para análises mais avançadas
- Gerar relatórios e visualizações em HTML, ODT, texto simples ou Excel
- Importar textos em vários formatos (TXT, ODT, DOCX, HTML, Markdown, EPUB, RTF, PDF) e exportar/importar projetos no padrão aberto REFI-QDA, compatível com outras ferramentas de QDA
- Usar codificação assistida por IA (opcional), com apoio de [modelos](../conceitos/modelo.md) de linguagem para sugerir códigos ou explorar os dados

## Exemplo de uso

Uma equipe de pesquisa está analisando entrevistas em áudio, fotografias de campo e documentos textuais de um projeto de história local, e precisa codificar os três tipos de material de forma integrada. Usando o QualCoder, cada membro da equipe codifica seu conjunto de dados (áudio, imagem ou texto) com o mesmo esquema de códigos hierárquico, e a equipe usa consultas para cruzar temas que aparecem tanto nas entrevistas quanto nas fotografias, gerando relatórios para a publicação final.

## Quando pode não ser a melhor opção

- Se você quer algo simples, para um projeto de codificação apenas de texto: o [Taguette](taguette.md) tem uma curva de aprendizado mais suave para esse caso
- Se você quer usar o recurso de IA com o modelo GPT: ele não é gratuito em si — exige créditos pagos à OpenAI (a partir de US$ 5); há uma alternativa gratuita para uso acadêmico, o Blablador, ou ainda a opção de rodar modelos localmente (com requisitos de hardware maiores)
- Se você precisa de suporte comercial dedicado ou uma interface mais polida: NVivo e ATLAS.ti, embora pagos, oferecem esse tipo de suporte
- Por ser um projeto mantido por uma equipe pequena, a curva de aprendizado dos recursos mais avançados (consultas SQL, codificação de mídia) pode ser maior do que em ferramentas comerciais mais estabelecidas

## Tipo de acesso

Totalmente gratuito e de código aberto (licença LGPL v3).

## Sistemas em que roda

Windows, macOS e Linux — via instaladores prontos ou instalação a partir do código-fonte (Python 3.13 ou superior).

## Integrações

- OpenAI (recurso opcional de codificação assistida por IA; exige créditos pagos à parte)
- Blablador (serviço de modelos de linguagem gratuito, voltado a uso acadêmico, como alternativa sem custo ao OpenAI)

## Alternativas

- [Taguette](taguette.md) (mais simples, gratuito, foco só em texto)
- NVivo (proprietário, pago, referência comercial em análise qualitativa)
- ATLAS.ti (proprietário, pago, outra referência comercial no campo)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://qualcoder.org/](https://qualcoder.org/)
- Documentação: [https://qualcoder.org/doc/en/](https://qualcoder.org/doc/en/)
- Repositório: [https://github.com/ccbogel/QualCoder](https://github.com/ccbogel/QualCoder)
- Discussões da comunidade: [https://github.com/ccbogel/QualCoder/discussions](https://github.com/ccbogel/QualCoder/discussions)

## Observações

O QualCoder é uma opção sólida para equipes de pesquisa que precisam de recursos mais próximos aos de ferramentas comerciais de QDA, mas sem custo de licença — inclusive com codificação de múltiplos tipos de mídia, algo que o Taguette não oferece. A documentação está disponível em vários idiomas, incluindo português, o que facilita a adoção em contextos de pesquisa brasileiros. Assim como no AntConc, vale deixar claro que o recurso de IA é opcional e tem um custo separado (ou uma alternativa acadêmica gratuita, o Blablador) — não faz parte do núcleo gratuito da ferramenta.

