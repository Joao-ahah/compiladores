# 7. Análise do Lexer Usado no Laboratório

## 7.1 Introdução

Este documento analisa o tipo de gramática usada em analisadores léxicos típicos e como adaptar o lexer trabalhado em laboratório para a linguagem DoceLang.

---

## 7.2 Tipo de Gramática Usada no Lexer

### 7.2.1 Gramática Regular (Tipo 3)

**Analisadores léxicos utilizam Gramáticas Regulares (Tipo 3 de Chomsky)**

**Características**:
- Reconhecidas por **Autômatos Finitos** (AF ou DFA/NFA)
- Mais simples que gramáticas livres de contexto
- Produção sempre da forma: `A → aB` ou `A → a`
- **Não têm pilha** - apenas estados e transições

---

### 7.2.2 Hierarquia de Chomsky

```
Tipo 0: Recursivamente Enumerável
   ↑
Tipo 1: Sensível ao Contexto
   ↑
Tipo 2: Livre de Contexto (PARSER usa isso)
   ↑
Tipo 3: Regular (LEXER usa isso) ← DoceLang Lexer
```

**Por que Lexer usa Tipo 3?**
- Tokens são padrões simples (identificadores, números, palavras-chave)
- Não precisam de estrutura aninhada
- AFDs são muito eficientes (O(n) linear)

---

### 7.2.3 Exemplo: Identificador como Gramática Regular

**Gramática Regular para IDENTIFIER**:
```
<identificador> ::= letra <resto>
<resto> ::= letra <resto>
          | digito <resto>
          | _ <resto>
          | ε
```

**Equivalente em Regex**:
```regex
[a-zA-Z][a-zA-Z0-9_]*
```

**Autômato Finito Determinístico (AFD)**:
```
       letra
(q0) --------> ((q1))
               |   ^
               |   |
               +---+
          letra|dígito|_
```

---

## 7.3 Lexer Trabalhado em Laboratório

### 7.3.1 Estrutura Típica (Exemplo em C)

```c
// lexer.c - Estrutura típica de laboratório

typedef enum {
    TOKEN_KEYWORD,
    TOKEN_IDENTIFIER,
    TOKEN_NUMBER,
    TOKEN_OPERATOR,
    TOKEN_DELIMITER,
    TOKEN_EOF
} TokenType;

typedef struct {
    TokenType type;
    char lexeme[256];
    int line;
    int column;
} Token;

Token getNextToken(char *source, int *position) {
    // Pular espaços em branco
    while (isspace(source[*position])) {
        (*position)++;
    }
    
    // EOF
    if (source[*position] == '\0') {
        return createToken(TOKEN_EOF, "", line, col);
    }
    
    // Identificadores e palavras-chave
    if (isalpha(source[*position])) {
        return scanIdentifier(source, position);
    }
    
    // Números
    if (isdigit(source[*position])) {
        return scanNumber(source, position);
    }
    
    // Delimitadores
    if (source[*position] == '{' || source[*position] == '}' || ...) {
        return createToken(TOKEN_DELIMITER, ...);
    }
    
    // Erro
    error("Caractere inválido");
}
```

---

### 7.3.2 Funções Auxiliares Típicas

```c
Token scanIdentifier(char *source, int *pos) {
    char buffer[256];
    int i = 0;
    
    // Primeiro caractere: letra
    buffer[i++] = source[(*pos)++];
    
    // Resto: letra | dígito | _
    while (isalnum(source[*pos]) || source[*pos] == '_') {
        buffer[i++] = source[(*pos)++];
    }
    buffer[i] = '\0';
    
    // Verificar se é palavra-chave
    if (isKeyword(buffer)) {
        return createToken(TOKEN_KEYWORD, buffer, ...);
    }
    
    return createToken(TOKEN_IDENTIFIER, buffer, ...);
}

Token scanNumber(char *source, int *pos) {
    char buffer[256];
    int i = 0;
    
    while (isdigit(source[*pos])) {
        buffer[i++] = source[(*pos)++];
    }
    buffer[i] = '\0';
    
    return createToken(TOKEN_NUMBER, buffer, ...);
}
```

---

## 7.4 Adaptação para DoceLang

### 7.4.1 Mudanças Necessárias

#### 1. Adicionar Novos Tipos de Token

```c
typedef enum {
    // Palavras-chave
    TOKEN_RECIPE,
    TOKEN_INGREDIENTS,
    TOKEN_PREPARATION,
    TOKEN_ADD,
    TOKEN_MIX,
    TOKEN_HEAT,
    TOKEN_WAIT,
    TOKEN_SERVE,
    TOKEN_REPEAT,
    TOKEN_TIMES,
    
    // Literais
    TOKEN_IDENTIFIER,
    TOKEN_NUMBER,
    TOKEN_TIME,          // ← NOVO!
    TOKEN_TEMPERATURE,   // ← NOVO!
    
    // Delimitadores
    TOKEN_LBRACE,
    TOKEN_RBRACE,
    TOKEN_SEMICOLON,
    
    TOKEN_EOF
} TokenType;
```

---

#### 2. Função para Reconhecer TEMPO

