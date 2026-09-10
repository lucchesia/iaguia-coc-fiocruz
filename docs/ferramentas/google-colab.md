---
title: "Google Colab"
slug: "google-colab"

entry_type: "ferramenta"
tool_type: "serviço web"

category: "notebooks e pesquisa computacional"

tags:
  - notebooks e pesquisa computacional
aliases:
  - "Colaboratory"

source_model: proprietário
access_model: freemium

systems:
  - Web
curva_aprendizado: "baixa a moderada"
integrations:
  - Google Drive
  - GitHub
  - Jupyter

concepts: []
alternatives:
  - Jupyter
  - Kaggle Notebooks
  - Binder

official_site: "https://colab.research.google.com/"
documentation: "https://research.google.com/colaboratory/faq.html"
forum: "não disponível"

caveats:
  - envia dados para serviço externo
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Google Colab (ou Colaboratory) é um serviço gratuito da Google que hospeda notebooks no formato [Jupyter](jupyter.md), acessíveis direto pelo navegador, sem qualquer instalação. Diferente do Jupyter instalado localmente, o Colab roda os notebooks nos servidores da Google, com acesso gratuito (mas limitado) a GPUs e TPUs — hardware especializado que acelera tarefas de aprendizado de máquina.

## Para que serve

- Escrever e executar notebooks Jupyter direto no navegador, sem instalar Python ou nenhuma dependência no próprio computador
- Usar GPUs e TPUs gratuitamente (com limites de uso) para tarefas que exigem mais poder de processamento, como treinar modelos de aprendizado de máquina
- Salvar e organizar notebooks automaticamente no Google Drive, compartilhando-os como qualquer outro documento do Google
- Carregar notebooks diretamente de repositórios do GitHub
- Colaborar em tempo real no mesmo notebook com outras pessoas, como num documento do Google Docs

## Exemplo de uso

Um estudante de pós-graduação quer treinar um [modelo](../conceitos/modelo.md) de reconhecimento de entidades nomeadas em um corpus de documentos históricos, usando bibliotecas como o spaCy, mas seu notebook pessoal não tem placa de vídeo suficiente para isso. Em vez de precisar de um computador mais potente, ele abre um notebook no Google Colab, ativa o acesso gratuito a uma GPU e roda o treinamento diretamente no navegador, sem instalar nada localmente.

## Quando pode não ser a melhor opção

- Se você trabalha com dados sensíveis ou sigilosos: a Google coleta os comandos, o código e os resultados gerados no Colab, retendo esses dados por até 18 meses, com possibilidade de revisão humana para fins de melhoria do serviço — vale essa ressalva para pesquisa com informação confidencial
- Se você precisa de sessões de trabalho muito longas ou ambiente sempre disponível: o plano gratuito limita a execução contínua a 12 horas e prioriza quem está usando o notebook ativamente, podendo desconectar sessões ociosas
- Se você já tem um ambiente Python configurado localmente e não precisa de GPU/TPU: o [Jupyter](jupyter.md) rodando no próprio computador evita essas limitações e mantém os dados só na sua máquina
- Se você precisa de recursos garantidos e previsíveis: mesmo nos planos pagos (Colab Pro, Pro+), o acesso a hardware não é garantido nem ilimitado — apenas prioritário

## Tipo de acesso

Freemium: o plano gratuito exige apenas uma conta Google e já inclui acesso limitado a GPU/TPU. Planos pagos (Colab Pro, a partir de US$ 9,99/mês, e Pro+) oferecem mais unidades de computação e prioridade de acesso a hardware melhor, mas não removem os limites por completo.

## Sistemas em que roda

Funciona em qualquer navegador moderno — não há instalação necessária.

## Integrações

- Google Drive (armazenamento e compartilhamento automático dos notebooks)
- GitHub (é possível abrir notebooks diretamente de um repositório)
- [Jupyter](jupyter.md): o Colab usa o mesmo formato de arquivo (.ipynb) e é compatível com notebooks Jupyter existentes

## Alternativas

- [Jupyter](jupyter.md) (instalado localmente, sem depender de servidores da Google)
- Kaggle Notebooks (também gratuito, com acesso a GPU, integrado à plataforma de competições de ciência de dados Kaggle)
- Binder (transforma um repositório do GitHub num ambiente de notebook temporário e gratuito, sem conta Google)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://colab.research.google.com/](https://colab.research.google.com/)
- Perguntas frequentes (FAQ oficial): [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

## Observações

O Google Colab é bastante usado em cursos introdutórios de ciência de dados e aprendizado de máquina justamente por eliminar a barreira de instalação — muitos tutoriais e cursos online de PLN e IA voltados a humanidades digitais são distribuídos diretamente como notebooks do Colab, prontos para rodar com um clique. A principal ressalva, reforçada acima, é a política de retenção e revisão de dados da Google, relevante para quem trabalha com fontes sensíveis.

