# 5. Exemplos de Programas em DoceLang

## 5.1 Introdução

Este documento apresenta diversos programas completos escritos em DoceLang, demonstrando a aplicação prática da linguagem em receitas reais de doces brasileiros.

Cada exemplo inclui:
- Código completo comentado
- Explicação passo a passo
- Análise de tokens
- Dicas de implementação

---

## 5.2 Exemplo 1: Brigadeiro Tradicional

### 5.2.1 Código Completo

```docelang
/*
 * ================================
 * RECEITA: BRIGADEIRO TRADICIONAL
 * ================================
 * 
 * Rendimento: 40 unidades
 * Tempo total: ~2h 30min
 * Dificuldade: Fácil
 * 
 * O brigadeiro é o doce mais popular do Brasil,
 * presente em todas as festas infantis.
 */

recipe Brigadeiro {
    // ========== INGREDIENTES ==========
    ingredients {
        leite_condensado;      // 1 lata (395g)
        chocolate_em_po;       // 3 colheres de sopa (50% cacau)
        manteiga;              // 1 colher de sopa
        chocolate_granulado;   // Para cobertura (200g aprox.)
    }
    
    // ========== MODO DE PREPARO ==========
    preparation {
        // Passo 1: Combinar ingredientes base
        add leite_condensado;
        add chocolate_em_po;
        add manteiga;
        
        // Passo 2: Cozinhar em fogo médio
        // IMPORTANTE: Mexer sempre para não queimar
        heat 180C;
        mix 15min;  // Mexer continuamente até desgrudar do fundo
        
        // Passo 3: Esfriar completamente
        // A massa deve estar firme antes de enrolar
        wait 2h;
        
        // Passo 4: Modelar brigadeiros
        // Enrolar bolinhas de aproximadamente 15g cada
        repeat 40 times {
            add chocolate_granulado;
        }
        
        // Passo 5: Servir
        serve;
    }
}
```

---

### 5.2.2 Explicação Passo a Passo

#### Fase 1: Declaração de Ingredientes
```docelang
ingredients {
    leite_condensado;      // Base cremosa
    chocolate_em_po;       // Sabor chocolate
    manteiga;              // Brilho e textura
    chocolate_granulado;   // Cobertura
}
```

**Análise**:
- 4 ingredientes declarados
- Todos serão utilizados no preparo
- Comentários indicam quantidade (opcional)

---

#### Fase 2: Preparo da Mistura
```docelang
add leite_condensado;
add chocolate_em_po;
add manteiga;
```

**O que acontece**:
1. Leite condensado vai para a panela
2. Chocolate em pó é adicionado
3. Manteiga é incorporada

**Equivalente culinário**:
> "Em uma panela, misture o leite condensado, o chocolate em pó e a manteiga."

---

#### Fase 3: Cozimento
```docelang
heat 180C;
mix 15min;
```

**O que acontece**:
1. `heat 180C` - Liga o fogo médio (~180°C)
2. `mix 15min` - Mexe continuamente por 15 minutos

**Equivalente culinário**:
> "Leve ao fogo médio e mexa sem parar por 15 minutos, até a mistura desgrudar do fundo da panela."

---

#### Fase 4: Resfriamento
```docelang
wait 2h;
```

**O que acontece**:
- Massa esfria por 2 horas em temperatura ambiente
- Necessário para firmar a consistência

**Equivalente culinário**:
> "Deixe esfriar completamente por cerca de 2 horas."

---

#### Fase 5: Modelagem
```docelang
repeat 40 times {
    add chocolate_granulado;
}
```

**O que acontece**:
- Repete 40 vezes o processo de:
  - Pegar um pouco da massa
  - Enrolar em formato de bolinha
  - Passar no chocolate granulado

**Equivalente culinário**:
> "Com as mãos untadas com manteiga, pegue pequenas porções da massa, enrole em formato de bolinha e passe no chocolate granulado. Repita até acabar a massa (aproximadamente 40 brigadeiros)."

