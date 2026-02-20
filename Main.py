"""
Script principal interactivo - VERSIÓN SIMPLIFICADA
ALDA 2026 - AI Algorithm Solver

Autor: Julian David Castiblanco Real
Escuela de Ingenieros - Universidad de Los Andes
"""

import sys
import os
from pathlib import Path

# Agregar src al path para poder importar el módulo Agent
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from src.Agent import DPAgent, Solution


# ==================== PROBLEMAS INTERNOS (5 problemas incluidos) ====================

PROBLEMAS_INTERNOS = {
    "1": {
        "nombre": "Fibonacci Number",
        "texto": """
Problem: Fibonacci Number

The Fibonacci numbers form a sequence where each number is the sum of 
the two preceding ones, starting from 0 and 1.

F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1

Given n, calculate F(n).

Example 1:
Input: n = 2, Output: 1

Example 2:
Input: n = 4, Output: 3

Constraints: 0 <= n <= 30
""",
        "dificultad": "Básico"
    },
    
    "2": {
        "nombre": "Climbing Stairs",
        "texto": """
Problem: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2, Output: 2
Explanation: Two ways: (1,1) or (2)

Example 2:
Input: n = 3, Output: 3
Explanation: Three ways: (1,1,1), (1,2), or (2,1)

Constraints: 1 <= n <= 45
""",
        "dificultad": "Básico"
    },
    
    "3": {
        "nombre": "Coin Change",
        "texto": """
Problem: Coin Change

You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins needed to make up that amount.
If the amount cannot be made up, return -1.
You have infinite number of each coin.

Example 1:
Input: coins = [1,2,5], amount = 11, Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3, Output: -1

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
""",
        "dificultad": "Medio"
    },
    
    "4": {
        "nombre": "Longest Common Subsequence",
        "texto": """
Problem: Longest Common Subsequence (LCS)

Given two strings text1 and text2, return the length of their 
longest common subsequence. If there is no common subsequence, return 0.

A subsequence is derived by deleting some or no elements without 
changing the order of remaining elements.

Example 1:
Input: text1 = "abcde", text2 = "ace", Output: 3
Explanation: The LCS is "ace" with length 3.

Example 2:
Input: text1 = "abc", text2 = "abc", Output: 3

Example 3:
Input: text1 = "abc", text2 = "def", Output: 0

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
""",
        "dificultad": "Medio"
    },
    
    "5": {
        "nombre": "0/1 Knapsack",
        "texto": """
Problem: 0/1 Knapsack

Given weights and values of n items, put these items in a knapsack 
of capacity W to get maximum total value.

Note: You cannot break an item, either pick the complete item or 
don't pick it (0-1 property).

Example:
Input:
- values = [60, 100, 120]
- weights = [10, 20, 30]
- W = 50

Output: 220
Explanation: Pick items with values 100 and 120.

Constraints:
- 1 <= n <= 1000
- 1 <= W <= 1000
- 1 <= values[i] <= 1000
- 1 <= weights[i] <= 1000
""",
        "dificultad": "Medio"
    }
}


# ==================== FUNCIONES AUXILIARES ====================

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_banner():
    """Muestra el banner principal del programa"""
    print("="*70)
    print("🤖 AI ALGORITHM SOLVER - Dynamic Programming Agent")
    print("="*70)
    print("ALDA 2026 | Julian David Castiblanco Real")
    print("="*70)
    print()


def mostrar_menu():
    """Muestra el menú principal con 3 opciones"""
    print("\n📋 MENÚ PRINCIPAL")
    print("-"*70)
    print("1. 📚 Resolver problemas internos (5 incluidos)")
    print("2. ✍️  Resolver problema adicional (escribe el tuyo)")
    print("0. 🚪 Salir")
    print("-"*70)


def mostrar_problemas_internos():
    """Muestra la lista de 5 problemas incluidos"""
    print("\n📚 PROBLEMAS INTERNOS DISPONIBLES")
    print("-"*70)
    for key, prob in PROBLEMAS_INTERNOS.items():
        print(f"{key}. {prob['nombre']} [{prob['dificultad']}]")
    print("0. Volver al menú")
    print("-"*70)


