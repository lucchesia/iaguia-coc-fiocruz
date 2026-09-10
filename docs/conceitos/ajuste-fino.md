---
title: "Fine-tuning"
title_pt: "Ajuste Fino"
slug: "ajuste-fino"

entry_type: "conceito"
concept_type: "conceito"

category: "aprendizado de máquina"

tags:
  - aprendizado de máquina
  - inteligência artificial

aliases:
  - "fine-tuning"
  - "fine tuning"
  - "tuning"

related_terms:
  - pre-treinamento
prerequisites:
  - pre-treinamento

references:
  - title: "fine-tuning — Glossary | NIST Computer Security Resource Center (citando NIST SP 800-226 e NIST AI 100-2e2025)"
    url: "https://csrc.nist.gov/glossary/term/fine_tuning"
    type: "glossário técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Ajuste Fino

## O que é

Ajuste fino é a etapa de treinamento que parte de um modelo já [pré-treinado](pre-treinamento.md) e o especializa para uma tarefa ou domínio específico, usando um volume de dados bem menor e mais direcionado do que o pré-treinamento. Segundo a norma NIST SP 800-226, ajuste fino é "uma etapa de treinamento que parte de um modelo pré-treinado (às vezes chamado de modelo fundacional) e acrescenta informação específica de uma tarefa ou domínio". O documento NIST AI 100-2e2025 detalha que essa etapa "envolve treinar ainda mais o modelo com dados específicos da tarefa" e costuma ser, em geral, uma tarefa de aprendizado supervisionado.

## Por que isso importa?

Ajuste fino é o que torna possível adaptar um modelo genérico e caro de treinar (como um grande modelo de linguagem ou um modelo de reconhecimento de fala) para um uso específico, sem repetir todo o processo de pré-treinamento — com um volume de dados e um custo computacional muito menores. Isso é relevante para projetos de pesquisa: em vez de treinar um modelo do zero, costuma ser mais viável partir de um modelo já pré-treinado e ajustá-lo com um conjunto pequeno de dados de um domínio específico — por exemplo, transcrições revisadas de um dialeto regional ou de um vocabulário técnico de uma área.

## Exemplo

O [eScriptorium](../ferramentas/escriptorium.md) permite ajustar modelos de HTR já pré-treinados a uma caligrafia específica: a pesquisadora usa um modelo existente para transcrever algumas páginas, corrige os erros manualmente e usa essas páginas corrigidas para ajustar (fine-tune) o modelo — em geral, algumas dezenas de páginas já são suficientes, bem menos do que o volume necessário para treinar um modelo do zero.

## Não confunda com

Ajuste fino não é sinônimo de pré-treinamento: pré-treinamento usa um volume muito grande de dados genéricos para produzir um modelo base; ajuste fino parte desse modelo base e o especializa com um volume bem menor de dados voltados a uma tarefa específica. Também não é sinônimo de treinamento em geral: treinamento é o termo mais amplo, que inclui tanto o pré-treinamento quanto o ajuste fino como suas etapas.

## Termos relacionados

## Referências

- NIST Computer Security Resource Center. *fine-tuning — Glossary* (citando NIST SP 800-226 e NIST AI 100-2e2025).
  [csrc.nist.gov/glossary/term/fine_tuning](https://csrc.nist.gov/glossary/term/fine_tuning)
