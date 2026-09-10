---
title: "Mistral Vibe"
slug: "mistral-vibe"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "inteligência artificial generativa"

tags:
  - inteligência artificial generativa
aliases:
  - "Le Chat"
  - "Le Chat Mistral"

source_model: proprietário
software_license: proprietária
access_model: freemium

systems:
  - Web
  - iOS
  - Android
curva_aprendizado: "baixa a moderada"
integrations:
  - Google Drive
  - Slack
  - GitHub

concepts:
  - ia-generativa
alternatives:
  - ChatGPT
  - Claude
  - Gemini

official_site: "https://chat.mistral.ai/"
documentation: "https://docs.mistral.ai/vibe/overview"
forum: "não disponível"

caveats: []
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Mistral Vibe é o assistente de [IA generativa](../conceitos/ia-generativa.md) da Mistral AI, empresa francesa com forte ênfase em soberania de dados europeia. Até maio de 2026, o produto se chamava **Le Chat** — a Mistral renomeou-o para Vibe ao ampliar seu escopo de um chatbot de conversação para um "agente de trabalho" mais completo, com modos dedicados a tarefas de escritório e programação. A URL de acesso e as contas de usuários existentes permaneceram as mesmas após a mudança de nome.

## Para que serve

- Conversar em linguagem natural para escrever, revisar, resumir ou explicar textos e conceitos
- Executar código Python diretamente na conversa, com bibliotecas de análise de dados já instaladas (pandas, NumPy, matplotlib), útil para explorar planilhas e arquivos CSV
- Conectar-se a ferramentas externas (Google Drive, Slack, Notion, GitHub, SharePoint, entre outras) para buscar e usar informações de fora da conversa
- Realizar tarefas mais longas de forma semiautônoma, em dois modos: "Work Mode" (fluxos de trabalho de escritório) e "Code Mode" (tarefas de programação, incluindo criação de pull requests)

## Exemplo de uso

Um pesquisador está organizando dados de um levantamento bibliográfico numa planilha e quer identificar padrões nos anos de publicação e nas áreas temáticas. Ele envia o arquivo para o Mistral Vibe e usa o recurso de execução de código para gerar, em linguagem natural, gráficos de distribuição por ano e por área, sem precisar escrever o código Python manualmente.

## Quando pode não ser a melhor opção

- Se você precisa de precisão factual garantida, sem verificação posterior: como qualquer [modelo](../conceitos/modelo.md) de linguagem, pode gerar informações incorretas com aparência de certeza — conteúdo histórico ou factual gerado precisa ser conferido em fontes confiáveis
- Se você trabalha com dados sensíveis e usa o plano gratuito: as conversas podem ser usadas para treinar modelos futuros por padrão; o modo sem telemetria (que desativa isso) só está disponível a partir do plano Pro
- Se você já usa bastante ChatGPT, Claude ou Gemini e não tem motivo específico para trocar: a diferença mais relevante do Mistral Vibe é a base europeia da empresa e a ênfase em soberania de dados — relevante sobretudo para instituições com exigências específicas de localização de dados
- Se você está procurando pela ferramenta pelo nome antigo "Le Chat": vale saber que ela foi renomeada, para não se confundir ao procurar documentação ou suporte

## Tipo de acesso

Freemium: o plano gratuito permite uso básico, com limite diário de mensagens. O plano Pro (a partir de US$ 14,99/mês) amplia os limites e libera o modo sem telemetria; há também planos Team e Enterprise para equipes e instituições, este último com opção de hospedagem em infraestrutura dedicada na Europa.

## Sistemas em que roda

Navegador (qualquer sistema operacional) e aplicativos para iOS e Android.

## Integrações

- Google Drive, SharePoint (acesso a arquivos e documentos)
- Slack, Notion (ferramentas de produtividade e comunicação)
- GitHub (repositórios de código, relevante para o "Code Mode")

## Alternativas

- [ChatGPT](chatgpt.md) (da OpenAI, com proposta semelhante)
- [Claude](claude.md) (da Anthropic, com proposta semelhante)
- [Gemini](gemini.md) (do Google, integrado ao ecossistema de produtos Google)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://chat.mistral.ai/](https://chat.mistral.ai/)
- Documentação: [https://docs.mistral.ai/vibe/overview](https://docs.mistral.ai/vibe/overview)

## Observações

Vale registrar a mudança de nome explicitamente: quem já conhecia a ferramenta como "Le Chat" pode não reconhecer o nome "Mistral Vibe" à primeira vista, embora seja o mesmo produto (mesma conta, mesmo endereço de acesso). A Mistral AI também é conhecida por publicar alguns de seus modelos de linguagem como modelos abertos (pesos abertos) — uma prática distinta de o Mistral Vibe em si ser de código aberto, já que o produto/serviço permanece proprietário.

