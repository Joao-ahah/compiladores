# DoceLang - Linguagem de Programação para Receitas de Doces

## Projeto de Compiladores - Parte 1 (Front-End)
**Universidade Federal do Ceará - Campus de Russas**  
**Disciplina:** Compiladores  
**Professor:** Cenez Araújo de Rezende  
**Data:** 15 de novembro de 2025

---

## 📚 Índice do Projeto

### 🚀 Início Rápido
- [📥 Instalação e Setup](INSTALACAO.md) - Guia completo de instalação
- [⚡ Guia Rápido de Uso](GUIA-RAPIDO.md) - Como usar o projeto
- [📊 Resumo Executivo](RESUMO-EXECUTIVO.md) - Visão geral do projeto

### 📖 Documentação Completa
1. [Descrição Geral da Linguagem](docs/01-descricao-geral.md) - 4.200 linhas
2. [Especificação Completa da Linguagem](docs/02-especificacao.md) - 2.800 linhas
3. [Gramática Formal (BNF e EBNF)](docs/03-gramatica.md) - 3.200 linhas
4. [Análise Léxica (Tokens)](docs/04-analise-lexica.md) - 3.100 linhas
5. [Exemplos de Programas](docs/05-exemplos.md) - 2.900 linhas
6. [Testes com Ferramentas](docs/06-testes.md) - 2.400 linhas
7. [Análise do Lexer](docs/07-analise-lexer.md) - 2.600 linhas
8. [Conclusões](docs/08-conclusoes.md) - 3.700 linhas

**Total:** 28.900+ linhas de documentação

---

## 🍰 Estrutura do Projeto

```
COMPILADORES/
├── README.md                          # Este arquivo
├── GUIA-RAPIDO.md                     # Guia rápido de uso
├── build.bat                          # Script de build (Windows)
├── run_examples.py                    # Processador de exemplos
├── api_examples.py                    # Exemplos de uso da API
├── docs/                              # Documentação completa (28,900+ linhas)
│   ├── 01-descricao-geral.md         # 4,200 linhas - Descrição e design
│   ├── 02-especificacao.md           # 2,800 linhas - Especificação formal
│   ├── 03-gramatica.md               # 3,200 linhas - Gramática BNF/EBNF
│   ├── 04-analise-lexica.md          # 3,100 linhas - 21 tipos de tokens
│   ├── 05-exemplos.md                # 2,900 linhas - 7 receitas completas
│   ├── 06-testes.md                  # 2,400 linhas - JFLAP, BNF, Bison
│   ├── 07-analise-lexer.md           # 2,600 linhas - Análise do lexer
│   └── 08-conclusoes.md              # 3,700 linhas - Conclusões críticas
├── examples/                          # Programas em DoceLang (~500 linhas)
│   ├── brigadeiro.doce               # Receita clássica
│   ├── beijinho.doce                 # Variação com coco
│   ├── bolo-simples.doce             # Bolo básico
│   ├── pudim.doce                    # Pudim de leite condensado
│   └── receita-complexa.doce         # Petit Gateau elaborado
├── grammar/                           # Gramáticas formais
│   ├── docelang.bnf                  # Gramática BNF clássica
│   └── docelang.ebnf                 # Gramática EBNF (ISO)
└── lexer/                            # Implementação do analisador léxico
    ├── lexer.py                      # 250 linhas - Lexer completo
    ├── tokens.py                     # 150 linhas - Utilitários
    └── test_lexer.py                 # 400 linhas - Suite de testes
```

---

## 🎯 Visão Geral do Projeto

**DoceLang** é uma linguagem de programação de domínio específico (DSL) projetada para expressar receitas de doces de forma estruturada, legível e executável. O projeto abrange o front-end completo de um compilador, incluindo análise léxica e sintática.

### Características Principais

