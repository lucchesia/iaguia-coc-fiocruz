---
title: "Model Context Protocol"
title_pt: "Protocolo de Contexto do Modelo"
slug: "mcp"

entry_type: "conceito"
concept_type: "protocolo"

category: "agentes e integração"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "MCP"
  - "model context protocol"

related_terms:
  - api
  - agente-de-ia
prerequisites:
  - api
  - modelo-de-linguagem-grande

references:
  - title: "Introducing the Model Context Protocol — Anthropic"
    url: "https://www.anthropic.com/news/model-context-protocol"
    type: "anúncio oficial do desenvolvedor"
  - title: "Specification (2025-11-25) — Model Context Protocol"
    url: "https://modelcontextprotocol.io/specification/2025-11-25"
    type: "especificação técnica oficial"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Protocolo de Contexto do Modelo

## O que é

MCP (Protocolo de Contexto do Modelo, do inglês *Model Context Protocol*) é um padrão aberto, criado pela Anthropic, que define uma forma comum de conectar [modelos de linguagem](modelo-de-linguagem-grande.md) a fontes de dados e ferramentas externas — como bancos de dados, repositórios de arquivos ou aplicações de trabalho. Segundo o anúncio oficial da Anthropic, "o Model Context Protocol é um padrão aberto que permite que desenvolvedores construam conexões seguras e bidirecionais entre suas fontes de dados e ferramentas de IA". A especificação técnica oficial descreve o MCP como "um protocolo aberto que permite integração contínua entre aplicações baseadas em modelos de linguagem grande e fontes de dados e ferramentas externas", padronizando como esses modelos recebem contexto e executam ações.

## Por que isso importa?

Antes de padrões como o MCP, cada ferramenta de IA precisava de uma integração feita sob medida para se conectar a cada fonte de dados ou sistema externo diferente. O MCP busca resolver esse problema criando uma "linguagem comum" entre modelos de IA e as ferramentas ou bases de dados que eles usam. Para pesquisa, isso é relevante porque abre caminho para que assistentes de IA se conectem de forma mais padronizada a bases de dados institucionais, repositórios de pesquisa ou sistemas de gestão de referências, em vez de depender de integrações proprietárias e fechadas de cada fornecedor.

## Exemplo

Uma instituição de pesquisa pode disponibilizar o acervo de seu repositório digital por meio de um "servidor MCP", permitindo que diferentes assistentes de IA — como o [Claude](../ferramentas/claude.md) ou outras ferramentas compatíveis com o protocolo — consultem esse acervo diretamente durante uma conversa, sem que a equipe da instituição precise desenvolver uma integração separada para cada ferramenta de IA diferente que queira se conectar a esse acervo.

## Não confunda com

MCP não é sinônimo de [API](api.md) em geral: uma API é o conceito amplo de ponto de acesso entre dois programas; MCP é um protocolo específico, construído sobre a ideia de API, com uma especificação padronizada voltada à conexão entre modelos de linguagem e ferramentas ou dados externos. Também não é sinônimo de [agente de IA](agente-de-ia.md): um agente de IA pode usar o MCP como uma das formas de acessar ferramentas externas durante seu funcionamento, mas o protocolo em si não é, por si só, um agente.

## Termos relacionados

## Referências

- Anthropic. *Introducing the Model Context Protocol*.
  [anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol)
- Model Context Protocol. *Specification (2025-11-25)*.
  [modelcontextprotocol.io/specification/2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
