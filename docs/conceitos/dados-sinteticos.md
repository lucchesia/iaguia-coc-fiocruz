---
title: "Synthetic Data"
title_pt: "Dados Sintéticos"
slug: "dados-sinteticos"

entry_type: "conceito"
concept_type: "conceito"

category: "limitações e letramento crítico"

tags:
  - ia generativa
  - aprendizado de máquina

aliases:
  - "synthetic data"

related_terms:
  - conteudo-sintetico
prerequisites:
  - dados
  - dados-de-treinamento

references:
  - title: "synthetic data generation — Glossary | NIST Computer Security Resource Center (citando NIST SP 800-188)"
    url: "https://csrc.nist.gov/glossary/term/synthetic_data_generation"
    type: "glossário técnico institucional"

status: "publicado"
reviewed: true
last_reviewed: "2026-08-21"
---

# Dados Sintéticos

## O que é

Dados sintéticos são dados artificiais, gerados por computador a partir de um processo estatístico ou algorítmico, criados para reproduzir algumas das características de dados reais, sem serem coletados diretamente do mundo real. Segundo o glossário técnico do NIST (citando a NIST SP 800-188), a geração de dados sintéticos é "um processo em que dados de referência são usados para criar dados artificiais que têm algumas das características estatísticas dos dados de referência". Dados sintéticos podem ser usados, por exemplo, para treinar modelos de IA sem expor dados reais sensíveis, ou para preencher lacunas em conjuntos de dados de treinamento pouco representativos.

## Por que isso importa?

Dados sintéticos são cada vez mais usados para treinar modelos de IA em situações onde dados reais são escassos, sensíveis ou desequilibrados (representando pouco certos grupos ou situações). Para pesquisa, é importante entender que dados sintéticos reproduzem apenas padrões estatísticos dos dados originais — não fatos ou eventos reais —, o que pode introduzir distorções sutis se amplificarem, sem perceber, vieses já presentes nos dados de referência usados para gerá-los.

## Exemplo

Uma equipe que desenvolve um modelo de reconhecimento de fala para um dialeto regional pouco documentado pode gerar áudio sintético — vozes artificiais lendo textos nesse dialeto — para complementar um conjunto pequeno de gravações reais, embora esse áudio sintético não substitua a riqueza e a autenticidade de gravações reais de falantes.

## Não confunda com

Dados sintéticos não é sinônimo de conteúdo sintético: dados sintéticos costumam ser gerados para uso técnico, principalmente para treinar outros modelos de IA, com foco em reproduzir propriedades estatísticas; conteúdo sintético é um termo mais amplo, usado para qualquer tipo de conteúdo gerado ou significativamente alterado por IA, com foco no resultado final consumido por pessoas. Também não é sinônimo de dados falsos ou fraudulentos: dados sintéticos são gerados de forma declarada e com propósito técnico legítimo, diferente de uma falsificação deliberada para enganar.

## Termos relacionados

## Referências

- NIST Computer Security Resource Center. *synthetic data generation — Glossary* (citando NIST SP 800-188).
  [csrc.nist.gov/glossary/term/synthetic_data_generation](https://csrc.nist.gov/glossary/term/synthetic_data_generation)
