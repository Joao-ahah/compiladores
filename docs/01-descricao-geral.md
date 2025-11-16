# 1. Descrição Geral da Linguagem DoceLang

## 1.1 O que é a DoceLang?

**DoceLang** (Doce Language) é uma linguagem de programação de domínio específico (DSL - Domain-Specific Language) projetada especificamente para expressar receitas de doces de forma estruturada, legível e executável. Ela traduz o processo culinário em uma sintaxe de programação intuitiva, permitindo que receitas sejam escritas como programas que podem ser validados, analisados e potencialmente executados por sistemas automatizados.

### Características Fundamentais

- **Domínio Específico**: Focada exclusivamente em receitas culinárias de doces
- **Declarativa e Imperativa**: Combina declaração de ingredientes com comandos imperativos de preparo
- **Sintaxe Legível**: Inspirada em linguagens modernas como Python e JavaScript
- **Estruturada**: Organizada em blocos lógicos (receita, ingredientes, preparo)
- **Tipagem Implícita**: Tipos são inferidos pelo contexto (ingredientes, tempos, temperaturas)

---

## 1.2 Objetivo da Linguagem

### Objetivos Primários

1. **Padronização de Receitas**
   - Criar um formato único e consistente para descrever receitas
   - Eliminar ambiguidades presentes em receitas textuais tradicionais
   - Facilitar o compartilhamento e reprodução de receitas

2. **Validação Automática**
   - Verificar se todos os ingredientes declarados são utilizados
   - Garantir que as quantidades e unidades sejam válidas
   - Detectar inconsistências no preparo (ex: temperatura negativa)

3. **Educação em Compiladores**
   - Servir como exemplo didático de construção de linguagens
   - Demonstrar conceitos de análise léxica e sintática
   - Ilustrar o processo de design de linguagens de programação

4. **Automação Futura**
   - Permitir integração com sistemas de cozinha inteligente
   - Possibilitar cálculo automático de porções e ingredientes
   - Facilitar conversão de unidades e adaptações de receitas

### Objetivos Secundários

- Tornar programação mais acessível através de um domínio familiar
- Criar uma ponte entre culinária e ciência da computação
- Demonstrar como DSLs podem resolver problemas específicos

---

## 1.3 Como a DoceLang Funciona

### Estrutura Básica de um Programa

Um programa em DoceLang é organizado em três seções principais:

```docelang
recipe NomeDaReceita {
    // 1. Declaração de ingredientes
    ingredients {
        leite_condensado;
        chocolate_em_po;
        manteiga;
        chocolate_granulado;
    }
    
    // 2. Processo de preparo
    preparation {
        add leite_condensado;
        add chocolate_em_po;
        add manteiga;
        mix 5min;
        heat 180C;
        wait 15min;
        serve;
    }
}
```

### Fluxo de Execução

1. **Análise Léxica (Lexer)**
   - Divide o código em tokens (palavras-chave, identificadores, símbolos)
   - Reconhece padrões como números, unidades, identificadores
   - Ignora espaços em branco e comentários

2. **Análise Sintática (Parser)**
   - Verifica se a sequência de tokens segue a gramática
   - Constrói uma árvore sintática abstrata (AST)
   - Detecta erros de sintaxe

3. **Análise Semântica**
   - Valida se ingredientes declarados são utilizados
   - Verifica consistência de tipos (tempos, temperaturas)
   - Garante ordem lógica de operações

4. **Interpretação/Compilação**
   - Gera instruções executáveis ou representação intermediária
   - Pode gerar documentação formatada da receita
   - Permite simulação do processo de preparo

### Paradigmas Utilizados

- **Declarativo**: Declaração de ingredientes
- **Imperativo**: Comandos sequenciais de preparo
- **Estruturado**: Blocos organizados hierarquicamente

---

## 1.4 Justificativas das Escolhas de Design

### 1.4.1 Sintaxe com Chaves `{ }`

**Escolha**: Uso de chaves para delimitar blocos

**Justificativa**:
- Familiaridade com linguagens mainstream (C, Java, JavaScript)
- Clareza visual na delimitação de escopo
- Facilita parsing com gramáticas livres de contexto
- Permite formatação automática e identação consistente

**Alternativas consideradas**:
- Identação (estilo Python) - rejeitada por dificultar parsing
- `begin/end` (estilo Pascal) - mais verbosa

---

### 1.4.2 Palavras-Chave em Inglês

**Escolha**: Comandos em inglês (`add`, `mix`, `heat`, `wait`, `serve`)

**Justificativa**:
- Padrão universal em linguagens de programação
- Concisão e memorização facilitada
- Internacionalização - receitas podem ser compartilhadas globalmente
- Evita caracteres especiais (acentuação)

**Consideração futura**: Versões localizadas (pt-BR, es, etc.)

---

### 1.4.3 Identificadores com Underscore

**Escolha**: Ingredientes usando snake_case (ex: `leite_condensado`)

