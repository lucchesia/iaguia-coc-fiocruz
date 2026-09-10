---
title: JabRef
slug: jabref
entry_type: ferramenta
tool_type: aplicativo
category: gestão de referências
tags:
  - gestão de referências
  - escrita acadêmica
  - integração com Word
  - integração com LibreOffice
  - open source
  - gratuito para pesquisa
aliases: []
source_model: aberto
software_license: MIT
access_model: gratuito
systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: moderada
integrations:
  - Microsoft Word
  - LibreOffice Writer
concepts:
  - modelo-de-linguagem
alternatives:
  - Zotero
  - Mendeley
  - EndNote
  - Paperpile
official_site: https://www.jabref.org
documentation: https://docs.jabref.org
forum: https://discourse.jabref.org
repository: https://github.com/JabRef/jabref
caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: '2026-08-19'
---

## O que é

JabRef é um programa gratuito e de código aberto para gerenciar bibliotecas de referências bibliográficas no formato BibTeX/BibLaTeX (.bib). Mantido por uma comunidade de voluntários — doutorandos, pós-doutorandos e outros pesquisadores — desde 2003, é voltado especialmente para quem escreve em LaTeX, mas também oferece recursos para inserir citações em Word e LibreOffice.

## Para que serve

- Organizar referências em bibliotecas no formato .bib, um arquivo de texto simples, legível e independente de qualquer programa específico
- Buscar e importar referências diretamente de bases como CrossRef, Google Scholar, PubMed, arXiv e outras, dentro do próprio programa
- Importar referências do navegador com a extensão oficial (Firefox, Chrome, Edge, Vivaldi)
- Agrupar referências em coleções hierárquicas e organizar por palavras-chave
- Inserir e formatar citações em documentos do Word e do LibreOffice/OpenOffice
- Sincronizar bibliotecas compartilhadas por meio de um banco de dados SQL
- Opcionalmente, usar recursos de IA para resumir artigos e conversar com o conteúdo de PDFs vinculados (requer configurar um provedor de IA externo ou rodar um [modelo](../conceitos/modelo.md) local)

## Exemplo de uso

Um doutorando está escrevendo a tese em LaTeX e precisa manter a bibliografia sincronizada com o documento. Ele usa o JabRef para organizar todas as referências em um arquivo `.bib`, que é referenciado diretamente no código-fonte do LaTeX (com o comando `\cite{}`). Ao adicionar uma nova referência, ele só precisa salvar o arquivo `.bib` — a bibliografia é atualizada automaticamente na compilação do documento.

## Quando pode não ser a melhor opção

- Se você não usa LaTeX e busca uma ferramenta mais simples e visual: o JabRef é organizado em torno do formato BibTeX, o que pode ser menos intuitivo para quem só escreve no Word ou no Google Docs
- Se você precisa de armazenamento e anotação de PDFs na nuvem, integrados à biblioteca: diferente de Zotero e Mendeley, o JabRef não oferece isso nativamente — os PDFs ficam vinculados por caminho de arquivo local
- Se você quer usar os recursos de IA (resumo, chat com PDFs): eles exigem configurar uma chave de API de um provedor externo pago (OpenAI, Mistral) ou rodar um [modelo de linguagem](../conceitos/modelo-de-linguagem.md) local — não há um serviço de IA gratuito embutido no próprio JabRef
- Não há integração oficial com Google Docs

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MIT). Não há planos pagos, limites de armazenamento ou funcionalidades bloqueadas — inclusive os recursos de IA, quando usados com um provedor externo, geram custo separado (da API), não do JabRef em si.

## Sistemas em que roda

Windows, macOS e Linux — é uma aplicação multiplataforma.

## Integrações

- Microsoft Word (inserção e formatação de citações)
- LibreOffice Writer / Apache OpenOffice (inserção e formatação de citações)
- Editores de LaTeX, por meio do formato nativo .bib (compatível, por exemplo, com Overleaf)
- Extensão de navegador para importar referências (Firefox, Chrome, Edge, Vivaldi)

## Alternativas

- [Zotero](zotero.md) (código aberto, mais voltado a Word/Google Docs do que a LaTeX)
- [Mendeley](mendeley.md) (freemium, mantido pela Elsevier)
- [EndNote](endnote.md) (pago, licença institucional comum em universidades)
- [Paperpile](paperpile.md) (pago por assinatura, integrado ao Google Docs)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.jabref.org](https://www.jabref.org)
- Documentação: [https://docs.jabref.org](https://docs.jabref.org)
- Fórum da comunidade: [https://discourse.jabref.org](https://discourse.jabref.org)

## Observações

O JabRef é mantido de forma independente por uma comunidade acadêmica voluntária desde 2003 — não pertence a nenhuma editora comercial, diferente do Mendeley (Elsevier) e do EndNote (Clarivate). Por ser baseado no formato de texto simples .bib, é a opção mais indicada do glossário para quem escreve em LaTeX. Os recursos de IA são recentes (desde a versão 6) e opcionais: funcionam com provedores externos (mediante chave de API própria, com custo variável do provedor) ou com um modelo de linguagem rodando localmente no computador.

