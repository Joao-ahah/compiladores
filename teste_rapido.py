from lexer.lexer import AnalisadorLexico, ErroLexico

codigo = """
/*
 * Receita: Bolinho de Chuva
 * Rendimento: 30 bolinhos
 * Tempo total: 40 minutos
 */

recipe BolinhoDeChuva {
    ingredients {
        farinha_de_trigo;
        acucar;
        ovos;
        leite;
        fermento_em_po;
        canela_em_po;
        oleo_para_fritar;
        acucar_com_canela;
    }
    
    preparation {
        // Preparar a massa
        add farinha_de_trigo;
        add acucar;
        
        // Adicionar ovos um a um
        repeat 2 times {
            add ovos;
            mix 1min;
        }
        
        add leite;
        mix 3min;
        
        add fermento_em_po;
        add canela_em_po;
        mix 2min;
        
        // Aquecer óleo
        add oleo_para_fritar;
        heat 180C;
        wait 5min;
        
        // Fritar bolinhos
        repeat 30 times {
            wait 2min;  // Fritar cada bolinho
        }
        
        // Polvilhar com açúcar e canela
        add acucar_com_canela;
        
        serve;
    }
}
"""

print("🍰 DOCELANG - Teste Rápido: Bolinho de Chuva 🍰")
print("=" * 60)

try:
    analisador = AnalisadorLexico(codigo)
    tokens = analisador.tokenizar()
    
    print(f"\n✅ Tokenização concluída com sucesso!")
    print(f"📊 Total de tokens: {len(tokens)}\n")
    
    # Mostrar primeiros 15 tokens
    print("🔍 Primeiros 15 tokens:")
    print("-" * 60)
    for i, token in enumerate(tokens[:15], 1):
        print(f"{i:2d}. {token.tipo.value:20s} → '{token.valor}'")
    
    if len(tokens) > 15:
        print(f"\n... e mais {len(tokens) - 15} tokens")
    
    # Estatísticas
    print(f"\n📈 Estatísticas:")
    print("-" * 60)
    tipos_count = {}
    for token in tokens:
        tipo_nome = token.tipo.value
        tipos_count[tipo_nome] = tipos_count.get(tipo_nome, 0) + 1
    
    for tipo, count in sorted(tipos_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {tipo:20s}: {count:3d} ocorrências")
    
    print("\n" + "=" * 60)
    print("✨ Receita de Bolinho de Chuva tokenizada com sucesso! ✨")
    
except ErroLexico as e:
    print(f"❌ Erro Léxico: {e}")
