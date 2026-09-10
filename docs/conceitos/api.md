---
title: "Application Programming Interface"
title_pt: "API"
slug: "api"

entry_type: "conceito"
concept_type: "conceito"

category: "agentes e integração"

tags:
  - fundamentos de computação

aliases:
  - "application programming interface"
  - "interface de programação de aplicações"

related_terms:
  - mcp
prerequisites: []

references:
  - title: "application programming interface — Glossary | NIST Computer Security Resource Center (citando NISTIR 5153)"
    url: "https://csrc.nist.gov/glossary/term/application_programming_interface"
    type: "glossário técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# API

## O que é

API (Interface de Programação de Aplicações, do inglês *Application Programming Interface*) é um ponto de acesso padronizado que permite que um programa de computador use funcionalidades de outro programa ou serviço, sem precisar conhecer os detalhes internos de como esse serviço funciona. Segundo o glossário técnico do NIST (citando a NISTIR 5153), uma API é "um ponto de acesso de sistema ou função de biblioteca que tem uma sintaxe bem definida e é acessível a partir de programas de aplicação ou código de usuário, para fornecer uma funcionalidade bem definida". Uma API funciona como um "contrato": define exatamente quais pedidos um programa pode fazer a outro, e que tipo de resposta deve esperar receber.

## Por que isso importa?

Muitas ferramentas digitais usadas em pesquisa — de gerenciadores de referências a modelos de IA — oferecem uma API para que outros programas possam usar seus recursos de forma automatizada, sem precisar interagir manualmente com a interface visual da ferramenta. Entender o que é uma API ajuda a interpretar, por exemplo, por que algumas ferramentas de IA cobram por "uso de API" separadamente do plano de assinatura da interface visual, e por que integrações entre ferramentas diferentes costumam depender da existência de uma API pública e bem documentada.

## Exemplo

Uma pesquisadora que quer processar automaticamente centenas de transcrições de entrevistas de história oral pode escrever um pequeno script, em uma ferramenta como o [Jupyter](../ferramentas/jupyter.md), que envia cada transcrição para a API do [Claude](../ferramentas/claude.md) ou do [ChatGPT](../ferramentas/chatgpt.md), em vez de copiar e colar cada texto manualmente na interface de chat — economizando tempo quando o volume de documentos é grande.

## Não confunda com

API não é sinônimo de MCP (Model Context Protocol): MCP é um protocolo específico, mais recente, criado para padronizar como modelos de IA se conectam a ferramentas e fontes de dados externas; API é o conceito mais geral e antigo de ponto de acesso entre dois programas, do qual o MCP é, em certo sentido, um caso especializado voltado a IA. Também não é sinônimo de interface visual (a tela que uma pessoa usuária vê e clica): uma API é feita para ser usada por outros programas, não diretamente por pessoas.

## Termos relacionados

## Referências

- NIST Computer Security Resource Center. *application programming interface — Glossary* (citando NISTIR 5153).
  [csrc.nist.gov/glossary/term/application_programming_interface](https://csrc.nist.gov/glossary/term/application_programming_interface)
