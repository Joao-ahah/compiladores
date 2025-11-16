# 2. Especificação Completa da Linguagem DoceLang

## 2.1 Estrutura Geral do Programa

### 2.1.1 Anatomia de um Programa DoceLang

Todo programa em DoceLang segue uma estrutura hierárquica bem definida:

```
PROGRAMA
└── RECIPE
    ├── IDENTIFICADOR (nome da receita)
    ├── BLOCO DE INGREDIENTES (ingredients)
    │   └── LISTA DE INGREDIENTES
    └── BLOCO DE PREPARO (preparation)
        └── SEQUÊNCIA DE COMANDOS
```

### 2.1.2 Sintaxe Formal da Estrutura

```docelang
recipe <IDENTIFICADOR> {
    ingredients {
        <ingrediente1>;
        <ingrediente2>;
        ...
        <ingredienteN>;
    }
    
    preparation {
        <comando1>;
        <comando2>;
        ...
        <comandoN>;
    }
}
```

### 2.1.3 Regras Estruturais

1. **Palavra-chave `recipe`** é obrigatória e inicia o programa
2. **Nome da receita** deve ser um identificador válido
3. **Bloco `ingredients`** é obrigatório e precede `preparation`
4. **Bloco `preparation`** é obrigatório e contém os comandos
5. **Chaves** delimitam todos os blocos
6. **Ponto e vírgula** finaliza cada declaração/comando
7. **Ordem** dos blocos é fixa: ingredients → preparation

---

## 2.2 Tipos de Comandos Existentes

### 2.2.1 Comandos Básicos

DoceLang possui 5 comandos básicos fundamentais:

#### 📌 Comando `add` (Adicionar)

**Sintaxe**:
```docelang
add <ingrediente>;
```

**Descrição**: Adiciona um ingrediente à preparação

**Semântica**:
- O `<ingrediente>` deve ter sido declarado no bloco `ingredients`
- Representa ação de adicionar ingrediente à mistura/recipiente

**Exemplos**:
```docelang
add leite_condensado;
add acucar;
add ovos;
```

**Erros comuns**:
```docelang
add farinha;  // ❌ ERRO: farinha não declarada em ingredients
add 200g;     // ❌ ERRO: esperado identificador, recebido número
```

---

#### 📌 Comando `mix` (Misturar)

**Sintaxe**:
```docelang
mix <tempo>;
```

**Descrição**: Mistura/bate/mexe os ingredientes por um período de tempo

**Semântica**:
- `<tempo>` deve ser um número seguido de unidade temporal (s, min, h)
- Representa ação de misturar continuamente

**Exemplos**:
```docelang
mix 5min;      // Misturar por 5 minutos
mix 30s;       // Misturar por 30 segundos
mix 1h;        // Misturar por 1 hora
```

**Erros comuns**:
```docelang
mix 5;         // ❌ ERRO: falta unidade de tempo
mix 180C;      // ❌ ERRO: esperado tempo, recebido temperatura
mix leite;     // ❌ ERRO: esperado tempo, recebido ingrediente
```

---

#### 📌 Comando `heat` (Aquecer)

**Sintaxe**:
```docelang
heat <temperatura>;
```

**Descrição**: Aquece o preparo a uma temperatura específica

**Semântica**:
- `<temperatura>` deve ser um número seguido de unidade térmica (C, F)
- Representa ação de levar ao fogo/forno

**Exemplos**:
```docelang
heat 180C;     // Aquecer a 180 graus Celsius
heat 350F;     // Aquecer a 350 graus Fahrenheit
heat 100C;     // Ferver (100°C)
```

**Erros comuns**:
```docelang
heat 180;      // ❌ ERRO: falta unidade de temperatura
heat 5min;     // ❌ ERRO: esperado temperatura, recebido tempo
heat -20C;     // ⚠️  AVISO: temperatura negativa incomum
```

---

#### 📌 Comando `wait` (Aguardar)

**Sintaxe**:
```docelang
wait <tempo>;
```

**Descrição**: Aguarda/descansa o preparo por um período

**Semântica**:
- `<tempo>` deve ser um número seguido de unidade temporal
- Representa descanso, resfriamento, ou tempo de espera
- Diferente de `mix`: não há ação ativa durante a espera

**Exemplos**:
```docelang
wait 2h;       // Aguardar 2 horas (descanso da massa)
wait 30min;    // Aguardar 30 minutos (resfriamento)
wait 24h;      // Aguardar 24 horas (geladeira)
```

**Diferença entre `mix` e `wait`**:
```docelang
mix 5min;      // Mexer ATIVAMENTE por 5 minutos
wait 5min;     // Deixar PARADO por 5 minutos
```

