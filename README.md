# 🤖 AI Algorithm Solver - Dynamic Programming

> **AI Agent Conversacional con Chat Post-Solución**

---

## 👨‍💻 Autor

**Julian David Castiblanco Real**  
Escuela de Colombiana de ingenieria Julio Garavito

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características Principales](#-características-principales)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Funcionalidad de Chat](#-funcionalidad-de-chat-nuevo)
- [Problemas Incluidos](#-problemas-incluidos)
- [Arquitectura](#-arquitectura)
- [Ejemplos](#-ejemplos)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)

---

## 🎯 Descripción

**AI Algorithm Solver** es un agente de inteligencia artificial especializado en resolver problemas de **Dynamic Programming**. El proyecto va más allá de ser un simple "solver" automático: incluye un **sistema de chat post-solución** que permite al usuario hacer preguntas específicas sobre el código generado, complejidad, alternativas y optimizaciones.

### ¿Qué hace?

1. **Resuelve automáticamente** problemas de DP usando Google Gemini API
2. **Genera código Python** optimizado con type hints y documentación
3. **Calcula complejidad** temporal y espacial (Big-O)
4. **Crea casos de prueba** comprehensivos
5. **Conversación:** Chat interactivo para hacer preguntas sobre la solución

### ¿Por qué es único?

A diferencia de otros solvers que solo dan la respuesta, este proyecto:
- ✅ **Enseña** - Explica el razonamiento detrás de cada decisión
- ✅ **Conversa** - Responde preguntas específicas sobre TU solución
- ✅ **Personaliza** - Cada explicación es contextual al problema resuelto
- ✅ **Interactúa** - No es una respuesta estática, es una conversación

---

## ✨ Características Principales

### 🎯 Resolución Automática de Problemas

- **Análisis de patrones DP** - Identifica automáticamente el patrón (fibonacci-like, knapsack, subsequence, etc.)
- **Generación de código** - Produce código Python profesional con:
  - Type hints completos
  - Docstrings estilo Google
  - Comentarios explicativos
  - Manejo de casos edge
  - Cumple con PEP 8
- **Análisis de complejidad** - Calcula y explica Big-O temporal y espacial
- **Generación de tests** - Crea 5-10 casos de prueba (básicos, edge cases, frontera)

### 💬 Chat Post-Solución (NUEVO)

**La funcionalidad estrella del proyecto:**

Después de resolver un problema, puedes chatear con el AI sobre ESA solución específica:

**Preguntas que puedes hacer:**
- "¿Por qué usaste un array dp en lugar de variables?"
- "¿Cuál es la complejidad y por qué?"
- "¿Hay otra forma de resolver esto?"
- "¿Qué optimizaciones son posibles?"
- "¿Por qué elegiste tabulation y no memoization?"
- "¿Cómo maneja este código los casos edge?"

El bot tiene **contexto completo** de tu solución y responde específicamente sobre el código que generó.

### 📚 Biblioteca de Problemas

**5 Problemas Pre-cargados:**
1. Fibonacci Number (Básico)
2. Climbing Stairs (Básico)
3. Coin Change (Medio)
4. Longest Common Subsequence (Medio)
5. 0/1 Knapsack (Medio)

**Problemas Personalizados:**
- Acepta **cualquier problema DP**
- Copia y pega de LeetCode, HackerRank, etc.
- Ideal para problemas del profesor o evidencia

### 💾 Persistencia

- Guarda todas las soluciones en formato JSON
- Organizado en carpeta `results/`
- UTF-8 encoding
- Pretty printing (legible)

### 🎨 Interfaz Profesional

- CLI interactivo limpio
- Progreso visible (Paso 1/3, 2/3, 3/3)
- Banner personalizado con tu nombre
- Mensajes de error claros
- Formato bonito con emojis

---

## 🚀 Instalación

### Requisitos Previos

- **Python 3.10+** (probado con 3.13)
- **Cuenta Google** (para API key gratuita)
- **Conexión a internet**

### Paso 1: Clonar/Descargar el Proyecto

```bash
# Si está en GitHub:
git clone https://github.com/TU-USUARIO/ai-algorithm-solver.git
cd ai-algorithm-solver

# O descargar ZIP y extraer
```

### Paso 2: Crear Virtual Environment

```bash
# Crear venv
python -m venv venv

# Activar venv
# Windows (Git Bash):
source venv/Scripts/activate

# Windows (CMD):
venv\Scripts\activate.bat

# Windows (PowerShell):
venv\Scripts\Activate.ps1

# Mac/Linux:
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Dependencias:**
- `google-generativeai` - Cliente de Gemini API
- `python-dotenv` - Manejo de variables de entorno

### Paso 4: Configurar API Key

#### 4.1. Obtener API Key (GRATIS)

1. Ve a: https://makersuite.google.com/app/apikey
2. Inicia sesión con tu cuenta Google
3. Click en **"Create API Key"**
4. Copia el key (empieza con `AIzaSy...`)

**Es 100% GRATIS:**
- Sin tarjeta de crédito
- Límites generosos (20-1,500 requests/día según modelo)
- Suficiente para completar el proyecto

#### 4.2. Crear archivo .env

```bash
# Copiar template
cp .env.example .env

# Editar .env y agregar tu key
# En .env debe quedar:
GEMINI_API_KEY=tu-key-aqui
```

**Verificar:**
```bash
cat .env
# Debe mostrar: GEMINI_API_KEY=AIzaSy...
```

### Paso 5: Verificar Instalación

```bash
# Verificar que todo funciona
python -c "from src.Agent import DPAgent, SolutionChat; print('✅ Instalación correcta')"
```

Si ves `✅ Instalación correcta` → ¡Listo para usar!

---

## 💻 Uso

### Ejecutar el Programa

```bash
python Main.py
```

### Menú Principal

```
======================================================================
🤖 AI Algorithm Solver - Dynamic Programming
ALDA 2026 | Julian David Castiblanco Real
======================================================================

1. 📚 Problemas internos
2. ✍️  Problema personalizado
0. 🚪 Salir

🔢 Selecciona opción:
```

---

## 📚 Opción 1: Problemas Internos

### Paso 1: Seleccionar opción 1

```
🔢 Selecciona opción: 1
```

### Paso 2: Elegir problema

```
📚 Problemas disponibles:

1. Fibonacci Number [Básico]
2. Climbing Stairs [Básico]
3. Coin Change [Medio]
4. Longest Common Subsequence [Medio]
5. 0/1 Knapsack [Medio]
0. Volver

Selecciona: 1
```

### Paso 3: Ver problema y confirmar

```
======================================================================
📌 Problema seleccionado: Fibonacci Number
======================================================================

Problem: Fibonacci Number

The Fibonacci numbers form a sequence where each number is the sum of 
the two preceding ones, starting from 0 and 1.
[...]

¿Resolver este problema? (s/n): s
```

### Paso 4: El agent trabaja

```
======================================================================
🤖 Resolviendo: Fibonacci Number
======================================================================

📊 Paso 1/3: Analizando problema...
   ✅ Patrón identificado: Fibonacci-like

💻 Paso 2/3: Generando código...
   ✅ Código generado (45 líneas)

🧪 Paso 3/3: Generando tests...
   ✅ 10 casos de prueba

======================================================================
✨ ¡Solución completada!
======================================================================
```

### Paso 5: Ver solución

```
╔══════════════════════════════════════════════════════════════╗
║                        Fibonacci Number                        ║
╚══════════════════════════════════════════════════════════════╝

📊 ANÁLISIS DEL PROBLEMA
----------------------------------------------------------------
[Análisis completo del problema...]

🎯 PATRÓN IDENTIFICADO
----------------------------------------------------------------
Fibonacci-like / Overlapping subproblems

⚙️  ALGORITMO
----------------------------------------------------------------
Dynamic Programming (tabulation)

💻 CÓDIGO PYTHON
----------------------------------------------------------------
def fib(n: int) -> int:
    """
    Calculates the nth Fibonacci number using DP.
    [...]
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

⏱️  COMPLEJIDAD TEMPORAL
----------------------------------------------------------------
O(n) - Un solo loop de 2 hasta n

💾 COMPLEJIDAD ESPACIAL
----------------------------------------------------------------
O(n) - Array de tamaño n+1

📝 EXPLICACIÓN
----------------------------------------------------------------
[Explicación paso a paso completa...]

🧪 CASOS DE PRUEBA
----------------------------------------------------------------
Test 1: Caso base F(0)
  Input: 0
  Expected: 0
[... 10 tests totales ...]

✅ Guardado en results/fibonacci_number_solution.json
```

---

## 💬 Funcionalidad de Chat (NUEVO)

### ¿Qué es?

Después de resolver un problema, puedes hacer **preguntas específicas** sobre esa solución. El bot tiene contexto completo del código generado.

### ¿Cuándo se activa?

Después de guardar la solución:

```
✅ Guardado en results/fibonacci_number_solution.json

======================================================================
💬 ¿Tienes preguntas sobre esta solución?
======================================================================

Puedo explicarte:
  • Por qué usé esta estructura
  • Cómo funciona el código
  • La complejidad
  • Alternativas y optimizaciones

¿Quieres hacerme preguntas? (s/n):
```

### Activar Chat

```
¿Quieres hacerme preguntas? (s/n): s

======================================================================
💬 MODO CHAT - Pregunta sobre la solución
======================================================================

Puedes preguntarme sobre:
  • Por qué usé cierta estructura de datos
  • Cómo funciona alguna parte del código
  • La complejidad (temporal o espacial)
  • Alternativas a este enfoque
  • Optimizaciones posibles
  • Casos edge que manejo

Escribe 'salir' para volver al menú
----------------------------------------------------------------------
```

### Ejemplos de Conversación

#### Ejemplo 1: Preguntar sobre estructura

```
Tú: ¿por qué usas un array dp en lugar de solo dos variables?

🤖 Bot: ¡Excelente pregunta! Tienes razón en que para Fibonacci 
específicamente podríamos optimizar el espacio.

En el código actual uso:
```python
dp = [0] * (n + 1)
```

Esto almacena TODOS los valores de F(0) hasta F(n), lo que nos da
complejidad espacial O(n).

Sin embargo, nota que en cada paso solo necesitamos los dos valores
anteriores:
```python
dp[i] = dp[i-1] + dp[i-2]
         ^^^^^    ^^^^^
         solo necesitamos estos dos
```

Podríamos optimizar a O(1) espacio con dos variables...

[Continúa con explicación detallada y código alternativo]

¿Quieres que te explique cuándo usar cada enfoque?
```

#### Ejemplo 2: Preguntar sobre complejidad

```
Tú: ¿por qué es O(n) y no O(n²)?

🤖 Bot: Excelente pregunta de complejidad!

Es O(n) porque solo tenemos UN loop:

```python
for i in range(2, n + 1):  # ← Este loop se ejecuta n-1 veces
    dp[i] = dp[i-1] + dp[i-2]  # ← Operación O(1)
```

Análisis línea por línea:

1. El for itera desde 2 hasta n
   → Total iteraciones: n - 1 ≈ O(n)

2. Dentro del loop:
   - Acceso a array: O(1)
   - Suma: O(1)
   - Asignación: O(1)
   → Total: O(1)

Entonces: O(n) × O(1) = O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sería O(n²) si tuvieras un loop DENTRO de otro:

```python
for i in range(n):        # O(n)
    for j in range(n):    # O(n)
        # hacer algo      # O(1)
```

Pero en Fibonacci no existe ese loop anidado.

¿Tiene sentido?
```

#### Ejemplo 3: Preguntar por alternativas

```
Tú: ¿hay otra forma de resolver esto?

🤖 Bot: ¡Sí! Hay al menos 4 formas de resolver Fibonacci:

1️⃣ RECURSIÓN SIMPLE (lo que NO hice)
   ❌ O(2^n) - muy lento
   
2️⃣ MEMOIZATION (Top-Down)
   ✅ O(n) - con cache
   ⚠️  Usa recursión
   
3️⃣ TABULATION (Bottom-Up) ← LO QUE USÉ
   ✅ O(n) tiempo
   ✅ Iterativo
   
4️⃣ OPTIMIZADO (2 variables)
   ✅ O(n) tiempo
   ✅ O(1) espacio

En la solución usé TABULATION porque:
- Es eficiente O(n)
- Es clara y fácil de entender
- Demuestra bien el concepto de DP
- Se generaliza a otros problemas

¿Quieres que te explique alguna en detalle?
```

### Salir del Chat

```
Tú: salir

👋 Volviendo al menú...
```

---

## ✍️ Opción 2: Problema Personalizado

### Paso 1: Seleccionar opción 2

```
🔢 Selecciona opción: 2
```

### Paso 2: Escribir o pegar problema

```
📝 Escribe tu problema (FIN para terminar):

Problem: House Robber

You are a robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
The constraint is that you cannot rob two adjacent houses.

Given an array of integers representing the amount of money,
return the maximum amount you can rob without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

FIN
```

**Tip:** Puedes copiar problemas completos de LeetCode/HackerRank

### Paso 3: Dar nombre

```
📌 Nombre del problema: House Robber
```

(O presiona Enter para "Custom Problem")

### Paso 4-6: Igual que problemas internos

- Resuelve automáticamente
- Muestra solución
- Ofrece chat

---

## 📁 Problemas Incluidos

### Básicos
1. **Fibonacci Number**
   - Patrón: Fibonacci-like
   - Complejidad: O(n) / O(n)
   - Tests: 10 casos

2. **Climbing Stairs**
   - Patrón: Fibonacci variant
   - Complejidad: O(n) / O(n)
   - Tests: 8 casos

### Medios
3. **Coin Change**
   - Patrón: Knapsack variant
   - Complejidad: O(n×m) / O(n)
   - Tests: 7 casos

4. **Longest Common Subsequence**
   - Patrón: 2D DP
   - Complejidad: O(n×m) / O(n×m)
   - Tests: 9 casos

5. **0/1 Knapsack**
   - Patrón: Classic knapsack
   - Complejidad: O(n×W) / O(n×W)
   - Tests: 6 casos

---

## 🏗️ Arquitectura

### Estructura del Proyecto

```
ai-algorithm-solver/
│
├── Main.py                 # CLI interactivo
├── src/
│   └── Agent.py           # DPAgent + SolutionChat
│
├── results/               # Soluciones guardadas (JSON)
│
├── requirements.txt       # Dependencias
├── .env                   # API key (NO subir a GitHub)
├── .env.example          # Template de .env
├── .gitignore            # Git ignore
└── README.md             # Este archivo
```

### Componentes Principales

#### 1. `Solution` (Dataclass)
Estructura de datos inmutable para soluciones:
```python
@dataclass
class Solution:
    problem_name: str
    analysis: str
    pattern: str
    algorithm: str
    approach: str
    code: str
    time_complexity: str
    space_complexity: str
    explanation: str
    test_cases: Optional[List[Dict]]
```

#### 2. `DPAgent` (Motor Principal)
Orquestador de la resolución:
- `solve()` - Método principal (3 fases)
- `_analyze_problem()` - Identifica patrón
- `_generate_solution()` - Genera código
- `_generate_tests()` - Crea tests

#### 3. `SolutionChat` (Chat Interactivo) ⭐ NUEVO
Sistema de chat post-solución:
```python
class SolutionChat:
    def __init__(self, agent, solution):
        # Guarda contexto completo de la solución
        
    def start_chat(self):
        # Loop de preguntas y respuestas
        
    def _get_response(self, question):
        # Llama a Gemini con contexto de la solución
```

#### 4. `Application` (Controlador)
Maneja la interfaz CLI:
- Menú principal
- Navegación
- Llamadas a DPAgent
- Activación de chat

### Flujo de Datos

```
Usuario → Main.py → Application
                        ↓
                    DPAgent.solve()
                        ↓
            ┌───────────┼───────────┐
            ↓           ↓           ↓
        Análisis    Código      Tests
            ↓           ↓           ↓
            └───────────┼───────────┘
                        ↓
                    Solution
                        ↓
                ┌───────┴───────┐
                ↓               ↓
         Guardar JSON      SolutionChat
                                ↓
                        Usuario pregunta
                                ↓
                        Gemini responde
```

---

## 🎓 Metodología

### Pipeline de 3 Fases

#### Fase 1: Análisis (1 request)
```
Problema → Gemini API
         ↓
    Identifica:
    - Patrón DP
    - Enfoque (memoization/tabulation)
    - Estructura de subproblemas
```

#### Fase 2: Generación (1 request)
```
Problema + Análisis → Gemini API
                     ↓
                 Genera:
                 - Código Python
                 - Complejidad temporal
                 - Complejidad espacial
                 - Explicación
```

#### Fase 3: Testing (1 request)
```
Problema + Código → Gemini API
                   ↓
               Genera:
               - Casos básicos
               - Edge cases
               - Casos de frontera
```

#### Fase 4: Chat (N requests) ⭐ NUEVO
```
Pregunta + Contexto completo → Gemini API
                              ↓
                          Responde:
                          - Explicación contextual
                          - Referencia al código específico
```

**Total requests por problema:**
- Sin chat: 3 requests
- Con chat: 3 + N requests (N = preguntas)

---

## 📊 Ejemplos Completos

### Ejemplo 1: Fibonacci con Chat

```bash
$ python Main.py

======================================================================
🤖 AI Algorithm Solver - Dynamic Programming
ALDA 2026 | Julian David Castiblanco Real
======================================================================

1. 📚 Problemas internos
2. ✍️  Problema personalizado
0. 🚪 Salir

🔢 Selecciona opción: 1

📚 Problemas disponibles:

1. Fibonacci Number [Básico]
2. Climbing Stairs [Básico]
3. Coin Change [Medio]
4. Longest Common Subsequence [Medio]
5. 0/1 Knapsack [Medio]
0. Volver

Selecciona: 1

======================================================================
📌 Problema seleccionado: Fibonacci Number
======================================================================

[... muestra problema completo ...]

¿Resolver este problema? (s/n): s

======================================================================
🤖 Resolviendo: Fibonacci Number
======================================================================

📊 Paso 1/3: Analizando problema...
   ✅ Patrón identificado: Fibonacci-like

💻 Paso 2/3: Generando código...
   ✅ Código generado (45 líneas)

🧪 Paso 3/3: Generando tests...
   ✅ 10 casos de prueba

[... muestra solución completa ...]

✅ Guardado en results/fibonacci_number_solution.json

======================================================================
💬 ¿Tienes preguntas sobre esta solución?
======================================================================

¿Quieres hacerme preguntas? (s/n): s

======================================================================
💬 MODO CHAT - Pregunta sobre la solución
======================================================================

Tú: ¿por qué usas dp[i-1] + dp[i-2]?

🤖 Bot: Esa es la relación de recurrencia de Fibonacci. En cada paso...
[explicación detallada]

Tú: ¿se puede optimizar el espacio?

🤖 Bot: ¡Sí! En lugar de un array completo, podrías usar solo dos variables...
[código alternativo]

Tú: salir

👋 Volviendo al menú...
```

---

## 🔧 Troubleshooting

### Error: API key no encontrada

```
❌ API key no encontrada!
Por favor:
1. Obtén tu key en: https://makersuite.google.com/app/apikey
2. Créala en .env: GEMINI_API_KEY=tu-key-aqui
```

**Solución:**
```bash
# Verificar que existe .env
ls -la .env

# Verificar contenido
cat .env

# Debe mostrar:
GEMINI_API_KEY=AIzaSy...
```

### Error: No module named 'google.generativeai'

```
ModuleNotFoundError: No module named 'google.generativeai'
```

**Solución:**
```bash
# Verificar que venv está activado
which python
# Debe mostrar: /ruta/a/tu/proyecto/venv/...

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: cannot import name 'SolutionChat'

```
ImportError: cannot import name 'SolutionChat'
```

**Solución:**
Verifica que `src/Agent.py` tiene la clase `SolutionChat` agregada al final (antes de `if __name__ == "__main__"`).

### Error: 429 You exceeded your current quota

```
429 You exceeded your current quota, please check your plan
```

**Solución:**
- Has alcanzado el límite de requests/día
- **Opción 1:** Espera 24 horas (se resetea)
- **Opción 2:** Genera un nuevo API key en https://makersuite.google.com/app/apikey
- **Opción 3:** Resuelve problemas sin tests (`include_tests=False`)

### Modelo no disponible

```
404 models/gemini-X is not found
```

**Solución:**
El agent auto-detecta modelos. Si falla:
```python
# En src/Agent.py, línea ~90
# Cambiar manualmente a:
self.model = genai.GenerativeModel("gemini-pro")
```

---

## 📈 Roadmap

### ✅ Completado
- [x] Agent funcional con Gemini
- [x] Resolución automática de problemas
- [x] 5 problemas pre-cargados
- [x] Modo custom para nuevos problemas
- [x] Generación de tests
- [x] Chat post-solución interactivo
- [x] Persistencia en JSON

### 🚧 En Progreso
- [ ] Resolver 8-10 problemas para evidencia
- [ ] Screenshots de cada solución
- [ ] Video demostración

### 🔮 Futuro (Post-entrega)
- [ ] Ejecutar y validar código generado
- [ ] Comparar con soluciones conocidas
- [ ] Sistema de rating de soluciones
- [ ] Soporte para más algoritmos (Greedy, Divide & Conquer)
- [ ] GUI web con React

---

## 💰 Costos

### API de Gemini (100% GRATIS)

**Límites según modelo:**
| Modelo | Requests/día | Requests/minuto |
|--------|--------------|-----------------|
| gemini-2.5-flash | 20 | 2 |
| gemini-1.5-flash | 1,500 | 15 |
| gemini-1.5-pro | 50 | 2 |

**Para completar el proyecto:**
- 10 problemas × 3 requests = 30 requests
- Chat: ~3-5 preguntas por problema = 30-50 requests
- **Total:** 60-80 requests

**Estrategia:**
- Usa 1-2 API keys
- Resuelve 5 problemas por día
- 2-3 días para completar todo

**Costo total: $0** 💰

---

## 🙏 Agradecimientos

- **Google Gemini Team** - Por proporcionar API gratuita de alta calidad
- **Profesor ALDA** - Por el proyecto y guía
- **Universidad de Los Andes** - Escuela de Ingenieros

---

## 📝 Licencia

Proyecto académico - ALDA 2026  
Universidad de Los Andes  
Solo para fines educativos

---

## 📞 Contacto

**Julian David Castiblanco Real**  
Escuela de Ingenieros  
Universidad de Los Andes

---

## ⚡ Quick Start (TL;DR)

```bash
# 1. Clonar/descargar proyecto
cd ai-algorithm-solver

# 2. Crear venv
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate      # Mac/Linux

# 3. Instalar
pip install -r requirements.txt

# 4. Configurar API
cp .env.example .env
# Editar .env y agregar GEMINI_API_KEY=tu-key

# 5. Ejecutar
python Main.py

# 6. Resolver Fibonacci
# Opción 1 → Problema 1 → s → [ve solución] → s → [chatea]

# ¡Listo! 🎉
```

---

**Última actualización:** Marzo 2026  
**Versión:** 2.0 (Con Chat)  
**Estado:** ✅ Funcional y completo

---

<div align="center">

**⭐ Si este proyecto te fue útil, dale una estrella ⭐**

Hecho con ❤️ para ALDA 2026

</div>