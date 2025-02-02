
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

O Trabalho Prático II de Introdução à Inteligência Artificial consistiu na implementação (em Python) de 3 variações do algoritmo _Q-Learning_ para _Path-Finding_, em mapas de um jogo simples (o mesmo jogo do TP I). As variações foram: o _Q-Learning_ padrão (`standard`); com matriz de recompensa positiva (`positive`) e com movimento estocástico (`stochastic`). O repositório deste trabalho pode ser encontrado neste #link("https://github.com/igorlfs/tp2-iia")[link].

A documentação está divida da seguinte maneira: esta breve introdução descreve o que foi realizado, a @dsm descreve a modelagem do programa, entrando nos detalhes das estruturas de dados; a @ql, por sua vez, foca no algoritmo (e variações) implementadas. Por fim, a @anac é uma análise experimental dos diversos algoritmos implementados.

// • Apresentação das estruturas usadas e da modelagem dos componentes (estado, agente, ambiente, etc.).
= Estruturas de Dados e Modelagem <dsm>

Similarmente ao TP I, a estrutura de dados mais prevalente foi a matriz. As matrizes foram usadas em diversos contextos: para armazenar o mapa (caracteres), as recompensas das posições e, claro, gerenciar a matriz (tensor) $Q$. A matriz $Q$ é inicializada com valores aleatórios entre -1 e 1 (somente posições válidas são preenchidas). Além disso, outra estrutura auxiliar utilizada ao longo do programa foi uma tupla, para representar as coordenadas no mapa.

Também foi criado um tipo (`enum`) `Action` para auxiliar no mapeamento das direções em que o agente pode se mover. Ele é particularmente útil no que diz respeito à escolha de uma direção perpendicular, na variação estocástica do algoritmo. Assim como no TP I, foi tomado certo cuidado para lidar com o sistema de coordenadas. Após a leitura do mapa, os dados são transpostos e, no final, após o processamento do algoritmo, os dados são novamente transpostos.

No mais, o restante da implementação é bem similar ao pseudocódigo visto nas aulas. Começando do estado inicial, um _loop_ escolhe uma ação. Geralmente esta é a melhor ação (para aquele estado), mas devido ao mecanismo de exploração $epsilon$-_greedy_, há a chance (10%) de ser alguma outra. A próxima posição é calculada, considerando que é possível não sair do lugar ao tentar realizar um movimento para uma posição inválida.

Caso o agente tenha atingido o estado objetivo (`O`) ou um estado com fogo (`x`), a simulação é reiniciada e a matriz $Q$ é atualizada com base na recompensa do estado atingido. Caso contrário, é buscada a recompensa mais promissora do estado atingido, e é ela que é utilizada para atualizar a recompensa da transição realizada (considerando, claro, a taxa de aprendizado de 0.1 e a taxa de desconto de 0.9). A variação `positive` consiste apenas na troca da matriz de recompensas, enquanto a variação `stochastic` traz nuances que são detalhadas na @ql.

Em resumo, o estado contém todas as posições atingíveis; as ações são os 4 movimentos permitidos; o agente sempre se encontra em uma dada posição e a recompensa é calculada pela estimativa inicial (aleatória) e as sucessivas iterações, conforme descrito nos parágrafos anteriores.

// • Breve descrição do método utilizado e das eventuais modificações
= _Q-Learning_ <ql>

// • Análise comparando as políticas geradas pelo método original e suas modificações. Qual o efeito da mudança? A política se alterou? Porque?
= Análise Comparativa <anac>

