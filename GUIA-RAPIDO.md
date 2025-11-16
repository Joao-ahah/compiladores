# 🍰 DoceLang - Guia Rápido de Uso

## 📋 Índice
1. [Instalação](#instalação)
2. [Executando Testes](#executando-testes)
3. [Processando Exemplos](#processando-exemplos)
4. [Usando o Lexer](#usando-o-lexer)
5. [Estrutura do Projeto](#estrutura-do-projeto)

---

## 🚀 Instalação

### Pré-requisitos
- **Python 3.7+** instalado
- Sistema operacional: Windows, Linux ou macOS

### Verificar Instalação
```bash
python --version
```

Se o Python não estiver instalado, baixe em: https://www.python.org/downloads/

---

## 🧪 Executando Testes

### Opção 1: Usando o script batch (Windows)
```bash
build.bat
```
Escolha a opção **1** para executar os testes.

### Opção 2: Comando direto
```bash
python lexer/test_lexer.py
```

### O que os testes verificam?
- ✅ Programa mínimo válido
- ✅ Todos os comandos da linguagem
- ✅ Comentários (linha e bloco)
- ✅ Unidades de tempo (s, min, h)
- ✅ Unidades de temperatura (C, F)
- ✅ Detecção de erros (caracteres inválidos)
- ✅ Receita completa (Brigadeiro)

---

## 📄 Processando Exemplos

### Processar todos os arquivos .doce
```bash
python run_examples.py
```

Ou use o `build.bat` e escolha a opção **2**.

### Exemplos disponíveis:
1. `brigadeiro.doce` - Receita clássica de brigadeiro
2. `beijinho.doce` - Variação com coco
3. `bolo-simples.doce` - Bolo básico
4. `pudim.doce` - Pudim de leite condensado
5. `receita-complexa.doce` - Petit Gateau elaborado

---

## 💻 Usando o Lexer

### Uso básico em Python

```python
from lexer.lexer import DoceLangLexer
from lexer.tokens import print_tokens_table

# Código DoceLang
code = """
recipe Brigadeiro {
    ingredients {
        leite_condensado;
        chocolate_em_po;
    }
    preparation {
        add leite_condensado;
        add chocolate_em_po;
        mix 15min;
        serve;
    }
}
"""

# Criar lexer e tokenizar
lexer = DoceLangLexer(code)
tokens = lexer.tokenize()

# Exibir tokens
print(f"Total de tokens: {len(tokens)}")
print_tokens_table(tokens)
```

### Processar arquivo .doce

```python
from lexer.lexer import DoceLangLexer

# Ler arquivo
with open('examples/brigadeiro.doce', 'r', encoding='utf-8') as f:
    code = f.read()

# Tokenizar
lexer = DoceLangLexer(code)
tokens = lexer.tokenize()

# Processar tokens...
for token in tokens:
    print(f"{token.type.value:15s} {token.value}")
```

### Tratar erros léxicos

```python
from lexer.lexer import DoceLangLexer, LexicalError

code = "recipe Erro { /* código inválido */ }"

try:
    lexer = DoceLangLexer(code)
    tokens = lexer.tokenize()
except LexicalError as e:
    print(f"Erro léxico: {e}")
```

---

## 📁 Estrutura do Projeto

```
COMPILADORES/
│
├── README.md                    # Documentação principal
├── build.bat                    # Script de build (Windows)
├── run_examples.py              # Processador de exemplos
│
├── docs/                        # Documentação completa
│   ├── 01-descricao-geral.md    # Descrição da linguagem
│   ├── 02-especificacao.md      # Especificação formal
│   ├── 03-gramatica.md          # Gramática BNF/EBNF
│   ├── 04-analise-lexica.md     # Análise léxica
│   ├── 05-exemplos.md           # Exemplos comentados
│   ├── 06-testes.md             # Metodologia de testes
│   ├── 07-analise-lexer.md      # Análise do lexer
│   └── 08-conclusoes.md         # Conclusões do projeto
│
├── examples/                    # Exemplos em .doce
│   ├── brigadeiro.doce
│   ├── beijinho.doce
│   ├── bolo-simples.doce
│   ├── pudim.doce
│   └── receita-complexa.doce
│
├── grammar/                     # Gramáticas formais
│   ├── docelang.bnf             # Gramática BNF
│   └── docelang.ebnf            # Gramática EBNF
│
└── lexer/                       # Implementação do lexer
    ├── lexer.py                 # Analisador léxico
    ├── tokens.py                # Utilitários de tokens
    └── test_lexer.py            # Testes do lexer
```

---

## 🎯 Comandos Rápidos

### Testar tudo
```bash
python lexer/test_lexer.py
python run_examples.py
```

### Ver tokens de um arquivo
```bash
python -c "from lexer.lexer import DoceLangLexer; from lexer.tokens import print_tokens_table; code=open('examples/brigadeiro.doce', 'r', encoding='utf-8').read(); tokens=DoceLangLexer(code).tokenize(); print_tokens_table(tokens)"
```

### Verificar estrutura
```bash
tree /F      # Windows
tree -L 3    # Linux/Mac
```

---

## 📚 Documentação Completa

Para entender a fundo a linguagem DoceLang, leia os documentos em ordem:

1. **Descrição Geral** (`docs/01-descricao-geral.md`)
   - O que é DoceLang?
   - Por que foi criada?
   - Escolhas de design

2. **Especificação** (`docs/02-especificacao.md`)
   - Estrutura da linguagem
   - Comandos disponíveis
   - Regras semânticas

3. **Gramática** (`docs/03-gramatica.md`)
   - Gramática formal (BNF/EBNF)
   - Árvores de derivação
   - Análise LL(1)

4. **Análise Léxica** (`docs/04-analise-lexica.md`)
   - 21 tipos de tokens
   - Expressões regulares
   - Autômatos finitos

5. **Exemplos** (`docs/05-exemplos.md`)
   - 7 receitas completas
   - Análise token por token
   - Validação sintática

6. **Testes** (`docs/06-testes.md`)
   - JFLAP, BNF Playground, Bison
   - Testes semânticos
   - Casos de erro

7. **Análise do Lexer** (`docs/07-analise-lexer.md`)
   - Gramática regular (Tipo 3)
   - Implementação em Python
   - Comparação de abordagens

8. **Conclusões** (`docs/08-conclusoes.md`)
   - Lições aprendidas
   - Limitações atuais
   - Futuro da DoceLang

---

## 🎓 Contexto Acadêmico

**Disciplina:** Compiladores  
**Instituição:** UFC - Campus Russas  
**Projeto:** Parte 1 - Front-End (Análise Léxica e Sintática)  
**Tema:** Linguagem de Domínio Específico para Receitas de Doces

---

## 💡 Dicas

### Para programar em DoceLang:
1. Toda receita começa com `recipe Nome {`
2. Declare ingredientes em `ingredients { }`
3. Descreva o preparo em `preparation { }`
4. Use ponto-e-vírgula após cada ingrediente e comando
5. Tempos: `30s`, `5min`, `2h`
6. Temperaturas: `180C`, `350F`

### Para testar o lexer:
1. Escreva código em arquivo `.doce`
2. Execute `python run_examples.py`
3. Verifique a tabela de tokens
4. Confirme que não há erros léxicos

### Para entender os tokens:
1. Leia `docs/04-analise-lexica.md`
2. Veja exemplos em `docs/05-exemplos.md`
3. Teste com `lexer/test_lexer.py`

---

## 🐛 Solução de Problemas

### Erro: "Python não encontrado"
**Solução:** Instale Python 3.7+ e adicione ao PATH do sistema.

### Erro: "ModuleNotFoundError: No module named 'lexer'"
**Solução:** Execute os comandos a partir da raiz do projeto (diretório `COMPILADORES/`).

### Erro: "LexicalError: Caractere inválido"
**Solução:** DoceLang aceita apenas caracteres ASCII. Use `_` no lugar de acentos.
- ❌ `açúcar` → ✅ `acucar` ou `acucar_refinado`

### Tokens não reconhecidos corretamente
**Solução:** Verifique espaçamento. Unidades de tempo/temperatura devem estar **coladas** ao número:
- ❌ `5 min` → ✅ `5min`
- ❌ `180 C` → ✅ `180C`

---

## 📞 Ajuda

Para dúvidas sobre a linguagem, consulte:
- `README.md` - Visão geral
- `docs/01-descricao-geral.md` - Filosofia e design
- `docs/02-especificacao.md` - Referência completa
- `docs/05-exemplos.md` - Receitas de exemplo

---

## 🎉 Próximos Passos

Após dominar o lexer, você pode:
1. Estudar a gramática (`docs/03-gramatica.md`)
2. Implementar o parser (Parte 2 do projeto)
3. Adicionar análise semântica
4. Criar gerador de código
5. Desenvolver interpretador/compilador completo

---

**Desenvolvido com 💙 para a disciplina de Compiladores**  
*UFC - Campus Russas | 2025*
