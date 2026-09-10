---
title: Gamera
slug: gamera
entry_type: ferramenta
tool_type: biblioteca
category: transcrição
tags:
  - OCR
  - linha de comando
  - open source
  - uso offline
  - gratuito para pesquisa
aliases: []
source_model: aberto
software_license: GPL-2.0
access_model: gratuito
systems:
  - macOS
  - Linux
curva_aprendizado: alta
integrations:
  - Python
  - NumPy
  - wxPython
concepts: []
alternatives:
  - Kraken
  - Calamari
  - Tesseract
  - eScriptorium
official_site: https://gamera.informatik.hsnr.de
documentation: https://gamera.informatik.hsnr.de/docs/gamera-docs/
forum: https://github.com/hsnr-gamera/gamera-4/issues
repository: https://github.com/hsnr-gamera/gamera-4
caveats:
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: estável
status: publicado
reviewed: true
last_reviewed: '2026-08-18'
---

## O que é

Gamera é uma biblioteca de código aberto para análise de imagens de documentos e reconhecimento óptico de caracteres (OCR), escrita em Python com extensões em C++. Ao contrário de ferramentas prontas para uso, o Gamera é um arcabouço — um conjunto de blocos de construção que pesquisadores com perfil técnico usam para criar seus próprios sistemas de reconhecimento de documentos históricos. Foi desenvolvido originalmente no Peabody Institute da Johns Hopkins University e é mantido atualmente pela Hochschule Niederrhein (Alemanha).

## Para que serve

- Construir sistemas personalizados de OCR para tipos específicos de documentos históricos
- Analisar e segmentar imagens de documentos (separar linhas, palavras, caracteres)
- Extrair características visuais de símbolos gráficos para classificação automática
- Desenvolver pipelines de reconhecimento para notação musical antiga, escrita medieval e outros tipos de documentos com características visuais específicas
- Processar lotes de imagens de forma programática, sem interface gráfica

## Exemplo de uso

Uma equipe de pesquisa quer automatizar o reconhecimento de notação musical em manuscritos medievais digitalizados — tarefa que ferramentas de OCR comuns não conseguem realizar. Uma pesquisadora com formação em programação usa o Gamera para construir um classificador treinado com exemplos do corpus específico. O resultado é um sistema personalizado capaz de identificar e transcrever automaticamente aquele tipo particular de notação.

## Quando pode não ser a melhor opção

- Para a grande maioria dos pesquisadores de história sem experiência em programação, o Gamera não é uma opção prática: ele não tem interface gráfica para as funções principais e requer escrever código em Python para qualquer tarefa
- Não é um programa para instalar e usar imediatamente: exige configuração de ambiente Python, instalação de dependências e familiaridade com linha de comando
- Para Windows, não há suporte oficial
- Se você precisa de uma ferramenta pronta para transcrever documentos manuscritos, ferramentas como [Transkribus](transkribus.md) ou [eScriptorium](escriptorium.md) são muito mais acessíveis
- O Gamera é mais adequado para projetos de pesquisa em humanidades digitais que contam com colaboração de cientistas da computação

## Tipo de acesso

Gratuito e de código aberto (licença GNU GPL v2 ou posterior). A documentação tem licença Creative Commons. Não há custo de uso, mas a instalação requer conhecimento técnico (Python 3.7 ou superior, compilador C++).

## Sistemas em que roda

macOS e Linux. Não há suporte oficial para Windows. Requer Python entre 3.5 e 3.11 instalado no sistema (Python 3.12 ou superior não é compatível devido a uma mudança na linguagem).

## Integrações

- Python (linguagem necessária para usar a biblioteca)
- NumPy (biblioteca Python para computação numérica, necessária)
- wxPython (biblioteca para interface gráfica — usada em algumas ferramentas construídas sobre o Gamera)

## Alternativas

- Kraken (código aberto, linha de comando, focado em HTR e OCR para textos históricos)
- Calamari (código aberto, Python, mais simples de usar para OCR)
- [Tesseract](tesseract.md) (código aberto, motor de OCR da Google, mais fácil de instalar e usar)
- [eScriptorium](escriptorium.md) (código aberto, interface web, muito mais acessível para não-programadores)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://gamera.informatik.hsnr.de](https://gamera.informatik.hsnr.de)
- Documentação: [https://gamera.informatik.hsnr.de/docs/gamera-docs/](https://gamera.informatik.hsnr.de/docs/gamera-docs/)
- Repositório de código: [https://github.com/hsnr-gamera/gamera-4](https://github.com/hsnr-gamera/gamera-4)

## Observações

O Gamera é uma ferramenta para especialistas, não para usuários gerais. Seu ponto forte é a flexibilidade: permite construir sistemas de reconhecimento altamente customizados para tipos de documentos que ferramentas genéricas não conseguem lidar bem. Para projetos de humanidades digitais que envolvam documentos com características visuais muito específicas — notação musical, escrita em línguas antigas, simbologias especiais — o Gamera pode ser a escolha técnica mais adequada, desde que haja colaboração com profissionais de computação. A versão atual (Gamera 4) é mantida ativamente e suporta Python 3.

