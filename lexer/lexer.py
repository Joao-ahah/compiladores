"""
DoceLang Lexer (Analisador Léxico)
===================================

Implementação do analisador léxico para a linguagem DoceLang.
Converte código-fonte em sequência de tokens.

Autor: Projeto Compiladores 2025
Data: 15 de novembro de 2025
"""

import re
from enum import Enum
from typing import List, Optional
from dataclasses import dataclass


class TokenType(Enum):
    """Tipos de tokens da linguagem DoceLang"""
    
    # Palavras-chave
    RECIPE = 'RECIPE'
    INGREDIENTS = 'INGREDIENTS'
    PREPARATION = 'PREPARATION'
    ADD = 'ADD'
    MIX = 'MIX'
    HEAT = 'HEAT'
    WAIT = 'WAIT'
    SERVE = 'SERVE'
    REPEAT = 'REPEAT'
    TIMES = 'TIMES'
    
    # Delimitadores
    LBRACE = 'LBRACE'
    RBRACE = 'RBRACE'
    SEMICOLON = 'SEMICOLON'
    
    # Literais
    IDENTIFIER = 'IDENTIFIER'
    NUMBER = 'NUMBER'
    TIME = 'TIME'
    TEMPERATURE = 'TEMPERATURE'
    
    # Especiais
    EOF = 'EOF'
    
    def __str__(self):
        return self.value


@dataclass
class Token:
    """Representa um token identificado pelo lexer"""
    type: TokenType
    value: str
    line: int
    column: int
    
    def __repr__(self):
        return f"Token({self.type.value}, '{self.value}', {self.line}:{self.column})"


class LexicalError(Exception):
    """Exceção para erros léxicos"""
    pass


class DoceLangLexer:
    """Analisador léxico para DoceLang"""
    
    # Palavras-chave da linguagem
    KEYWORDS = {
        'recipe': TokenType.RECIPE,
        'ingredients': TokenType.INGREDIENTS,
        'preparation': TokenType.PREPARATION,
        'add': TokenType.ADD,
        'mix': TokenType.MIX,
        'heat': TokenType.HEAT,
        'wait': TokenType.WAIT,
        'serve': TokenType.SERVE,
        'repeat': TokenType.REPEAT,
        'times': TokenType.TIMES,
    }
    
    # Padrões regex (ordem importa!)
    PATTERNS = [
        # Comentários
        (r'//[^\n]*', None),  # Comentário de linha
        (r'/\*.*?\*/', None),  # Comentário de bloco
        
        # Tempo (antes de número)
        (r'\d+(s|min|h)', TokenType.TIME),
        
        # Temperatura (antes de número)
        (r'\d+(C|F)', TokenType.TEMPERATURE),
        
        # Número
        (r'\d+', TokenType.NUMBER),
        
        # Identificador (palavra-chave ou identificador)
        (r'[a-zA-Z][a-zA-Z0-9_]*', 'KEYWORD_OR_IDENTIFIER'),
        
        # Delimitadores
        (r'\{', TokenType.LBRACE),
        (r'\}', TokenType.RBRACE),
        (r';', TokenType.SEMICOLON),
        
        # Espaços em branco (ignorar)
        (r'[ \t\n\r]+', None),
    ]
    
    def __init__(self, source_code: str):
        """
        Inicializa o lexer com código-fonte
        
        Args:
            source_code: String contendo o código DoceLang
        """
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def tokenize(self) -> List[Token]:
        """
        Realiza análise léxica completa do código
        
        Returns:
            Lista de tokens identificados
            
        Raises:
            LexicalError: Se encontrar caractere inválido
        """
        while self.position < len(self.source):
            matched = False
            
            # Tentar casar cada padrão
            for pattern, token_type in self.PATTERNS:
                regex = re.compile(pattern, re.DOTALL)  # DOTALL permite . capturar \n
                match = regex.match(self.source, self.position)
                
                if match:
                    value = match.group(0)
                    
                    # Pular comentários e espaços
                    if token_type is None:
                        # Atualizar linha/coluna
                        for char in value:
                            if char == '\n':
                                self.line += 1
                                self.column = 1
                            else:
                                self.column += 1
                    
                    # Identificadores e palavras-chave
                    elif token_type == 'KEYWORD_OR_IDENTIFIER':
                        actual_type = self.KEYWORDS.get(value, TokenType.IDENTIFIER)
                        token = Token(actual_type, value, self.line, self.column)
                        self.tokens.append(token)
                        self.column += len(value)
                    
                    # Outros tokens
                    else:
                        token = Token(token_type, value, self.line, self.column)
                        self.tokens.append(token)
                        self.column += len(value)
                    
                    self.position = match.end()
                    matched = True
                    break
            
            if not matched:
                char = self.source[self.position]
                raise LexicalError(
                    f"Caractere inválido '{char}' na linha {self.line}, "
                    f"coluna {self.column}"
                )
        
        # Adicionar EOF
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens
    
    def get_tokens(self) -> List[Token]:
        """Retorna lista de tokens (tokeniza se necessário)"""
        if not self.tokens:
            self.tokenize()
        return self.tokens


def main():
    """Função principal para teste do lexer"""
    
    # Código de exemplo
    example_code = """
    /*
     * Exemplo: Brigadeiro
     */
    recipe Brigadeiro {
        ingredients {
            leite_condensado;
            chocolate_em_po;
            manteiga;
        }
        
        preparation {
            add leite_condensado;
            add chocolate_em_po;
            add manteiga;
            heat 180C;
            mix 15min;
            wait 2h;
            serve;
        }
    }
    """
    
    print("=" * 60)
    print("DOCELANG LEXER - ANÁLISE LÉXICA")
    print("=" * 60)
    print("\nCódigo de entrada:")
    print("-" * 60)
    print(example_code)
    print("-" * 60)
    
    try:
        lexer = DoceLangLexer(example_code)
        tokens = lexer.tokenize()
        
        print(f"\n✅ Análise léxica concluída com sucesso!")
        print(f"📊 Total de tokens: {len(tokens)}\n")
        
        print("Tokens identificados:")
        print("-" * 60)
        
        for i, token in enumerate(tokens, 1):
            print(f"{i:3d}. {token}")
        
    except LexicalError as e:
        print(f"\n❌ ERRO LÉXICO: {e}")


if __name__ == '__main__':
    main()
