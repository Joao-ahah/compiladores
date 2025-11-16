# 3. Gramática Formal Completa da DoceLang

## 3.1 Introdução à Gramática

Este documento apresenta a gramática formal da DoceLang em duas notações:
- **BNF** (Backus-Naur Form) - notação clássica
- **EBNF** (Extended BNF) - notação estendida com operadores de repetição

A gramática está organizada em três versões:
1. **Versão Simples** - comandos básicos apenas
2. **Versão Intermediária** - adiciona estrutura `repeat`
3. **Versão Avançada** - versão completa com todas as funcionalidades

---

## 3.2 Gramática em BNF - Versão Simples

### 3.2.1 Produções Principais

```bnf
<programa> ::= <receita>

<receita> ::= "recipe" <identificador> "{" <bloco_ingredientes> <bloco_preparacao> "}"

<bloco_ingredientes> ::= "ingredients" "{" <lista_ingredientes> "}"

<lista_ingredientes> ::= <ingrediente> ";"
                       | <ingrediente> ";" <lista_ingredientes>

<ingrediente> ::= <identificador>

<bloco_preparacao> ::= "preparation" "{" <lista_comandos> "}"

<lista_comandos> ::= <comando> ";"
                   | <comando> ";" <lista_comandos>

<comando> ::= <comando_add>
            | <comando_mix>
            | <comando_heat>
            | <comando_wait>
            | <comando_serve>

<comando_add> ::= "add" <identificador>

<comando_mix> ::= "mix" <tempo>

<comando_heat> ::= "heat" <temperatura>

<comando_wait> ::= "wait" <tempo>

<comando_serve> ::= "serve"
```

### 3.2.2 Produções Léxicas

```bnf
<identificador> ::= <letra> <resto_identificador>

<resto_identificador> ::= ε
                        | <letra> <resto_identificador>
                        | <digito> <resto_identificador>
                        | "_" <resto_identificador>

<tempo> ::= <numero> <unidade_tempo>

<unidade_tempo> ::= "s" | "min" | "h"

<temperatura> ::= <numero> <unidade_temperatura>

<unidade_temperatura> ::= "C" | "F"

<numero> ::= <digito> <resto_numero>

<resto_numero> ::= ε
                 | <digito> <resto_numero>

<letra> ::= "a" | "b" | "c" | ... | "z" | "A" | "B" | ... | "Z"

<digito> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

---

## 3.3 Gramática em EBNF - Versão Simples

### 3.3.1 Produções Principais (EBNF)

```ebnf
programa = receita ;

receita = "recipe" identificador "{" bloco_ingredientes bloco_preparacao "}" ;

bloco_ingredientes = "ingredients" "{" lista_ingredientes "}" ;

lista_ingredientes = ingrediente ";" { ingrediente ";" } ;

ingrediente = identificador ;

bloco_preparacao = "preparation" "{" lista_comandos "}" ;

lista_comandos = comando ";" { comando ";" } ;

comando = comando_add
        | comando_mix
        | comando_heat
        | comando_wait
        | comando_serve ;

comando_add = "add" identificador ;

comando_mix = "mix" tempo ;

comando_heat = "heat" temperatura ;

comando_wait = "wait" tempo ;

comando_serve = "serve" ;
```

### 3.3.2 Produções Léxicas (EBNF)

```ebnf
identificador = letra { letra | digito | "_" } ;

tempo = numero unidade_tempo ;

unidade_tempo = "s" | "min" | "h" ;

temperatura = numero unidade_temperatura ;

unidade_temperatura = "C" | "F" ;

numero = digito { digito } ;

letra = "a" | "b" | ... | "z" | "A" | "B" | ... | "Z" ;

digito = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

**Legenda dos operadores EBNF**:
- `{ }` - repetição zero ou mais vezes
- `[ ]` - opcional (zero ou uma vez)
- `|` - alternativa
- `;` - fim de produção

---

## 3.4 Gramática em BNF - Versão Completa (com repeat)

### 3.4.1 Produções Principais