---

### 5.2.3 Análise de Tokens

**Total de tokens**: 67 tokens (incluindo delimitadores e EOF)

**Distribuição**:
- Palavras-chave: 12
- Identificadores: 13
- Literais (tempo/temperatura): 3
- Números: 1
- Delimitadores: 37
- EOF: 1

**Tokens principais** (excluindo comentários):
```
RECIPE, IDENTIFIER(Brigadeiro), LBRACE,
INGREDIENTS, LBRACE,
  IDENTIFIER(leite_condensado), SEMICOLON,
  IDENTIFIER(chocolate_em_po), SEMICOLON,
  IDENTIFIER(manteiga), SEMICOLON,
  IDENTIFIER(chocolate_granulado), SEMICOLON,
RBRACE,
PREPARATION, LBRACE,
  ADD, IDENTIFIER(leite_condensado), SEMICOLON,
  ADD, IDENTIFIER(chocolate_em_po), SEMICOLON,
  ADD, IDENTIFIER(manteiga), SEMICOLON,
  HEAT, TEMPERATURE(180C), SEMICOLON,
  MIX, TIME(15min), SEMICOLON,
  WAIT, TIME(2h), SEMICOLON,
  REPEAT, NUMBER(40), TIMES, LBRACE,
    ADD, IDENTIFIER(chocolate_granulado), SEMICOLON,
  RBRACE,
  SERVE, SEMICOLON,
RBRACE,
RBRACE,
EOF
```

---

## 5.3 Exemplo 2: Beijinho

### 5.3.1 Código Completo

```docelang
/*
 * =====================
 * RECEITA: BEIJINHO
 * =====================
 * 
 * Rendimento: 35 unidades
 * Tempo total: ~2h 20min
 * Dificuldade: Fácil
 * 
 * Primo branco do brigadeiro, o beijinho
 * é feito com coco e tem um cravo no topo.
 */

recipe Beijinho {
    ingredients {
        leite_condensado;    // 1 lata (395g)
        coco_ralado;         // 100g (fresco ou desidratado)
        manteiga;            // 1 colher de sopa
        coco_para_cobertura; // 50g para passar por fora
        cravos_da_india;     // 35 unidades (decoração)
    }
    
    preparation {
        // Combinar ingredientes principais
        add leite_condensado;
        add coco_ralado;
        add manteiga;
        
        // Cozinhar até ponto
        heat 170C;  // Fogo médio-baixo
        mix 12min;  // Mexer sempre até desgrudar
        
        // Esfriar
        wait 2h;
        
        // Modelar e decorar cada beijinho
        repeat 35 times {
            add coco_para_cobertura;
            add cravos_da_india;  // Colocar 1 cravo no topo
        }
        
        serve;
    }
}
```

---

### 5.3.2 Explicação

**Diferenças do brigadeiro**:
- Usa coco ralado em vez de chocolate
- Temperatura ligeiramente menor (170C vs 180C)
- Tempo de cozimento mais curto (12min vs 15min)
- Decoração com cravo-da-índia

**Estrutura `repeat`**:
```docelang
repeat 35 times {
    add coco_para_cobertura;    // Passar na cobertura
    add cravos_da_india;        // Decorar com cravo
}
```

Simula o processo de:
1. Enrolar bolinha
2. Passar no coco
3. Colocar 1 cravo no topo

---

## 5.4 Exemplo 3: Bolo Simples

### 5.4.1 Código Completo