def resolver_problema_interno(agent: DPAgent):
    """
    Función para resolver uno de los 5 problemas internos
    
    Flujo:
    1. Muestra lista de problemas
    2. Usuario selecciona uno
    3. Muestra el problema completo
    4. Pide confirmación
    5. El agent lo resuelve usando Gemini
    6. Guarda resultado en results/
    """
    mostrar_problemas_internos()
    
    opcion = input("\n🔢 Selecciona un problema (0-5): ").strip()
    
    if opcion == "0":
        return
    
    if opcion not in PROBLEMAS_INTERNOS:
        print("❌ Opción inválida")
        input("\nPresiona Enter para continuar...")
        return
    
    problema = PROBLEMAS_INTERNOS[opcion]
    
    # Mostrar problema completo
    print(f"\n{'='*70}")
    print(f"📌 Problema seleccionado: {problema['nombre']}")
    print(f"{'='*70}")
    print(problema['texto'])
    
    confirmar = input("\n¿Resolver este problema? (s/n): ").lower()
    
    if confirmar != 's':
        return
    
    try:
        # AQUÍ ES DONDE LA MAGIA OCURRE
        # El agent usa Gemini para:
        # 1. Analizar el problema
        # 2. Generar código Python
        # 3. Calcular complejidad
        # 4. Crear tests
        solution = agent.solve(
            problem_name=problema['nombre'],
            problem_text=problema['texto'],
            include_tests=True
        )
        
        # Mostrar solución formateada bonita
        print(agent.format_solution(solution))
        
        # Guardar en archivo JSON
        filename = f"results/{problema['nombre'].replace(' ', '_').lower()}_solution.json"
        os.makedirs("results", exist_ok=True)
        solution.save_to_file(filename)
        
        print(f"\n✅ Solución guardada en: {filename}")
        
    except Exception as e:
        print(f"\n❌ Error resolviendo problema: {e}")
    
    input("\nPresiona Enter para continuar...")


def resolver_problema_adicional(agent: DPAgent):
    """
    Función para resolver un problema que tú escribas
    
    Flujo:
    1. Pides al usuario que escriba/pegue el problema
    2. Usuario escribe línea por línea
    3. Escribe 'FIN' para terminar
    4. El agent lo resuelve igual que los internos
    5. Guarda resultado
    
    Esto es útil para:
    - Problemas nuevos de LeetCode
    - Problemas del profesor
    - Problemas para la evidencia final
    """
    print("\n📝 PROBLEMA ADICIONAL")
    print("-"*70)
    print("Escribe o pega tu problema.")
    print("Escribe 'FIN' en una línea para terminar.")
    print()
    
    lineas = []
    while True:
        linea = input()
        if linea.strip().upper() == 'FIN':
            break
        lineas.append(linea)
    
    problema_texto = '\n'.join(lineas)
    
    if not problema_texto.strip():
        print("❌ No se ingresó ningún problema")
        input("\nPresiona Enter para continuar...")
        return
    
    nombre = input("\n📌 Nombre del problema: ").strip() or "Problema Custom"
    
    try:
        # Mismo proceso que con problemas internos
        solution = agent.solve(
            problem_name=nombre,
            problem_text=problema_texto,
            include_tests=True
        )
        
        print(agent.format_solution(solution))
        
        filename = f"results/{nombre.replace(' ', '_').lower()}_solution.json"
        os.makedirs("results", exist_ok=True)
        solution.save_to_file(filename)
        
        print(f"\n✅ Solución guardada en: {filename}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
    
    input("\nPresiona Enter para continuar...")


# ==================== PROGRAMA PRINCIPAL ====================

def main():
    """
    Función principal que controla todo el flujo del programa
    
    Flujo general:
    1. Crea el agent (conecta con Gemini)
    2. Entra en loop infinito mostrando menú
    3. Usuario selecciona opción
    4. Ejecuta la función correspondiente
    5. Vuelve al menú
    6. Sale cuando usuario elige 0
    """
    
    try:
        # PASO CRÍTICO: Crear el agent
        # Esto:
        # - Lee tu API key del archivo .env
        # - Se conecta a Gemini
        # - Detecta qué modelo usar (gemini-pro, etc.)
        agent = DPAgent()
        
        # Loop principal del programa
        while True:
            limpiar_pantalla()
            mostrar_banner()
            mostrar_menu()
            
            opcion = input("\n🔢 Selecciona una opción: ").strip()
            
            if opcion == "0":
                print("\n👋 ¡Hasta luego!")
                break
            
            elif opcion == "1":
                # Opción 1: Problemas internos (los 5 incluidos)
                resolver_problema_interno(agent)
            
            elif opcion == "2":
                # Opción 2: Problema adicional (tú lo escribes)
                resolver_problema_adicional(agent)
            
            else:
                print("❌ Opción inválida")
                input("\nPresiona Enter para continuar...")
    
    except ValueError as e:
        # Error: No hay API key configurada
        print(f"\n{e}")
        print("\n💡 Configuración rápida:")
        print("1. Ve a: https://makersuite.google.com/app/apikey")
        print("2. Crea un API key")
        print("3. Crea archivo .env: echo 'GEMINI_API_KEY=tu-key' > .env")
        print("4. Ejecuta de nuevo este script")
    
    except KeyboardInterrupt:
        # Usuario presionó Ctrl+C
        print("\n\n⚠️  Interrumpido por el usuario")
        print("👋 ¡Hasta luego!")
    
    except Exception as e:
        # Cualquier otro error inesperado
        print(f"\n❌ Error inesperado: {e}")


# Punto de entrada del programa
# Esto se ejecuta cuando haces: python main.py
if __name__ == "__main__":
    main()