```bnf
<programa> ::= <receita>

<receita> ::= "recipe" <identificador> "{" <bloco_ingredientes> <bloco_preparacao> "}"

<bloco_ingredientes> ::= "ingredients" "{" <lista_ingredientes> "}"

<lista_ingredientes> ::= <ingrediente> ";"
                       | <ingrediente> ";" <lista_ingredientes>

<ingrediente> ::= <identificador>

<bloco_preparacao> ::= "preparation" "{" <lista_comandos> "}"

<lista_comandos> ::= <comando> ";"
                   | <comando> ";" <lista_comandos>

<comando> ::= <comando_simples>
            | <comando_composto>

<comando_simples> ::= <comando_add>
                    | <comando_mix>
                    | <comando_heat>
                    | <comando_wait>
                    | <comando_serve>

<comando_composto> ::= <comando_repeat>

<comando_add> ::= "add" <identificador>

<comando_mix> ::= "mix" <tempo>

<comando_heat> ::= "heat" <temperatura>

<comando_wait> ::= "wait" <tempo>

<comando_serve> ::= "serve"

<comando_repeat> ::= "repeat" <numero> "times" "{" <lista_comandos> "}"
```

### 3.4.2 Produções Léxicas

```bnf
<identificador> ::= <letra> <resto_id>

<resto_id> ::= ε
             | <letra> <resto_id>
             | <digito> <resto_id>
             | "_" <resto_id>

<tempo> ::= <numero> <unidade_tempo>

<unidade_tempo> ::= "s" | "min" | "h"

<temperatura> ::= <numero> <unidade_temperatura>

<unidade_temperatura> ::= "C" | "F"

<numero> ::= <digito> <resto_num>

<resto_num> ::= ε
              | <digito> <resto_num>

<letra> ::= "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" |
            "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" |
            "u" | "v" | "w" | "x" | "y" | "z" |
            "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" |
            "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" |
            "U" | "V" | "W" | "X" | "Y" | "Z"

<digito> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

---

## 3.5 Gramática em EBNF - Versão Completa

### 3.5.1 Gramática Completa Compacta

```ebnf
(* Gramática DoceLang - Versão Completa *)

programa = receita ;

receita = "recipe" identificador "{" bloco_ingredientes bloco_preparacao "}" ;

bloco_ingredientes = "ingredients" "{" lista_ingredientes "}" ;

lista_ingredientes = ingrediente ";" { ingrediente ";" } ;

ingrediente = identificador ;

bloco_preparacao = "preparation" "{" lista_comandos "}" ;

lista_comandos = comando ";" { comando ";" } ;

comando = comando_simples | comando_composto ;

comando_simples = comando_add
                | comando_mix
                | comando_heat
                | comando_wait
                | comando_serve ;

comando_composto = comando_repeat ;

comando_add = "add" identificador ;

comando_mix = "mix" tempo ;

comando_heat = "heat" temperatura ;

comando_wait = "wait" tempo ;

comando_serve = "serve" ;

comando_repeat = "repeat" numero "times" "{" lista_comandos "}" ;

(* Tokens Léxicos *)

identificador = letra { letra | digito | "_" } ;

tempo = numero unidade_tempo ;

unidade_tempo = "s" | "min" | "h" ;

temperatura = numero unidade_temperatura ;

unidade_temperatura = "C" | "F" ;

numero = digito { digito } ;

letra = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" |
        "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" |
        "u" | "v" | "w" | "x" | "y" | "z" |
        "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" |
        "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" |
        "U" | "V" | "W" | "X" | "Y" | "Z" ;

digito = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

---

## 3.6 Diagrama de Sintaxe (Railroad Diagram)

### 3.6.1 Estrutura Principal

