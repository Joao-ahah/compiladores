# 4. Análise Léxica (Tokens) da DoceLang

## 4.1 Introdução à Análise Léxica

O **analisador léxico** (lexer ou scanner) é a primeira fase do compilador. Ele recebe o código-fonte como entrada e produz uma sequência de **tokens** como saída.

### 4.1.1 Função do Lexer

```
Código-fonte (string) → LEXER → Sequência de Tokens → PARSER
```

**Responsabilidades**:
1. Dividir o código em unidades significativas (tokens)
2. Classificar cada token por tipo
3. Ignorar espaços em branco e comentários
4. Detectar erros léxicos
5. Manter rastreamento de posição (linha/coluna)

---

## 4.2 Lista Completa de Tokens

### 4.2.1 Tabela de Tokens

| ID | Nome do Token | Tipo | Exemplo | Regex/Padrão |
|----|---------------|------|---------|--------------|
| 1 | `RECIPE` | Palavra-chave | `recipe` | `recipe` |
| 2 | `INGREDIENTS` | Palavra-chave | `ingredients` | `ingredients` |
| 3 | `PREPARATION` | Palavra-chave | `preparation` | `preparation` |
| 4 | `ADD` | Palavra-chave | `add` | `add` |
| 5 | `MIX` | Palavra-chave | `mix` | `mix` |
| 6 | `HEAT` | Palavra-chave | `heat` | `heat` |
| 7 | `WAIT` | Palavra-chave | `wait` | `wait` |
| 8 | `SERVE` | Palavra-chave | `serve` | `serve` |
| 9 | `REPEAT` | Palavra-chave | `repeat` | `repeat` |
| 10 | `TIMES` | Palavra-chave | `times` | `times` |
| 11 | `LBRACE` | Delimitador | `{` | `\{` |
| 12 | `RBRACE` | Delimitador | `}` | `\}` |
| 13 | `SEMICOLON` | Delimitador | `;` | `;` |
| 14 | `IDENTIFIER` | Identificador | `leite_condensado` | `[a-zA-Z][a-zA-Z0-9_]*` |
| 15 | `TIME` | Literal | `5min` | `[0-9]+(s\|min\|h)` |
| 16 | `TEMPERATURE` | Literal | `180C` | `[0-9]+(C\|F)` |
| 17 | `NUMBER` | Literal | `42` | `[0-9]+` |
| 18 | `COMMENT_LINE` | Comentário | `// texto` | `//.*` |
| 19 | `COMMENT_BLOCK` | Comentário | `/* texto */` | `/\*(.|\n)*?\*/` |
| 20 | `WHITESPACE` | Espaço | ` `, `\t`, `\n` | `[ \t\n\r]+` |
| 21 | `EOF` | Fim de arquivo | - | - |

**Total**: 21 tipos de tokens

---

## 4.3 Expressões Regulares Detalhadas

### 4.3.1 Palavras-Chave (Keywords)

```regex
RECIPE       = recipe
INGREDIENTS  = ingredients
PREPARATION  = preparation
ADD          = add
MIX          = mix
HEAT         = heat
WAIT         = wait
SERVE        = serve
REPEAT       = repeat
TIMES        = times
```

**Observações**:
- Case-sensitive (apenas minúsculas)
- Têm prioridade sobre identificadores
- Não podem ser usadas como nomes de variáveis/ingredientes

---

### 4.3.2 Identificadores

```regex
IDENTIFIER = [a-zA-Z][a-zA-Z0-9_]*
```

**Descrição**: Letra seguida de zero ou mais letras, dígitos ou underscores

**Exemplos válidos**:
```
leite_condensado    ✅
chocolate_em_po     ✅
acucar              ✅
Brigadeiro          ✅
ingrediente123      ✅
_privado            ✅ (tecnicamente válido)
```

**Exemplos inválidos**:
```
1_ingrediente       ❌ (começa com dígito)
ingrediente-nome    ❌ (contém hífen)
açúcar              ❌ (contém acento)
leite condensado    ❌ (contém espaço)
add                 ❌ (palavra-chave reservada)
```

**Diagrama de Estados (AFD)**:

```
       letra
(q0) --------> ((q1))
               |   ^
               |   |
               +---+
          letra|dígito|_
```

---

### 4.3.3 Números

```regex
NUMBER = [0-9]+
```

**Descrição**: Uma ou mais dígitos decimais

**Exemplos**:
```
0       ✅
42      ✅
180     ✅
1000    ✅
```

