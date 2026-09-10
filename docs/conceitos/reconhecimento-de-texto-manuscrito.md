---
title: "Handwritten Text Recognition"
title_pt: "Reconhecimento de Texto Manuscrito"
slug: "reconhecimento-de-texto-manuscrito"

entry_type: "conceito"
concept_type: "técnica"

category: "linguagem, documentos, imagem e áudio"

tags:
  - inteligência artificial
  - aprendizado de máquina

aliases:
  - "HTR"
  - "handwritten text recognition"

related_terms:
  - reconhecimento-optico-de-caracteres
  - tei
prerequisites:
  - reconhecimento-optico-de-caracteres
  - aprendizado-profundo

references:
  - title: "What is Handwritten Text Recognition? — Transkribus"
    url: "https://www.transkribus.org/what-is-handwritten-text-recognition"
    type: "documentação técnica"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Reconhecimento de Texto Manuscrito

## O que é

HTR (Reconhecimento de Texto Manuscrito, do inglês *Handwritten Text Recognition*) é a tecnologia que converte imagens de texto escrito à mão em texto digital editável. Segundo a documentação técnica do Transkribus — uma das principais ferramentas dessa área —, HTR "usa aprendizado profundo para converter documentos manuscritos em texto legível por máquina". Diferente do [OCR](reconhecimento-optico-de-caracteres.md) tradicional, o HTR é treinado especificamente com amostras reais de caligrafia, o que permite decifrar escritas históricas, cursivas e letras conectadas que sistemas baseados em regras fixas não conseguem processar.

## Por que isso importa?

HTR é especialmente relevante para pesquisa histórica, já que grande parte das fontes primárias manuscritas — cartas, registros paroquiais, atas, diários — não pode ser processada por OCR comum. Entender que o HTR depende de um modelo treinado especificamente para um tipo de caligrafia, período ou região ajuda a explicar por que a qualidade do reconhecimento varia tanto entre diferentes documentos: uma caligrafia bem representada nos dados de treinamento de um modelo tende a ser reconhecida com muito mais precisão do que uma caligrafia rara ou pouco documentada.

## Exemplo

Ferramentas como o [Transkribus](../ferramentas/transkribus.md) e o [eScriptorium](../ferramentas/escriptorium.md) permitem treinar um modelo de HTR específico para a caligrafia de um conjunto de documentos — uma pesquisadora transcreve manualmente algumas páginas, e o sistema usa esse exemplo para aprender a reconhecer aquele estilo de escrita, acelerando a transcrição do restante da coleção.

## Não confunda com

HTR não é sinônimo de OCR: OCR é voltado a texto impresso, com formas de letra relativamente padronizadas; HTR é voltado especificamente a texto manuscrito, cuja variação de caligrafia exige uma abordagem técnica diferente. Também não é sinônimo de transcrição manual: HTR é um processo automatizado (ainda que exija revisão humana); transcrição manual é feita inteiramente por uma pessoa, sem uso de reconhecimento automático.

## Termos relacionados

## Referências

- Transkribus. *What is Handwritten Text Recognition?*.
  [transkribus.org/what-is-handwritten-text-recognition](https://www.transkribus.org/what-is-handwritten-text-recognition)
