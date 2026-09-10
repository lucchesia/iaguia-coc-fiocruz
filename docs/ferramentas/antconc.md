---
title: "AntConc"
slug: "antconc"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "análise de texto"

tags:
  - análise de texto
  - sem código
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
  - OpenAI

concepts:
  - processamento-de-linguagem-natural
alternatives:
  - Voyant Tools
  - spaCy
  - CATMA

official_site: "https://www.laurenceanthony.net/software/antconc/"
documentation: "https://antconc-manual.readthedocs.io/"
forum: "https://groups.google.com/g/antconc"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

AntConc é um programa gratuito para análise de corpus e concordância, criado e mantido por Laurence Anthony, professor da Universidade Waseda (Japão). É "freeware" — gratuito, mas de código fechado, diferente do [Voyant Tools](voyant-tools.md), que é de código aberto. É uma referência consolidada em linguística de corpus, usado há mais de duas décadas em pesquisa e ensino.

## Para que serve

- Fazer buscas de concordância (KWIC — keyword in context), mostrando cada ocorrência de uma palavra ou expressão cercada pelo contexto onde aparece
- Gerar listas de frequência de palavras e de palavras-chave (comparando um corpus de estudo com um corpus de referência)
- Analisar clusters e n-gramas (sequências de palavras que aparecem repetidamente)
- Identificar colocações — palavras que tendem a aparecer próximas de um termo específico
- Construir e gerenciar corpora de texto diretamente no programa
- Opcionalmente, conversar com os resultados da análise usando [modelos](../conceitos/modelo.md) de linguagem de IA (recurso novo, que exige uma chave de API paga da OpenAI, fornecida pela própria pessoa usuária)

## Exemplo de uso

Uma pesquisadora de história está estudando como um jornal do início do século XX usava o termo "progresso" em diferentes contextos. Ela reúne os textos digitalizados em um corpus no AntConc e usa a ferramenta de concordância para ver todas as ocorrências da palavra lado a lado, com o texto ao redor. Em seguida, usa a lista de colocações para identificar quais palavras aparecem com mais frequência perto de "progresso" naquele período, revelando associações de sentido que seriam difíceis de perceber lendo o jornal manualmente.

## Quando pode não ser a melhor opção

- Se você prefere uma ferramenta de código aberto, com código auditável: o AntConc é freeware, não open source — o [Voyant Tools](voyant-tools.md) é uma alternativa de código aberto com proposta parecida
- Se você quer visualizações mais variadas (nuvens de palavras, gráficos de tendência, redes): o Voyant Tools tem uma variedade maior de visualizações prontas
- Se você quer usar o recurso de IA integrado: ele não é gratuito em si — depende de uma chave de API da OpenAI paga à parte, com custo por uso
- Se você precisa de [processamento de linguagem natural](../conceitos/processamento-de-linguagem-natural.md) mais avançado (reconhecimento de entidades, análise sintática automatizada): ferramentas como o [spaCy](spacy.md), que exigem programação, oferecem mais controle

## Tipo de acesso

Gratuito (freeware), mas de código fechado — não é open source. O autor aceita doações voluntárias para manutenção contínua do projeto.

## Sistemas em que roda

Windows, macOS (incluindo Apple Silicon) e Linux (via Flatpak).

## Integrações

- OpenAI (recurso opcional de IA conversacional sobre os resultados da análise; exige chave de API própria, paga separadamente à OpenAI)

## Alternativas

- [Voyant Tools](voyant-tools.md) (código aberto, mais visual, também sem programação)
- [spaCy](spacy.md) (biblioteca de código aberto para PLN, exige programação, mais flexível)
- CATMA (ferramenta de anotação e análise de texto colaborativa, com proposta parecida)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.laurenceanthony.net/software/antconc/](https://www.laurenceanthony.net/software/antconc/)
- Documentação: [https://antconc-manual.readthedocs.io/](https://antconc-manual.readthedocs.io/)
- Fórum da comunidade: [https://groups.google.com/g/antconc](https://groups.google.com/g/antconc)

## Observações

O AntConc é um dos programas mais citados em manuais de linguística de corpus e é frequentemente ensinado em cursos de introdução à análise textual computacional, ao lado do Voyant Tools. A adição recente de um recurso de IA conversacional é opcional e não afeta as ferramentas tradicionais do programa — vale deixar claro para quem for indicar a ferramenta que esse recurso específico tem custo à parte (via OpenAI), diferente do restante do programa, que é inteiramente gratuito.