**Exemplos inválidos**:
```
3.14    ❌ (ponto decimal - versão futura)
-5      ❌ (sinal negativo - tratado separadamente)
0x1F    ❌ (hexadecimal - não suportado)
```

**Diagrama de Estados (AFD)**:

```
       dígito
(q0) --------> ((q1))
                |  ^
                |  |
                +--+
               dígito
```

---

### 4.3.4 Tempo

```regex
TIME = [0-9]+(s|min|h)
```

**Descrição**: Número seguido de unidade de tempo

**Componentes**:
- `[0-9]+` - parte numérica
- `(s|min|h)` - unidade de tempo

**Exemplos**:
```
30s      ✅ (30 segundos)
5min     ✅ (5 minutos)
2h       ✅ (2 horas)
90min    ✅ (90 minutos)
```

**Exemplos inválidos**:
```
5        ❌ (falta unidade)
min      ❌ (falta número)
5m       ❌ (unidade inválida, use 'min')
5 min    ❌ (espaço não permitido)
```

**Diagrama de Estados (AFD)**:

```
       dígito        s
(q0) --------> (q1) ----> ((q2))
                |
                | m
                +----> (q3) ----> ((q5))
                         i        n
                      
                | h
                +----> ((q6))
```

---

### 4.3.5 Temperatura

```regex
TEMPERATURE = [0-9]+(C|F)
```

**Descrição**: Número seguido de unidade de temperatura

**Componentes**:
- `[0-9]+` - parte numérica
- `(C|F)` - unidade de temperatura

**Exemplos**:
```
100C     ✅ (100 graus Celsius)
180C     ✅ (180 graus Celsius)
350F     ✅ (350 graus Fahrenheit)
```

**Exemplos inválidos**:
```
180      ❌ (falta unidade)
C        ❌ (falta número)
180c     ❌ (case-sensitive, use 'C' maiúsculo)
180 C    ❌ (espaço não permitido)
```

**Diagrama de Estados (AFD)**:

```
       dígito        C
(q0) --------> (q1) ----> ((q2))
                |
                | F
                +----> ((q3))
```

---

### 4.3.6 Delimitadores

```regex
LBRACE    = \{
RBRACE    = \}
SEMICOLON = ;
```

**Exemplos**:
```
{    ✅ LBRACE
}    ✅ RBRACE
;    ✅ SEMICOLON
```

---

### 4.3.7 Comentários

#### Comentário de Linha

```regex
COMMENT_LINE = //.*
```

**Descrição**: `//` seguido de qualquer caractere até o fim da linha

**Exemplos**:
```
// Este é um comentário              ✅
add leite; // Adicionar leite        ✅
//                                   ✅ (comentário vazio)
```

#### Comentário de Bloco

```regex
COMMENT_BLOCK = /\*(.|\n)*?\*/
```

**Descrição**: `/*` seguido de qualquer caractere (incluindo quebras de linha) até `*/`

**Observação**: Usa matching não-guloso (`*?`) para parar no primeiro `*/`

**Exemplos**:
```
/* comentário simples */                          ✅

/*
 * Comentário
 * multi-linha
 */                                                ✅

/* /* comentários aninhados? */ */                ⚠️  (primeiro */ fecha)
```

**Problema com Aninhamento**:
```
/* comentário /* aninhado */ ainda comentário? */
                            ^--- FECHA AQUI
```

DoceLang **NÃO suporta** comentários aninhados. O primeiro `*/` sempre fecha.

---

### 4.3.8 Espaços em Branco

```regex
WHITESPACE = [ \t\n\r]+
```

**Descrição**: Um ou mais caracteres de espaço, tab, nova linha ou retorno de carro

**Componentes**:
- ` ` (espaço)
- `\t` (tab)
- `\n` (nova linha - Unix/Linux)
- `\r` (retorno de carro - Windows)

**Comportamento**: Ignorado pelo lexer (não gera token)

---

## 4.4 Ordem de Prioridade (Precedência)

Quando múltiplos padrões podem casar, a ordem importa:

1. **Palavras-chave** (antes de identificadores)
   ```
   "recipe" → TOKEN: RECIPE (não IDENTIFIER)
   ```

2. **Literais específicos** (antes de número genérico)
   ```
   "5min" → TOKEN: TIME (não NUMBER seguido de IDENTIFIER)
   ```

3. **Identificadores** (última opção para texto)
   ```
   "leite" → TOKEN: IDENTIFIER
   ```

### Tabela de Precedência