```
programa:
┌────────┐
│receita │
└────────┘

receita:
┌───────┐  ┌──────────────┐  ┌─┐  ┌───────────────────┐  ┌───────────────────┐  ┌─┐
│recipe │─▶│identificador │─▶│{│─▶│bloco_ingredientes│─▶│bloco_preparacao   │─▶│}│
└───────┘  └──────────────┘  └─┘  └───────────────────┘  └───────────────────┘  └─┘

bloco_ingredientes:
┌────────────┐  ┌─┐  ┌─────────────────────┐  ┌─┐
│ingredients │─▶│{│─▶│lista_ingredientes  │─▶│}│
└────────────┘  └─┘  └─────────────────────┘  └─┘

bloco_preparacao:
┌────────────┐  ┌─┐  ┌───────────────┐  ┌─┐
│preparation│─▶│{│─▶│lista_comandos │─▶│}│
└────────────┘  └─┘  └───────────────┘  └─┘

lista_comandos:
         ┌──────────────┐
         │              │
         │     ┌─┐      ▼
┌───────┐│  ┌─▶│;│─▶┌────────┐
│comando││  │  └─┘  │comando │
└───────┘│  │       └────────┘
         │  │           │
         └──┘◀──────────┘

comando:
              ┌───────────────┐
              │comando_add    │
              ├───────────────┤
              │comando_mix    │
┌────────┐    ├───────────────┤
│        │───▶│comando_heat   │
└────────┘    ├───────────────┤
              │comando_wait   │
              ├───────────────┤
              │comando_serve  │
              ├───────────────┤
              │comando_repeat │
              └───────────────┘
```

---

## 3.7 Árvore de Derivação - Exemplo

### Programa Exemplo

```docelang
recipe Brigadeiro {
    ingredients {
        leite_condensado;
        chocolate;
    }
    
    preparation {
        add leite_condensado;
        mix 5min;
        serve;
    }
}
```

### Árvore de Derivação (Parcial)

```
programa
  │
  └── receita
        ├── "recipe"
        ├── identificador (Brigadeiro)
        ├── "{"
        ├── bloco_ingredientes
        │     ├── "ingredients"
        │     ├── "{"
        │     ├── lista_ingredientes
        │     │     ├── ingrediente
        │     │     │     └── identificador (leite_condensado)
        │     │     ├── ";"
        │     │     ├── ingrediente
        │     │     │     └── identificador (chocolate)
        │     │     └── ";"
        │     └── "}"
        ├── bloco_preparacao
        │     ├── "preparation"
        │     ├── "{"
        │     ├── lista_comandos
        │     │     ├── comando
        │     │     │     └── comando_add
        │     │     │           ├── "add"
        │     │     │           └── identificador (leite_condensado)
        │     │     ├── ";"
        │     │     ├── comando
        │     │     │     └── comando_mix
        │     │     │           ├── "mix"
        │     │     │           └── tempo
        │     │     │                 ├── numero (5)
        │     │     │                 └── unidade_tempo ("min")
        │     │     ├── ";"
        │     │     ├── comando
        │     │     │     └── comando_serve
        │     │     │           └── "serve"
        │     │     └── ";"
        │     └── "}"
        └── "}"
```

---

## 3.8 Tabela de Tokens e Produções

### 3.8.1 Terminais (Tokens)

| Token | Tipo | Regex | Exemplo |
|-------|------|-------|---------|
| `recipe` | PALAVRA-CHAVE | `recipe` | `recipe` |
| `ingredients` | PALAVRA-CHAVE | `ingredients` | `ingredients` |
| `preparation` | PALAVRA-CHAVE | `preparation` | `preparation` |
| `add` | PALAVRA-CHAVE | `add` | `add` |
| `mix` | PALAVRA-CHAVE | `mix` | `mix` |
| `heat` | PALAVRA-CHAVE | `heat` | `heat` |
| `wait` | PALAVRA-CHAVE | `wait` | `wait` |
| `serve` | PALAVRA-CHAVE | `serve` | `serve` |
| `repeat` | PALAVRA-CHAVE | `repeat` | `repeat` |
| `times` | PALAVRA-CHAVE | `times` | `times` |
| `{` | DELIMITADOR | `\{` | `{` |
| `}` | DELIMITADOR | `\}` | `}` |
| `;` | DELIMITADOR | `;` | `;` |
| IDENTIFICADOR | IDENTIFICADOR | `[a-zA-Z][a-zA-Z0-9_]*` | `leite_condensado` |
| NUMERO | NUMERO | `[0-9]+` | `42` |
| TEMPO | TEMPO | `[0-9]+(s\|min\|h)` | `5min` |
| TEMPERATURA | TEMPERATURA | `[0-9]+(C\|F)` | `180C` |

### 3.8.2 Não-Terminais (Produções)

