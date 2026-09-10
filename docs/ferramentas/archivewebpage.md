---
title: "ArchiveWeb.page"
slug: "archivewebpage"

entry_type: "ferramenta"
tool_type: "extensão"

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
curva_aprendizado: "baixa a moderada"
integrations:
  - Browsertrix
  - ReplayWeb.page

concepts: []
alternatives:
  - Wayback Machine
  - HTTrack
  - SingleFile

official_site: "https://webrecorder.net/archivewebpage/"
documentation: "https://archiveweb.page/guide"
forum: "https://forum.webrecorder.net/c/help/5"
repository: "https://github.com/webrecorder/archiveweb.page"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

ArchiveWeb.page é uma ferramenta gratuita e de código aberto para arquivar páginas da web com alta fidelidade, capturando não só o texto e as imagens, mas também interações (cliques, rolagem, formulários) enquanto a pessoa navega. É desenvolvida pelo projeto Webrecorder e está disponível tanto como extensão para navegadores baseados em Chromium (Chrome, Brave, Edge) quanto como aplicativo desktop independente (via Electron), com funcionalidade idêntica nas duas formas.

## Para que serve

- Capturar páginas web interativamente enquanto a pessoa navega, incluindo conteúdo carregado dinamicamente (JavaScript, vídeos incorporados, formulários preenchidos)
- Organizar as capturas em coleções, agrupando páginas relacionadas de uma mesma sessão de arquivamento
- Reproduzir as páginas arquivadas offline, com o motor de reprodução [ReplayWeb.page](replaywebpage.md) integrado
- Exportar os arquivos nos formatos abertos WARC e WACZ, padrões usados por bibliotecas e arquivos de preservação web
- Enviar coleções capturadas diretamente para o Browsertrix, para arquivamento em maior escala

## Exemplo de uso

Uma pesquisadora está estudando um movimento social que se organiza principalmente em redes sociais e páginas que podem sair do ar a qualquer momento. Usando a extensão ArchiveWeb.page no navegador, ela visita e interage com as páginas relevantes — abrindo comentários, rolando feeds, reproduzindo vídeos — enquanto a ferramenta captura tudo com alta fidelidade. O resultado é um arquivo WACZ que ela pode reproduzir depois, mesmo se a página original não existir mais, preservando a experiência de navegação, não só uma captura de tela estática.

## Quando pode não ser a melhor opção

- Se você precisa arquivar sites em grande escala, de forma automatizada (milhares de páginas, sem interação manual): o Browsertrix é mais adequado para esse volume
- Se você só precisa salvar uma única página estática, sem interações: capturas mais simples, como o SingleFile ou o próprio "Salvar página" do navegador, podem bastar
- Se você quer garantir que uma página fique preservada publicamente por terceiros, sem depender do seu próprio arquivo: a Wayback Machine, do Internet Archive, é uma opção complementar (embora com menos controle sobre a fidelidade da captura)
- Se você não usa um navegador baseado em Chromium e não quer instalar a versão desktop: a extensão não funciona em navegadores como Firefox ou Safari

## Tipo de acesso

Totalmente gratuito e de código aberto (licença AGPL v3).

## Sistemas em que roda

Como extensão, em navegadores baseados em Chromium (Chrome, Brave, Edge). Como aplicativo desktop independente, em Windows, macOS (10.15 ou superior) e Linux.

## Integrações

- Browsertrix (envio direto de coleções capturadas, para arquivamento automatizado em maior escala)
- [ReplayWeb.page](replaywebpage.md) (motor de reprodução integrado, usado para visualizar as páginas arquivadas)

## Alternativas

- Wayback Machine (serviço público do Internet Archive, sem controle direto da pessoa pesquisadora sobre a captura)
- HTTrack (baixa sites inteiros para navegação offline, sem captura de interações dinâmicas)
- SingleFile (extensão simples para salvar uma única página como arquivo HTML)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://webrecorder.net/archivewebpage/](https://webrecorder.net/archivewebpage/)
- Guia de uso: [https://archiveweb.page/guide](https://archiveweb.page/guide)
- Repositório: [https://github.com/webrecorder/archiveweb.page](https://github.com/webrecorder/archiveweb.page)
- Fórum de ajuda: [https://forum.webrecorder.net/c/help/5](https://forum.webrecorder.net/c/help/5)

## Observações

Diferente de uma captura de tela ou de "salvar página" simples, o ArchiveWeb.page preserva a página como um objeto navegável e interativo, o que é especialmente valioso para pesquisa com fontes nascidas digitais (redes sociais, sites de notícias, páginas governamentais) que podem ser removidas ou alteradas a qualquer momento. Todos os dados capturados ficam armazenados localmente e são privados por padrão — só são compartilhados se a pessoa usuária decidir exportar ou publicar o arquivo.