| Ordem | Padrão | Tipo |
|-------|--------|------|
| 1 | Comentários | COMMENT_LINE, COMMENT_BLOCK |
| 2 | Palavras-chave | RECIPE, ADD, MIX, etc. |
| 3 | Tempo | TIME |
| 4 | Temperatura | TEMPERATURE |
| 5 | Número | NUMBER |
| 6 | Identificador | IDENTIFIER |
| 7 | Delimitadores | {, }, ; |
| 8 | Espaço | WHITESPACE (ignorado) |

---

## 4.5 Exemplos de Tokenização

### 4.5.1 Exemplo Simples

**Entrada**:
```docelang
recipe Brigadeiro {
    ingredients {
        leite_condensado;
    }
}
```

**Saída (Tokens)**:
```
1. RECIPE          "recipe"              (linha 1, coluna 1)
2. IDENTIFIER      "Brigadeiro"          (linha 1, coluna 8)
3. LBRACE          "{"                   (linha 1, coluna 19)
4. INGREDIENTS     "ingredients"         (linha 2, coluna 5)
5. LBRACE          "{"                   (linha 2, coluna 18)
6. IDENTIFIER      "leite_condensado"    (linha 3, coluna 9)
7. SEMICOLON       ";"                   (linha 3, coluna 26)
8. RBRACE          "}"                   (linha 4, coluna 5)
9. RBRACE          "}"                   (linha 5, coluna 1)
10. EOF                                  (linha 5, coluna 2)
```

---

### 4.5.2 Exemplo com Comandos

**Entrada**:
```docelang
preparation {
    add leite;
    mix 5min;
    heat 180C;
}
```

**Saída (Tokens)**:
```
1. PREPARATION     "preparation"         (linha 1, coluna 1)
2. LBRACE          "{"                   (linha 1, coluna 13)
3. ADD             "add"                 (linha 2, coluna 5)
4. IDENTIFIER      "leite"               (linha 2, coluna 9)
5. SEMICOLON       ";"                   (linha 2, coluna 14)
6. MIX             "mix"                 (linha 3, coluna 5)
7. TIME            "5min"                (linha 3, coluna 9)
8. SEMICOLON       ";"                   (linha 3, coluna 13)
9. HEAT            "heat"                (linha 4, coluna 5)
10. TEMPERATURE    "180C"                (linha 4, coluna 10)
11. SEMICOLON      ";"                   (linha 4, coluna 14)
12. RBRACE         "}"                   (linha 5, coluna 1)
13. EOF                                  (linha 5, coluna 2)
```

---

### 4.5.3 Exemplo com Repeat

**Entrada**:
```docelang
repeat 3 times {
    add ovo;
}
```

**Saída (Tokens)**:
```
1. REPEAT          "repeat"              (linha 1, coluna 1)
2. NUMBER          "3"                   (linha 1, coluna 8)
3. TIMES           "times"               (linha 1, coluna 10)
4. LBRACE          "{"                   (linha 1, coluna 16)
5. ADD             "add"                 (linha 2, coluna 5)
6. IDENTIFIER      "ovo"                 (linha 2, coluna 9)
7. SEMICOLON       ";"                   (linha 2, coluna 12)
8. RBRACE          "}"                   (linha 3, coluna 1)
9. EOF                                   (linha 3, coluna 2)
```

---

### 4.5.4 Exemplo com Comentários

**Entrada**:
```docelang
// Receita tradicional
recipe Pudim { /* calda e pudim */
    ingredients {
        acucar;  // para a calda
    }
}
```

**Saída (Tokens)** (comentários ignorados):
```
1. RECIPE          "recipe"              (linha 2, coluna 1)
2. IDENTIFIER      "Pudim"               (linha 2, coluna 8)
3. LBRACE          "{"                   (linha 2, coluna 14)
4. INGREDIENTS     "ingredients"         (linha 3, coluna 5)
5. LBRACE          "{"                   (linha 3, coluna 18)
6. IDENTIFIER      "acucar"              (linha 4, coluna 9)
7. SEMICOLON       ";"                   (linha 4, coluna 15)
8. RBRACE          "}"                   (linha 5, coluna 5)
9. RBRACE          "}"                   (linha 6, coluna 1)
10. EOF                                  (linha 6, coluna 2)
```

---

## 4.6 Ambiguidades e Resoluções

### 4.6.1 Palavra-chave vs Identificador

**Problema**: "add" pode ser palavra-chave ou identificador?

**Resolução**: Palavras-chave têm prioridade

