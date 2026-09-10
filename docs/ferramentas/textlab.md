---
title: TextLab
slug: textlab
entry_type: ferramenta
tool_type: serviço web
category: anotação e marcação
tags:
  - anotação de fontes
  - transcrição manual
  - escrita acadêmica
  - open source
aliases: []
source_model: aberto
software_license: GPL-3.0
access_model: gratuito
systems:
  - Web
curva_aprendizado: moderada a alta
integrations:
  - TEI
concepts: []
alternatives:
  - Juxta
  - CollateX
  - CATMA
  - Transkribus
official_site: https://melville.electroniclibrary.org/textlab
documentation: https://melville.electroniclibrary.org/pdf/textlab_user_manual.pdf
forum: não disponível
repository: https://github.com/performant-software/textlab
caveats:
  - requer infraestrutura própria
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: legada
status: publicado
reviewed: true
last_reviewed: '2026-08-18'
---

## O que é

TextLab é uma ferramenta web para transcrição e anotação de manuscritos literários segundo os princípios da *crítica genética* — uma abordagem que estuda a evolução de um texto ao longo de suas diferentes versões (rascunhos, revisões, versões publicadas). Desenvolvida na Hofstra University pela equipe do projeto Herman Melville Electronic Library, com apoio da empresa Performant Software, ela permite que pesquisadores transcrevam imagens de manuscritos e marquem as camadas de revisão de um texto: o que foi acrescentado, riscado, substituído, em qual ordem. O código-fonte é aberto (licença GPL-3.0).

## Para que serve

- Transcrever manuscritos literários ou acadêmicos diretamente sobre imagens digitalizadas
- Registrar e marcar as camadas de revisão de um texto: inserções, supressões, substituições
- Comparar versões de um mesmo texto e visualizar sua evolução (crítica genética)
- Criar edições digitais que mostram o processo de escrita de uma obra
- Exportar transcrições codificadas no padrão TEI (Text Encoding Initiative)

## Exemplo de uso

Um pesquisador estuda os manuscritos de um intelectual brasileiro do início do século XX cujos cadernos de trabalho foram digitalizados. Usando o TextLab, ele transcreve as páginas e marca cada camada de revisão: o que estava escrito inicialmente, o que foi riscado, o que foi inserido nas margens. O resultado é uma edição digital que permite a qualquer leitor ver não apenas o texto final, mas todo o processo de escrita e reescrita.

## Quando pode não ser a melhor opção

- Para transcrição simples de documentos históricos sem interesse nas camadas de revisão (como registros cartoriais, atas ou correspondências), ferramentas como [Transkribus](transkribus.md) ou [Transcribo](transcribo.md) são mais diretas e práticas
- O TextLab não tem transcrição automática (HTR/OCR) — toda a transcrição é feita manualmente pelo pesquisador
- A última versão oficial foi lançada em 2018; o projeto está em modo de manutenção, sem atualizações regulares — isso pode representar risco de instabilidade ou incompatibilidade futura com navegadores e servidores mais novos
- Instalar e rodar sua própria instância do TextLab requer conhecimento técnico de servidores web (Ruby on Rails, banco de dados PostgreSQL); sem suporte técnico, não é viável para usuários sem formação em TI
- A ferramenta foi construída para a tradição da crítica genética literária e pode ser conceitualmente estranha para pesquisadores não familiarizados com esse campo

## Tipo de acesso

Gratuito e de código aberto (GPL-3.0). É possível usar a instância hospedada pelo projeto Melville Electronic Library diretamente, sem instalação. Para projetos independentes, é necessário instalar e configurar o sistema em um servidor próprio.

## Sistemas em que roda

Interface web acessada pelo navegador (qualquer sistema operacional). Não há aplicativo desktop.

## Integrações

- TEI (Text Encoding Initiative): exportação de transcrições no formato padrão para edições digitais de fontes primárias

## Alternativas

- Juxta (comparação e colação de versões de textos, interface mais simples)
- CollateX (código aberto, colação automática de variantes textuais, linha de comando)
- CATMA (código aberto, anotação de textos com interface web, mais ativo)
- Transkribus (transcrição automática com HTR, mais acessível para não-especialistas)

## Aprenda a usar

### Onde encontrar

- Site oficial e acesso: [https://melville.electroniclibrary.org/textlab](https://melville.electroniclibrary.org/textlab)
- Manual do usuário: [https://melville.electroniclibrary.org/pdf/textlab_user_manual.pdf](https://melville.electroniclibrary.org/pdf/textlab_user_manual.pdf)
- Repositório de código: [https://github.com/performant-software/textlab](https://github.com/performant-software/textlab)

## Observações

O TextLab é uma ferramenta especializada para um campo específico da crítica textual. Sua utilidade é alta para pesquisadores que trabalham com gênese de textos literários ou acadêmicos — especialmente em projetos de edição crítica digital. Para historiadores cujo foco está em outros tipos de documentos, a relevância pode ser menor. O fato de estar em modo de manutenção desde 2018 é um ponto de atenção: a ferramenta continua funcionando para os fins para os quais foi construída, mas novos recursos não estão sendo desenvolvidos.