**Justificativa**:
- Nomes compostos são comuns em ingredientes
- Snake_case é legível e familiar (Python, Ruby)
- Evita ambiguidade com espaços
- Facilita análise léxica (regex simples)

**Exemplo**:
```docelang
leite_condensado    // ✅ Válido
leite condensado    // ❌ Inválido (dois tokens)
leiteCondensado     // ⚠️  Válido mas menos legível neste contexto
```

---

### 1.4.4 Unidades Integradas na Sintaxe

**Escolha**: Unidades anexadas aos números (`5min`, `180C`, `2L`)

**Justificativa**:
- Clareza semântica - não há ambiguidade de unidades
- Validação em tempo de compilação
- Reflete notação natural em receitas
- Facilita conversões automáticas

**Tipos de unidades suportadas**:
- **Tempo**: `s` (segundos), `min` (minutos), `h` (horas)
- **Temperatura**: `C` (Celsius), `F` (Fahrenheit)
- **Volume**: `ml`, `L`, `xic` (xícaras)
- **Massa**: `g`, `kg`, `col` (colheres)

**Exemplo**:
```docelang
mix 5min;        // ✅ Claro e sem ambiguidade
wait 2h;         // ✅ Duas horas
heat 180C;       // ✅ 180 graus Celsius
```

---

### 1.4.5 Comando `repeat` para Repetições

**Escolha**: Estrutura `repeat N times { ... }`

**Justificativa**:
- Naturalidade linguística ("repetir N vezes")
- Comum em receitas (ex: "bater 3 vezes")
- Mais legível que `for` ou `while` neste contexto
- Limitação intencional - apenas repetições simples

**Exemplo**:
```docelang
repeat 3 times {
    add clara_de_ovo;
    mix 2min;
}
```

**Por que não `while` ou `for`?**
- Receitas raramente têm loops condicionais complexos
- Simplicidade é prioridade em uma DSL
- Reduz complexidade da gramática

---

### 1.4.6 Seções Explícitas (ingredients/preparation)

**Escolha**: Separação clara entre ingredientes e preparo

**Justificativa**:
- Reflete estrutura natural de receitas tradicionais
- Facilita validação (ingredientes declarados vs. usados)
- Permite otimizações (pré-carregar todos os ingredientes)
- Melhora legibilidade

**Estrutura**:
```docelang
recipe Brigadeiro {
    ingredients {
        // Todos os ingredientes necessários
    }
    
    preparation {
        // Passos sequenciais
    }
}
```

---

### 1.4.7 Comentários Estilo C/Java

**Escolha**: Comentários com `//` (linha) e `/* */` (bloco)

**Justificativa**:
- Familiaridade com linguagens populares
- Dois estilos atendem diferentes necessidades
- Fácil implementação no lexer
- Permite documentação inline

**Exemplo**:
```docelang
// Esta é uma receita tradicional brasileira
recipe Brigadeiro {
    ingredients {
        leite_condensado;  // 1 lata
        /* 
         * Chocolate em pó de boa qualidade
         * preferencialmente 50% cacau
         */
        chocolate_em_po;
    }
    // ... resto da receita
}
```

---

### 1.4.8 Simplicidade sobre Completude

**Escolha**: Conjunto reduzido de comandos (add, mix, heat, wait, serve, repeat)

**Justificativa**:
- Princípio KISS (Keep It Simple, Stupid)
- Facilita aprendizado e implementação
- Reduz complexidade do compilador
- Comandos cobrem 90% dos casos de uso
- Extensível para versões futuras

**Comandos atuais**:
- `add` - Adicionar ingrediente
- `mix` - Misturar por tempo
- `heat` - Aquecer a temperatura
- `wait` - Aguardar tempo
- `serve` - Finalizar receita
- `repeat` - Repetir ações

**Possíveis extensões futuras**:
- `cool` - Resfriar
- `bake` - Assar (heat + wait combinados)
- `stir` - Mexer continuamente
- `if/else` - Condicionais (consistência, pontos de açúcar)

---

### 1.4.9 Tipagem Implícita e Forte

**Escolha**: Tipos inferidos pelo contexto, mas validados rigidamente

**Justificativa**:
- Ingredientes são sempre identificadores
- Tempos sempre têm unidades de tempo
- Temperaturas sempre têm unidades de temperatura
- Validação em tempo de compilação previne erros

**Exemplo de validação**:
```docelang
heat 5min;       // ❌ ERRO: temperatura esperada, tempo fornecido
wait 180C;       // ❌ ERRO: tempo esperado, temperatura fornecida
add 10g;         // ❌ ERRO: ingrediente esperado, quantidade fornecida
mix leite;       // ❌ ERRO: tempo esperado, ingrediente fornecido
```

---

### 1.4.10 Ponto e Vírgula Obrigatório

**Escolha**: Comandos terminam com `;`

**Justificativa**:
- Elimina ambiguidades no parsing
- Familiar em linguagens C-like
- Permite comandos em múltiplas linhas
- Facilita recuperação de erros