```
"add"      → KEYWORD: ADD       ✅
"additive" → IDENTIFIER         ✅ (não é palavra-chave exata)
```

**Implementação**:
```python
keywords = {
    'recipe', 'ingredients', 'preparation',
    'add', 'mix', 'heat', 'wait', 'serve',
    'repeat', 'times'
}

def tokenize_word(word):
    if word in keywords:
        return Token(KEYWORD, word)
    else:
        return Token(IDENTIFIER, word)
```

---

### 4.6.2 Tempo vs Número + Identificador

**Problema**: "5min" é um token ou dois?

**Resolução**: Matching guloso (greedy) - pega o maior token possível

```
"5min" → TIME: "5min"           ✅ (um token)
NOT:
"5"    → NUMBER: "5"            ❌
"min"  → IDENTIFIER: "min"      ❌
```

**Implementação**: Regex para TIME deve ser testada antes de NUMBER

---

### 4.6.3 Temperatura vs Identificador

**Problema**: Distinguir "180C" de "180" + "C"

**Resolução**: Mesmo que acima - matching guloso

```
"180C"      → TEMPERATURE: "180C"    ✅
"180Celsius" → NUMBER: "180" + IDENTIFIER: "Celsius" (dois tokens)
```

**Observação**: "C" e "F" sozinhos são identificadores:

```
"C"    → IDENTIFIER: "C"        ✅
"180C" → TEMPERATURE: "180C"    ✅
```

---

### 4.6.4 Comentário vs Divisão

**Problema**: Em linguagens com operador `/`, distinguir `/` de `//`

**Resolução**: DoceLang não tem operador de divisão, então não há ambiguidade

```
"//"   → COMMENT_LINE    ✅
"/"    → ERRO LÉXICO     ❌ (caractere inválido)
```

---

### 4.6.5 Underscore Inicial

**Problema**: "_ingrediente" é válido?

**Resolução**: Tecnicamente válido pela regex, mas não recomendado

```regex
[a-zA-Z][a-zA-Z0-9_]*   ← padrão atual (NÃO permite _ inicial)
```

**Decisão de design**: Underscore inicial PROIBIDO (seguindo convenção de linguagens mainstream)

```
"_ingrediente" → ERRO: Identificador não pode começar com underscore
```

**Se fosse permitido**:
```regex
[a-zA-Z_][a-zA-Z0-9_]*   ← alternativa (permite _ inicial)
```

---

## 4.7 Tratamento de Erros Léxicos

### 4.7.1 Caracteres Inválidos

**Erro**: Caractere não reconhecido por nenhum padrão

**Exemplo**:
```docelang
add leite@condensado;
          ^--- ERRO
```

**Mensagem**:
```
ERRO LÉXICO: Caractere inválido '@' na linha 1, coluna 10
```

---

### 4.7.2 Comentário Não Fechado

**Erro**: `/*` sem `*/` correspondente

**Exemplo**:
```docelang
/* Este comentário nunca termina
recipe Bolo {
    ...
```

**Mensagem**:
```
ERRO LÉXICO: Comentário de bloco não fechado (iniciado na linha 1)
```

---

### 4.7.3 Identificador Começando com Dígito

**Erro**: Identificador inicia com número

**Exemplo**:
```docelang
ingredients {
    1_leite;
}
```

**Mensagem**:
```
ERRO LÉXICO: Identificador '1_leite' não pode começar com dígito (linha 2, coluna 5)
Sugestão: Use 'leite1' ou 'leite_1'
```

---

### 4.7.4 Caracteres Especiais

**Erro**: Acentuação ou caracteres não-ASCII

**Exemplo**:
```docelang
ingredients {
    açúcar;
}
```

**Mensagem**:
```
ERRO LÉXICO: Caractere inválido 'ç' na linha 2, coluna 6
Sugestão: Use apenas caracteres ASCII (a-z, A-Z, 0-9, _)
```

---

## 4.8 Estrutura de Token

### 4.8.1 Classe Token (Python)

```python
class Token:
    def __init__(self, type, value, line, column):
        self.type = type        # Tipo do token (ex: IDENTIFIER, NUMBER)
        self.value = value      # Valor literal (ex: "leite", "42")
        self.line = line        # Linha no código-fonte
        self.column = column    # Coluna no código-fonte
    
    def __repr__(self):
        return f"Token({self.type}, '{self.value}', {self.line}:{self.column})"
```

**Exemplo de uso**:
```python
token = Token('IDENTIFIER', 'leite_condensado', 3, 9)
print(token)
# Saída: Token(IDENTIFIER, 'leite_condensado', 3:9)
```

