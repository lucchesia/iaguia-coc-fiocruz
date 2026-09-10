---
title: "LibreTranslate"
slug: "libretranslate"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "tradução"

tags:
  - tradução automática
  - open source
  - uso offline
  - gratuito para pesquisa
aliases: []

source_model: aberto
software_license: AGPL-3.0
access_model: gratuito

systems:
  - Web
  - Windows
  - macOS
  - Linux
curva_aprendizado: "baixa a moderada"
integrations:
  - Argos Translate
  - Docker

concepts: []
alternatives:
  - DeepL
  - Google Tradutor
  - Argos Translate

official_site: "https://libretranslate.com/"
documentation: "https://docs.libretranslate.com/"
forum: "não disponível"
repository: "https://github.com/LibreTranslate/LibreTranslate"

caveats:
  - requer infraestrutura própria
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

LibreTranslate é uma API e aplicativo web gratuitos e de código aberto para tradução automática, que não depende de serviços proprietários como Google ou Microsoft para funcionar. O motor de tradução por trás dele é o Argos Translate, também de código aberto. Diferente do [DeepL](deepl.md), que é um serviço fechado mantido por uma empresa, o LibreTranslate pode ser instalado e rodado inteiramente no próprio computador ou servidor, sem enviar nenhum texto a terceiros.

## Para que serve

- Traduzir textos entre cerca de 20 idiomas, incluindo português, diretamente pela interface web ou por uma API
- Ser instalado e rodado localmente (self-hosted), inclusive sem conexão à internet depois de configurado, para quem precisa de controle total sobre onde os dados são processados
- Integrar a tradução automática a outros sistemas e aplicações, via API compatível com múltiplas linguagens de programação
- Servir de alternativa a serviços de tradução comerciais para projetos com restrições de orçamento ou de privacidade

## Exemplo de uso

Uma equipe de pesquisa está processando um grande volume de documentos em vários idiomas europeus e precisa traduzir tudo para o português, mas os documentos contêm informações sigilosas que não podem ser enviadas a servidores de terceiros. A equipe instala o LibreTranslate em um servidor próprio, usando Docker, e processa os documentos localmente através da API, sem que nenhum texto saia da infraestrutura da instituição.

## Quando pode não ser a melhor opção

- Se você precisa da melhor qualidade de tradução possível, especialmente para textos acadêmicos ou técnicos: o [DeepL](deepl.md) costuma produzir traduções mais naturais e precisas para esse tipo de conteúdo
- Se você não tem conhecimento técnico para instalar e manter um servidor: usar a instância pública em libretranslate.com é mais simples, mas tem limites de uso e menos garantias de privacidade do que uma instalação própria
- Se você precisa de muitos idiomas ou de pares de idiomas menos comuns: o LibreTranslate cobre uma lista mais limitada de idiomas do que serviços comerciais maiores
- Se você precisa de tradução de documentos inteiros com formatação preservada (Word, PDF): esse tipo de recurso é mais maduro em ferramentas comerciais como o DeepL

## Tipo de acesso

Totalmente gratuito e de código aberto (licença AGPL v3) para quem instala e roda a própria instância, sem limites de uso. A instância pública hospedada em libretranslate.com tem uso gratuito limitado, com planos pagos (a partir de aproximadamente US$ 29/mês) para quem precisa de mais volume via API sem hospedar nada.

## Sistemas em que roda

Funciona em qualquer navegador ao acessar a instância pública ou uma instância própria. A instalação própria roda em Windows, macOS e Linux, tipicamente via Docker.

## Integrações

- Argos Translate (motor de tradução de código aberto usado internamente)
- Docker (forma mais comum de instalar e rodar uma instância própria)

## Alternativas

- [DeepL](deepl.md) (proprietário, geralmente com qualidade de tradução superior para textos formais)
- Google Tradutor (gratuito, mais idiomas, também proprietário)
- Argos Translate (o motor por trás do LibreTranslate, usável isoladamente como biblioteca Python ou aplicativo)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://libretranslate.com/](https://libretranslate.com/)
- Documentação: [https://docs.libretranslate.com/](https://docs.libretranslate.com/)
- Repositório: [https://github.com/LibreTranslate/LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)

## Observações

O LibreTranslate é especialmente relevante para projetos de pesquisa que lidam com fontes sensíveis ou sigilosas e não podem depender de serviços de tradução comerciais que processam o texto em servidores de terceiros. A qualidade das traduções, embora tenha melhorado ao longo do tempo, ainda costuma ficar atrás de serviços proprietários como o DeepL para textos com registro mais formal ou técnico — vale testar com uma amostra do próprio material antes de adotar a ferramenta para um projeto inteiro.

