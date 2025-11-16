"""
DoceLang - Definições de Tokens
================================

Definições e utilitários para tokens da linguagem DoceLang.

Autor: Projeto Compiladores 2025
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .lexer import TipoToken, Token
else:
    try:
        from lexer.lexer import TipoToken, Token
    except ImportError:
        from .lexer import TipoToken, Token


# Mapeamento de tipos de tokens para descrições legíveis
DESCRICOES_TOKENS = {
    TipoToken.RECEITA: "Palavra-chave 'recipe'",
    TipoToken.INGREDIENTES: "Palavra-chave 'ingredients'",
    TipoToken.PREPARO: "Palavra-chave 'preparation'",
    TipoToken.ADICIONAR: "Comando 'add'",
    TipoToken.MISTURAR: "Comando 'mix'",
    TipoToken.AQUECER: "Comando 'heat'",
    TipoToken.ESPERAR: "Comando 'wait'",
    TipoToken.SERVIR: "Comando 'serve'",
    TipoToken.REPETIR: "Comando 'repeat'",
    TipoToken.VEZES: "Palavra-chave 'times'",
    TipoToken.CHAVE_ESQ: "Delimitador '{'",
    TipoToken.CHAVE_DIR: "Delimitador '}'",
    TipoToken.PONTO_VIRGULA: "Delimitador ';'",
    TipoToken.IDENTIFICADOR: "Identificador",
    TipoToken.NUMERO: "Número inteiro",
    TipoToken.TEMPO: "Tempo (com unidade)",
    TipoToken.TEMPERATURA: "Temperatura (com unidade)",
    TipoToken.FIM_ARQUIVO: "Fim de arquivo",
}


def token_para_string(token: Token) -> str:
    """
    Converte token para string descritiva
    
    Args:
        token: Token a ser convertido
        
    Returns:
        String formatada com informações do token
    """
    desc = DESCRICOES_TOKENS.get(token.tipo, "Desconhecido")
    return f"{desc:30s} | Valor: '{token.valor:15s}' | Posição: {token.linha}:{token.coluna}"


def imprimir_tabela_tokens(tokens):
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
        print(f"{i:<5} {token.tipo.value:<20} {token.valor:<20} {token.linha}:{token.coluna}")
    
    print("=" * 80)


def validar_sequencia_tokens(tokens):
    """
    Valida sequência básica de tokens
    
    Args:
        tokens: Lista de tokens a validar
        
    Returns:
        tuple: (eh_valido, erros)
    """
    erros = []
    
    # Deve começar com RECEITA
    if not tokens or tokens[0].tipo != TipoToken.RECEITA:
        erros.append("Programa deve começar com 'recipe'")
    
    # Deve terminar com FIM_ARQUIVO
    if tokens and tokens[-1].tipo != TipoToken.FIM_ARQUIVO:
        erros.append("Última token deve ser FIM_ARQUIVO")
    
    # Verificar balanceamento de chaves
    contador_chaves = 0
    for token in tokens:
        if token.tipo == TipoToken.CHAVE_ESQ:
            contador_chaves += 1
        elif token.tipo == TipoToken.CHAVE_DIR:
            contador_chaves -= 1
        
        if contador_chaves < 0:
            erros.append(f"Chave fechada sem correspondente na linha {token.linha}")
    
    if contador_chaves > 0:
        erros.append("Chaves não balanceadas - faltam fechamentos")
    
    return (len(erros) == 0, erros)


# Exemplos de padrões válidos
PADROES_VALIDOS = {
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
PADROES_INVALIDOS = {
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
    for categoria, padroes in PADROES_VALIDOS.items():
        print(f"\n{categoria}:")
        for padrao in padroes:
            print(f"  ✅ {padrao}")
    
    print("\n\nPadrões INVÁLIDOS:")
    print("-" * 60)
    for categoria, padroes in PADROES_INVALIDOS.items():
        print(f"\n{categoria}:")
        for padrao, motivo in padroes:
            print(f"  ❌ {padrao:<20} - {motivo}")