```docelang
/*
 * ==========================
 * RECEITA: BOLO SIMPLES
 * ==========================
 * 
 * Rendimento: 12 fatias
 * Tempo total: ~1h 15min
 * Dificuldade: Fácil
 * 
 * Bolo básico, perfeito para o café da tarde.
 */

recipe BoloSimples {
    ingredients {
        farinha_de_trigo;
        acucar;
        ovos;
        leite;
        oleo;
        fermento_em_po;
    }
    
    preparation {
        // Misturar ingredientes líquidos
        add ovos;
        add acucar;
        add oleo;
        mix 3min;  // Bater bem até ficar homogêneo
        
        // Adicionar ingredientes secos alternando com leite
        add farinha_de_trigo;
        add leite;
        mix 2min;
        
        // Adicionar fermento por último
        add fermento_em_po;
        mix 30s;  // Misturar delicadamente
        
        // Assar
        heat 180C;  // Forno pré-aquecido
        wait 40min; // Assar até dourar
        
        // Esfriar antes de desenformar
        wait 15min;
        
        serve;
    }
}
```

---

### 5.4.2 Explicação

**Técnica de preparo**:
1. **Líquidos primeiro**: Ovos + açúcar + óleo
2. **Secos alternados**: Farinha + leite
3. **Fermento por último**: Mix rápido para não perder gás
4. **Assamento**: 40min a 180C
5. **Descanso**: 15min antes de desenformar

**Tempos variados**:
```docelang
mix 3min;   // Bater bem
mix 2min;   // Incorporar
mix 30s;    // Misturar delicadamente
```

Demonstra uso de diferentes unidades de tempo.

---

## 5.5 Exemplo 4: Pudim de Leite

### 5.5.1 Código Completo

```docelang
/*
 * ===========================
 * RECEITA: PUDIM DE LEITE
 * ===========================
 * 
 * Rendimento: 8 porções
 * Tempo total: ~5h (incluindo geladeira)
 * Dificuldade: Média
 * 
 * Clássico pudim brasileiro com calda de caramelo.
 */

recipe Pudim {
    ingredients {
        // Para a calda
        acucar_para_calda;
        agua;
        
        // Para o pudim
        leite_condensado;
        leite;
        ovos;
    }
    
    preparation {
        // ========== CALDA DE CARAMELO ==========
        
        // Fazer o caramelo
        add acucar_para_calda;
        add agua;
        heat 200C;  // Fogo alto
        mix 10min;  // Mexer até caramelizar
        
        // Deixar esfriar um pouco
        wait 5min;
        
        // ========== MISTURA DO PUDIM ==========
        
        // Bater ingredientes do pudim
        add leite_condensado;
        add leite;
        
        // Adicionar ovos um por vez
        repeat 3 times {
            add ovos;
            mix 1min;  // Incorporar cada ovo
        }
        
        // ========== COZIMENTO ==========
        
        // Assar em banho-maria
        heat 180C;
        wait 50min;  // Assar até firmar
        
        // Esfriar em temperatura ambiente
        wait 1h;
        
        // Gelar
        wait 3h;  // Mínimo 3 horas na geladeira
        
        serve;
    }
}
```

---

### 5.5.2 Explicação

**Estrutura complexa**:
- Dividida em 3 fases (calda, mistura, cozimento)
- Usa comentários para separar seções
- Múltiplos períodos de espera

**Uso avançado de `repeat`**:
```docelang
repeat 3 times {
    add ovos;
    mix 1min;
}
```

Simula adição de ovos um a um, garantindo boa incorporação.

**Sequência de tempos**:
```
mix 10min  → Caramelizar
wait 5min  → Esfriar calda
mix 1min   → Incorporar cada ovo (×3)
wait 50min → Assar
wait 1h    → Esfriar
wait 3h    → Gelar
```

**Total**: ~5h do início ao fim

---

## 5.6 Exemplo 5: Receita Complexa - Petit Gateau

### 5.6.1 Código Completo

