---
title: "oTranscribe"
slug: "otranscribe"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "transcrição"

tags:
  - transcrição manual
  - história oral
  - open source
  - uso offline
aliases: []

source_model: aberto
software_license: MIT
access_model: gratuito

systems:
  - Web
curva_aprendizado: "baixa"
integrations:
  - Google Drive

concepts: []
alternatives:
  - SayMore
  - Lameta
  - Whisper

official_site: "https://otranscribe.com/"
documentation: "https://otranscribe.com/classic/help/"
forum: "não disponível"
repository: "https://github.com/oTranscribe/oTranscribe"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

oTranscribe é uma ferramenta gratuita e de código aberto para transcrição manual de áudio e vídeo, direto no navegador. Foi criada pelo jornalista Elliot Bentley e, desde 2018, é mantida pela MuckRock Foundation, organização sem fins lucrativos voltada a jornalismo investigativo. Diferente de ferramentas de reconhecimento automático de fala, o oTranscribe não gera texto sozinho — ele só facilita o trabalho de quem está transcrevendo manualmente.

## Para que serve

- Reproduzir um arquivo de áudio ou vídeo (carregado do computador ou por URL, incluindo vídeos do YouTube) enquanto a pessoa digita a transcrição ao lado, na mesma tela
- Controlar a reprodução (pausar, retroceder, avançar, mudar a velocidade) por atalhos de teclado, sem precisar tirar as mãos do teclado
- Inserir marcações de tempo (timestamps) clicáveis no texto, que levam de volta ao ponto exato do áudio
- Formatar o texto com negrito e itálico durante a digitação
- Exportar a transcrição em texto simples (.txt), Markdown (.md) ou no formato próprio .otr (que preserva os timestamps)

## Exemplo de uso

Um pesquisador está transcrevendo uma entrevista de história oral gravada em áudio. Ele carrega o arquivo no oTranscribe, digita a transcrição enquanto ouve, usando os atalhos de teclado para pausar e retroceder sem tirar as mãos do teclado, e insere marcações de tempo em trechos que quer citar depois. Como tudo roda no navegador e o áudio nunca é enviado a um servidor, ele pode fazer esse trabalho mesmo com dados sensíveis de participantes da pesquisa, sem preocupação de privacidade.

## Quando pode não ser a melhor opção

- Se você precisa de transcrição automática gerada por IA: o oTranscribe não faz reconhecimento de fala — é puramente uma ferramenta de apoio à transcrição manual
- Se você precisa gerenciar sessões de gravação, metadados de participantes ou consentimento informado de um projeto de campo maior: SayMore ou Lameta são mais adequados
- Se você precisa fazer anotação temporal detalhada em múltiplas camadas (tiers): o ELAN é mais indicado
- A exportação direta para o Google Drive já foi relatada como instável por usuários; o mais seguro é exportar em .txt/.md e fazer upload manual se for preciso guardar em nuvem

## Tipo de acesso

Totalmente gratuito e de código aberto (licença MIT).

## Sistemas em que roda

Funciona em qualquer navegador moderno (Chrome, Firefox, Edge), sem instalação. Depois do primeiro carregamento, continua funcionando offline (exceto o recurso de carregar vídeos do YouTube, que precisa de internet).

## Integrações

Exportação para o Google Drive (recurso oficial, mas com relatos de instabilidade). Fora isso, não se integra a outras ferramentas — os dados ficam salvos localmente no navegador (localStorage).

## Alternativas

- [SayMore](saymore.md) (organização de sessões e metadados de campo, além de transcrição básica)
- [Lameta](lameta.md) (organização de metadados de projeto, sem ferramentas de transcrição)
- [Whisper](whisper.md) (transcrição automática por IA, em vez de manual)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://otranscribe.com/](https://otranscribe.com/)
- Documentação: [https://otranscribe.com/classic/help/](https://otranscribe.com/classic/help/)
- Repositório: [https://github.com/oTranscribe/oTranscribe](https://github.com/oTranscribe/oTranscribe)

## Observações

O oTranscribe é bastante usado em jornalismo investigativo (por isso é mantido pela MuckRock Foundation) e também é recomendado em guias de história oral acadêmica, justamente pela simplicidade e por manter o áudio inteiramente no dispositivo da pessoa que transcreve, sem upload — um ponto relevante para pesquisa com dados sensíveis ou sigilo de fonte.