---

### 4.8.2 Enumeração de Tipos

```python
from enum import Enum

class TokenType(Enum):
    # Palavras-chave
    RECIPE = 'RECIPE'
    INGREDIENTS = 'INGREDIENTS'
    PREPARATION = 'PREPARATION'
    ADD = 'ADD'
    MIX = 'MIX'
    HEAT = 'HEAT'
    WAIT = 'WAIT'
    SERVE = 'SERVE'
    REPEAT = 'REPEAT'
    TIMES = 'TIMES'
    
    # Delimitadores
    LBRACE = 'LBRACE'
    RBRACE = 'RBRACE'
    SEMICOLON = 'SEMICOLON'
    
    # Literais
    IDENTIFIER = 'IDENTIFIER'
    NUMBER = 'NUMBER'
    TIME = 'TIME'
    TEMPERATURE = 'TEMPERATURE'
    
    # Especiais
    EOF = 'EOF'
```

---

## 4.9 Implementação do Lexer

### 4.9.1 Algoritmo Básico

```python
def tokenize(source_code):
    tokens = []
    position = 0
    line = 1
    column = 1
    
    while position < len(source_code):
        # Ignorar espaços em branco
        if source_code[position].isspace():
            if source_code[position] == '\n':
                line += 1
                column = 1
            else:
                column += 1
            position += 1
            continue
        
        # Tentar casar padrões (ordem de precedência)
        matched = False
        
        for pattern, token_type in PATTERNS:
            match = pattern.match(source_code, position)
            if match:
                value = match.group(0)
                tokens.append(Token(token_type, value, line, column))
                position = match.end()
                column += len(value)
                matched = True
                break
        
        if not matched:
            raise LexicalError(f"Caractere inválido '{source_code[position]}' "
                             f"na linha {line}, coluna {column}")
    
    tokens.append(Token(TokenType.EOF, '', line, column))
    return tokens
```

---

### 4.9.2 Padrões Regex em Python

```python
import re

PATTERNS = [
    # Comentários (primeiro, para ignorar)
    (re.compile(r'//.*'), TokenType.COMMENT_LINE),
    (re.compile(r'/\*.*?\*/', re.DOTALL), TokenType.COMMENT_BLOCK),
    
    # Palavras-chave (antes de identificadores)
    (re.compile(r'\brecipe\b'), TokenType.RECIPE),
    (re.compile(r'\bingredients\b'), TokenType.INGREDIENTS),
    (re.compile(r'\bpreparation\b'), TokenType.PREPARATION),
    (re.compile(r'\badd\b'), TokenType.ADD),
    (re.compile(r'\bmix\b'), TokenType.MIX),
    (re.compile(r'\bheat\b'), TokenType.HEAT),
    (re.compile(r'\bwait\b'), TokenType.WAIT),
    (re.compile(r'\bserve\b'), TokenType.SERVE),
    (re.compile(r'\brepeat\b'), TokenType.REPEAT),
    (re.compile(r'\btimes\b'), TokenType.TIMES),
    
    # Literais (antes de número genérico)
    (re.compile(r'\d+(s|min|h)'), TokenType.TIME),
    (re.compile(r'\d+(C|F)'), TokenType.TEMPERATURE),
    (re.compile(r'\d+'), TokenType.NUMBER),
    
    # Identificadores
    (re.compile(r'[a-zA-Z][a-zA-Z0-9_]*'), TokenType.IDENTIFIER),
    
    # Delimitadores
    (re.compile(r'\{'), TokenType.LBRACE),
    (re.compile(r'\}'), TokenType.RBRACE),
    (re.compile(r';'), TokenType.SEMICOLON),
]
```

**Observação**: `\b` indica word boundary (fronteira de palavra)

---

## 4.10 Testes do Lexer

### 4.10.1 Teste 1: Programa Mínimo

**Entrada**:
```docelang
recipe A { ingredients { b; } preparation { serve; } }
```

**Saída Esperada**:
```python
[
    Token(RECIPE, 'recipe', 1, 1),
    Token(IDENTIFIER, 'A', 1, 8),
    Token(LBRACE, '{', 1, 10),
    Token(INGREDIENTS, 'ingredients', 1, 12),
    Token(LBRACE, '{', 1, 24),
    Token(IDENTIFIER, 'b', 1, 26),
    Token(SEMICOLON, ';', 1, 27),
    Token(RBRACE, '}', 1, 29),
    Token(PREPARATION, 'preparation', 1, 31),
    Token(LBRACE, '{', 1, 43),
    Token(SERVE, 'serve', 1, 45),
    Token(SEMICOLON, ';', 1, 50),
    Token(RBRACE, '}', 1, 52),
    Token(RBRACE, '}', 1, 54),
    Token(EOF, '', 1, 55)
]
```

