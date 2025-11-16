"""
DoceLang - Exemplos de Uso da API
==================================

Este arquivo demonstra como usar o lexer DoceLang em diferentes cenários.

Autor: Projeto Compiladores 2025
"""

from lexer.lexer import DoceLangLexer, TokenType, Token, LexicalError
from lexer.tokens import print_tokens_table, validate_token_sequence


# ============================================
# EXEMPLO 1: Uso Básico
# ============================================
def exemplo_basico():
    """Uso mais simples possível"""
    print("\n" + "="*60)
    print("EXEMPLO 1: Uso Básico")
    print("="*60)
    
    code = """
    recipe Simples {
        ingredients { acucar; }
        preparation { add acucar; serve; }
    }
    """
    
    lexer = DoceLangLexer(code)
    tokens = lexer.tokenize()
    
    print(f"✅ {len(tokens)} tokens encontrados")
    for token in tokens:
        print(f"  {token.type.value:15s} '{token.value}'")


# ============================================
# EXEMPLO 2: Análise de Arquivo
# ============================================
def exemplo_arquivo():
    """Processar arquivo .doce"""
    print("\n" + "="*60)
    print("EXEMPLO 2: Processar Arquivo")
    print("="*60)
    
    filepath = 'examples/brigadeiro.doce'
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        lexer = DoceLangLexer(code)
        tokens = lexer.tokenize()
        
        print(f"📄 Arquivo: {filepath}")
        print(f"✅ Tokens: {len(tokens)}")
        
        # Contar por tipo
        counts = {}
        for token in tokens:
            counts[token.type.value] = counts.get(token.type.value, 0) + 1
        
        print("\n📊 Distribuição:")
        for type_name, count in sorted(counts.items()):
            print(f"  {type_name:15s}: {count}")
            
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {filepath}")


# ============================================
# EXEMPLO 3: Filtrar Tokens por Tipo
# ============================================
def exemplo_filtrar_tokens():
    """Extrair apenas tokens específicos"""
    print("\n" + "="*60)
    print("EXEMPLO 3: Filtrar Tokens")
    print("="*60)
    
    code = """
    recipe Filtro {
        ingredients {
            leite;
            acucar;
            ovos;
        }
        preparation {
            add leite;
            add acucar;
            add ovos;
            mix 10min;
            heat 180C;
            wait 1h;
            serve;
        }
    }
    """
    
    lexer = DoceLangLexer(code)
    tokens = lexer.tokenize()
    
    # Filtrar ingredientes (IDENTIFIERs após INGREDIENTS ou SEMICOLON dentro do bloco)
    identifiers = [t.value for t in tokens if t.type == TokenType.IDENTIFIER]
    print(f"🔍 Identificadores: {identifiers}")
    
    # Filtrar comandos
    commands = [t for t in tokens if t.type in (
        TokenType.ADD, TokenType.MIX, TokenType.HEAT,
        TokenType.WAIT, TokenType.SERVE, TokenType.REPEAT
    )]
    print(f"\n🔍 Comandos ({len(commands)}):")
    for cmd in commands:
        print(f"  - {cmd.value} (linha {cmd.line}, coluna {cmd.column})")
    
    # Filtrar tempos
    times = [t for t in tokens if t.type == TokenType.TIME]
    print(f"\n🔍 Tempos: {[t.value for t in times]}")
    
    # Filtrar temperaturas
    temps = [t for t in tokens if t.type == TokenType.TEMPERATURE]
    print(f"🔍 Temperaturas: {[t.value for t in temps]}")