---

#### 📌 Comando `serve` (Servir)

**Sintaxe**:
```docelang
serve;
```

**Descrição**: Finaliza a receita e indica que está pronta para servir

**Semântica**:
- Não aceita parâmetros
- Deve ser o último comando da receita (boa prática)
- Marca conclusão do preparo

**Exemplos**:
```docelang
serve;  // Receita finalizada
```

**Observações**:
- Opcional sintaticamente, mas recomendado semanticamente
- Em versões futuras, pode ser obrigatório
- Pode aparecer dentro de `repeat` (para porções individuais)

---

### 2.2.2 Comando Composto

#### 📌 Estrutura `repeat` (Repetir)

**Sintaxe**:
```docelang
repeat <número> times {
    <comando1>;
    <comando2>;
    ...
    <comandoN>;
}
```

**Descrição**: Repete um bloco de comandos N vezes

**Semântica**:
- `<número>` deve ser um inteiro positivo maior que zero
- Comandos internos são executados sequencialmente N vezes
- Permite aninhamento (repeat dentro de repeat)

**Exemplos Simples**:
```docelang
// Adicionar 3 ovos
repeat 3 times {
    add ovo;
}

// Modelar 20 brigadeiros
repeat 20 times {
    add chocolate_granulado;
    serve;
}
```

**Exemplo com Aninhamento**:
```docelang
// Fazer 3 camadas, cada uma com 2 coberturas
repeat 3 times {
    add massa;
    
    repeat 2 times {
        add recheio;
    }
}
```

**Erros comuns**:
```docelang
repeat 0 times { }      // ❌ ERRO: número deve ser > 0
repeat -5 times { }     // ❌ ERRO: número deve ser positivo
repeat 3.5 times { }    // ❌ ERRO: número deve ser inteiro
repeat three times { }  // ❌ ERRO: esperado número, recebido identificador
```

---

## 2.3 Regras Sintáticas Detalhadas

### 2.3.1 Identificadores

**Definição**: Nome dado a receitas e ingredientes

**Regras**:
1. Deve começar com letra (a-z, A-Z)
2. Pode conter letras, dígitos (0-9) e underscore (_)
3. Não pode ser palavra-chave reservada
4. Case-sensitive (Açucar ≠ acucar)

**Regex**: `[a-zA-Z][a-zA-Z0-9_]*`

**Exemplos Válidos**:
```docelang
leite_condensado
chocolate_em_po
acucar_cristal
farinha_de_trigo
ovo1
clara_de_ovo_2
Brigadeiro
BoloDeChocolate
```

**Exemplos Inválidos**:
```docelang
1_leite           // ❌ Começa com número
leite-condensado  // ❌ Contém hífen
leite condensado  // ❌ Contém espaço
add               // ❌ Palavra-chave reservada
_leite            // ⚠️  Tecnicamente válido, mas não recomendado
```

---

### 2.3.2 Palavras-Chave Reservadas

Lista completa de palavras reservadas que **NÃO** podem ser usadas como identificadores:

```
recipe          // Estrutura principal
ingredients     // Bloco de ingredientes
preparation     // Bloco de preparo
add             // Comando adicionar
mix             // Comando misturar
heat            // Comando aquecer
wait            // Comando aguardar
serve           // Comando servir
repeat          // Estrutura de repetição
times           // Parte do repeat
```

**Total**: 10 palavras-chave

---

### 2.3.3 Literais Numéricos

#### Números Inteiros

**Regex**: `[0-9]+`

**Exemplos**:
```docelang
0
1
42
100
1000
```

#### Números Decimais (Opcional - Versão Futura)

**Regex**: `[0-9]+\.[0-9]+`

**Exemplos**:
```docelang
3.14
0.5
2.75
```

---

### 2.3.4 Unidades de Medida

#### Unidades de Tempo

| Unidade | Significado | Exemplo |
|---------|-------------|---------|
| `s`     | segundos    | `30s`   |
| `min`   | minutos     | `15min` |
| `h`     | horas       | `2h`    |

**Sintaxe**: `<número><unidade>`  
**Regex**: `[0-9]+(s|min|h)`

**Exemplos**:
```docelang
30s      // 30 segundos
5min     // 5 minutos
2h       // 2 horas
90min    // 90 minutos (equivale a 1h30min)
```

#### Unidades de Temperatura

| Unidade | Significado        | Exemplo |
|---------|-------------------|---------|
| `C`     | Celsius           | `180C`  |
| `F`     | Fahrenheit        | `350F`  |

**Sintaxe**: `<número><unidade>`  
**Regex**: `[0-9]+(C|F)`