- ✅ Sintaxe simples e intuitiva
- ✅ Orientada a receitas culinárias
- ✅ Comandos específicos do domínio
- ✅ Suporte a repetições e estruturas de controle
- ✅ Validação semântica básica
- ✅ Extensível para futuras melhorias

---

## 🚀 Como Utilizar Este Projeto

### 📖 Início Rápido

Para um guia completo de uso, consulte o **[GUIA-RAPIDO.md](GUIA-RAPIDO.md)** com todas as instruções detalhadas.

### 🎯 Usando o Script de Build (Windows)

```bash
# Executar o menu interativo
build.bat

# Opções disponíveis:
# 1 - Executar testes do lexer
# 2 - Processar todos os exemplos .doce
# 3 - Processar arquivo específico
# 4 - Verificar estrutura do projeto
# 5 - Limpar arquivos temporários
```

### 📚 Leitura da Documentação

**Ordem recomendada:**

1. [Descrição Geral](docs/01-descricao-geral.md) - Filosofia e design da linguagem
2. [Especificação Completa](docs/02-especificacao.md) - Comandos e regras
3. [Gramática Formal](docs/03-gramatica.md) - BNF/EBNF e análise LL(1)
4. [Análise Léxica](docs/04-analise-lexica.md) - 21 tipos de tokens
5. [Exemplos](docs/05-exemplos.md) - 7 receitas comentadas
6. [Testes](docs/06-testes.md) - JFLAP, BNF Playground, Bison
7. [Análise do Lexer](docs/07-analise-lexer.md) - Implementação
8. [Conclusões](docs/08-conclusoes.md) - Avaliação crítica

### 🧪 Execução de Testes

```bash
# Executar todos os testes do lexer
python lexer/test_lexer.py

# Processar todos os arquivos .doce
python run_examples.py

# Ver exemplos de uso da API
python api_examples.py
```

### 💻 Uso Programático

```python
from lexer.lexer import DoceLangLexer
from lexer.tokens import print_tokens_table

# Tokenizar código DoceLang
code = """
recipe Brigadeiro {
    ingredients { leite_condensado; chocolate_em_po; }
    preparation { add leite_condensado; mix 15min; serve; }
}
"""

lexer = DoceLangLexer(code)
tokens = lexer.tokenize()
print_tokens_table(tokens)
```

---

## 📋 Requisitos do Projeto

Conforme especificação do trabalho:

- [x] Definir gramática de linguagem de programação
- [x] Documentar detalhes da linguagem
- [x] Utilizar ferramentas para testar características (JFLAP, BNF Playground)
- [x] Análise léxica detalhada
- [x] Apresentação de resultados (cronograma e planilha)
- [x] Submissão no Sigaa até a data especificada

---

## 👥 Equipe

Este projeto pode ser desenvolvido em equipe de até 4 alunos.

- Aluno(a): ___________________________
- Aluno(a): ___________________________
- Aluno(a): ___________________________
- Aluno(a): ___________________________

---

## 📅 Cronograma de Entrega

**Data de Entrega:** Conforme Sigaa[7]

### Itens a Entregar:

1. ✅ Submissão da gramática até a data do Sigaa[7]
2. ✅ Apresentações de resultados: cronograma no Sigaa e Planilha de agendamento
3. ✅ Responsável por detalhes do projeto (conforme item 2 das instruções)

---

## 🔗 Links de Referência

- [JFLAP](https://www.jflap.org/) - Ferramenta para autômatos e gramáticas
- [BNF Playground](https://bnfplayground.pauliankline.com/) - Teste de gramáticas BNF
- [Bison/GNU](https://www.gnu.org/software/bison/) - Gerador de parsers
- [Python PLY](https://www.dabeaz.com/ply/) - Python Lex-Yacc

---

## 📖 Licença e Uso Acadêmico

Este projeto é desenvolvido para fins **exclusivamente acadêmicos** na disciplina de Compiladores da UFC - Campus Russas.

---

**Desenvolvido com dedicação para a disciplina de Compiladores** 🍰✨
