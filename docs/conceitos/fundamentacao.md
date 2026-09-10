---
title: "Grounding"
title_pt: "Fundamentação"
slug: "fundamentacao"

entry_type: "conceito"
concept_type: "conceito"

category: "representação, busca e recuperação"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "grounding"
  - "dados de fundamentação"

related_terms:
  - rag
prerequisites:
  - rag

references:
  - title: "Grounding Data Design for AI Workloads on Azure — Microsoft Azure Well-Architected Framework | Microsoft Learn"
    url: "https://learn.microsoft.com/en-us/azure/well-architected/ai/grounding-data-design"
    type: "documentação técnica"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Fundamentação

## O que é

Fundamentação (do inglês *grounding*) é o processo de basear as respostas de um modelo de linguagem em informações externas e verificáveis, fornecidas no momento da consulta, em vez de depender apenas do conhecimento que o modelo memorizou durante o treinamento. Segundo a documentação técnica da Microsoft Azure, "dados de fundamentação são informações fornecidas a um modelo de linguagem no momento da inferência, para ajudá-lo a gerar respostas mais precisas e relevantes para a consulta de uma pessoa usuária. Esse processo de 'fundamentar o modelo' envolve complementar o modelo com dados que não faziam parte do seu treinamento original" — esses dados podem vir de sistemas internos, como bancos de dados de uma instituição, ou de fontes externas.

## Por que isso importa?

Um modelo de linguagem "puro" responde com base em padrões memorizados durante o treinamento, sem acesso a informações específicas ou atualizadas depois desse momento. Fundamentar um modelo — por exemplo, fornecendo a ele o texto de documentos específicos de um acervo, ou resultados de uma busca atualizada — reduz (embora não elimine) o risco de respostas inventadas ou desatualizadas, e permite, em muitos casos, que a resposta cite ou aponte para a fonte específica de onde a informação veio. Essa é uma diferença importante para avaliar a confiabilidade de uma ferramenta de IA usada em pesquisa.

## Exemplo

Um assistente de IA integrado ao catálogo digital de um arquivo histórico, ao responder a uma pergunta sobre um documento específico, é "fundamentado" quando recebe, junto com a pergunta, o texto real daquele documento — em vez de responder apenas com base em conhecimento genérico memorizado durante o treinamento. Isso permite que a resposta seja verificável e ligada à fonte primária real, em vez de uma reconstrução aproximada e potencialmente imprecisa feita pelo modelo.

## Não confunda com

Fundamentação não é sinônimo de [RAG](rag.md): RAG (Geração Aumentada por Recuperação) é uma técnica específica que usa busca para encontrar e fornecer dados de fundamentação a um modelo; fundamentação é o conceito mais amplo — o próprio ato de basear uma resposta em dados externos —, que pode ser implementado de formas diferentes (RAG é a mais comum, mas não a única). Também não é sinônimo de [ajuste fino](ajuste-fino.md): fundamentação fornece informação no momento da consulta, sem alterar o modelo; ajuste fino modifica de fato os parâmetros internos do modelo, de forma permanente.

## Termos relacionados

## Referências

- Microsoft. *Grounding Data Design for AI Workloads on Azure* (Azure Well-Architected Framework, Microsoft Learn).
  [learn.microsoft.com/en-us/azure/well-architected/ai/grounding-data-design](https://learn.microsoft.com/en-us/azure/well-architected/ai/grounding-data-design)
