---
title: Whisper
slug: whisper
entry_type: ferramenta
tool_type: modelo
category: transcrição
tags:
  - transcrição automática
  - reconhecimento de fala
  - uso offline
  - linha de comando
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
curva_aprendizado: alta
integrations:
  - Python
  - ffmpeg
concepts:
  - reconhecimento-automatico-de-fala
alternatives:
  - oTranscribe
  - AssemblyAI
  - Otter.ai
  - Whisper.cpp
official_site: https://openai.com/research/whisper
documentation: https://github.com/openai/whisper
forum: https://github.com/openai/whisper/discussions
repository: https://github.com/openai/whisper
caveats:
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: '2026-08-18'
---

## O que é

Whisper é um [modelo](../conceitos/modelo.md) de [reconhecimento de fala](../conceitos/reconhecimento-automatico-de-fala.md) desenvolvido pela OpenAI e disponibilizado gratuitamente como código aberto. Ele transcreve automaticamente áudio e vídeo para texto em mais de 90 idiomas, incluindo o português brasileiro, com alta precisão. Ao contrário de serviços como o Google Docs por voz, o Whisper pode ser instalado no próprio computador e funcionar completamente sem conexão à internet.

## Para que serve

- Transcrever gravações de entrevistas, depoimentos orais e registros sonoros
- Converter gravações de áudio ou vídeo em texto editável
- Transcrever materiais em português, inglês e dezenas de outros idiomas
- Processar arquivos de áudio em lote (vários arquivos de uma vez)
- Funcionar sem enviar dados a servidores externos, preservando a privacidade das fontes

## Exemplo de uso

Um pesquisador realizou 30 entrevistas de história oral com trabalhadores da saúde pública. As entrevistas foram gravadas em MP3. Usando o Whisper instalado no próprio computador, ele transcreve automaticamente todos os arquivos em texto, que depois revisa manualmente. O processo leva horas em vez de semanas, e nenhum áudio é enviado a terceiros.

## Quando pode não ser a melhor opção

- Se você não tem familiaridade com terminal ou linha de comando: a instalação e o uso do Whisper exigem executar comandos de texto, o que pode ser intimidador sem experiência prévia. Existem interfaces gráficas de terceiros (como o [Whisper Transcription](macwhisper.md) para macOS ou o Const-me/Whisper para Windows) que facilitam o uso
- Se o áudio for de falantes não nativos de inglês: Graham e Roll (2024) mediram a taxa de erro do modelo em inglês falado por pessoas de origens linguísticas variadas e registraram desempenho pior nesse grupo. Sobreposição de vozes, ruído de fundo intenso e sotaques muito regionais também derrubam a precisão. Em projetos com entrevistas multilíngues, conte com mais tempo de revisão
- Se você precisar de uma solução imediata e simples sem instalação: serviços web como AssemblyAI ou Otter.ai são mais acessíveis, mas enviam os dados a servidores externos
- O processamento pode ser lento em computadores antigos sem placa de vídeo dedicada

## Tipo de acesso

Gratuito e de código aberto (licença MIT). Não há custo algum para uso. Requer instalação via Python (linguagem de programação) e um gerenciador de pacotes. Existem também versões otimizadas para uso local, como o `whisper.cpp`, que roda em computadores com hardware mais modesto.

## Sistemas em que roda

Windows, macOS e Linux. Requer Python 3.8 ou superior instalado no computador. O processamento pode ser acelerado com placa de vídeo NVIDIA (GPU), mas funciona também apenas com o processador principal (CPU).

## Integrações

- Python (linguagem necessária para rodar o Whisper padrão)
- ffmpeg (programa de linha de comando para processamento de áudio e vídeo, necessário para alguns formatos)
- Interfaces gráficas de terceiros disponíveis para Windows e macOS

## Alternativas

- oTranscribe (transcrição manual assistida, gratuito, funciona no navegador)
- AssemblyAI (transcrição automática via API, pago, sem necessidade de instalação)
- Otter.ai (transcrição automática, freemium, foco em inglês)
- whisper.cpp (versão do Whisper otimizada para rodar localmente com menor consumo de recursos)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://openai.com/research/whisper](https://openai.com/research/whisper)
- Documentação e código-fonte: [https://github.com/openai/whisper](https://github.com/openai/whisper)
- Discussões da comunidade: [https://github.com/openai/whisper/discussions](https://github.com/openai/whisper/discussions)

### Material de apoio

O Whisper é um modelo, e o material que ensina a usá-lo vem em boa parte de fora da OpenAI.
O guia da UFPel é o ponto de entrada mais direto para quem lê em português: foi produzido por
um grupo de pesquisa brasileiro e percorre a tarefa inteira, da instalação à transcrição de
um arquivo. A documentação oficial cobre o mesmo percurso em inglês, com o comando de
transcrição e os modelos disponíveis.

- Guia "OpenAI Whisper: transcrição automática para pesquisa", do Grupo de Pesquisa Ideologia
  e Análise de Discurso da UFPel, 2025, em português, com PDF anexo:
  [https://wp.ufpel.edu.br/idad/openai-whisper-transcricao-automatica-para-pesquisa/](https://wp.ufpel.edu.br/idad/openai-whisper-transcricao-automatica-para-pesquisa/)
- README do repositório oficial, com instalação e comando de transcrição:
  [https://github.com/openai/whisper](https://github.com/openai/whisper)

## Uso em pesquisa e ensino

O Whisper aparece na literatura acadêmica como objeto de avaliação e como ferramenta de
trabalho em acervos. Graham e Roll mediram seu desempenho em falantes de inglês com sotaques
diversos e traços variados de fala. As bibliotecas da Emory testaram o modelo sobre uma
amostra de 250 horas de material audiovisual, com financiamento do Lyrasis Catalyst Fund,
avaliando o desempenho por tipo de conteúdo, vocabulário técnico, variedade regional e
qualidade de gravação.

- GRAHAM, Calbert; ROLL, Nathan. Evaluating OpenAI's Whisper ASR: performance analysis across
  diverse accents and speaker traits. *JASA Express Letters*, 2024:
  [https://doi.org/10.1121/10.0024876](https://doi.org/10.1121/10.0024876)
- Emory University Libraries, testagem do Whisper em acervo audiovisual digitalizado:
  [https://guides.libraries.emory.edu/whisper](https://guides.libraries.emory.edu/whisper)

## Observações

Whisper foi lançado pela OpenAI em 2022 e rapidamente se tornou referência em transcrição automática de código aberto. O fato de rodar localmente é especialmente relevante para pesquisas que envolvem fontes sensíveis, como entrevistas com sujeitos vulneráveis ou documentos sigilosos: nenhum dado é enviado a servidores de terceiros. Para quem não tem conforto com linha de comando, recomenda-se buscar interfaces gráficas de terceiros ou pedir apoio técnico para a instalação inicial.