**Exemplos**:
```docelang
100C     // 100 graus Celsius (fervura da água)
180C     // 180 graus Celsius (forno médio)
350F     // 350 graus Fahrenheit (~177C)
```

---

### 2.3.5 Símbolos e Delimitadores

| Símbolo | Uso                          | Exemplo              |
|---------|------------------------------|----------------------|
| `{`     | Abre bloco                   | `recipe Bolo {`      |
| `}`     | Fecha bloco                  | `}`                  |
| `;`     | Termina comando/declaração   | `add leite;`         |
| `//`    | Comentário de linha          | `// Comentário`      |
| `/*`    | Inicia comentário de bloco   | `/* Comentário`      |
| `*/`    | Finaliza comentário de bloco | `Comentário */`      |

---

### 2.3.6 Comentários

#### Comentário de Linha

**Sintaxe**: `// texto`

**Comportamento**: Todo texto após `//` até o fim da linha é ignorado

**Exemplos**:
```docelang
// Esta é uma receita tradicional
add leite;  // 1 xícara de leite
```

#### Comentário de Bloco

**Sintaxe**: `/* texto */`

**Comportamento**: Todo texto entre `/*` e `*/` é ignorado, pode ocupar múltiplas linhas

**Exemplos**:
```docelang
/*
 * Receita: Brigadeiro Gourmet
 * Autor: Chef Ana
 * Data: 2025-11-15
 */

/* Ingrediente opcional */ add coco_ralado;
```

---

## 2.4 Regras Semânticas Básicas

### 2.4.1 Validação de Ingredientes

**Regra 1**: Todo ingrediente usado em `preparation` deve estar declarado em `ingredients`

```docelang
recipe Bolo {
    ingredients {
        farinha;
        acucar;
    }
    
    preparation {
        add farinha;   // ✅ OK - declarado
        add acucar;    // ✅ OK - declarado
        add ovos;      // ❌ ERRO - não declarado
    }
}
```

**Regra 2**: Ingredientes declarados mas não usados geram aviso (warning)

```docelang
recipe Pudim {
    ingredients {
        leite;
        ovos;
        acucar;
        baunilha;  // ⚠️ WARNING - declarado mas não usado
    }
    
    preparation {
        add leite;
        add ovos;
        add acucar;
        // baunilha nunca foi adicionado
    }
}
```

---

### 2.4.2 Validação de Tipos

**Regra 3**: `add` aceita apenas identificadores (ingredientes)

```docelang
add leite;      // ✅ OK
add 5min;       // ❌ ERRO - esperado identificador
add 180C;       // ❌ ERRO - esperado identificador
```

**Regra 4**: `mix` e `wait` aceitam apenas tempos

```docelang
mix 5min;       // ✅ OK
mix 180C;       // ❌ ERRO - esperado tempo
wait 2h;        // ✅ OK
wait farinha;   // ❌ ERRO - esperado tempo
```

**Regra 5**: `heat` aceita apenas temperaturas

```docelang
heat 180C;      // ✅ OK
heat 5min;      // ❌ ERRO - esperado temperatura
heat acucar;    // ❌ ERRO - esperado temperatura
```

---

### 2.4.3 Validação de Valores

**Regra 6**: Números em `repeat` devem ser positivos e inteiros

```docelang
repeat 5 times { }     // ✅ OK
repeat 0 times { }     // ❌ ERRO - deve ser > 0
repeat -3 times { }    // ❌ ERRO - deve ser positivo
repeat 2.5 times { }   // ❌ ERRO - deve ser inteiro
```

**Regra 7**: Temperaturas negativas geram aviso

```docelang
heat 180C;      // ✅ OK
heat -20C;      // ⚠️ WARNING - temperatura negativa (freezer?)
```

**Regra 8**: Tempos devem ser positivos

```docelang
mix 5min;       // ✅ OK
mix 0min;       // ⚠️ WARNING - tempo zero não faz sentido
wait -1h;       // ❌ ERRO - tempo negativo inválido
```

---

### 2.4.4 Validação de Ordem

**Regra 9**: `ingredients` deve preceder `preparation`

```docelang
// ✅ Correto
recipe Bolo {
    ingredients { ... }
    preparation { ... }
}

// ❌ Incorreto
recipe Bolo {
    preparation { ... }
    ingredients { ... }
}
```

**Regra 10**: `serve` deve ser o último comando (boa prática)

```docelang
// ✅ Recomendado
preparation {
    add leite;
    mix 5min;
    serve;
}

// ⚠️ Não recomendado (mas sintaticamente válido)
preparation {
    serve;
    add leite;  // Adicionando depois de servir?
}
```