| Não-Terminal | Primeira Derivação | Exemplo |
|--------------|-------------------|---------|
| `<programa>` | `recipe` | Todo o programa |
| `<receita>` | `recipe` | Estrutura completa da receita |
| `<bloco_ingredientes>` | `ingredients` | Bloco de declaração |
| `<bloco_preparacao>` | `preparation` | Bloco de comandos |
| `<lista_ingredientes>` | IDENTIFICADOR | Lista de IDs |
| `<lista_comandos>` | `add`, `mix`, `heat`, `wait`, `serve`, `repeat` | Sequência |
| `<comando>` | `add`, `mix`, `heat`, `wait`, `serve`, `repeat` | Comando individual |
| `<identificador>` | letra | Nome válido |
| `<tempo>` | dígito | `5min` |
| `<temperatura>` | dígito | `180C` |
| `<numero>` | dígito | `42` |

---

## 3.9 Propriedades da Gramática

### 3.9.1 Classificação Hierárquica de Chomsky

**DoceLang é uma Gramática Livre de Contexto (Tipo 2)**

**Justificativa**:
- Todas as produções têm a forma: `<A> ::= α` onde A é não-terminal e α é sequência de terminais/não-terminais
- Permite estruturas aninhadas (repeat dentro de repeat)
- Pode ser reconhecida por autômato com pilha (PDA)
- Possui árvore de derivação única (não ambígua)

### 3.9.2 Ambiguidade

**A gramática é NÃO-AMBÍGUA**

**Demonstração**:
1. Não há produções com múltiplas derivações para mesma entrada
2. Ordem dos blocos é fixa: ingredients → preparation
3. Comandos são distinguíveis pela palavra-chave inicial
4. Não há conflitos shift-reduce ou reduce-reduce

**Exemplo**: `add leite;` só pode ser derivado de uma forma:
```
comando → comando_add → "add" identificador → "add" leite
```

### 3.9.3 Recursividade

**Recursão à Direita**: Em listas (ingredientes e comandos)

```bnf
<lista_comandos> ::= <comando> ";"
                   | <comando> ";" <lista_comandos>
```

**Recursão Indireta**: Em `comando_repeat`

```bnf
<comando> ::= <comando_repeat>
<comando_repeat> ::= "repeat" <numero> "times" "{" <lista_comandos> "}"
<lista_comandos> ::= <comando> ";" ...
```

Isso permite aninhamento infinito:
```docelang
repeat 2 times {
    repeat 3 times {
        repeat 4 times {
            add ingrediente;
        }
    }
}
```

### 3.9.4 Factorização

**A gramática está factorizada à esquerda**

Não há produções da forma:
```
<A> ::= α β
<A> ::= α γ
```

Todos os comandos começam com palavras-chave únicas:
- `add` → comando_add
- `mix` → comando_mix
- `heat` → comando_heat
- `wait` → comando_wait
- `serve` → comando_serve
- `repeat` → comando_repeat

---

## 3.10 Gramática Aumentada para Parsing

### 3.10.1 Símbolos de Fim de Entrada

```bnf
<S'> ::= <programa> $

<programa> ::= <receita>

...
```

Onde `$` representa fim de arquivo (EOF).

### 3.10.2 Produções com Precedência (Futuro)

Para versões avançadas com expressões:

```bnf
<expressao> ::= <termo>
              | <expressao> "+" <termo>
              | <expressao> "-" <termo>

<termo> ::= <fator>
          | <termo> "*" <fator>
          | <termo> "/" <fator>

<fator> ::= <numero>
          | "(" <expressao> ")"
```

---

## 3.11 Tabela First e Follow

### 3.11.1 Conjuntos First

| Não-Terminal | First |
|--------------|-------|
| `<programa>` | {`recipe`} |
| `<receita>` | {`recipe`} |
| `<bloco_ingredientes>` | {`ingredients`} |
| `<bloco_preparacao>` | {`preparation`} |
| `<lista_ingredientes>` | {IDENTIFICADOR} |
| `<lista_comandos>` | {`add`, `mix`, `heat`, `wait`, `serve`, `repeat`} |
| `<comando>` | {`add`, `mix`, `heat`, `wait`, `serve`, `repeat`} |
| `<comando_add>` | {`add`} |
| `<comando_mix>` | {`mix`} |
| `<comando_heat>` | {`heat`} |
| `<comando_wait>` | {`wait`} |
| `<comando_serve>` | {`serve`} |
| `<comando_repeat>` | {`repeat`} |
| `<identificador>` | {letra} |
| `<tempo>` | {dígito} |
| `<temperatura>` | {dígito} |
| `<numero>` | {dígito} |