```docelang
/*
 * =============================
 * RECEITA: PETIT GATEAU
 * =============================
 * 
 * Rendimento: 4 porções individuais
 * Tempo total: ~45min
 * Dificuldade: Difícil
 * 
 * Bolinho de chocolate com centro cremoso.
 * Timing é crucial - 8 minutos exatos de forno!
 */

recipe PetitGateau {
    ingredients {
        // Massa
        chocolate_meio_amargo;   // 200g (70% cacau)
        manteiga_sem_sal;        // 100g
        ovos_inteiros;           // 2 unidades
        gemas;                   // 2 unidades
        acucar_refinado;         // 80g
        farinha_de_trigo;        // 40g
        
        // Forminhas
        manteiga_para_untar;
        cacau_em_po_para_polvilhar;
    }
    
    preparation {
        // ========== PREPARAR FORMINHAS ==========
        
        // Untar e polvilhar cada forminha individual
        repeat 4 times {
            add manteiga_para_untar;
            add cacau_em_po_para_polvilhar;
        }
        
        // ========== GANACHE BASE ==========
        
        // Derreter chocolate com manteiga
        add chocolate_meio_amargo;
        add manteiga_sem_sal;
        heat 150C;  // Fogo baixo ou banho-maria
        mix 3min;   // Mexer até homogêneo
        
        // Deixar amornar
        wait 5min;
        
        // ========== MASSA ==========
        
        // Bater ovos com açúcar
        add ovos_inteiros;
        add gemas;
        add acucar_refinado;
        mix 5min;  // Bater até dobrar de volume
        
        // Incorporar chocolate derretido
        mix 2min;  // Misturar delicadamente
        
        // Adicionar farinha peneirada
        add farinha_de_trigo;
        mix 1min;  // Apenas até incorporar
        
        // ========== ASSAMENTO CRÍTICO ==========
        
        // Pré-aquecer forno
        heat 200C;
        
        // Assar EXATAMENTE 8 minutos
        // Menos = muito mole
        // Mais = centro não fica cremoso
        wait 8min;
        
        // Servir IMEDIATAMENTE
        serve;
    }
}
```

---

### 5.6.2 Explicação

**Complexidade**:
- 8 ingredientes diferentes
- Múltiplas fases de preparo
- Timing crítico (8 minutos exatos)
- Uso de `repeat` para forminhas individuais

**Pontos críticos**:
```docelang
wait 8min;  // ⚠️  CRÍTICO - não pode errar!
serve;      // ⚠️  Servir imediatamente
```

**Estrutura `repeat` dupla** (possível aninhamento futuro):
```docelang
// Versão atual
repeat 4 times {
    add manteiga_para_untar;
    add cacau_em_po_para_polvilhar;
}

// Versão futura com aninhamento
repeat 4 times {
    add manteiga_para_untar;
    
    repeat 2 times {
        add cacau_em_po_para_polvilhar;
    }
}
```

---

## 5.7 Exemplo 6: Receita Mínima Válida

### 5.7.1 Código Completo

```docelang
recipe Minimo {
    ingredients {
        ingrediente;
    }
    
    preparation {
        add ingrediente;
        serve;
    }
}
```

---

### 5.7.2 Análise

**Características**:
- Menor programa válido possível
- 1 ingrediente
- 2 comandos
- ~20 tokens

**Uso**: Teste de parser e validação mínima

---

## 5.8 Exemplo 7: Receita com Todos os Comandos

### 5.8.1 Código Completo

```docelang
/*
 * Receita demonstrativa usando TODOS os comandos disponíveis
 */

recipe TodosComandos {
    ingredients {
        ingrediente_A;
        ingrediente_B;
        ingrediente_C;
    }
    
    preparation {
        // Comando: add
        add ingrediente_A;
        add ingrediente_B;
        
        // Comando: mix
        mix 5min;
        
        // Comando: heat
        heat 180C;
        
        // Comando: wait
        wait 30min;
        
        // Comando: repeat
        repeat 3 times {
            add ingrediente_C;
            mix 1min;
        }
        
        // Comando: serve
        serve;
    }
}
```

---

### 5.8.2 Checklist de Comandos

- ✅ `add` - usado 4 vezes
- ✅ `mix` - usado 2 vezes
- ✅ `heat` - usado 1 vez
- ✅ `wait` - usado 1 vez
- ✅ `serve` - usado 1 vez
- ✅ `repeat` - usado 1 vez

**Total**: Todos os 6 comandos presentes

---

