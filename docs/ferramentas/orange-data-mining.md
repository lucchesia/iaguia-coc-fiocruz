---
title: "Orange Data Mining"
slug: "orange-data-mining"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "dados e transformação"

tags:
  - dados e transformação
  - sem código
  - open source
  - uso offline
  - gratuito para pesquisa
aliases:
  - "Orange"

source_model: aberto
software_license: GPL-3.0
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "baixa a moderada"
integrations:
  - Python

concepts:
  - aprendizado-de-maquina
alternatives:
  - OpenRefine
  - Voyant Tools
  - KNIME

official_site: "https://orangedatamining.com/"
documentation: "https://orangedatamining.com/docs/"
forum: "https://github.com/biolab/orange3/discussions"
repository: "https://github.com/biolab/orange3"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Orange Data Mining é um programa gratuito e de código aberto para análise de dados, visualização e [aprendizado de máquina](../conceitos/aprendizado-de-maquina.md), desenvolvido pela Universidade de Ljubljana (Eslovênia). Sua característica principal é a programação visual: em vez de escrever código, a pessoa usuária monta um fluxo de trabalho conectando blocos visuais ("widgets") numa tela, cada um representando uma etapa da análise (carregar dados, filtrar, visualizar, aplicar um [modelo](../conceitos/modelo.md)). Diferente do [OpenRefine](openrefine.md), que foca em limpeza de dados, o Orange vai além: cobre também visualização, mineração e modelagem preditiva.

## Para que serve

- Montar fluxos de análise de dados sem programar, conectando widgets numa tela (carregar dados, filtrar, transformar, visualizar, modelar)
- Criar visualizações interativas: gráficos de dispersão, mapas de calor, árvores de decisão, agrupamento hierárquico (clustering), projeções de redução de dimensionalidade
- Aplicar algoritmos de aprendizado de máquina prontos, sem precisar programar (classificação, regressão, clustering)
- Ampliar as funcionalidades com extensões (add-ons) especializadas — inclusive uma extensão de mineração de texto, com ferramentas de pré-processamento, nuvens de palavras e modelagem de tópicos, e outra de análise de redes
- Ser usado também como biblioteca Python, para quem programa e quer combinar os dois modos de trabalho

## Exemplo de uso

Um grupo de pesquisa tem uma base de dados com informações socioeconômicas de centenas de municípios ao longo de um século e quer identificar padrões de agrupamento entre eles, sem ter conhecimento de programação. A equipe monta um fluxo de trabalho no Orange: carrega a planilha, aplica um widget de agrupamento hierárquico e visualiza o resultado num mapa de calor interativo, identificando grupos de municípios com trajetórias socioeconômicas parecidas — tudo sem escrever uma linha de código.

## Quando pode não ser a melhor opção

- Se você só precisa limpar e padronizar uma planilha, sem análise ou modelagem: o [OpenRefine](openrefine.md) é mais direto para essa tarefa específica
- Se você já programa em Python e prefere controle total sobre o processo: usar bibliotecas como pandas e scikit-learn diretamente pode ser mais flexível do que a interface visual
- Se você precisa de análise textual mais robusta (concordância, colocações): o [Voyant Tools](voyant-tools.md), com proposta mais focada em texto, pode ser mais direto — a extensão de mineração de texto do Orange é boa, mas não é o foco central da ferramenta
- No Linux, não há instalador gráfico oficial — a instalação é feita via Anaconda, pip ou compilação do código-fonte

## Tipo de acesso

Totalmente gratuito e de código aberto (licença GPL v3 ou posterior).

## Sistemas em que roda

Windows e macOS (instaladores oficiais, incluindo versão para Apple Silicon). Linux é suportado via Anaconda, pip ou compilação a partir do código-fonte, sem instalador gráfico dedicado.

## Integrações

- Python: o Orange pode ser usado como biblioteca dentro de scripts Python, para quem quer combinar a interface visual com código

## Alternativas

- [OpenRefine](openrefine.md) (foco em limpeza de dados, não em modelagem ou aprendizado de máquina)
- [Voyant Tools](voyant-tools.md) (foco em análise textual, sem programação)
- KNIME (proposta parecida de programação visual para ciência de dados, também gratuito em sua versão principal)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://orangedatamining.com/](https://orangedatamining.com/)
- Documentação: [https://orangedatamining.com/docs/](https://orangedatamining.com/docs/)
- Repositório: [https://github.com/biolab/orange3](https://github.com/biolab/orange3)
- Discussões da comunidade: [https://github.com/biolab/orange3/discussions](https://github.com/biolab/orange3/discussions)

## Observações

O Orange é amplamente usado em cursos introdutórios de ciência de dados, justamente pela proposta de ensinar conceitos de análise e aprendizado de máquina sem exigir programação prévia. A extensão de mineração de texto (Orange3-Text) é um ponto de interesse específico para humanidades digitais, pois permite montar fluxos visuais que combinam pré-processamento de texto, modelagem de tópicos e visualizações — uma alternativa a scripts em [spaCy](spacy.md) para quem não programa.

