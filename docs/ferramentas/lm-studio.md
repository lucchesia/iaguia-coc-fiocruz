---
title: "LM Studio"
slug: "lm-studio"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "modelos locais"

tags:
  - modelos locais
  - uso offline
  - gratuito para pesquisa
aliases: []

source_model: proprietário
software_license: proprietária
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "baixa a moderada"
integrations:
  - Hugging Face

concepts:
  - aprendizado-de-maquina
alternatives:
  - Ollama
  - llama.cpp
  - GPT4All

official_site: "https://lmstudio.ai/"
documentation: "https://lmstudio.ai/docs/app"
forum: "https://discord.com/invite/lmstudio"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

LM Studio é um aplicativo de desktop, gratuito mas de código fechado, para baixar e rodar modelos de [aprendizado de máquina](../conceitos/aprendizado-de-maquina.md) de linguagem localmente, com uma interface gráfica mais completa desde o início do que a do [Ollama](ollama.md). É desenvolvido pela Element Labs e, embora o aplicativo em si seja proprietário, usa por baixo dos panos motores de execução de código aberto, como o llama.cpp e o MLX (este último otimizado para Macs com chip Apple Silicon).

## Para que serve

- Buscar, baixar e gerenciar [modelos](../conceitos/modelo.md) de linguagem abertos diretamente pela interface do aplicativo, com um navegador de modelos integrado ao Hugging Face
- Conversar com o modelo numa interface de chat, com controle sobre parâmetros como temperatura e outros ajustes de geração
- Anexar documentos (PDF, TXT, DOCX, Markdown, código) à conversa, com o aplicativo decidindo automaticamente entre incluir o texto inteiro ou indexá-lo para busca (RAG), dependendo do tamanho
- Expor um servidor local com API compatível com o padrão da OpenAI, para conectar outros programas ao modelo rodando na própria máquina
- Ajustar automaticamente as configurações de hardware para tirar melhor proveito da placa de vídeo ou do chip disponível no computador

## Exemplo de uso

Um pesquisador quer experimentar diferentes modelos de linguagem para uma tarefa de resumo de documentos históricos, mas não tem experiência com linha de comando. Ele instala o LM Studio, usa o navegador de modelos integrado para encontrar e baixar um modelo adequado ao hardware do seu computador, e testa diretamente na interface de chat — anexando os documentos que quer resumir sem precisar escrever nenhum comando.

## Quando pode não ser a melhor opção

- Se você quer uma ferramenta de código aberto, com código auditável: o LM Studio é proprietário — o [Ollama](ollama.md) é uma alternativa de código aberto com proposta semelhante
- Se o computador não tem hardware suficiente: como qualquer ferramenta de modelos locais, exige mais recursos do que usar um serviço em nuvem, e modelos maiores podem ser lentos ou inviáveis em máquinas mais simples
- Se você prefere trabalhar por linha de comando e integrar modelos a scripts: o LM Studio é pensado primariamente para uso via interface gráfica, embora também tenha uma CLI (`lms`) e uma API local
- Se você quer a qualidade dos modelos proprietários mais avançados do mercado: modelos de código aberto rodando localmente costumam ficar atrás de modelos como os do ChatGPT, Claude ou Gemini em tarefas complexas

## Tipo de acesso

Gratuito tanto para uso pessoal quanto profissional/comercial (política vigente desde 2025), embora o aplicativo em si seja de código fechado. Há também planos pagos de Enterprise, com recursos adicionais como login único (SSO) e controle de acesso a modelos para equipes.

## Sistemas em que roda

Windows, macOS e Linux, com interface gráfica completa em todas as plataformas.

## Integrações

- Hugging Face (navegador de modelos integrado, para buscar e baixar modelos diretamente pela plataforma)

## Alternativas

- [Ollama](ollama.md) (código aberto, mais focado em linha de comando e API, embora também tenha interface gráfica)
- llama.cpp (motor de execução mais técnico, usado por baixo dos panos pelo próprio LM Studio)
- GPT4All (outra opção gratuita e de código aberto, com foco em simplicidade)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://lmstudio.ai/](https://lmstudio.ai/)
- Documentação: [https://lmstudio.ai/docs/app](https://lmstudio.ai/docs/app)
- Discord da comunidade: [https://discord.com/invite/lmstudio](https://discord.com/invite/lmstudio)

## Observações

O LM Studio costuma ser recomendado como porta de entrada para quem quer experimentar modelos de linguagem localmente sem lidar com linha de comando — a interface gráfica cobre desde a busca e download de modelos até o ajuste de parâmetros técnicos, tornando o processo mais acessível do que alternativas mais voltadas a quem já programa. Como no caso do Ollama, rodar modelos localmente com o LM Studio é relevante para pesquisa com dados sensíveis, desde que o hardware disponível seja suficiente.

