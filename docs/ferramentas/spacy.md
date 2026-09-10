---
title: "spaCy"
slug: "spacy"

entry_type: "ferramenta"
tool_type: "biblioteca"

category: "análise de texto"

tags:
  - análise de texto
  - open source
  - uso offline
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: MIT
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "alta"
integrations:
  - Python
  - Hugging Face
  - Jupyter

concepts:
  - aprendizado-de-maquina
  - processamento-de-linguagem-natural
alternatives:
  - NLTK
  - Voyant Tools
  - AntConc

official_site: "https://spacy.io/"
documentation: "https://spacy.io/usage"
forum: "https://github.com/explosion/spaCy/discussions"
repository: "https://github.com/explosion/spaCy"

caveats:
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

spaCy é uma biblioteca de código aberto para [processamento de linguagem natural (PLN)](../conceitos/processamento-de-linguagem-natural.md) em Python, criada por Matthew Honnibal e Ines Montani, fundadores da empresa Explosion. Diferente do [Voyant Tools](voyant-tools.md) e do [AntConc](antconc.md), que têm interface pronta e não exigem programação, o spaCy é uma biblioteca — precisa ser usada dentro de um script Python, o que exige conhecimento técnico, mas em troca oferece muito mais controle e a possibilidade de automatizar análises em larga escala. Usa modelos de [aprendizado de máquina](../conceitos/aprendizado-de-maquina.md) para as tarefas de reconhecimento e análise.

## Para que serve

- Dividir um texto em palavras e frases (tokenização) de forma sensível às particularidades de cada idioma
- Reconhecer entidades nomeadas (NER) — identificar automaticamente nomes de pessoas, lugares, organizações e datas num texto
- Analisar a estrutura sintática das frases (dependency parsing) e classificar palavras gramaticalmente (POS tagging)
- Classificar textos automaticamente por categoria ou tema
- Processar grandes volumes de texto de forma automatizada, como parte de um pipeline de pesquisa maior
- Combinar com [modelos](../conceitos/modelo.md) de linguagem mais recentes (como os disponíveis no Hugging Face) para tarefas mais avançadas

## Exemplo de uso

Um grupo de pesquisa tem um corpus de dez mil atas de câmaras municipais brasileiras do século XIX, já transcritas, e quer identificar automaticamente todos os nomes de pessoas e lugares mencionados, para depois cruzar essas informações com outras fontes. Como o volume de texto é grande demais para revisar manualmente, um membro da equipe com conhecimento de Python escreve um script usando o spaCy para extrair essas entidades de todos os documentos de uma vez, gerando uma planilha com os nomes encontrados e onde aparecem.

## Quando pode não ser a melhor opção

- Se você não programa e não tem apoio técnico disponível: o spaCy não tem interface gráfica própria — é preciso escrever código Python para qualquer tarefa. Para análise textual sem programação, o [Voyant Tools](voyant-tools.md) ou o [AntConc](antconc.md) são muito mais acessíveis
- Se você só precisa de concordância, listas de frequência ou nuvens de palavras: essas tarefas mais simples são feitas de forma muito mais direta em ferramentas prontas como o Voyant Tools
- Para português, alguns modelos e recursos (especialmente para variantes históricas da língua) são menos completos do que para inglês — pode ser necessário treinar ou adaptar modelos para textos antigos
- Se você precisa de uma solução pronta para depositar/instalar rapidamente sem configurar um ambiente Python: a curva de instalação e configuração é real

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MIT), mantido pela empresa Explosion (que também vende produtos comerciais complementares, como a ferramenta de anotação Prodigy — mas o spaCy em si não depende deles).

## Sistemas em que roda

Windows, macOS e Linux, em qualquer ambiente com Python instalado.

## Integrações

- Python (linguagem necessária para usar a biblioteca)
- Hugging Face (modelos de linguagem mais recentes, incluindo transformers, podem ser incorporados via extensões do spaCy)
- [Jupyter](jupyter.md) (comumente usado em notebooks para análises interativas)

## Alternativas

- NLTK (biblioteca Python de PLN mais antiga, com foco mais didático/acadêmico)
- [Voyant Tools](voyant-tools.md) (sem programação, mais visual, menos flexível)
- [AntConc](antconc.md) (sem programação, foco em concordância e linguística de corpus)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://spacy.io/](https://spacy.io/)
- Documentação: [https://spacy.io/usage](https://spacy.io/usage)
- Repositório: [https://github.com/explosion/spaCy](https://github.com/explosion/spaCy)
- Discussões da comunidade: [https://github.com/explosion/spaCy/discussions](https://github.com/explosion/spaCy/discussions)

## Observações

O spaCy é considerado uma das bibliotecas de PLN mais usadas em contextos de produção (não só de pesquisa acadêmica), por sua ênfase em velocidade e robustez. Para pesquisa em história, ele é mais indicado quando já existe algum apoio técnico disponível (bolsista, colaborador de humanidades digitais, ou a própria pessoa pesquisadora com conhecimento de programação) e o volume de texto justifica automatizar tarefas que, feitas manualmente, tomariam muito tempo — como extrair nomes e lugares de milhares de documentos.

