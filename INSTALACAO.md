# 🚀 DoceLang - Instalação e Setup

## 📋 Índice
1. [Requisitos](#requisitos)
2. [Instalação do Python](#instalação-do-python)
3. [Verificação do Ambiente](#verificação-do-ambiente)
4. [Primeiro Uso](#primeiro-uso)
5. [Solução de Problemas](#solução-de-problemas)

---

## ✅ Requisitos

### Sistema Operacional
- Windows 7 ou superior ✅
- Linux (qualquer distribuição recente) ✅
- macOS 10.12 ou superior ✅

### Software Necessário
- **Python 3.7 ou superior** (OBRIGATÓRIO)
- Editor de texto (VS Code, Notepad++, Sublime, etc.) (Opcional)

### Espaço em Disco
- Mínimo: 50 MB
- Recomendado: 100 MB

---

## 🐍 Instalação do Python

### Windows

#### Opção 1: Microsoft Store (Mais Fácil)
1. Abra a **Microsoft Store**
2. Busque por "Python 3.12" ou "Python 3.11"
3. Clique em **Instalar**
4. Aguarde a instalação

#### Opção 2: Site Oficial
1. Acesse: https://www.python.org/downloads/
2. Clique em **Download Python 3.x.x**
3. Execute o instalador baixado
4. ⚠️ **IMPORTANTE:** Marque a opção **"Add Python to PATH"**
5. Clique em **Install Now**
6. Aguarde a conclusão

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Linux (Fedora/RHEL)
```bash
sudo dnf install python3 python3-pip
```

### macOS
```bash
# Usando Homebrew
brew install python3

# OU baixe do site oficial
# https://www.python.org/downloads/macos/
```

---

## 🔍 Verificação do Ambiente

### 1. Verificar Python
Abra o terminal/prompt e execute:

```bash
python --version
```

**Resultado esperado:**
```
Python 3.x.x
```

Se não funcionar, tente:
```bash
python3 --version
```

### 2. Verificar pip (gerenciador de pacotes)
```bash
pip --version
```

**Resultado esperado:**
```
pip xx.x.x from ... (python 3.x)
```

### 3. Testar Python
```bash
python -c "print('Hello, DoceLang!')"
```

**Resultado esperado:**
```
Hello, DoceLang!
```

---

## 🎯 Primeiro Uso

### 1. Baixar/Clonar o Projeto

Se você tem o projeto em ZIP:
```bash
# Extraia o arquivo ZIP para uma pasta
# Por exemplo: C:\Users\SEU_USUARIO\DoceLang
```

Se você tem acesso ao Git:
```bash
git clone [URL_DO_REPOSITORIO]
cd COMPILADORES
```

### 2. Navegar até o Diretório
```bash
# Windows
cd C:\Users\juanp\OneDrive\Área de Trabalho\COMPILADORES

# Linux/Mac
cd ~/COMPILADORES
```

### 3. Executar o Menu de Build (Windows)
```bash
build.bat
```

### 4. Executar Testes (Todos os sistemas)
```bash
# Testar o lexer
python lexer/test_lexer.py

# Processar exemplos
python run_examples.py

# Ver exemplos de API
python api_examples.py
```

---

## 🧪 Teste Rápido

### Teste 1: Verificar estrutura do projeto
```bash
# Windows
dir

# Linux/Mac
ls -la
```

**Você deve ver:**
- README.md
- build.bat
- docs/
- examples/
- lexer/
- grammar/

### Teste 2: Executar exemplo simples
```bash
python -c "from lexer.lexer import DoceLangLexer; lexer = DoceLangLexer('recipe Test { ingredients { x; } preparation { add x; serve; } }'); tokens = lexer.tokenize(); print(f'OK - {len(tokens)} tokens')"
```

**Resultado esperado:**
```
OK - 15 tokens
```

### Teste 3: Processar arquivo .doce
```bash
python -c "from lexer.lexer import DoceLangLexer; code = open('examples/brigadeiro.doce', 'r', encoding='utf-8').read(); tokens = DoceLangLexer(code).tokenize(); print(f'Brigadeiro: {len(tokens)} tokens')"
```

**Resultado esperado:**
```
Brigadeiro: 78 tokens
```

---

## 🐛 Solução de Problemas

### Problema 1: "Python não é reconhecido como comando"

**Causa:** Python não está no PATH do sistema

**Solução Windows:**
1. Desinstale e reinstale o Python
2. ⚠️ Marque a opção **"Add Python to PATH"**
3. OU adicione manualmente ao PATH:
   - Painel de Controle → Sistema → Configurações Avançadas
   - Variáveis de Ambiente
   - Adicionar `C:\Python3x` ao PATH

**Solução Linux/Mac:**
Use `python3` ao invés de `python`:
```bash
python3 --version
python3 lexer/test_lexer.py
```

### Problema 2: "ModuleNotFoundError: No module named 'lexer'"

**Causa:** Executando de diretório errado

**Solução:**
```bash
# Navegue até a raiz do projeto
cd C:\Users\juanp\OneDrive\Área de Trabalho\COMPILADORES

# Execute novamente
python lexer/test_lexer.py
```

### Problema 3: "UnicodeDecodeError"

**Causa:** Encoding incorreto

**Solução:**
Os arquivos já usam `encoding='utf-8'`. Se o erro persistir:
```bash
# Windows - Configurar UTF-8
chcp 65001

# Depois execute o comando
python lexer/test_lexer.py
```

### Problema 4: Erro ao abrir arquivos .doce

**Causa:** Caminho do arquivo incorreto

**Solução:**
```bash
# Use caminhos absolutos ou relativos corretos
# Sempre execute da raiz do projeto

# Windows
python run_examples.py

# Se não funcionar, tente:
python -m run_examples
```

### Problema 5: "Permission denied"

**Causa:** Falta de permissões

**Solução Linux/Mac:**
```bash
chmod +x build.bat
chmod +x lexer/*.py
chmod +x *.py
```

**Solução Windows:**
Execute o terminal como Administrador

### Problema 6: Mensagens em português não aparecem corretamente

**Causa:** Terminal não suporta UTF-8

**Solução Windows:**
```bash
# Configurar código de página UTF-8
chcp 65001

# Executar comando
python lexer/test_lexer.py
```

**Solução Linux/Mac:**
```bash
export LANG=pt_BR.UTF-8
python lexer/test_lexer.py
```

---

## 📚 Estrutura de Diretórios Explicada

```
COMPILADORES/
│
├── build.bat                # [Windows] Script de build interativo
├── run_examples.py          # Processa todos os exemplos .doce
├── api_examples.py          # Demonstrações de uso da API
│
├── lexer/                   # Implementação do lexer
│   ├── lexer.py            # Analisador léxico
│   ├── tokens.py           # Utilitários de tokens
│   └── test_lexer.py       # Testes automatizados
│
├── examples/                # Exemplos de código DoceLang
│   ├── brigadeiro.doce
│   ├── beijinho.doce
│   ├── bolo-simples.doce
│   ├── pudim.doce
│   └── receita-complexa.doce
│
├── docs/                    # Documentação completa
│   ├── 01-descricao-geral.md
│   ├── 02-especificacao.md
│   └── ... (8 arquivos)
│
└── grammar/                 # Gramáticas formais
    ├── docelang.bnf
    └── docelang.ebnf
```

---

## 🎯 Comandos Essenciais

### Executar tudo (verificação completa)
```bash
# Windows
build.bat
# Escolher opção 1 e depois opção 2

# Linux/Mac
python3 lexer/test_lexer.py
python3 run_examples.py
```

### Processar um arquivo específico
```bash
python -c "from lexer.lexer import DoceLangLexer; from lexer.tokens import print_tokens_table; code=open('examples/brigadeiro.doce', 'r', encoding='utf-8').read(); tokens=DoceLangLexer(code).tokenize(); print_tokens_table(tokens)"
```

### Ver estatísticas de um exemplo
```bash
python -c "from lexer.lexer import DoceLangLexer; code=open('examples/brigadeiro.doce', 'r', encoding='utf-8').read(); tokens=DoceLangLexer(code).tokenize(); print(f'Tokens: {len(tokens)}'); stats = {}; [stats.update({t.type.value: stats.get(t.type.value, 0) + 1}) for t in tokens]; [print(f'{k}: {v}') for k, v in sorted(stats.items())]"
```

---

## 📖 Próximos Passos

Após a instalação bem-sucedida:

1. ✅ Leia o [GUIA-RAPIDO.md](GUIA-RAPIDO.md)
2. ✅ Execute `python lexer/test_lexer.py`
3. ✅ Execute `python run_examples.py`
4. ✅ Leia a documentação em `docs/01-descricao-geral.md`
5. ✅ Explore os exemplos em `examples/`
6. ✅ Teste a API com `python api_examples.py`

---

## 🆘 Ajuda Adicional

### Recursos Úteis
- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)
- [Tutorial Python para iniciantes](https://docs.python.org/pt-br/3/tutorial/)
- [GUIA-RAPIDO.md](GUIA-RAPIDO.md) - Uso do projeto

### Verificação de Saúde do Sistema
```bash
# Criar arquivo test_system.py
python -c "import sys; print(f'Python {sys.version}'); print(f'Plataforma: {sys.platform}'); print(f'Encoding: {sys.getdefaultencoding()}')"
```

**Resultado esperado:**
```
Python 3.x.x (...)
Plataforma: win32 / linux / darwin
Encoding: utf-8
```

---

## ✅ Checklist de Instalação

Marque conforme for completando:

- [ ] Python 3.7+ instalado
- [ ] Comando `python --version` funciona
- [ ] Comando `pip --version` funciona
- [ ] Projeto baixado/extraído
- [ ] Navegado até o diretório COMPILADORES
- [ ] Executado `python lexer/test_lexer.py` com sucesso
- [ ] Executado `python run_examples.py` com sucesso
- [ ] Lido o GUIA-RAPIDO.md

**Quando todos estiverem marcados: 🎉 INSTALAÇÃO COMPLETA! 🎉**

---

## 🔧 Configurações Avançadas (Opcional)

### Criar ambiente virtual Python
```bash
# Criar ambiente
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Depois use normalmente
python lexer/test_lexer.py
```

### Instalar IDE (Opcional mas Recomendado)

**Visual Studio Code:**
1. Baixe: https://code.visualstudio.com/
2. Instale a extensão "Python"
3. Abra a pasta do projeto
4. Execute os scripts pelo terminal integrado

**PyCharm Community:**
1. Baixe: https://www.jetbrains.com/pycharm/download/
2. Abra o projeto
3. Configure o interpretador Python
4. Execute os scripts

---

**Desenvolvido com 💙 para facilitar o uso do DoceLang**  
*UFC - Campus Russas | 2025*