# ============================================
# EXEMPLO 4: Validação e Detecção de Erros
# ============================================
def exemplo_validacao():
    """Detectar erros em código"""
    print("\n" + "="*60)
    print("EXEMPLO 4: Validação e Erros")
    print("="*60)
    
    # Código válido
    valid_code = """
    recipe Valido {
        ingredients { x; }
        preparation { add x; serve; }
    }
    """
    
    # Código inválido (caractere especial)
    invalid_code = """
    recipe Inválido {
        ingredients { açúcar; }
        preparation { add açúcar; serve; }
    }
    """
    
    print("📝 Testando código VÁLIDO:")
    try:
        lexer = DoceLangLexer(valid_code)
        tokens = lexer.tokenize()
        print(f"  ✅ {len(tokens)} tokens - SEM ERROS")
    except LexicalError as e:
        print(f"  ❌ Erro: {e}")
    
    print("\n📝 Testando código INVÁLIDO:")
    try:
        lexer = DoceLangLexer(invalid_code)
        tokens = lexer.tokenize()
        print(f"  ⚠️  {len(tokens)} tokens processados")
    except LexicalError as e:
        print(f"  ✅ Erro detectado corretamente: {e}")


# ============================================
# EXEMPLO 5: Estatísticas Detalhadas
# ============================================
def exemplo_estatisticas():
    """Gerar estatísticas completas"""
    print("\n" + "="*60)
    print("EXEMPLO 5: Estatísticas Detalhadas")
    print("="*60)
    
    code = """
    recipe Estatisticas {
        ingredients {
            ingrediente_1;
            ingrediente_2;
            ingrediente_3;
        }
        preparation {
            add ingrediente_1;
            add ingrediente_2;
            mix 5min;
            heat 180C;
            wait 30min;
            repeat 10 times {
                add ingrediente_3;
            }
            serve;
        }
    }
    """
    
    lexer = DoceLangLexer(code)
    tokens = lexer.tokenize()
    
    print(f"📊 ESTATÍSTICAS GERAIS:")
    print(f"  Total de tokens: {len(tokens)}")
    print(f"  Linhas de código: {len(code.splitlines())}")
    print(f"  Caracteres: {len(code)}")
    
    # Tokens por categoria
    keywords = [t for t in tokens if t.type.value in (
        'RECIPE', 'INGREDIENTS', 'PREPARATION',
        'ADD', 'MIX', 'HEAT', 'WAIT', 'SERVE', 'REPEAT', 'TIMES'
    )]
    identifiers = [t for t in tokens if t.type == TokenType.IDENTIFIER]
    numbers = [t for t in tokens if t.type == TokenType.NUMBER]
    times = [t for t in tokens if t.type == TokenType.TIME]
    temps = [t for t in tokens if t.type == TokenType.TEMPERATURE]
    symbols = [t for t in tokens if t.type in (
        TokenType.LBRACE, TokenType.RBRACE,
        TokenType.SEMICOLON
    )]
    
    print(f"\n📊 POR CATEGORIA:")
    print(f"  Palavras-chave: {len(keywords)}")
    print(f"  Identificadores: {len(identifiers)}")
    print(f"  Números: {len(numbers)}")
    print(f"  Tempos: {len(times)}")
    print(f"  Temperaturas: {len(temps)}")
    print(f"  Símbolos: {len(symbols)}")
    
    # Complexidade
    loops = [t for t in tokens if t.type == TokenType.REPEAT]
    commands = [t for t in tokens if t.type in (
        TokenType.ADD, TokenType.MIX, TokenType.HEAT,
        TokenType.WAIT, TokenType.SERVE
    )]
    
    print(f"\n📊 COMPLEXIDADE:")
    print(f"  Comandos: {len(commands)}")
    print(f"  Loops: {len(loops)}")
    print(f"  Ingredientes: {len(identifiers)}")


# ============================================
# EXEMPLO 6: Posição dos Tokens (Debug)
# ============================================
def exemplo_posicoes():
    """Mostrar posição exata de cada token"""
    print("\n" + "="*60)
    print("EXEMPLO 6: Posições dos Tokens")
    print("="*60)
    
    code = """recipe Mini {
    ingredients { x; }
    preparation { add x; serve; }
}"""
    
    print(f"Código:\n{code}\n")
    
    lexer = DoceLangLexer(code)
    tokens = lexer.tokenize()
    
    print("Token                 Tipo              Linha  Coluna")
    print("-" * 60)
    for token in tokens:
        print(f"{token.value:20s} {token.type.value:15s} {token.line:5d}  {token.column:5d}")


