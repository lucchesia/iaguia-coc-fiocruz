---
title: "System Prompt"
title_pt: "Prompt de Sistema"
slug: "prompt-de-sistema"

entry_type: "conceito"
concept_type: "conceito"

category: "interação com modelos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "system prompt"
  - "prompt do sistema"

related_terms:
  - prompt
prerequisites:
  - prompt

references:
  - title: "system prompt — Glossary | NIST Computer Security Resource Center (citando NIST AI 100-2e2025)"
    url: "https://csrc.nist.gov/glossary/term/system_prompt"
    type: "glossário técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Prompt de Sistema

## O que é

Prompt de sistema é um conjunto de instruções definidas por quem desenvolve uma ferramenta de IA generativa (ou a integra a uma aplicação), inserido automaticamente antes do texto que a pessoa usuária escreve, para orientar o comportamento geral do modelo naquele contexto. Segundo o documento NIST AI 100-2e2025, prompt de sistema são "instruções específicas de uma aplicação, fornecidas no contexto a um sistema de IA generativa pelo desenvolvedor do modelo ou da aplicação. Prompts de sistema costumam ser inseridos antes de outras entradas, e podem ter um nível de confiança mais alto do que outras formas de entrada". Diferente do [prompt](prompt.md) escrito pela pessoa usuária a cada interação, o prompt de sistema geralmente permanece fixo (ou quase) durante toda a conversa, e a pessoa usuária normalmente não o vê.

## Por que isso importa?

Entender que existe um prompt de sistema por trás de cada ferramenta de IA generativa ajuda a compreender por que diferentes ferramentas construídas sobre o mesmo modelo podem se comportar de formas distintas — o prompt de sistema pode definir, por exemplo, o tom de voz, restrições de conteúdo, o formato padrão das respostas ou instruções sobre como citar fontes. Também ajuda a entender riscos de segurança específicos de IA generativa, como tentativas de manipular um sistema para ignorar essas instruções (um tipo de ataque chamado "injeção de prompt").

## Exemplo

Quando uma ferramenta de IA generativa integrada ao site de uma biblioteca digital responde apenas sobre o acervo daquela instituição, e educadamente recusa perguntas fora desse escopo, é provável que um prompt de sistema definido por quem desenvolveu a ferramenta esteja instruindo o modelo a se comportar dessa forma — mesmo que a pessoa usuária nunca veja esse texto diretamente.

## Não confunda com

Prompt de sistema não é sinônimo de prompt (o que a pessoa usuária escreve): prompt de sistema é definido por quem desenvolve a ferramenta, geralmente invisível à pessoa usuária final, e vem antes do prompt digitado por ela numa conversa. Também não é sinônimo de [engenharia de prompt](engenharia-de-prompt.md): engenharia de prompt é a prática de elaborar prompts eficazes (seja um prompt de sistema ou um prompt comum); prompt de sistema é um tipo específico de prompt, com uma função técnica particular.

## Termos relacionados

## Referências

- NIST Computer Security Resource Center. *system prompt — Glossary* (citando NIST AI 100-2e2025).
  [csrc.nist.gov/glossary/term/system_prompt](https://csrc.nist.gov/glossary/term/system_prompt)