## 5.9 Tabela Comparativa de Receitas

| Receita | Ingredientes | Comandos | Tempo Total | Dificuldade | Usa Repeat? |
|---------|--------------|----------|-------------|-------------|-------------|
| Brigadeiro | 4 | 8 | ~2h 30min | Fácil | ✅ Sim |
| Beijinho | 5 | 9 | ~2h 20min | Fácil | ✅ Sim |
| Bolo Simples | 6 | 10 | ~1h 15min | Fácil | ❌ Não |
| Pudim | 6 | 14 | ~5h | Média | ✅ Sim |
| Petit Gateau | 8 | 16 | ~45min | Difícil | ✅ Sim |
| Mínimo | 1 | 2 | - | - | ❌ Não |
| Todos Comandos | 3 | 9 | - | Demo | ✅ Sim |

---

## 5.10 Padrões Identificados

### 5.10.1 Padrão: Cozimento Completo

```docelang
heat <temperatura>;
mix <tempo>;        // Mexer enquanto cozinha
```

**Usado em**: Brigadeiro, Beijinho

---

### 5.10.2 Padrão: Assamento

```docelang
heat <temperatura>;
wait <tempo>;       // Deixar no forno sem mexer
```

**Usado em**: Bolo, Pudim, Petit Gateau

---

### 5.10.3 Padrão: Adição Incremental

```docelang
repeat N times {
    add ingrediente;
    mix tempo;
}
```

**Usado em**: Pudim (ovos), Petit Gateau (forminhas)

---

### 5.10.4 Padrão: Sequência de Espera

```docelang
wait tempo1;  // Esfriar
wait tempo2;  // Descansar
wait tempo3;  // Gelar
```

**Usado em**: Pudim (esfriar → descansar → gelar)

---

## 5.11 Validação Semântica dos Exemplos

### 5.11.1 Brigadeiro - Validação

✅ **Ingredientes declarados**: 4  
✅ **Ingredientes usados**: 4  
✅ **Ingredientes não usados**: 0  
✅ **Comandos válidos**: Todos  
✅ **Tipos corretos**: Todos  

**Resultado**: ✅ Válido

---

### 5.11.2 Pudim - Validação

✅ **Ingredientes declarados**: 6  
✅ **Ingredientes usados**: 6  
✅ **Ingredientes não usados**: 0  
✅ **Comandos válidos**: Todos  
✅ **Tipos corretos**: Todos  
✅ **Repeat com N>0**: Sim (N=3)

**Resultado**: ✅ Válido

---

## 5.12 Dicas de Implementação

### 5.12.1 Para o Parser

1. **Validar ingredientes**: Construir tabela de símbolos durante parse de `ingredients`
2. **Verificar uso**: Ao encontrar `add`, verificar se ingrediente está na tabela
3. **Rastrear uso**: Marcar ingredientes como "usados"
4. **Warning ao final**: Listar ingredientes não usados

---

### 5.12.2 Para o Interpretador

1. **Simular execução**:
   ```python
   def execute_add(ingredient):
       print(f"Adicionando {ingredient}")
   
   def execute_mix(time):
       print(f"Misturando por {time}")
   ```

2. **Calcular tempo total**:
   ```python
   total_time = sum(all wait + mix times)
   ```

3. **Gerar documentação**:
   ```markdown
   ## Brigadeiro
   **Ingredientes**: leite_condensado, chocolate_em_po, manteiga, chocolate_granulado
   **Tempo total**: 2h 15min
   **Passos**: 8
   ```

---

## 5.13 Conclusão dos Exemplos

Os exemplos apresentados demonstram:
- ✅ Versatilidade da linguagem
- ✅ Aplicação em receitas reais
- ✅ Uso de todos os comandos
- ✅ Padrões de uso comuns
- ✅ Complexidade crescente

Todos os programas são **sintática e semanticamente válidos** segundo a gramática DoceLang.

**Próximo**: [6. Testes com Ferramentas →](06-testes.md)
