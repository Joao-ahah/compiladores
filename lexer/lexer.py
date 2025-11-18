import re
from enum import Enum
from typing import List, Optional
from dataclasses import dataclass


class TipoToken(Enum):
    """Tipos de tokens da linguagem DoceLang"""
    
    # Palavras-chave
    RECEITA = 'RECEITA'
    INGREDIENTES = 'INGREDIENTES'
    PREPARO = 'PREPARO'
    ADICIONAR = 'ADICIONAR'
    MISTURAR = 'MISTURAR'
    AQUECER = 'AQUECER'
    ESPERAR = 'ESPERAR'
    SERVIR = 'SERVIR'
    REPETIR = 'REPETIR'
    VEZES = 'VEZES'
    
    # Delimitadores
    CHAVE_ESQ = 'CHAVE_ESQ'
    CHAVE_DIR = 'CHAVE_DIR'
    PONTO_VIRGULA = 'PONTO_VIRGULA'
    
    # Literais
    IDENTIFICADOR = 'IDENTIFICADOR'
    NUMERO = 'NUMERO'
    TEMPO = 'TEMPO'
    TEMPERATURA = 'TEMPERATURA'
    
    # Especiais
    FIM_ARQUIVO = 'FIM_ARQUIVO'
    
    def __str__(self):
        return self.value


@dataclass
class Token:
    """Representa um token identificado pelo lexer"""
    tipo: TipoToken
    valor: str
    linha: int
    coluna: int
    
    def __repr__(self):
        return f"Token({self.tipo.value}, '{self.valor}', {self.linha}:{self.coluna})"


class ErroLexico(Exception):
    """Exceção para erros léxicos"""
    pass


class AnalisadorLexico:
    """Analisador léxico para DoceLang"""
    
    # Palavras-chave da linguagem
    PALAVRAS_CHAVE = {
        'recipe': TipoToken.RECEITA,
        'ingredients': TipoToken.INGREDIENTES,
        'preparation': TipoToken.PREPARO,
        'add': TipoToken.ADICIONAR,
        'mix': TipoToken.MISTURAR,
        'heat': TipoToken.AQUECER,
        'wait': TipoToken.ESPERAR,
        'serve': TipoToken.SERVIR,
        'repeat': TipoToken.REPETIR,
        'times': TipoToken.VEZES,
    }
    
    # Padrões regex 
    PADROES = [
        # Comentários
        (r'//[^\n]*', None),  
        (r'/\*.*?\*/', None), 
        
        # Tempo (antes de número)
        (r'\d+(s|min|h)', TipoToken.TEMPO),
        
        # Temperatura (antes de número)
        (r'\d+(C|F)', TipoToken.TEMPERATURA),
        
        # Número
        (r'\d+', TipoToken.NUMERO),
        
        # Identificador palavra-chave ou identificador
        (r'[a-zA-Z][a-zA-Z0-9_]*', 'PALAVRA_CHAVE_OU_IDENTIFICADOR'),
        
        # Delimitadores
        (r'\{', TipoToken.CHAVE_ESQ),
        (r'\}', TipoToken.CHAVE_DIR),
        (r';', TipoToken.PONTO_VIRGULA),
        
        # Espaços em branco ignora
        (r'[ \t\n\r]+', None),
    ]
    
    def __init__(self, codigo_fonte: str):
        self.fonte = codigo_fonte
        self.posicao = 0
        self.linha = 1
        self.coluna = 1
        self.tokens: List[Token] = []
    
    def tokenizar(self) -> List[Token]:
        
        while self.posicao < len(self.fonte):
            casou = False
            
            # Tentar casar cada padrão
            for padrao, tipo_token in self.PADROES:
                regex = re.compile(padrao, re.DOTALL)  # DOTALL permite . capturar \n
                casamento = regex.match(self.fonte, self.posicao)
                
                if casamento:
                    valor = casamento.group(0)
                    
                    # Pular comentários e espaços
                    if tipo_token is None:
                        # Atualizar linha/coluna
                        for char in valor:
                            if char == '\n':
                                self.linha += 1
                                self.coluna = 1
                            else:
                                self.coluna += 1
                    
                    # Identificadores e palavras-chave
                    elif tipo_token == 'PALAVRA_CHAVE_OU_IDENTIFICADOR':
                        tipo_real = self.PALAVRAS_CHAVE.get(valor, TipoToken.IDENTIFICADOR)
                        token = Token(tipo_real, valor, self.linha, self.coluna)
                        self.tokens.append(token)
                        self.coluna += len(valor)
                    
                    # Outros tokens
                    else:
                        token = Token(tipo_token, valor, self.linha, self.coluna)
                        self.tokens.append(token)
                        self.coluna += len(valor)
                    
                    self.posicao = casamento.end()
                    casou = True
                    break
            
            if not casou:
                char = self.fonte[self.posicao]
                raise ErroLexico(
                    f"Caractere inválido '{char}' na linha {self.linha}, "
                    f"coluna {self.coluna}"
                )
        
        # Adicionar EOF
        self.tokens.append(Token(TipoToken.FIM_ARQUIVO, '', self.linha, self.coluna))
        return self.tokens
    
    def obter_tokens(self) -> List[Token]:
        """Retorna lista de tokens (tokeniza se necessário)"""
        if not self.tokens:
            self.tokenizar()
        return self.tokens


def main():
    """Função principal para teste do lexer"""
    
    # Código de exemplo
    codigo_exemplo = """
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
    print(codigo_exemplo)
    print("-" * 60)
    
    try:
        lexer = AnalisadorLexico(codigo_exemplo)
        tokens = lexer.tokenizar()
        
        print(f"\n✅ Análise léxica concluída com sucesso!")
        print(f"📊 Total de tokens: {len(tokens)}\n")
        
        print("Tokens identificados:")
        print("-" * 60)
        
        for i, token in enumerate(tokens, 1):
            print(f"{i:3d}. {token}")
        
    except ErroLexico as e:
        print(f"\n❌ ERRO LÉXICO: {e}")


if __name__ == '__main__':
    main()
