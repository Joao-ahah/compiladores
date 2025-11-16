"""
DoceLang Lexer Package
======================

Analisador léxico para a linguagem DoceLang

Autor: Projeto Compiladores 2025
"""

from .lexer import (
    TipoToken,
    Token,
    ErroLexico,
    AnalisadorLexico
)

from .tokens import (
    DESCRICOES_TOKENS,
    token_para_string,
    imprimir_tabela_tokens,
    validar_sequencia_tokens,
    PADROES_VALIDOS,
    PADROES_INVALIDOS
)

__all__ = [
    # Classes principais
    'TipoToken',
    'Token',
    'ErroLexico',
    'AnalisadorLexico',
    
    # Utilitários
    'DESCRICOES_TOKENS',
    'token_para_string',
    'imprimir_tabela_tokens',
    'validar_sequencia_tokens',
    'PADROES_VALIDOS',
    'PADROES_INVALIDOS',
]
