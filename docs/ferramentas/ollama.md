---
title: "Ollama"
slug: "ollama"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "modelos locais"

tags:
  - modelos locais
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
curva_aprendizado: "moderada"
integrations:
  - Python
  - LangChain

concepts:
  - aprendizado-de-maquina
alternatives:
  - LM Studio
  - llama.cpp
  - GPT4All

official_site: "https://ollama.com/"
documentation: "https://docs.ollama.com/"
forum: "não disponível"
repository: "https://github.com/ollama/ollama"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Ollama é um programa gratuito e de código aberto para baixar e rodar localmente modelos de [aprendizado de máquina](../conceitos/aprendizado-de-maquina.md) de linguagem, diretamente no próprio computador, sem depender de servidores de terceiros. Criado por ex-integrantes da equipe do Docker, funciona principalmente por linha de comando, mas desde 2026 também tem uma interface gráfica oficial para Windows e macOS, com aparência de chat, para quem prefere não usar o terminal.

## Para que serve

- Baixar e rodar modelos de linguagem abertos (como Llama, Qwen, DeepSeek, Gemma, entre outros) localmente, com um único comando
- Conversar com o [modelo](../conceitos/modelo.md) por uma interface gráfica de chat (Windows/macOS) ou por linha de comando (todas as plataformas)
- Expor uma API local compatível com o padrão da OpenAI, permitindo que outros programas e editores de código se conectem ao modelo rodando na própria máquina
- Processar arquivos e usar modelos com capacidade de visão (imagens) ou raciocínio mais avançado, dependendo do modelo escolhido
- Garantir que nenhuma informação da conversa saia do computador, já que o processamento é inteiramente local

## Exemplo de uso

Um pesquisador quer usar um assistente de IA para revisar rascunhos de um artigo com dados sensíveis de entrevistas, mas não quer enviar esse conteúdo a servidores externos. Ele instala o Ollama no próprio computador, baixa um modelo de linguagem de código aberto adequado ao hardware disponível, e passa a interagir com ele localmente pela interface de chat — sem que nenhum trecho do texto saia da máquina.

## Quando pode não ser a melhor opção

- Se o computador não tem hardware suficiente (RAM e, idealmente, placa de vídeo dedicada): modelos rodando localmente exigem mais recursos do que usar um serviço em nuvem como ChatGPT ou Claude, e modelos maiores podem ser lentos ou inviáveis em máquinas mais simples
- Se você quer a qualidade dos modelos mais avançados do mercado: os modelos de código aberto que rodam localmente costumam ficar atrás dos modelos proprietários mais recentes (como os usados no ChatGPT, Claude ou Gemini) em tarefas complexas
- Se você não tem nenhuma familiaridade técnica e está no Linux: a interface gráfica oficial só existe para Windows e macOS; no Linux, o uso principal ainda é por linha de comando
- Se você prefere não gerenciar nada disso sozinho: o Ollama também oferece um serviço de nuvem opcional e pago (Ollama Cloud) para rodar modelos maiores sem depender do hardware local — mas nesse caso, o processamento deixa de ser 100% local

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MIT) para uso local, sem limites. Há também o Ollama Cloud, serviço opcional e pago (planos Free, Pro e Max) para rodar modelos maiores nos servidores da própria Ollama — mas o uso local do programa continua gratuito e ilimitado independentemente disso.

## Sistemas em que roda

Windows, macOS e Linux. A interface gráfica oficial está disponível para Windows e macOS; no Linux, o uso é primariamente por linha de comando.

## Integrações

- Python (biblioteca oficial para integrar o Ollama a scripts e aplicações)
- LangChain (framework popular para construir aplicações com modelos de linguagem, com suporte nativo ao Ollama)

## Alternativas

- [LM Studio](lm-studio.md) (também roda modelos localmente, com interface gráfica mais desenvolvida desde o início)
- llama.cpp (motor de execução mais técnico, usado inclusive por baixo dos panos por ferramentas como o próprio Ollama)
- GPT4All (outra opção gratuita e de código aberto, com foco em simplicidade para quem não tem experiência técnica)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://ollama.com/](https://ollama.com/)
- Documentação: [https://docs.ollama.com/](https://docs.ollama.com/)
- Repositório: [https://github.com/ollama/ollama](https://github.com/ollama/ollama)

## Observações

O Ollama se tornou uma das formas mais populares de rodar modelos de IA localmente, com dezenas de milhões de downloads de modelos por mês. Para pesquisa em humanidades que envolva dados sensíveis — entrevistas de história oral, informações de participantes de pesquisa, documentos sigilosos — rodar um modelo localmente com o Ollama é uma alternativa relevante a serviços em nuvem, desde que o hardware disponível seja suficiente e a pessoa pesquisadora esteja ciente de que a qualidade das respostas pode ser inferior à dos modelos proprietários mais avançados.