---

## 2.5 Exemplos Reais de Receitas

### 2.5.1 Exemplo Básico: Brigadeiro Simples

```docelang
/*
 * Receita: Brigadeiro Tradicional
 * Rendimento: 30 unidades
 * Tempo total: ~45 minutos
 */

recipe Brigadeiro {
    ingredients {
        leite_condensado;
        chocolate_em_po;
        manteiga;
        chocolate_granulado;
    }
    
    preparation {
        // Combinar ingredientes base
        add leite_condensado;
        add chocolate_em_po;
        add manteiga;
        
        // Cozinhar em fogo médio, mexendo sempre
        heat 180C;
        mix 15min;
        
        // Esfriar completamente
        wait 2h;
        
        // Modelar brigadeiros
        repeat 30 times {
            add chocolate_granulado;
        }
        
        serve;
    }
}
```

**Análise**:
- ✅ 4 ingredientes declarados
- ✅ 4 ingredientes utilizados
- ✅ Comandos em ordem lógica
- ✅ Tipos corretos em cada comando

---

### 2.5.2 Exemplo Intermediário: Pudim de Leite

```docelang
/*
 * Receita: Pudim de Leite Condensado
 * Rendimento: 8 porções
 * Tempo total: 4 horas (incluindo resfriamento)
 */

recipe Pudim {
    ingredients {
        leite_condensado;
        leite;
        ovos;
        acucar;
        agua;
    }
    
    preparation {
        // Preparar calda
        add acucar;
        add agua;
        heat 200C;
        mix 10min;  // Até caramelizar
        
        // Aguardar esfriar a calda
        wait 5min;
        
        // Preparar mistura do pudim
        add leite_condensado;
        add leite;
        
        // Adicionar ovos um a um
        repeat 3 times {
            add ovos;
            mix 1min;
        }
        
        // Assar em banho-maria
        heat 180C;
        wait 50min;
        
        // Esfriar
        wait 3h;
        
        serve;
    }
}
```

**Análise**:
- ✅ 5 ingredientes declarados
- ✅ 5 ingredientes utilizados
- ✅ Uso de `repeat` para adicionar ovos
- ✅ Sequência lógica: calda → mistura → assar → esfriar

---

### 2.5.3 Exemplo Avançado: Bolo de Cenoura com Cobertura

```docelang
/*
 * Receita: Bolo de Cenoura com Cobertura de Chocolate
 * Rendimento: 12 porções
 * Tempo total: 2 horas
 */

recipe BoloDeCenoura {
    ingredients {
        cenoura;
        ovos;
        oleo;
        acucar;
        farinha_de_trigo;
        fermento_em_po;
        chocolate_em_po;
        manteiga;
        leite;
    }
    
    preparation {
        // ========== MASSA ==========
        
        // Bater no liquidificador
        add cenoura;
        add ovos;
        add oleo;
        add acucar;
        mix 3min;
        
        // Adicionar ingredientes secos
        add farinha_de_trigo;
        add fermento_em_po;
        mix 2min;
        
        // Assar
        heat 180C;
        wait 40min;
        
        // Esfriar
        wait 30min;
        
        // ========== COBERTURA ==========
        
        // Preparar ganache
        add chocolate_em_po;
        add manteiga;
        add leite;
        
        // Aquecer até derreter
        heat 150C;
        mix 5min;
        
        // Despejar sobre o bolo
        wait 15min;  // Deixar firmar
        
        serve;
    }
}
```

**Análise**:
- ✅ 9 ingredientes declarados e utilizados
- ✅ Receita complexa com duas partes (massa e cobertura)
- ✅ Comentários organizando seções
- ✅ Sequência lógica e realista

---

### 2.5.4 Exemplo com Repetições Aninhadas: Petit Gateau

```docelang
/*
 * Receita: Petit Gateau (Porções Individuais)
 * Rendimento: 4 unidades
 */

recipe PetitGateau {
    ingredients {
        chocolate_meio_amargo;
        manteiga;
        ovos;
        gemas;
        acucar;
        farinha_de_trigo;
        manteiga_para_untar;
        acucar_para_polvilhar;
    }
    
    preparation {
        // Preparar forminhas individuais
        repeat 4 times {
            add manteiga_para_untar;
            add acucar_para_polvilhar;
        }
        
        // Derreter chocolate com manteiga
        add chocolate_meio_amargo;
        add manteiga;
        heat 150C;
        mix 3min;
        
        // Preparar massa
        add ovos;
        add gemas;
        add acucar;
        mix 5min;
        
        // Incorporar chocolate derretido
        mix 2min;
        
        add farinha_de_trigo;
        mix 1min;
        
        // Distribuir nas forminhas e assar
        heat 200C;
        wait 8min;  // Deixar centro mole
        
        serve;
    }
}
```

