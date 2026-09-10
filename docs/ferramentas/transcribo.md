---
title: Transcribo
slug: transcribo
entry_type: ferramenta
tool_type: aplicativo
category: transcrição
tags:
  - transcrição manual
  - anotação de fontes
  - uso offline
  - open source
  - gratuito para pesquisa
aliases: []
source_model: aberto
access_model: gratuito
systems:
  - Windows
  - macOS
curva_aprendizado: moderada a alta
integrations:
  - TEI
  - FuD
concepts: []
alternatives:
  - Transkribus
  - OTE
  - FromThePage
  - Scripto
official_site: https://tcdh.uni-trier.de/en/projekt/transcribo
documentation: https://tcdh.uni-trier.de/en/projekt/transcribo
forum: não disponível
repository: https://bitbucket.org/tcdh/transcribodownload
caveats:
  - licença não identificada
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: '2026-08-18'
---

## O que é

Transcribo é um programa para transcrição e anotação de manuscritos e datilografias históricas diretamente sobre imagens digitalizadas. Desenvolvido pelo Trier Center for Digital Humanities (TCDH) da Universidade de Trier (Alemanha), em parceria com a Universidade de Cambridge, ele foi criado originalmente para o projeto de edição crítica digital das obras de Arthur Schnitzler. O programa funciona como um editor de texto gráfico: o pesquisador vê a imagem do documento de um lado e transcreve e anota o texto do outro, podendo indicar com precisão onde cada trecho aparece no original. É um aplicativo Java instalado no computador, que pode funcionar sozinho (localmente) ou integrado a um sistema de banco de dados colaborativo.

## Para que serve

- Transcrever manuscritos e documentos datilografados sobre imagens digitalizadas
- Anotar variantes textuais, rasuras, inserções e outras características do documento
- Registrar informações texto-genéticas: as diferentes camadas de um texto, as correções e revisões do autor
- Trabalhar colaborativamente em equipes de pesquisa quando integrado ao sistema FuD
- Exportar as transcrições no formato TEI (Text Encoding Initiative), padrão para edições digitais
- Suporta todos os formatos de imagem comuns (BMP, GIF, JPEG, PNG, TIFF)

## Exemplo de uso

Um pesquisador trabalha com as cartas manuscritas de um médico brasileiro do século XIX, digitalizadas em alta resolução. Ele instala o Transcribo no seu computador, importa as imagens e começa a transcrever: na tela, a imagem da carta aparece à esquerda; à direita, ele digita o texto enquanto marca visualmente cada linha e cada trecho problemático. As rasuras e acréscimos do autor são anotados com etiquetas específicas. Ao final, exporta a transcrição em TEI para continuar o trabalho de edição.

## Quando pode não ser a melhor opção

- O Transcribo não tem transcrição automática: todo o trabalho de leitura e digitação é feito manualmente pelo pesquisador. Para documentos em grande volume, ferramentas com HTR automático (como [Transkribus](transkribus.md)) são muito mais eficientes
- A instalação requer Java no computador e alguma familiaridade com a configuração de aplicativos de desktop — não é um processo de instalação simples como a maioria dos programas atuais
- A interface e a documentação são predominantemente em alemão e inglês, sem materiais em português
- O modelo de anotação texto-genética pressupõe familiaridade com os conceitos da crítica genética; para transcrição simples sem esse nível de detalhe, a complexidade pode ser desnecessária
- Para trabalho colaborativo, a integração com o FuD (sistema de banco de dados da Universidade de Trier) requer configuração técnica adicional

## Tipo de acesso

Gratuito. O código-fonte está disponível publicamente no Bitbucket, mas a licença específica não está documentada de forma explícita. Não há custo de uso. A instalação requer Java instalado no sistema.

## Sistemas em que roda

Windows (XP ou superior) e macOS (10.5.2 ou superior). Não há versão para Linux nem interface web.

## Integrações

- TEI (Text Encoding Initiative): formato de exportação padrão para edições digitais acadêmicas
- FuD (Forschungsnetzwerk und Datenbanksystem): sistema de banco de dados colaborativo da Universidade de Trier, que permite trabalho em equipe sobre o mesmo corpus

## Alternativas

- Transkribus (web, HTR automático, mais acessível, mais amplamente usado)
- OTE — Online Transcription Editor (web, também desenvolvido pela TCDH Trier, mais simples)
- FromThePage (web, especialmente bom para transcrição colaborativa com voluntários)
- Scripto (plugin para WordPress/Omeka, para transcrição colaborativa)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://tcdh.uni-trier.de/en/projekt/transcribo](https://tcdh.uni-trier.de/en/projekt/transcribo)
- Código-fonte: [https://bitbucket.org/tcdh/transcribodownload](https://bitbucket.org/tcdh/transcribodownload)

## Observações

O Transcribo foi desenvolvido para atender às exigências muito específicas da edição crítica literária — um nível de detalhe na anotação de manuscritos que vai além do que a maioria dos projetos de história necessita. É uma ferramenta acadêmica robusta, desenvolvida e mantida por um centro de humanidades digitais de renome, com desenvolvimento previsto até 2029. Para pesquisadores de história que precisam de transcrição com anotação detalhada de variantes — por exemplo, ao trabalhar com documentos de autor ou com manuscritos com revisões extensas —, o Transcribo oferece um nível de precisão difícil de encontrar em outras ferramentas gratuitas.

