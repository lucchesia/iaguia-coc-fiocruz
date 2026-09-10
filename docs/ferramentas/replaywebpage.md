---
title: "ReplayWeb.page"
slug: "replaywebpage"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "preservação digital"

tags:
  - preservação digital
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
curva_aprendizado: "baixa"
integrations:
  - ArchiveWeb.page
  - Browsertrix

concepts:
  - preservacao-digital
alternatives:
  - Wayback Machine
  - pywb
  - OpenWayback

official_site: "https://webrecorder.net/replaywebpage/"
documentation: "https://replayweb.page/docs/"
forum: "https://forum.webrecorder.net/c/help/5"
repository: "https://github.com/webrecorder/replayweb.page"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-27"
---

## O que é

ReplayWeb.page é uma ferramenta gratuita e de código aberto, do projeto Webrecorder, que reproduz arquivos web (nos formatos WARC e WACZ) inteiramente no navegador, sem precisar de nenhum servidor — o "back-end" roda como um service worker (via wabac.js) dentro do próprio navegador. Pode ser usado como visualizador hospedado em replayweb.page, como aplicativo desktop, como Progressive Web App instalável, ou incorporado (embed) em outros sites como componente.

## Para que serve

- Reproduzir localmente arquivos de páginas web capturados nos formatos WARC ou WACZ, sem enviar nada a um servidor
- Explorar coleções de páginas arquivadas com navegação interativa, como se estivesse acessando as páginas originais
- Buscar texto completo dentro do conteúdo arquivado (indexação full-text)
- Reproduzir capturas com Flash (via emulador Ruffle), útil para arquivos web mais antigos
- Incorporar (embed) o visualizador em outro site, para publicar arquivos web capturados sem depender de infraestrutura própria de servidor

## Exemplo de uso

Uma pesquisadora usou o [ArchiveWeb.page](archivewebpage.md) para capturar dezenas de páginas de um site governamental antes de ele ser retirado do ar. Depois, para compartilhar essas capturas com colegas de pesquisa sem precisar hospedar um servidor, ela abre os arquivos WACZ resultantes diretamente no ReplayWeb.page — tanto localmente pelo aplicativo desktop quanto enviando o arquivo para colegas explorarem no navegador deles, sem precisar instalar nada além do próprio ReplayWeb.page.

## Quando pode não ser a melhor opção

- Se você ainda não tem um arquivo WARC/WACZ para reproduzir: o ReplayWeb.page só reproduz capturas já feitas — para capturar páginas, é preciso primeiro usar uma ferramenta como o [ArchiveWeb.page](archivewebpage.md) ou o Browsertrix
- Se você precisa de um serviço de arquivamento público e permanente, mantido por terceiros: a Wayback Machine, do Internet Archive, cumpre esse papel; o ReplayWeb.page é para reproduzir arquivos que você (ou sua instituição) já possui
- Se você precisa hospedar a reprodução de arquivos em escala, com controle de acesso ou múltiplos usuários simultâneos em servidor próprio: soluções server-side como o pywb podem ser mais adequadas do que a reprodução client-side do ReplayWeb.page

## Tipo de acesso

Totalmente gratuito e de código aberto (licença AGPL v3).

## Sistemas em que roda

Funciona em qualquer navegador moderno (versão web hospedada ou incorporada via componente). Também há aplicativo desktop para Windows, macOS e Linux, e uma versão instalável como Progressive Web App (PWA).

## Integrações

- [ArchiveWeb.page](archivewebpage.md) (ferramenta de captura da mesma família Webrecorder; usa o ReplayWeb.page como motor de reprodução integrado)
- Browsertrix (plataforma de arquivamento em escala da Webrecorder; as coleções capturadas podem ser reproduzidas no ReplayWeb.page)

## Alternativas

- Wayback Machine (serviço público de arquivamento e reprodução do Internet Archive, sem necessidade de gerenciar os próprios arquivos)
- pywb (servidor de reprodução de arquivos web self-hosted, para quem precisa de reprodução do lado do servidor em vez de no navegador)
- OpenWayback (ferramenta mais antiga de reprodução de arquivos web, com desenvolvimento menos ativo atualmente)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://webrecorder.net/replaywebpage/](https://webrecorder.net/replaywebpage/)
- Documentação: [https://replayweb.page/docs/](https://replayweb.page/docs/)
- Repositório: [https://github.com/webrecorder/replayweb.page](https://github.com/webrecorder/replayweb.page)
- Fórum de ajuda: [https://forum.webrecorder.net/c/help/5](https://forum.webrecorder.net/c/help/5)

## Observações

ReplayWeb.page é o motor de reprodução usado por baixo dos panos por outras ferramentas do glossário, como o próprio [ArchiveWeb.page](archivewebpage.md) — mas também pode ser usado de forma independente, só para reproduzir arquivos WARC/WACZ já existentes, sem nenhuma etapa de captura. É especialmente útil para compartilhar arquivos web capturados com outras pessoas sem precisar manter um servidor próprio: basta enviar o arquivo WACZ e a pessoa destinatária abre no ReplayWeb.page.