---

### 4.10.2 Teste 2: Todos os Tipos de Comandos

**Entrada**:
```docelang
add leite;
mix 5min;
heat 180C;
wait 2h;
serve;
repeat 3 times { }
```

**Saída Esperada**:
```python
# Linha 1
Token(ADD, 'add', 1, 1)
Token(IDENTIFIER, 'leite', 1, 5)
Token(SEMICOLON, ';', 1, 10)

# Linha 2
Token(MIX, 'mix', 2, 1)
Token(TIME, '5min', 2, 5)
Token(SEMICOLON, ';', 2, 9)

# Linha 3
Token(HEAT, 'heat', 3, 1)
Token(TEMPERATURE, '180C', 3, 6)
Token(SEMICOLON, ';', 3, 10)

# Linha 4
Token(WAIT, 'wait', 4, 1)
Token(TIME, '2h', 4, 6)
Token(SEMICOLON, ';', 4, 8)

# Linha 5
Token(SERVE, 'serve', 5, 1)
Token(SEMICOLON, ';', 5, 6)

# Linha 6
Token(REPEAT, 'repeat', 6, 1)
Token(NUMBER, '3', 6, 8)
Token(TIMES, 'times', 6, 10)
Token(LBRACE, '{', 6, 16)
Token(RBRACE, '}', 6, 18)
```

---

### 4.10.3 Teste 3: Identificadores Complexos

**Entrada**:
```docelang
leite_condensado
chocolate_em_po
acucar_cristal_fino
IngredienteA
ingrediente123
_invalido
```

**Saída Esperada**:
```python
Token(IDENTIFIER, 'leite_condensado', 1, 1)      ✅
Token(IDENTIFIER, 'chocolate_em_po', 2, 1)       ✅
Token(IDENTIFIER, 'acucar_cristal_fino', 3, 1)   ✅
Token(IDENTIFIER, 'IngredienteA', 4, 1)          ✅
Token(IDENTIFIER, 'ingrediente123', 5, 1)        ✅
ERRO: '_invalido' - underscore inicial           ❌
```

---

## 4.11 Otimizações do Lexer

### 4.11.1 Lookahead Mínimo

DoceLang requer apenas **1 caractere de lookahead** para a maioria dos tokens.

**Exceções**:
- Comentários: `//` e `/*` requerem 2 caracteres
- Unidades: `min` requer até 3 caracteres

---

### 4.11.2 Tabela de Símbolos Preliminar

Durante análise léxica, podemos construir uma tabela de símbolos inicial:

```python
symbol_table = {
    'leite_condensado': {'type': 'ingredient', 'first_use': (3, 9)},
    'chocolate_em_po': {'type': 'ingredient', 'first_use': (4, 9)},
    'Brigadeiro': {'type': 'recipe_name', 'first_use': (1, 8)},
}
```

---

## 4.12 Tabela Resumo de Regex

| Token | Regex | Exemplo | Observações |
|-------|-------|---------|-------------|
| Palavra-chave | `\b(recipe\|add\|...)\b` | `recipe` | Case-sensitive |
| Identificador | `[a-zA-Z][a-zA-Z0-9_]*` | `leite_123` | Sem _ inicial |
| Número | `[0-9]+` | `42` | Apenas inteiros |
| Tempo | `[0-9]+(s\|min\|h)` | `5min` | Sem espaço |
| Temperatura | `[0-9]+(C\|F)` | `180C` | Case-sensitive |
| Comentário linha | `//.*` | `// texto` | Até fim da linha |
| Comentário bloco | `/\*(.|\n)*?\*/` | `/* texto */` | Não-guloso |
| Espaço | `[ \t\n\r]+` | ` ` | Ignorado |

---

## 4.13 Conclusão da Análise Léxica

O analisador léxico da DoceLang é:
- ✅ **Simples**: 21 tipos de tokens
- ✅ **Determinístico**: Sem ambiguidades
- ✅ **Eficiente**: Pode ser implementado com AFDs
- ✅ **Robusto**: Tratamento de erros claro
- ✅ **Extensível**: Fácil adicionar novos tokens

**Próximo**: [5. Exemplos de Programas →](05-exemplos.md)
