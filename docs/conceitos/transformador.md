---
title: "Transformer"
title_pt: "Transformador"
slug: "transformador"

entry_type: "conceito"
concept_type: "arquitetura"

category: "modelos generativos"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "transformer"
  - "arquitetura transformer"

related_terms:
  - modelo-de-linguagem-grande
prerequisites:
  - rede-neural-artificial

references:
  - title: "Attention Is All You Need — Vaswani et al., NeurIPS 2017"
    url: "https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf"
    type: "documento técnico de referência (artigo original)"
  - title: "generative pre-trained transformer — Glossary | NIST Computer Security Resource Center (citando NIST AI 100-2e2025)"
    url: "https://csrc.nist.gov/glossary/term/generative_pre_trained_transformer"
    type: "glossário técnico institucional"
  - title: "self-attention — Machine Learning Glossary | Google for Developers"
    url: "https://developers.google.com/machine-learning/glossary#self-attention"
    type: "glossário técnico"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Transformador

## O que é

Transformador (do inglês *Transformer*) é uma arquitetura de [rede neural artificial](rede-neural-artificial.md) baseada inteiramente em um mecanismo chamado "atenção" (*attention*), sem usar as camadas recorrentes ou convolucionais comuns em arquiteturas anteriores. Foi proposta em 2017 no artigo "Attention Is All You Need" (Vaswani et al.), que descreve o Transformer como uma arquitetura "baseada inteiramente em mecanismos de atenção, dispensando completamente recorrência e convoluções". Segundo o glossário técnico do Google for Developers, o mecanismo central dessa arquitetura — a autoatenção (*self-attention*) — "indica a importância de uma palavra ou parte de uma palavra" em relação às demais, permitindo ao modelo processar um texto inteiro de uma vez, em vez de palavra por palavra em sequência estrita. O documento NIST AI 100-2e2025 reconhece o Transformer como "a arquitetura atualmente predominante para grandes modelos de linguagem".

## Por que isso importa?

O Transformer é a base técnica de praticamente todos os LLMs usados hoje em ferramentas de pesquisa e ensino — [ChatGPT](../ferramentas/chatgpt.md), [Claude](../ferramentas/claude.md), [Gemini](../ferramentas/gemini.md). Entender, em linhas gerais, que essa arquitetura processa um texto inteiro de uma vez e "presta atenção" de forma diferente a diferentes partes do texto ajuda a compreender por que esses modelos conseguem manter coerência em textos longos e capturar relações entre partes distantes de uma frase ou de um documento — mas também por que erros de interpretação podem ocorrer quando o contexto relevante está muito distante ou é ambíguo.

## Exemplo

Quando uma pesquisadora envia um parágrafo longo para o Claude pedindo um resumo, o mecanismo de atenção do Transformer permite ao modelo relacionar palavras distantes entre si dentro do mesmo texto — por exemplo, associar um pronome no final do parágrafo ao nome da pessoa mencionada no início — para produzir um resumo coerente.

## Não confunda com

Transformer (a arquitetura) não é sinônimo de [modelo de linguagem grande](modelo-de-linguagem-grande.md) (LLM): Transformer é o desenho técnico da rede neural; LLM é um tipo de modelo — geralmente baseado em Transformer — treinado especificamente com grandes volumes de texto. Também não é sinônimo de rede neural artificial em geral: todo Transformer é uma rede neural artificial, mas é um tipo específico de arquitetura, com um mecanismo particular (atenção) que o distingue de outras arquiteturas, como as redes convolucionais ou recorrentes.

## Termos relacionados

## Referências

- Vaswani, A. et al. *Attention Is All You Need*. NeurIPS, 2017.
  [papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf](https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf)
- NIST Computer Security Resource Center. *generative pre-trained transformer — Glossary* (citando NIST AI 100-2e2025).
  [csrc.nist.gov/glossary/term/generative_pre_trained_transformer](https://csrc.nist.gov/glossary/term/generative_pre_trained_transformer)
- Google for Developers. *Machine Learning Glossary* (entrada "self-attention").
  [developers.google.com/machine-learning/glossary](https://developers.google.com/machine-learning/glossary#self-attention)
