---
title: "Jupyter"
slug: "jupyter"

entry_type: "ferramenta"
tool_type: "aplicativo"

category: "notebooks e pesquisa computacional"

tags:
  - notebooks e pesquisa computacional
  - open source
  - uso offline
  - gratuito para pesquisa
aliases:
  - "Jupyter Notebook"
  - "JupyterLab"

source_model: aberto
software_license: BSD-3-Clause
access_model: gratuito

systems:
  - Windows
  - macOS
  - Linux
curva_aprendizado: "moderada a alta"
integrations:
  - Python
  - R
  - Julia

concepts: []
alternatives:
  - Google Colab
  - RStudio
  - Observable

official_site: "https://jupyter.org/"
documentation: "https://docs.jupyter.org/"
forum: "https://discourse.jupyter.org/"
repository: "https://github.com/jupyter/notebook"

caveats:
  - requer conhecimentos técnicos
learning_resources: []
academic_use: []
tool_status: ativa
status: publicado
reviewed: true
last_reviewed: "2026-08-20"
---

## O que é

Jupyter é um projeto gratuito e de código aberto para criar "notebooks" computacionais — documentos que combinam código executável, texto explicativo, imagens e visualizações num único arquivo. Nasceu do projeto IPython em 2014 e hoje é mantido pelo Project Jupyter, uma organização sem fins lucrativos. O nome vem das três linguagens originalmente suportadas (Julia, Python, R), mas hoje o Jupyter funciona com mais de 40 linguagens de programação diferentes, por meio de componentes chamados "kernels".

## Para que serve

- Escrever e executar código em blocos (células), intercalando com texto explicativo, fórmulas matemáticas e imagens no mesmo documento
- Explorar e analisar dados de forma interativa, vendo o resultado de cada trecho de código imediatamente
- Documentar todo o processo de uma análise — do carregamento dos dados brutos até os gráficos finais — num único arquivo compartilhável
- Combinar código com narrativa, o que facilita tanto ensino quanto a reprodutibilidade de uma pesquisa (outras pessoas podem rodar o mesmo notebook e obter os mesmos resultados)
- Duas interfaces principais fazem parte do projeto: o Jupyter Notebook (mais simples, focada num documento por vez) e o JupyterLab (ambiente mais completo, com múltiplos painéis e arquivos abertos ao mesmo tempo)

## Exemplo de uso

Um pesquisador está processando uma grande base de dados de censos históricos e quer documentar cada etapa da análise, desde a limpeza dos dados até os gráficos finais, de forma que outros pesquisadores possam reproduzir o processo depois. Ele usa um notebook Jupyter para isso: cada célula de código processa uma etapa (importar os dados, filtrar, calcular estatísticas, gerar gráficos), intercalada com células de texto explicando as decisões metodológicas tomadas em cada passo. O arquivo final serve tanto como ferramenta de trabalho quanto como documentação transparente da pesquisa.

## Quando pode não ser a melhor opção

- Se você não programa: o Jupyter não tem interface visual sem código — é preciso escrever comandos em alguma linguagem de programação (geralmente Python)
- Se você não quer instalar nada no próprio computador: o [Google Colab](google-colab.md) oferece uma experiência de notebook parecida, rodando inteiramente na nuvem, sem instalação
- Se você trabalha principalmente em R e prefere um ambiente dedicado a essa linguagem: o RStudio é uma alternativa mais focada nesse ecossistema
- Se o projeto crescer para algo que várias pessoas precisam acessar ao mesmo tempo, num servidor compartilhado: isso exige configurar o JupyterHub, um componente à parte, com mais complexidade de administração

## Tipo de acesso

Totalmente gratuito e de código aberto (licença BSD revisada).

## Sistemas em que roda

Windows, macOS e Linux — instalado localmente, geralmente como parte de uma distribuição Python (como o Anaconda) ou via `pip install jupyterlab`.

## Integrações

- Python (linguagem mais usada com o Jupyter, embora não seja a única)
- R e Julia (outras linguagens com suporte nativo, via kernels próprios)

## Alternativas

- [Google Colab](google-colab.md) (mesma proposta de notebook, mas roda na nuvem, sem instalação local)
- RStudio (ambiente de desenvolvimento focado em R, com suporte a notebooks via R Markdown/Quarto)
- Observable (notebooks baseados em JavaScript, voltados a visualização de dados na web)

## Aprenda a usar

### Onde encontrar

- Site oficial: [https://jupyter.org/](https://jupyter.org/)
- Documentação: [https://docs.jupyter.org/](https://docs.jupyter.org/)
- Repositório: [https://github.com/jupyter/notebook](https://github.com/jupyter/notebook)
- Fórum da comunidade: [https://discourse.jupyter.org/](https://discourse.jupyter.org/)

## Observações

O Jupyter é hoje um padrão de fato em ciência de dados e pesquisa computacional reprodutível, usado tanto em ambientes acadêmicos quanto profissionais. Para pesquisa em história que envolva processamento de grandes volumes de dados (por exemplo, com bibliotecas Python como pandas, ou com o [spaCy](spacy.md) para PLN), o Jupyter costuma ser o ambiente de trabalho onde esse tipo de script é escrito e documentado.

