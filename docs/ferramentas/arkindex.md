---
title: Arkindex
slug: arkindex
entry_type: ferramenta
tool_type: serviço web
category: transcrição
tags:
  - transcrição automática
  - OCR
  - open source
  - colaboração em equipe
aliases: []
source_model: aberto
software_license: AGPL-3.0
access_model: freemium
systems:
  - Web
  - Linux
curva_aprendizado: alta
integrations:
  - IIIF
  - API REST
  - Python
concepts: []
alternatives:
  - Transkribus
  - eScriptorium
  - Google Document AI
  - ABBYY FineReader
official_site: https://arkindex.teklia.com
documentation: https://doc.arkindex.org
forum: não disponível
caveats:
  - requer infraestrutura própria
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: '2026-08-18'
---

## O que é

Arkindex é uma plataforma para processamento e análise automatizada de documentos digitalizados, desenvolvida pela empresa francesa Teklia. Combina tecnologias de OCR (reconhecimento óptico de caracteres para textos impressos), HTR (reconhecimento de texto manuscrito) e análise de layout para extrair e organizar informações de grandes coleções documentais. Desde 2024, a versão comunitária é distribuída como código aberto. É usada principalmente por bibliotecas, arquivos e projetos acadêmicos de grande escala que precisam processar milhares de documentos de forma sistemática.

## Para que serve

- Processar automaticamente grandes volumes de documentos digitalizados (manuscritos, impressos, registros históricos)
- Aplicar [modelos](../conceitos/modelo.md) de HTR e OCR a coleções inteiras de imagens
- Organizar e gerenciar metadados de documentos em projetos colaborativos
- Integrar diferentes modelos de [inteligência artificial](../conceitos/inteligencia-artificial.md) em fluxos de trabalho de digitalização
- Exportar transcrições e dados estruturados para outros sistemas

## Exemplo de uso

Um projeto institucional de digitalização de registros paroquiais do século XVIII tem 80 mil páginas digitalizadas armazenadas em um servidor. A equipe técnica implanta o Arkindex em um servidor Linux e configura um pipeline automatizado: as imagens são enviadas ao sistema, um modelo de HTR treinado para a caligrafia do período processa os documentos e gera as transcrições. Os pesquisadores revisam e corrigem os resultados pela interface web. O projeto inteiro pode ser gerenciado por uma equipe distribuída.

## Quando pode não ser a melhor opção

- Para pesquisadores individuais sem suporte de equipe técnica: a instalação da versão comunitária exige um servidor Linux com Docker, conhecimento de administração de sistemas e configuração de infraestrutura — tarefas que estão bem além do perfil de um pesquisador sem formação técnica
- Se você precisa transcrever sua própria coleção de documentos sem montar infraestrutura: o [Transkribus](transkribus.md) ou o [eScriptorium](escriptorium.md) são muito mais acessíveis para uso individual
- A versão hospedada pela Teklia (sem necessidade de servidor próprio) requer contato comercial para projetos acadêmicos — não há uma plataforma web pública de acesso imediato como o Transkribus
- Para documentos em português, pode ser necessário treinar ou adaptar modelos, já que a maioria dos modelos disponíveis foi treinada para idiomas europeus ocidentais

## Tipo de acesso

Freemium. A edição comunitária é gratuita e de código aberto (licença AGPLv3), mas requer instalação em servidor próprio. A edição acadêmica tem licença com desconto para universidades e limita o uso a 250 mil imagens. A edição empresarial é comercial. Todas as edições permitem número ilimitado de usuários.

## Sistemas em que roda

A interface do usuário é acessada pelo navegador web (qualquer sistema operacional). A implantação do sistema requer um servidor com Linux (Ubuntu LTS recomendado) e Docker. Não há aplicativo desktop. Há suporte para implantação em serviços de nuvem (AWS, Google Cloud, Azure).

## Integrações

- IIIF (International Image Interoperability Framework): padrão para compartilhamento de imagens de acervos digitais
- API REST: permite integração programática com outros sistemas
- Python: SDK disponível para automação e integração

## Alternativas

- Transkribus (serviço web, mais acessível para usuários individuais, freemium)
- [eScriptorium](escriptorium.md) (código aberto, pode ser instalado localmente, mais focado em HTR)
- Google Document AI (serviço pago por uso, alta capacidade, requer configuração técnica)
- ABBYY FineReader (proprietário, pago, excelente para OCR de textos impressos)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://arkindex.teklia.com](https://arkindex.teklia.com)
- Documentação técnica: [https://doc.arkindex.org](https://doc.arkindex.org)
- Site da empresa: [https://teklia.com](https://teklia.com)

## Observações

O Arkindex é uma ferramenta de nível institucional, projetada para projetos de grande escala com suporte técnico dedicado. Seu diferencial em relação ao Transkribus é a flexibilidade para integrar diferentes modelos de IA e a possibilidade de instalação em infraestrutura própria — relevante para instituições que têm políticas de privacidade de dados mais restritivas. Para pesquisadores individuais ou grupos pequenos sem equipe técnica, o Transkribus ou o [eScriptorium](escriptorium.md) são alternativas mais práticas para o mesmo tipo de tarefa.

