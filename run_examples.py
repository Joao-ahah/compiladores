"""
DoceLang - Executor de Exemplos
================================

Script para executar o lexer em todos os arquivos de exemplo .doce

Autor: Projeto Compiladores 2025
"""

import os
import sys
from pathlib import Path

# Adicionar diretório do lexer ao path
sys.path.insert(0, str(Path(__file__).parent / 'lexer'))

from lexer import AnalisadorLexico, ErroLexico
from tokens import imprimir_tabela_tokens, validar_sequencia_tokens


def process_file(filepath):
    """Processa um arquivo .doce"""
    print("\n" + "=" * 70)
    print(f"📄 Arquivo: {filepath}")
    print("=" * 70)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        print(f"\n📝 Código ({len(code)} caracteres, {len(code.splitlines())} linhas):")
        print("-" * 70)
        print(code)
        print("-" * 70)
        
        # Tokenizar
        analisador = AnalisadorLexico(code)
        tokens = analisador.tokenizar()
        
        print(f"\n✅ Tokenização concluída: {len(tokens)} tokens")
        
        # Estatísticas
        stats = {}
        for token in tokens:
            type_name = token.tipo.value
            stats[type_name] = stats.get(type_name, 0) + 1
        
        print("\n📊 Estatísticas de Tokens:")
        for token_type, count in sorted(stats.items(), key=lambda x: -x[1]):
            print(f"  {token_type:20s}: {count:3d}")
        
        # Tabela de tokens
        print("\n📋 Tabela de Tokens:")
        imprimir_tabela_tokens(tokens)
        
        # Validação
        eh_valido, erros = validar_sequencia_tokens(tokens)
        
        if eh_valido:
            print("\n✅ VALIDAÇÃO: Sequência de tokens válida!")
        else:
            print("\n⚠️  VALIDAÇÃO: Problemas encontrados:")
            for erro in erros:
                print(f"  - {erro}")
        
        return True, len(tokens), stats
        
    except ErroLexico as e:
        print(f"\n❌ ERRO LÉXICO: {e}")
        return False, 0, {}
        
    except FileNotFoundError:
        print(f"\n❌ ERRO: Arquivo não encontrado!")
        return False, 0, {}
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        return False, 0, {}


def main():
    """Função principal"""
    print("=" * 70)
    print("DOCELANG - ANÁLISE LÉXICA DE EXEMPLOS")
    print("=" * 70)
    
    # Diretório de exemplos
    examples_dir = Path(__file__).parent / 'examples'
    
    if not examples_dir.exists():
        print(f"\n❌ Diretório de exemplos não encontrado: {examples_dir}")
        return
    
    # Listar arquivos .doce
    doce_files = list(examples_dir.glob('*.doce'))
    
    if not doce_files:
        print(f"\n⚠️  Nenhum arquivo .doce encontrado em {examples_dir}")
        return
    
    print(f"\n📂 Encontrados {len(doce_files)} arquivo(s) .doce:")
    for f in doce_files:
        print(f"  - {f.name}")
    
    # Processar cada arquivo
    results = []
    for filepath in sorted(doce_files):
        success, token_count, stats = process_file(filepath)
        results.append({
            'file': filepath.name,
            'success': success,
            'tokens': token_count,
            'stats': stats
        })
    
    # Resumo final
    print("\n" + "=" * 70)
    print("RESUMO FINAL")
    print("=" * 70)
    
    successful = sum(1 for r in results if r['success'])
    failed = len(results) - successful
    
    print(f"\n✅ Sucesso: {successful}/{len(results)}")
    print(f"❌ Falhas:  {failed}/{len(results)}")
    
    if successful > 0:
        print("\n📊 Estatísticas Gerais:")
        total_tokens = sum(r['tokens'] for r in results if r['success'])
        print(f"  Total de tokens: {total_tokens}")
        print(f"  Média por arquivo: {total_tokens / successful:.1f}")
        
        # Combinar estatísticas
        combined_stats = {}
        for r in results:
            if r['success']:
                for token_type, count in r['stats'].items():
                    combined_stats[token_type] = combined_stats.get(token_type, 0) + count
        
        print("\n  Tokens mais comuns:")
        for token_type, count in sorted(combined_stats.items(), key=lambda x: -x[1])[:10]:
            print(f"    {token_type:20s}: {count:3d}")
    
    print("\n" + "=" * 70)
    
    if failed == 0:
        print("🎉 TODOS OS EXEMPLOS FORAM PROCESSADOS COM SUCESSO! 🎉")
    else:
        print(f"⚠️  {failed} exemplo(s) falharam")
    
    print("=" * 70)


if __name__ == '__main__':
    main()