### 3.11.2 Conjuntos Follow

| Não-Terminal | Follow |
|--------------|--------|
| `<programa>` | {$} |
| `<receita>` | {$} |
| `<bloco_ingredientes>` | {`preparation`} |
| `<bloco_preparacao>` | {`}`} |
| `<lista_ingredientes>` | {`}`} |
| `<lista_comandos>` | {`}`} |
| `<comando>` | {`;`} |
| `<comando_add>` | {`;`} |
| `<comando_mix>` | {`;`} |
| `<comando_heat>` | {`;`} |
| `<comando_wait>` | {`;`} |
| `<comando_serve>` | {`;`} |
| `<comando_repeat>` | {`;`} |
| `<identificador>` | {`;`, `{`} |
| `<tempo>` | {`;`} |
| `<temperatura>` | {`;`} |
| `<numero>` | {`s`, `min`, `h`, `C`, `F`, `times`} |

---

## 3.12 Derivações Exemplo

### 3.12.1 Derivação Mais à Esquerda

**Entrada**: `recipe Bolo { ingredients { farinha; } preparation { add farinha; } }`

```
<programa>
⇒ <receita>
⇒ "recipe" <identificador> "{" <bloco_ingredientes> <bloco_preparacao> "}"
⇒ "recipe" Bolo "{" <bloco_ingredientes> <bloco_preparacao> "}"
⇒ "recipe" Bolo "{" "ingredients" "{" <lista_ingredientes> "}" <bloco_preparacao> "}"
⇒ "recipe" Bolo "{" "ingredients" "{" <ingrediente> ";" "}" <bloco_preparacao> "}"
⇒ "recipe" Bolo "{" "ingredients" "{" <identificador> ";" "}" <bloco_preparacao> "}"
⇒ "recipe" Bolo "{" "ingredients" "{" farinha ";" "}" <bloco_preparacao> "}"
⇒ "recipe" Bolo "{" "ingredients" "{" farinha ";" "}" "preparation" "{" <lista_comandos> "}" "}"
⇒ "recipe" Bolo "{" "ingredients" "{" farinha ";" "}" "preparation" "{" <comando> ";" "}" "}"
⇒ "recipe" Bolo "{" "ingredients" "{" farinha ";" "}" "preparation" "{" <comando_add> ";" "}" "}"
⇒ "recipe" Bolo "{" "ingredients" "{" farinha ";" "}" "preparation" "{" "add" <identificador> ";" "}" "}"
⇒ "recipe" Bolo "{" "ingredients" "{" farinha ";" "}" "preparation" "{" "add" farinha ";" "}" "}"
```

### 3.12.2 Derivação Mais à Direita

```
<programa>
⇒ <receita>
⇒ "recipe" <identificador> "{" <bloco_ingredientes> <bloco_preparacao> "}"
⇒ "recipe" <identificador> "{" <bloco_ingredientes> "preparation" "{" <lista_comandos> "}" "}"
⇒ "recipe" <identificador> "{" <bloco_ingredientes> "preparation" "{" <comando> ";" "}" "}"
⇒ "recipe" <identificador> "{" <bloco_ingredientes> "preparation" "{" <comando_add> ";" "}" "}"
⇒ "recipe" <identificador> "{" <bloco_ingredientes> "preparation" "{" "add" <identificador> ";" "}" "}"
⇒ "recipe" <identificador> "{" <bloco_ingredientes> "preparation" "{" "add" farinha ";" "}" "}"
⇒ "recipe" <identificador> "{" "ingredients" "{" <lista_ingredientes> "}" "preparation" "{" "add" farinha ";" "}" "}"
⇒ "recipe" <identificador> "{" "ingredients" "{" <ingrediente> ";" "}" "preparation" "{" "add" farinha ";" "}" "}"
⇒ "recipe" <identificador> "{" "ingredients" "{" <identificador> ";" "}" "preparation" "{" "add" farinha ";" "}" "}"
⇒ "recipe" <identificador> "{" "ingredients" "{" farinha ";" "}" "preparation" "{" "add" farinha ";" "}" "}"
⇒ "recipe" Bolo "{" "ingredients" "{" farinha ";" "}" "preparation" "{" "add" farinha ";" "}" "}"
```