**Análise**:
- ✅ 8 ingredientes utilizados
- ✅ `repeat` para preparar múltiplas forminhas
- ✅ Tempo preciso (8min) crucial para textura
- ✅ Receita profissional e realista

---

### 2.5.5 Exemplo Minimalista: Doce de Leite Caseiro

```docelang
// Receita mais simples possível
recipe DoceDeLeite {
    ingredients {
        leite;
        acucar;
    }
    
    preparation {
        add leite;
        add acucar;
        heat 150C;
        mix 120min;  // 2 horas mexendo
        serve;
    }
}
```

**Análise**:
- ✅ Apenas 2 ingredientes
- ✅ Sequência linear simples
- ✅ Demonstra sintaxe mínima válida

---

## 2.6 Tabela Resumo de Comandos

| Comando | Parâmetro | Tipo | Exemplo | Descrição |
|---------|-----------|------|---------|-----------|
| `add` | ingrediente | IDENTIFICADOR | `add leite;` | Adiciona ingrediente |
| `mix` | tempo | TEMPO | `mix 5min;` | Mistura por tempo |
| `heat` | temperatura | TEMPERATURA | `heat 180C;` | Aquece a temperatura |
| `wait` | tempo | TEMPO | `wait 2h;` | Aguarda tempo |
| `serve` | - | - | `serve;` | Finaliza receita |
| `repeat` | número + bloco | INTEIRO + COMANDOS | `repeat 3 times { }` | Repete comandos |

---

## 2.7 Tabela de Unidades Suportadas

### Unidades de Tempo

| Unidade | Nome | Conversão para segundos |
|---------|------|------------------------|
| `s` | segundos | 1 |
| `min` | minutos | 60 |
| `h` | horas | 3600 |

**Exemplos**:
- `30s` = 30 segundos
- `5min` = 300 segundos
- `2h` = 7200 segundos

### Unidades de Temperatura

| Unidade | Nome | Fórmula de Conversão |
|---------|------|---------------------|
| `C` | Celsius | - |
| `F` | Fahrenheit | (F - 32) × 5/9 = C |

**Exemplos**:
- `100C` = ponto de ebulição da água
- `180C` = forno médio
- `350F` ≈ 177C

---

## 2.8 Mensagens de Erro Típicas

### Erros Léxicos

```
ERRO LÉXICO: Token inválido 'leite-condensado' na linha 5
Sugestão: Use underscore: 'leite_condensado'
```

### Erros Sintáticos

```
ERRO SINTÁTICO: Esperado ';' após 'add leite' na linha 12
```

```
ERRO SINTÁTICO: Esperado identificador após 'recipe' na linha 1
```

### Erros Semânticos

```
ERRO SEMÂNTICO: Ingrediente 'farinha' não declarado em 'ingredients' (linha 18)
```

```
ERRO SEMÂNTICO: Tipo incompatível - esperado TEMPO, recebido TEMPERATURA em 'mix 180C' (linha 15)
```

```
WARNING: Ingrediente 'baunilha' declarado mas nunca utilizado
```

---

## 2.9 Casos Especiais e Edge Cases

### 2.9.1 Receita Vazia (Inválida)

```docelang
recipe Vazio {
    ingredients {
    }
    
    preparation {
    }
}
```
❌ **ERRO**: Receita deve ter pelo menos 1 ingrediente e 1 comando

---

### 2.9.2 Ingrediente Usado Múltiplas Vezes (Válido)

```docelang
recipe BoloCamadas {
    ingredients {
        massa;
        recheio;
    }
    
    preparation {
        add massa;
        add recheio;
        add massa;    // ✅ OK - reutilizar ingrediente
        add recheio;
        add massa;
        serve;
    }
}
```

---

### 2.9.3 Repeat com N=1 (Válido mas Desnecessário)

```docelang
repeat 1 times {
    add ovo;
}
```
⚠️ **WARNING**: `repeat 1 times` é desnecessário, use comando direto

---

### 2.9.4 Blocos Vazios no Repeat (Inválido)

```docelang
repeat 5 times {
    // Nada aqui
}
```
❌ **ERRO**: Bloco do repeat não pode estar vazio

---

## 2.10 Próximos Passos

Esta especificação completa define todos os aspectos sintáticos e semânticos básicos da DoceLang. O próximo documento apresentará a **Gramática Formal** em notação BNF e EBNF.

**Próximo**: [3. Gramática Formal (BNF e EBNF) →](03-gramatica.md)
