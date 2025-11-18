import sys
from lexer import AnalisadorLexico, TipoToken, ErroLexico
from lexer.tokens import imprimir_tabela_tokens, validar_sequencia_tokens


def test_minimal_program():
    """Testa programa mínimo válido"""
    print("\n" + "=" * 60)
    print("TESTE 1: Programa Mínimo")
    print("=" * 60)
    
    code = """
    recipe Minimo {
        ingredients {
            ingrediente;
        }
        preparation {
            add ingrediente;
            serve;
        }
    }
    """
    
    print(f"Código:\n{code}")
    
    try:
        analisador = AnalisadorLexico(code)
        tokens = analisador.tokenizar()
        
        print(f"✅ Tokens: {len(tokens)}")
        imprimir_tabela_tokens(tokens)
        
        eh_valido, erros = validar_sequencia_tokens(tokens)
        if eh_valido:
            print("✅ Sequência de tokens válida!")
        else:
            print("❌ Erros encontrados:")
            for erro in erros:
                print(f"  - {erro}")
                
    except ErroLexico as e:
        print(f"❌ ERRO: {e}")


def test_all_commands():
    """Testa todos os tipos de comandos"""
    print("\n" + "=" * 60)
    print("TESTE 2: Todos os Comandos")
    print("=" * 60)
    
    code = """
    recipe TodosComandos {
        ingredients {
            x;
            y;
        }
        preparation {
            add x;
            mix 5min;
            heat 180C;
            wait 2h;
            repeat 3 times {
                add y;
            }
            serve;
        }
    }
    """
    
    print(f"Código:\n{code}")
    
    try:
        analisador = AnalisadorLexico(code)
        tokens = analisador.tokenizar()
        
        # Contar tipos de comandos
        commands = {
            'ADICIONAR': 0, 'MISTURAR': 0, 'AQUECER': 0,
            'ESPERAR': 0, 'SERVIR': 0, 'REPETIR': 0
        }
        
        for token in tokens:
            if token.tipo.value in commands:
                commands[token.tipo.value] += 1
        
        print(f"✅ Tokens: {len(tokens)}")
        print("\nComandos encontrados:")
        for cmd, count in commands.items():
            print(f"  {cmd}: {count}")
        
        if all(count > 0 for count in commands.values()):
            print("\n✅ Todos os comandos presentes!")
        else:
            print("\n⚠️  Alguns comandos faltando")
            
    except ErroLexico as e:
        print(f"❌ ERRO: {e}")


def test_comments():
    """Testa comentários"""
    print("\n" + "=" * 60)
    print("TESTE 3: Comentários")
    print("=" * 60)
    
    code = """
    // Comentário de linha
    recipe Comentarios { /* comentário de bloco */
        ingredients {
            x;  // ingrediente x
        }
        /* 
         * Bloco de preparo
         */
        preparation {
            add x;
            serve;
        }
    }
    """
    
    print(f"Código:\n{code}")
    
    try:
        analisador = AnalisadorLexico(code)
        tokens = analisador.tokenizar()
        
        print(f"✅ Tokens: {len(tokens)} (comentários ignorados)")
        
        # Verificar que não há tokens de comentário
        comment_tokens = [t for t in tokens if 'COMMENT' in str(t.tipo)]
        if not comment_tokens:
            print("✅ Comentários corretamente ignorados!")
        else:
            print(f"❌ {len(comment_tokens)} tokens de comentário encontrados")
            
    except ErroLexico as e:
        print(f"❌ ERRO: {e}")


def test_time_units():
    """Testa diferentes unidades de tempo"""
    print("\n" + "=" * 60)
    print("TESTE 4: Unidades de Tempo")
    print("=" * 60)
    
    code = """
    recipe TempoTeste {
        ingredients { x; }
        preparation {
            mix 30s;
            mix 5min;
            wait 2h;
            serve;
        }
    }
    """
    
    print(f"Código:\n{code}")
    
    try:
        analisador = AnalisadorLexico(code)
        tokens = analisador.tokenizar()
        
        time_tokens = [t for t in tokens if t.tipo == TipoToken.TEMPO]
        
        print(f"✅ Tempos encontrados: {len(time_tokens)}")
        for token in time_tokens:
            print(f"  - {token.valor}")
        
        expected_times = ['30s', '5min', '2h']
        if all(t.valor in expected_times for t in time_tokens):
            print("✅ Todas as unidades de tempo corretas!")
        else:
            print("❌ Unidades de tempo incorretas")
            
    except ErroLexico as e:
        print(f"❌ ERRO: {e}")


