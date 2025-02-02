
#set text(lang: "pt", 12pt)
#set heading(numbering: "1.")
#set par(justify: true)
#show link: set text(fill: blue)

// ------------- Header -------------
// Título no centro;
// Numeração das páginas alternada entre esquerda e direita.
#set page(
  header: context {
    align(center)[
      *Introdução à Inteligência Artificial*
      #context {
        let loc = here().page()
        if calc.even(loc) {
          align(left)[#counter(page).display("— 1 —")]
        } else if loc > 1 {
          align(right, counter(page).display("— 1 —"))
        }
      }
    ]
  },
)

#align(center)[
  #text(20pt)[*Trabalho Prático II - 2024/2*] \
  Igor Lacerda Faria da Silva
]

= Introdução

O Trabalho Prático II de Introdução à Inteligência Artificial consistiu na implementação (em Python) de 3 variações do algoritmo _Q-Learning_ para _Path-Finding_, em mapas de um jogo simples (o mesmo jogo do TP I). As variações foram: o _Q-Learning_ padrão (_standard_); com matriz de recompensa positiva (_positive_) e com movimento estocástico (_stochastic_). O repositório deste trabalho pode ser encontrado neste #link("https://github.com/igorlfs/tp2-iia")[link].

A documentação está divida da seguinte maneira: esta breve introdução descreve o que foi realizado, a @dsm descreve a modelagem do programa, entrando nos detalhes das estruturas de dados; a @ql, por sua vez, foca no algoritmo (e variações) implementadas. Por fim, a @anac é uma análise experimental dos diversos algoritmos implementados.

// • Apresentação das estruturas usadas e da modelagem dos componentes (estado, agente, ambiente, etc.).
= Estruturas de Dados e Modelagem <dsm>

== Outras decisões de implementação

// • Breve descrição do método utilizado e das eventuais modificações
= _Q-Learning_ <ql>

// • Análise comparando as políticas geradas pelo método original e suas modificações. Qual o efeito da mudança? A política se alterou? Porque?
= Análise Comparativa <anac>

