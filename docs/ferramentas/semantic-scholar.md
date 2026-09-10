---
title: Semantic Scholar
slug: semantic-scholar
entry_type: ferramenta
tool_type: serviço web
category: revisão de literatura
tags:
  - revisão de literatura
  - gratuito para pesquisa
  - sem código
aliases: []
source_model: proprietário
software_license: proprietária
access_model: gratuito
systems:
  - Web
curva_aprendizado: baixa
integrations:
  - Zotero
concepts:
  - embedding
alternatives:
  - OpenAlex
  - Google Scholar
  - Connected Papers
  - Scite
official_site: https://www.semanticscholar.org
documentation: https://www.semanticscholar.org/faq
forum: https://github.com/allenai/s2-folks
caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: '2026-08-19'
---

## O que é

Semantic Scholar é um motor de busca acadêmico gratuito, com recursos de [inteligência artificial](../conceitos/inteligencia-artificial.md), mantido pelo Allen Institute for AI (AI2), organização de pesquisa sem fins lucrativos fundada por Paul Allen (cofundador da Microsoft). Indexa centenas de milhões de artigos científicos de todas as áreas do conhecimento e usa IA para gerar resumos automáticos, identificar citações influentes, comparar o significado de artigos por meio de [embeddings](../conceitos/embedding.md) e recomendar trabalhos relacionados.

## Para que serve

- Buscar artigos científicos por tema, autor ou instituição, com resultados organizados por relevância e influência
- Ler resumos automáticos gerados por IA (TLDR) de cada artigo, para avaliar rapidamente se vale a pena ler o texto completo
- Identificar quais citações de um artigo são mais influentes para aquele trabalho (não apenas contá-las)
- Consultar dados acadêmicos (artigos, autores, citações) por meio de uma API gratuita, para pesquisas automatizadas
- Ler artigos em uma interface de leitura aumentada (Semantic Reader, em beta), com anotações e contexto adicionais
- Salvar artigos diretamente no Zotero a partir do Semantic Reader, incluindo o resumo TLDR

## Exemplo de uso

Um pesquisador está começando uma revisão de literatura sobre um tema pouco familiar em história da ciência. Antes de decidir quais artigos ler na íntegra, ele usa o Semantic Scholar para buscar o tema e lê os resumos automáticos (TLDR) de dezenas de resultados, priorizando a leitura completa apenas dos artigos mais relevantes — o que economiza um tempo considerável de triagem.

## Quando pode não ser a melhor opção

- Se você precisa de curadoria e revisão editorial tradicional, como a de bases comerciais: por depender de processamento automático (incluindo IA) para gerar resumos e classificar citações, os resultados podem conter imprecisões que uma curadoria manual evitaria
- Se você precisa de uso comercial da API: o acesso gratuito é voltado a uso acadêmico, de pesquisa e não comercial — aplicações comerciais exigem autorização especial da AI2
- Se você precisa de alto volume de consultas automatizadas sem qualquer limite: usuários sem chave de API compartilham um limite de requisições; é possível solicitar uma chave gratuita para limites maiores, mas ainda assim há restrições de uso

## Tipo de acesso

Totalmente gratuito para uso acadêmico e de pesquisa, tanto a interface web quanto a API — não há planos pagos para esse uso. A API tem limites de requisições para uso sem chave, mas uma chave gratuita com limites maiores pode ser solicitada. Uso comercial da API exige permissão separada da AI2. O serviço em si é proprietário (mantido pela AI2), embora alguns conjuntos de dados e bibliotecas de código relacionados sejam disponibilizados como projetos de código aberto à parte.

## Sistemas em que roda

Funciona inteiramente pela web — interface de busca em navegador e API. Não há aplicativo de desktop nem versão mobile dedicada.

## Integrações

- Zotero (por meio da extensão de navegador do Zotero, é possível salvar artigos do Semantic Reader diretamente na biblioteca, incluindo o resumo TLDR)
- API pública consumida por diversas outras ferramentas de pesquisa e bibliometria

## Alternativas

- [OpenAlex](openalex.md) (também gratuito e com dados abertos, mantido por uma ONG sem foco específico em IA)
- Google Scholar (mais conhecido, mas sem API aberta nem resumos automáticos)
- [Connected Papers](connected-papers.md) (foco em visualização de redes de artigos relacionados)
- [Scite](scite.md) (foco em análise do contexto das citações — concordam ou discordam do trabalho citado)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.semanticscholar.org](https://www.semanticscholar.org)
- Documentação: [https://www.semanticscholar.org/faq](https://www.semanticscholar.org/faq)
- Fórum da comunidade: [https://github.com/allenai/s2-folks](https://github.com/allenai/s2-folks)

## Observações

O Semantic Scholar é um dos exemplos mais conhecidos de aplicação de IA à descoberta de literatura acadêmica — o recurso TLDR (resumos automáticos) e a classificação de citações "influentes" usam [modelos](../conceitos/modelo.md) de linguagem e aprendizado de máquina desenvolvidos pela própria AI2. Diversos componentes de pesquisa por trás da plataforma (como o corpus S2ORC e o algoritmo de desambiguação de autores S2AND) são publicados como projetos de código aberto separados, embora a plataforma principal (semanticscholar.org) não seja, em si, um software de código aberto.

