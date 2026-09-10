---
title: Transkribus
slug: transkribus
entry_type: ferramenta
tool_type: serviço web
category: transcrição
tags:
  - transcrição automática
  - transcrição manual
  - OCR
  - anotação de fontes
  - escrita acadêmica
aliases: []
source_model: não identificado
access_model: freemium
systems:
  - Web
  - Windows
  - macOS
  - Linux
curva_aprendizado: moderada
integrations:
  - TEI (Text Encoding Initiative)
  - ALTO XML
  - Microsoft Word
concepts:
  - reconhecimento-de-texto-manuscrito
  - reconhecimento-optico-de-caracteres
alternatives:
  - eScriptorium
  - Google Document AI
  - ABBYY FineReader
  - Kraken
official_site: https://www.transkribus.org
documentation: https://help.transkribus.org/
forum: https://help.transkribus.org/
caveats:
  - envia dados para serviço externo
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: '2026-08-18'
---

## O que é

Transkribus é uma plataforma para transcrição automática e manual de documentos históricos, especialmente manuscritos. Ela usa tecnologia [HTR](../conceitos/reconhecimento-de-texto-manuscrito.md) (Handwritten Text Recognition — reconhecimento de texto manuscrito) para converter imagens de documentos escritos à mão em texto editável. Foi desenvolvida originalmente na Universidade de Innsbruck (Áustria) como projeto de pesquisa europeu e hoje é mantida pela empresa READ-COOP.

## Para que serve

- Transcrever automaticamente documentos históricos manuscritos (cartas, registros paroquiais, atas, inventários, etc.)
- Treinar [modelos](../conceitos/modelo.md) personalizados de reconhecimento para uma caligrafia ou período específico
- Trabalhar colaborativamente na transcrição de coleções de documentos
- Organizar e anotar imagens de documentos de arquivo
- Exportar transcrições em formatos como texto simples, Word ou XML (para projetos de edição digital)

## Exemplo de uso

Uma pesquisadora está trabalhando com registros de óbitos manuscritos de um hospital do século XIX. Ela faz upload das imagens no Transkribus e aplica um modelo de HTR treinado para documentos em português do período. O sistema gera uma primeira versão da transcrição, que ela então revisa e corrige diretamente na interface. O resultado final, muito mais rápido do que a transcrição completamente manual, é exportado como texto para análise.

## Quando pode não ser a melhor opção

- Para documentos datilografados ou impressos: ferramentas de [OCR](../conceitos/reconhecimento-optico-de-caracteres.md) comuns (como o ABBYY FineReader ou até o Adobe Acrobat) são mais simples e eficientes
- Caligrafias muito deterioradas, apagadas ou com danos físicos significativos podem resultar em transcrições com muitos erros, exigindo revisão quase integral
- O modelo gratuito tem limite de páginas por mês (a partir de 2024, o modelo de créditos permite cerca de 500 páginas gratuitas por mês); grandes coleções podem gerar custos
- A curva de aprendizado é real: configurar projetos, fazer upload de imagens e entender o fluxo de trabalho da plataforma leva algum tempo

## Tipo de acesso

Freemium. O cadastro é gratuito e inclui um número de créditos mensais para transcrição automática. Créditos adicionais podem ser comprados. Pesquisadores e projetos acadêmicos podem solicitar acesso a planos com mais créditos. A plataforma web é a forma principal de acesso; há também um aplicativo desktop (Transkribus Expert Client) para uso avançado.

## Sistemas em que roda

A plataforma web funciona em qualquer navegador moderno. O aplicativo desktop (Transkribus Expert Client) está disponível para Windows, macOS e Linux.

## Integrações

- TEI (Text Encoding Initiative): exportação em formato padrão para edição digital de fontes primárias
- ALTO XML: formato para descrição estrutural de páginas digitalizadas
- Microsoft Word: exportação direta de transcrições

## Alternativas

- [eScriptorium](escriptorium.md) (código aberto, gratuito, pode ser instalado em servidor próprio, voltado para coleções de grande escala)
- Google Document AI (serviço pago, alta capacidade, requer configuração técnica)
- ABBYY FineReader (pago, excelente para OCR de textos impressos, limitado para manuscritos)
- Kraken (código aberto, linha de comando, para usuários com perfil técnico)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://www.transkribus.org](https://www.transkribus.org)
- Documentação: [https://help.transkribus.org/](https://help.transkribus.org/)
- Central de Ajuda: [https://help.transkribus.org/](https://help.transkribus.org/)

## Observações

Transkribus é a ferramenta de referência para pesquisadores que trabalham com documentos manuscritos históricos. Sua adoção cresce na historiografia europeia e começa a se expandir no Brasil, especialmente em projetos ligados a história colonial, eclesiástica e administrativa. A qualidade da transcrição automática depende muito da existência de um modelo treinado para a caligrafia específica — para períodos e regiões menos cobertos, pode ser necessário contribuir com o treinamento do modelo. Os dados são armazenados nos servidores da READ-COOP; para coleções muito sensíveis, o [eScriptorium](escriptorium.md) instalado localmente pode ser preferível.