def test_temperature_units():
    """Testa diferentes unidades de temperatura"""
    print("\n" + "=" * 60)
    print("TESTE 5: Unidades de Temperatura")
    print("=" * 60)
    
    code = """
    recipe TemperaturaTeste {
        ingredients { x; }
        preparation {
            heat 100C;
            heat 180C;
            heat 350F;
            serve;
        }
    }
    """
    
    print(f"Código:\n{code}")
    
    try:
        analisador = AnalisadorLexico(code)
        tokens = analisador.tokenizar()
        
        temp_tokens = [t for t in tokens if t.tipo == TipoToken.TEMPERATURA]
        
        print(f"✅ Temperaturas encontradas: {len(temp_tokens)}")
        for token in temp_tokens:
            print(f"  - {token.valor}")
        
        expected_temps = ['100C', '180C', '350F']
        if all(t.valor in expected_temps for t in temp_tokens):
            print("✅ Todas as temperaturas corretas!")
        else:
            print("❌ Temperaturas incorretas")
            
    except ErroLexico as e:
        print(f"❌ ERRO: {e}")


def test_invalid_character():
    """Testa caractere inválido"""
    print("\n" + "=" * 60)
    print("TESTE 6: Erro - Caractere Inválido")
    print("=" * 60)
    
    code = """
    recipe Erro {
        ingredients {
            açúcar;
        }
    }
    """
    
    print(f"Código:\n{code}")
    
    try:
        analisador = AnalisadorLexico(code)
        tokens = analisador.tokenizar()
        print("❌ Deveria ter dado erro!")
        
    except ErroLexico as e:
        print(f"✅ Erro detectado corretamente: {e}")


def test_brigadeiro():
    """Testa receita completa de brigadeiro"""
    print("\n" + "=" * 60)
    print("TESTE 7: Receita Brigadeiro (Completa)")
    print("=" * 60)
    
    code = """
    recipe Brigadeiro {
        ingredients {
            leite_condensado;
            chocolate_em_po;
            manteiga;
            chocolate_granulado;
        }
        
        preparation {
            add leite_condensado;
            add chocolate_em_po;
            add manteiga;
            heat 180C;
            mix 15min;
            wait 2h;
            repeat 40 times {
                add chocolate_granulado;
            }
            serve;
        }
    }
    """
    
    print(f"Código:\n{code}")
    
    try:
        analisador = AnalisadorLexico(code)
        tokens = analisador.tokenizar()
        
        print(f"✅ Tokens: {len(tokens)}")
        
        # Estatísticas
        ingredients = [t for t in tokens if t.tipo == TipoToken.IDENTIFICADOR and tokens[tokens.index(t)-1].tipo in (TipoToken.INGREDIENTES, TipoToken.PONTO_VIRGULA)]
        commands = [t for t in tokens if t.tipo in (TipoToken.ADICIONAR, TipoToken.MISTURAR, TipoToken.AQUECER, TipoToken.ESPERAR, TipoToken.SERVIR, TipoToken.REPETIR)]
        
        print(f"\nEstatísticas:")
        print(f"  Comandos: {len(commands)}")
        print(f"  Palavras-chave: {len([t for t in tokens if t.tipo.value in ('RECIPE', 'INGREDIENTS', 'PREPARATION')])}")
        
        eh_valido, erros = validar_sequencia_tokens(tokens)
        if eh_valido:
            print("\n✅ Receita válida!")
        else:
            print("\n❌ Erros:")
            for erro in erros:
                print(f"  - {erro}")
                
    except ErroLexico as e:
        print(f"❌ ERRO: {e}")


def run_all_tests():
    """Executa todos os testes"""
    print("=" * 60)
    print("DOCELANG LEXER - SUITE DE TESTES")
    print("=" * 60)
    
    tests = [
        test_minimal_program,
        test_all_commands,
        test_comments,
        test_time_units,
        test_temperature_units,
        test_invalid_character,
        test_brigadeiro,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"\n❌ Teste falhou: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print("RESULTADO DOS TESTES")
    print("=" * 60)
    print(f"✅ Passou: {passed}/{len(tests)}")
    print(f"❌ Falhou: {failed}/{len(tests)}")
    
    if failed == 0:
        print("\n🎉 TODOS OS TESTES PASSARAM! 🎉")
    else:
        print(f"\n⚠️  {failed} teste(s) falharam")


if __name__ == '__main__':
    run_all_tests()