```c
Token scanTime(char *source, int *pos) {
    char buffer[256];
    int i = 0;
    
    // Parte numérica
    while (isdigit(source[*pos])) {
        buffer[i++] = source[(*pos)++];
    }
    
    // Unidade de tempo
    if (source[*pos] == 's') {
        buffer[i++] = source[(*pos)++];
    } else if (source[*pos] == 'm' && source[*pos+1] == 'i' && source[*pos+2] == 'n') {
        buffer[i++] = source[(*pos)++];
        buffer[i++] = source[(*pos)++];
        buffer[i++] = source[(*pos)++];
    } else if (source[*pos] == 'h') {
        buffer[i++] = source[(*pos)++];
    } else {
        error("Unidade de tempo inválida");
    }
    
    buffer[i] = '\0';
    return createToken(TOKEN_TIME, buffer, line, col);
}
```

---

#### 3. Função para Reconhecer TEMPERATURA

```c
Token scanTemperature(char *source, int *pos) {
    char buffer[256];
    int i = 0;
    
    // Parte numérica
    while (isdigit(source[*pos])) {
        buffer[i++] = source[(*pos)++];
    }
    
    // Unidade de temperatura
    if (source[*pos] == 'C' || source[*pos] == 'F') {
        buffer[i++] = source[(*pos)++];
    } else {
        error("Unidade de temperatura inválida");
    }
    
    buffer[i] = '\0';
    return createToken(TOKEN_TEMPERATURE, buffer, line, col);
}
```

---

#### 4. Modificar getNextToken

```c
Token getNextToken(char *source, int *position) {
    // ... (pular espaços e comentários)
    
    // Identificadores e palavras-chave
    if (isalpha(source[*position])) {
        return scanIdentifier(source, position);
    }
    
    // Números, Tempo ou Temperatura
    if (isdigit(source[*position])) {
        // Lookahead para determinar tipo
        int tempPos = *position;
        
        // Consumir dígitos
        while (isdigit(source[tempPos])) {
            tempPos++;
        }
        
        // Verificar unidade
        if (source[tempPos] == 's' || 
            (source[tempPos] == 'm' && source[tempPos+1] == 'i') ||
            source[tempPos] == 'h') {
            return scanTime(source, position);  // TEMPO
        } else if (source[tempPos] == 'C' || source[tempPos] == 'F') {
            return scanTemperature(source, position);  // TEMPERATURA
        } else {
            return scanNumber(source, position);  // NÚMERO
        }
    }
    
    // ... (resto)
}
```

---

#### 5. Tabela de Palavras-Chave

```c
const char *keywords[] = {
    "recipe", "ingredients", "preparation",
    "add", "mix", "heat", "wait", "serve",
    "repeat", "times"
};

int isKeyword(char *word) {
    for (int i = 0; i < 10; i++) {
        if (strcmp(word, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

TokenType getKeywordType(char *word) {
    if (strcmp(word, "recipe") == 0) return TOKEN_RECIPE;
    if (strcmp(word, "ingredients") == 0) return TOKEN_INGREDIENTS;
    if (strcmp(word, "preparation") == 0) return TOKEN_PREPARATION;
    if (strcmp(word, "add") == 0) return TOKEN_ADD;
    if (strcmp(word, "mix") == 0) return TOKEN_MIX;
    if (strcmp(word, "heat") == 0) return TOKEN_HEAT;
    if (strcmp(word, "wait") == 0) return TOKEN_WAIT;
    if (strcmp(word, "serve") == 0) return TOKEN_SERVE;
    if (strcmp(word, "repeat") == 0) return TOKEN_REPEAT;
    if (strcmp(word, "times") == 0) return TOKEN_TIMES;
    return TOKEN_IDENTIFIER;
}
```

---

#### 6. Tratamento de Comentários

```c
void skipComments(char *source, int *pos) {
    // Comentário de linha //
    if (source[*pos] == '/' && source[*pos+1] == '/') {
        (*pos) += 2;
        while (source[*pos] != '\n' && source[*pos] != '\0') {
            (*pos)++;
        }
    }
    
    // Comentário de bloco /* */
    else if (source[*pos] == '/' && source[*pos+1] == '*') {
        (*pos) += 2;
        while (!(source[*pos] == '*' && source[*pos+1] == '/')) {
            if (source[*pos] == '\0') {
                error("Comentário não fechado");
            }
            (*pos)++;
        }
        (*pos) += 2;  // Pular */
    }
}
```

---

## 7.5 Problemas e Limitações

### 7.5.1 Problema 1: Lookahead para Tempo/Temperatura

**Problema**: Distinguir `180` de `180C`

**Solução no Lexer**:
- Fazer lookahead após ler dígitos
- Verificar próximo caractere
- Decidir token apropriado

**Limitação**: Requer backtracking ou lookahead

---

### 7.5.2 Problema 2: Palavras-Chave vs Identificadores

**Problema**: "add" pode ser palavra-chave ou identificador?

**Solução**:
- Sempre verificar tabela de palavras-chave primeiro
- Se não for keyword → identificador