# ============================================
# EXEMPLO 7: Validação de Sequência
# ============================================
def exemplo_validacao_sequencia():
    """Validar sequência de tokens"""
    print("\n" + "="*60)
    print("EXEMPLO 7: Validação de Sequência")
    print("="*60)
    
    # Código completo
    complete = """
    recipe Completo {
        ingredients { x; }
        preparation { add x; serve; }
    }
    """
    
    # Código incompleto (sem serve)
    incomplete = """
    recipe Incompleto {
        ingredients { x; }
        preparation { add x; }
    }
    """
    
    print("📝 Código COMPLETO:")
    lexer = DoceLangLexer(complete)
    tokens = lexer.tokenize()
    is_valid, errors = validate_token_sequence(tokens)
    if is_valid:
        print("  ✅ Sequência válida!")
    else:
        print("  ❌ Problemas:")
        for error in errors:
            print(f"    - {error}")
    
    print("\n📝 Código INCOMPLETO:")
    lexer = DoceLangLexer(incomplete)
    tokens = lexer.tokenize()
    is_valid, errors = validate_token_sequence(tokens)
    if is_valid:
        print("  ✅ Sequência válida!")
    else:
        print("  ⚠️  Problemas detectados:")
        for error in errors:
            print(f"    - {error}")


# ============================================
# EXEMPLO 8: Comparar Múltiplos Códigos
# ============================================
def exemplo_comparacao():
    """Comparar diferentes receitas"""
    print("\n" + "="*60)
    print("EXEMPLO 8: Comparação de Receitas")
    print("="*60)
    
    receitas = {
        'Simples': """
        recipe Simples {
            ingredients { x; }
            preparation { add x; serve; }
        }
        """,
        'Média': """
        recipe Media {
            ingredients { a; b; }
            preparation {
                add a;
                add b;
                mix 5min;
                heat 180C;
                serve;
            }
        }
        """,
        'Complexa': """
        recipe Complexa {
            ingredients { x; y; z; }
            preparation {
                add x;
                mix 10min;
                repeat 5 times {
                    add y;
                }
                heat 200C;
                wait 1h;
                add z;
                serve;
            }
        }
        """
    }
    
    print("\nNome         Tokens  Comandos  Ingredientes  Loops")
    print("-" * 60)
    
    for name, code in receitas.items():
        lexer = DoceLangLexer(code)
        tokens = lexer.tokenize()
        
        comandos = len([t for t in tokens if t.type in (
            TokenType.ADD, TokenType.MIX, TokenType.HEAT,
            TokenType.WAIT, TokenType.SERVE
        )])
        
        ingredientes = len([t for t in tokens if t.type == TokenType.IDENTIFIER])
        loops = len([t for t in tokens if t.type == TokenType.REPEAT])
        
        print(f"{name:12s} {len(tokens):6d}  {comandos:8d}  {ingredientes:12d}  {loops:5d}")


# ============================================
# MAIN: Executar todos os exemplos
# ============================================
def main():
    """Executa todos os exemplos"""
    print("=" * 60)
    print("DOCELANG - EXEMPLOS DE USO DA API")
    print("=" * 60)
    
    exemplos = [
        exemplo_basico,
        exemplo_arquivo,
        exemplo_filtrar_tokens,
        exemplo_validacao,
        exemplo_estatisticas,
        exemplo_posicoes,
        exemplo_validacao_sequencia,
        exemplo_comparacao,
    ]
    
    for exemplo in exemplos:
        try:
            exemplo()
        except Exception as e:
            print(f"\n❌ Erro no exemplo: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 TODOS OS EXEMPLOS EXECUTADOS!")
    print("=" * 60)


if __name__ == '__main__':
    main()
