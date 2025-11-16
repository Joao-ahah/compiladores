"""
DoceLang Token Definitions
===========================

Definições e utilitários para tokens da linguagem DoceLang.

Autor: Projeto Compiladores 2025
"""

from lexer import TokenType, Token


# Mapeamento de tipos de tokens para descrições legíveis
TOKEN_DESCRIPTIONS = {
    TokenType.RECIPE: "Palavra-chave 'recipe'",
    TokenType.INGREDIENTS: "Palavra-chave 'ingredients'",
    TokenType.PREPARATION: "Palavra-chave 'preparation'",
    TokenType.ADD: "Comando 'add'",
    TokenType.MIX: "Comando 'mix'",
    TokenType.HEAT: "Comando 'heat'",
    TokenType.WAIT: "Comando 'wait'",
    TokenType.SERVE: "Comando 'serve'",
    TokenType.REPEAT: "Comando 'repeat'",
    TokenType.TIMES: "Palavra-chave 'times'",
    TokenType.LBRACE: "Delimitador '{'",
    TokenType.RBRACE: "Delimitador '}'",
    TokenType.SEMICOLON: "Delimitador ';'",
    TokenType.IDENTIFIER: "Identificador",
    TokenType.NUMBER: "Número inteiro",
    TokenType.TIME: "Tempo (com unidade)",
    TokenType.TEMPERATURE: "Temperatura (com unidade)",
    TokenType.EOF: "Fim de arquivo",
}


def token_to_string(token: Token) -> str:
    """
    Converte token para string descritiva
    
    Args:
        token: Token a ser convertido
        
    Returns:
        String formatada com informações do token
    """
    desc = TOKEN_DESCRIPTIONS.get(token.type, "Desconhecido")
    return f"{desc:30s} | Valor: '{token.value:15s}' | Posição: {token.line}:{token.column}"


def print_tokens_table(tokens):
    """
    Imprime tabela formatada de tokens
    
    Args:
        tokens: Lista de tokens a imprimir
    """
    print("\n" + "=" * 80)
    print("TABELA DE TOKENS")
    print("=" * 80)
    print(f"{'#':<5} {'Tipo':<20} {'Valor':<20} {'Linha:Coluna':<15}")
    print("-" * 80)
    
    for i, token in enumerate(tokens, 1):
        print(f"{i:<5} {token.type.value:<20} {token.value:<20} {token.line}:{token.column}")
    
    print("=" * 80)


def validate_token_sequence(tokens):
    """
    Valida sequência básica de tokens
    
    Args:
        tokens: Lista de tokens a validar
        
    Returns:
        tuple: (is_valid, errors)
    """
    errors = []
    
    # Deve começar com RECIPE
    if not tokens or tokens[0].type != TokenType.RECIPE:
        errors.append("Programa deve começar com 'recipe'")
    
    # Deve terminar com EOF
    if tokens and tokens[-1].type != TokenType.EOF:
        errors.append("Última token deve ser EOF")
    
    # Verificar balanceamento de chaves
    brace_count = 0
    for token in tokens:
        if token.type == TokenType.LBRACE:
            brace_count += 1
        elif token.type == TokenType.RBRACE:
            brace_count -= 1
        
        if brace_count < 0:
            errors.append(f"Chave fechada sem correspondente na linha {token.line}")
    
    if brace_count > 0:
        errors.append("Chaves não balanceadas - faltam fechamentos")
    
    return (len(errors) == 0, errors)


# Exemplos de padrões válidos
VALID_PATTERNS = {
    'IDENTIFICADOR': [
        'leite_condensado',
        'chocolate_em_po',
        'acucar',
        'Brigadeiro',
        'ingrediente123',
    ],
    'TEMPO': [
        '5s',
        '30min',
        '2h',
        '90min',
    ],
    'TEMPERATURA': [
        '100C',
        '180C',
        '350F',
    ],
    'NÚMERO': [
        '0',
        '42',
        '1000',
    ],
}


# Exemplos de padrões inválidos
INVALID_PATTERNS = {
    'IDENTIFICADOR': [
        ('1_ingrediente', 'Não pode começar com dígito'),
        ('ingrediente-nome', 'Hífen não permitido'),
        ('açúcar', 'Acentos não permitidos'),
        ('add', 'Palavra-chave reservada'),
    ],
    'TEMPO': [
        ('5', 'Falta unidade de tempo'),
        ('min', 'Falta número'),
        ('5 min', 'Espaço não permitido'),
    ],
    'TEMPERATURA': [
        ('180', 'Falta unidade de temperatura'),
        ('180c', 'Use C maiúsculo'),
        ('180 C', 'Espaço não permitido'),
    ],
}


if __name__ == '__main__':
    print("DoceLang - Definições de Tokens")
    print("=" * 60)
    
    print("\nPadrões VÁLIDOS:")
    print("-" * 60)
    for category, patterns in VALID_PATTERNS.items():
        print(f"\n{category}:")
        for pattern in patterns:
            print(f"  ✅ {pattern}")
    
    print("\n\nPadrões INVÁLIDOS:")
    print("-" * 60)
    for category, patterns in INVALID_PATTERNS.items():
        print(f"\n{category}:")
        for pattern, reason in patterns:
            print(f"  ❌ {pattern:<20} - {reason}")