**Exemplo**:
```docelang
add leite_condensado;
add chocolate_em_po;
mix 5min;

// Comando em múltiplas linhas (futuro)
repeat 3 times {
    add clara;
    mix 2min;
};
```

---

## 1.5 Filosofia de Design

### Princípios Norteadores

1. **Clareza sobre Concisão**
   - Código deve ser auto-explicativo
   - Priorizar legibilidade

2. **Domínio Específico sobre Generalidade**
   - Otimizada para receitas, não para computação geral
   - Comandos refletem ações culinárias

3. **Validação Rígida**
   - Melhor falhar em compilação que em execução
   - Erros claros e informativos

4. **Extensibilidade Planejada**
   - Estrutura permite futuras expansões
   - Compatibilidade retroativa considerada

---

## 1.6 Público-Alvo

### Usuários Primários
- **Estudantes de Compiladores**: Aprender conceitos através de domínio familiar
- **Chefs e Culinaristas**: Documentar receitas de forma precisa
- **Desenvolvedores**: Experimentar com DSLs

### Casos de Uso

1. **Educação**
   - Ensino de compiladores
   - Introdução à programação

2. **Documentação**
   - Padronização de receitas em restaurantes
   - Livros de receitas digitais

3. **Automação**
   - Robôs de cozinha
   - Apps de receitas inteligentes

---

## 1.7 Comparação com Outras Abordagens

### Receitas Tradicionais (Texto Livre)

❌ **Problemas**:
- Ambiguidade ("aqueça até ficar pronto")
- Inconsistência de formato
- Difícil validação automática

✅ **DoceLang resolve**:
- Sintaxe precisa e validável
- Formato padronizado
- Validação automática

### Formatos de Dados (JSON, YAML)

❌ **Problemas**:
- Verbosos e difíceis de escrever manualmente
- Focados em dados, não em processo
- Menos legíveis para humanos

✅ **DoceLang oferece**:
- Sintaxe concisa e legível
- Foco no processo sequencial
- Melhor para expressar fluxo de trabalho

### Linguagens Gerais (Python, JavaScript)

❌ **Problemas**:
- Muito complexas para o domínio
- Requerem conhecimento de programação
- Sem validação semântica específica

✅ **DoceLang vantagens**:
- Aprendizado rápido
- Validações específicas do domínio
- Sintaxe natural para receitas

---

## 1.8 Exemplo Ilustrativo Completo

```docelang
/*
 * Receita: Brigadeiro Tradicional Brasileiro
 * Rendimento: 40 unidades
 * Tempo: 30 minutos
 * Dificuldade: Fácil
 */

recipe Brigadeiro {
    // Declaração de todos os ingredientes necessários
    ingredients {
        leite_condensado;      // 1 lata (395g)
        chocolate_em_po;       // 3 colheres de sopa
        manteiga;              // 1 colher de sopa
        chocolate_granulado;   // Para cobertura
    }
    
    // Processo de preparo passo a passo
    preparation {
        // Combinar ingredientes base
        add leite_condensado;
        add chocolate_em_po;
        add manteiga;
        
        // Cozinhar em fogo médio
        heat 180C;
        mix 15min;  // Mexer continuamente
        
        // Esfriar e modelar
        wait 2h;    // Deixar esfriar
        
        // Finalização
        repeat 40 times {
            // Enrolar cada brigadeiro
            add chocolate_granulado;
        }
        
        serve;  // Receita finalizada
    }
}
```

**Saída esperada do compilador**:
```
✅ Análise léxica: 45 tokens identificados
✅ Análise sintática: Árvore sintática construída com sucesso
✅ Análise semântica: 
   - 4 ingredientes declarados
   - 4 ingredientes utilizados
   - 0 ingredientes não utilizados
   - Comandos em ordem válida
✅ Compilação concluída com sucesso!

Receita: Brigadeiro
Ingredientes: 4
Passos: 8
Tempo estimado: 2h 15min
```

---

## 1.9 Visão Futura

### Próximas Versões Planejadas

**DoceLang 2.0** (Intermediária):
- Condicionais (`if ponto_de_bala then ...`)
- Variáveis para quantidades
- Funções auxiliares (sub-receitas)

**DoceLang 3.0** (Avançada):
- Cálculo automático de porções
- Conversão de unidades
- Integração com APIs de nutrição
- Geração de lista de compras

---

## 1.10 Conclusão da Descrição Geral

DoceLang representa uma abordagem inovadora para padronização e automação de receitas culinárias, aplicando princípios sólidos de design de linguagens de programação a um domínio específico e acessível. Sua sintaxe cuidadosamente projetada equilibra simplicidade, clareza e poder expressivo, tornando-a ideal tanto para fins educacionais quanto para aplicações práticas em culinária e automação.

A linguagem demonstra como DSLs podem resolver problemas específicos de forma mais eficiente que linguagens de propósito geral, ao mesmo tempo em que serve como excelente ferramenta pedagógica para o ensino de compiladores.

---

**Próximo**: [2. Especificação Completa da Linguagem →](02-especificacao.md)
