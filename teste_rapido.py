"""
Teste Rápido - Lexer em Português
==================================
"""

from lexer.lexer import AnalisadorLexico, ErroLexico

codigo = """
recipe Teste {
    ingredients {
        acucar;
    }
    preparation {
        add acucar;
        mix 5min;
        serve;
    }
}
"""

print("Testando AnalisadorLexico...")
print("-" * 60)

try:
    analisador = AnalisadorLexico(codigo)
    tokens = analisador.tokenizar()
    
    print(f"✅ Sucesso! {len(tokens)} tokens encontrados\n")
    
    for i, token in enumerate(tokens[:10], 1):
        print(f"{i}. Tipo: {token.tipo.value:20s} Valor: '{token.valor}'")
    
    print("\n✅ Lexer funcionando perfeitamente em português!")
    
except ErroLexico as e:
    print(f"❌ Erro: {e}")