---

## 3.13 Versões da Gramática

### 3.13.1 Versão 1.0 - Simples

**Funcionalidades**:
- ✅ Estrutura básica (recipe, ingredients, preparation)
- ✅ 5 comandos básicos (add, mix, heat, wait, serve)
- ❌ Sem estruturas de repetição

**Arquivo**: `grammar/docelang-v1.0.bnf`

---

### 3.13.2 Versão 2.0 - Intermediária (Atual)

**Funcionalidades**:
- ✅ Tudo da v1.0
- ✅ Comando `repeat N times { }`
- ✅ Suporte a aninhamento de repeat
- ❌ Sem condicionais ou variáveis

**Arquivo**: `grammar/docelang-v2.0.bnf`

---

### 3.13.3 Versão 3.0 - Avançada (Futura)

**Funcionalidades Planejadas**:
- ✅ Tudo da v2.0
- ✅ Variáveis: `let quantidade = 200g;`
- ✅ Condicionais: `if temperatura > 100C then ... else ...`
- ✅ Expressões aritméticas: `quantidade * 2`
- ✅ Sub-receitas (funções): `function massa_base() { ... }`

**Gramática Planejada**:
```ebnf
comando = comando_simples
        | comando_composto
        | comando_variavel
        | comando_condicional ;

comando_variavel = "let" identificador "=" expressao ;

comando_condicional = "if" condicao "then" bloco [ "else" bloco ] ;

condicao = expressao comparador expressao ;

comparador = ">" | "<" | "==" | ">=" | "<=" | "!=" ;

expressao = termo { ( "+" | "-" ) termo } ;

termo = fator { ( "*" | "/" ) fator } ;

fator = numero | identificador | "(" expressao ")" ;
```

---

## 3.14 Gramática para Ferramentas

### 3.14.1 Formato para JFLAP

Arquivo: `grammar/docelang-jflap.txt`

```
S -> recipe I { B P }
B -> ingredients { L }
L -> I ;
L -> I ; L
P -> preparation { C }
C -> A ;
C -> A ; C
A -> add I
A -> mix T
A -> heat E
A -> wait T
A -> serve
A -> repeat N times { C }
I -> letra R
R -> letra R
R -> digito R
R -> _ R
R -> ε
T -> N U
U -> s
U -> min
U -> h
E -> N V
V -> C
V -> F
N -> digito D
D -> digito D
D -> ε
```

### 3.14.2 Formato para BNF Playground

Arquivo: `grammar/docelang-bnfplayground.txt`

```
<program> ::= <recipe>
<recipe> ::= "recipe" <id> "{" <ingredients> <preparation> "}"
<ingredients> ::= "ingredients" "{" <ing-list> "}"
<ing-list> ::= <id> ";" | <id> ";" <ing-list>
<preparation> ::= "preparation" "{" <cmd-list> "}"
<cmd-list> ::= <cmd> ";" | <cmd> ";" <cmd-list>
<cmd> ::= "add" <id> | "mix" <time> | "heat" <temp> | "wait" <time> | "serve" | "repeat" <num> "times" "{" <cmd-list> "}"
<id> ::= /[a-zA-Z][a-zA-Z0-9_]*/
<time> ::= /[0-9]+(s|min|h)/
<temp> ::= /[0-9]+(C|F)/
<num> ::= /[0-9]+/
```

---

## 3.15 Conclusão da Gramática

A gramática DoceLang apresentada é:
- ✅ **Livre de contexto** (Tipo 2 de Chomsky)
- ✅ **Não-ambígua** (derivação única)
- ✅ **Factorizada** (parsing LL(1) possível)
- ✅ **Recursiva** (permite aninhamento)
- ✅ **Extensível** (permite futuras adições)

**Próximo**: [4. Análise Léxica (Tokens) →](04-analise-lexica.md)