**Código**:
```c
if (isKeyword(buffer)) {
    return createToken(getKeywordType(buffer), ...);
} else {
    return createToken(TOKEN_IDENTIFIER, ...);
}
```

---

### 7.5.3 Problema 3: Comentários Aninhados

**Problema**: `/* comentário /* aninhado */ ainda comentário? */`

**Limitação**:
- Gramáticas regulares **NÃO** podem reconhecer estruturas aninhadas
- Necessário contador (não disponível em AFD)

**Solução DoceLang**:
- **Não suportar** comentários aninhados
- Primeiro `*/` sempre fecha

**Alternativa (requer pilha)**:
- Usar gramática livre de contexto para comentários
- Quebra a separação lexer/parser

---

### 7.5.4 Problema 4: Caracteres Especiais

**Problema**: Acentuação (`açúcar`)

**Solução**:
- **Proibir** caracteres não-ASCII
- Mensagem de erro clara

**Implementação**:
```c
if (!isascii(source[*pos])) {
    error("Caracteres não-ASCII não são permitidos");
}
```

---

## 7.6 Vantagens da Abordagem

### 7.6.1 Vantagens do Lexer Separado

1. **Modularidade**
   - Lexer e parser independentes
   - Fácil manutenção

2. **Performance**
   - AFDs são O(n) - muito eficientes
   - Não precisa de pilha

3. **Reutilização**
   - Mesmo lexer pode servir múltiplos parsers
   - Fácil adicionar novos tokens

4. **Depuração**
   - Testar lexer isoladamente
   - Ver tokens gerados

---

### 7.6.2 Vantagens Específicas DoceLang

1. **Sintaxe Simples**
   - Poucos tipos de tokens (21)
   - Padrões bem definidos

2. **Sem Ambiguidade**
   - Cada padrão é único
   - Lookahead mínimo (1-3 caracteres)

3. **Expressões Regulares Diretas**
   - Fácil implementar com regex
   - Ou manualmente com AFD

---

## 7.7 Comparação: Manual vs Regex vs Gerador

### 7.7.1 Implementação Manual (C)

**Vantagens**:
- ✅ Controle total
- ✅ Performance máxima
- ✅ Mensagens de erro personalizadas

**Desvantagens**:
- ❌ Mais código
- ❌ Mais propenso a bugs
- ❌ Difícil manutenção

---

### 7.7.2 Implementação com Regex (Python)

**Vantagens**:
- ✅ Código conciso
- ✅ Rápido desenvolvimento
- ✅ Menos bugs

**Desvantagens**:
- ❌ Performance ligeiramente inferior
- ❌ Menos controle fino

**Exemplo**:
```python
import re

patterns = [
    (r'\brecipe\b', 'RECIPE'),
    (r'\d+(s|min|h)', 'TIME'),
    (r'[a-zA-Z][a-zA-Z0-9_]*', 'IDENTIFIER'),
]

for pattern, token_type in patterns:
    match = re.match(pattern, source[pos:])
    if match:
        yield Token(token_type, match.group(0))
```

---

### 7.7.3 Gerador (Flex/Lex)

**Vantagens**:
- ✅ Automático (gera código C)
- ✅ Otimizado
- ✅ Padrão da indústria

**Desvantagens**:
- ❌ Ferramenta extra necessária
- ❌ Curva de aprendizado

**Exemplo** (já mostrado em [6. Testes](#))

---

## 7.8 Autômatos Finitos para Tokens DoceLang

### 7.8.1 AFD para IDENTIFIER

```
Estado inicial: q0
Estados finais: {q1}

       letra
(q0) --------> ((q1))
               |   ^
               |   |
               +---+
          letra|dígito|_
```

---

### 7.8.2 AFD para TIME

```
Estado inicial: q0
Estados finais: {q2, q5, q6}

       dígito        s
(q0) --------> (q1) ----> ((q2))
                |
                | m
                +----> (q3) -i-> (q4) -n-> ((q5))
                |
                | h
                +----> ((q6))
```

---

### 7.8.3 AFD para TEMPERATURE

```
Estado inicial: q0
Estados finais: {q2, q3}

       dígito        C
(q0) --------> (q1) ----> ((q2))
                |
                | F
                +----> ((q3))
```

---

## 7.9 Conclusão da Análise do Lexer

### Tipo de Gramática
- ✅ Lexer usa **Gramática Regular (Tipo 3)**
- ✅ Reconhecida por **Autômatos Finitos**
- ✅ Eficiente: O(n) linear

### Adaptação para DoceLang
- ✅ Modificações são **simples**
- ✅ Adicionar 2 novos tipos (TIME, TEMPERATURE)
- ✅ 10 palavras-chave
- ✅ Comentários padrão C

### Problemas
- ⚠️  Lookahead necessário para TIME/TEMPERATURE
- ⚠️  Comentários aninhados não suportados (por design)
- ✅ Todos os problemas têm solução simples

### Vantagens
- ✅ Lexer é modular e reutilizável
- ✅ Performance excelente
- ✅ Fácil manutenção e extensão

**Próximo**: [8. Conclusões →](08-conclusoes.md)
