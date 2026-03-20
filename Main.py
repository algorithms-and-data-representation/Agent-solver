"""
Interactive CLI - AI Algorithm Solver
ALDA 2026

Autor: Julian David Castiblanco Real
Universidad de Los Andes
"""

# ============================================================
# 1IMPORTS
# ============================================================

import os
from pathlib import Path
from typing import Optional
from src.Agent import DPAgent, Solution, SolutionChat


# ============================================================
# CONFIGURACIÓN GLOBAL
# ============================================================

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


# ============================================================
# PROBLEMAS INTERNOS
# ============================================================

PROBLEMAS_INTERNOS = {
    "1": ("Fibonacci Number", "Básico", """
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
"""),
    "2": ("Climbing Stairs", "Básico", """
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
"""),
    "3": ("Coin Change", "Medio", """
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
"""),    
    "4": ("Longest Common Subsequence", "Medio", """
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
"""),    
    "5": ("0/1 Knapsack", "Medio", """
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
"""),
}


# ============================================================
# UTILIDADES UI
# ============================================================

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    input("\nPresiona Enter para continuar...")


def banner() -> None:
    print("=" * 70)
    print("🤖 AI Algorithm Solver - Dynamic Programming")
    print("ALDA 2026 | Julian David Castiblanco Real")
    print("=" * 70)


# ============================================================
# 5️⃣ APPLICATION CONTROLLER
# ============================================================

class Application:

    def __init__(self):
        self.agent = DPAgent()

    # ---------------------------
    # MENÚ PRINCIPAL
    # ---------------------------
    def run(self):
        while True:
            clear_screen()
            banner()
            self._show_menu()

            option = input("\n🔢 Selecciona opción: ").strip()

            if option == "0":
                print("\n👋 Hasta luego!")
                break
            elif option == "1":
                self._solve_internal()
            elif option == "2":
                self._solve_custom()
            else:
                print("❌ Opción inválida")
                pause()

    # ---------------------------
    # MENÚ
    # ---------------------------
    def _show_menu(self):
        print("\n1. 📚 Problemas internos")
        print("2. ✍️  Problema personalizado")
        print("0. 🚪 Salir")

    # ---------------------------
    # PROBLEMAS INTERNOS
    # ---------------------------
    def _solve_internal(self):
        """Resuelve uno de los 5 problemas internos con chat post-solución"""
        
        print("\n📚 Problemas disponibles:\n")

        for key, (name, difficulty, _) in PROBLEMAS_INTERNOS.items():
            print(f"{key}. {name} [{difficulty}]")

        print("0. Volver")

        option = input("\nSelecciona: ").strip()

        if option == "0":
            return

        if option not in PROBLEMAS_INTERNOS:
            print("❌ Opción inválida")
            pause()
            return

        name, difficulty, text = PROBLEMAS_INTERNOS[option]
        
        # Mostrar problema completo
        print(f"\n{'='*70}")
        print(f"📌 Problema seleccionado: {name}")
        print(f"{'='*70}")
        print(text)
        
        confirmar = input("\n¿Resolver este problema? (s/n): ").lower()
        
        if confirmar != 's':
            return
        
        self._execute_solution(name, text, with_chat=True)

    # ---------------------------
    # PROBLEMA PERSONALIZADO
    # ---------------------------
    def _solve_custom(self):
        """Resuelve un problema personalizado con chat post-solución"""
        
        print("\n📝 Escribe tu problema (FIN para terminar):\n")

        lines = []
        while True:
            line = input()
            if line.strip().upper() == "FIN":
                break
            lines.append(line)

        if not lines:
            print("❌ No ingresaste problema")
            pause()
            return

        name = input("\nNombre del problema: ").strip() or "Custom Problem"
        text = "\n".join(lines)

        self._execute_solution(name, text, with_chat=True)

    # ---------------------------
    # EJECUCIÓN CENTRAL
    # ---------------------------
    def _execute_solution(self, name: str, text: str, with_chat: bool = True):
        """
        Ejecuta la resolución del problema y opcionalmente activa el chat
        
        Args:
            name: Nombre del problema
            text: Texto del problema
            with_chat: Si ofrecer modo chat después de resolver
        """
        
        try:
            print(f"\n🚀 Resolviendo {name}...\n")

            solution = self.agent.solve(
                problem_name=name,
                problem_text=text,
                include_tests=True
            )

            print(self.agent.format_solution(solution))

            file_path = RESULTS_DIR / f"{name.replace(' ', '_').lower()}_solution.json"
            solution.save_to_file(str(file_path))

            print(f"\n✅ Guardado en {file_path}")
            
            # ============================================================
            # CHAT POST-SOLUCIÓN (NUEVO)
            # ============================================================
            if with_chat:
                print("\n" + "="*70)
                print("💬 ¿Tienes preguntas sobre esta solución?")
                print("="*70)
                print()
                print("Puedo explicarte:")
                print("  • Por qué usé esta estructura")
                print("  • Cómo funciona el código")
                print("  • La complejidad")
                print("  • Alternativas y optimizaciones")
                print()
                
                quiere_chat = input("¿Quieres hacerme preguntas? (s/n): ").lower()
                
                if quiere_chat == 's':
                    chat = SolutionChat(self.agent, solution)
                    chat.start_chat()
                else:
                    print("\n👍 ¡Perfecto! Puedes revisar la solución en cualquier momento.")

        except Exception as e:
            print(f"\n❌ Error: {e}")

        pause()


# ============================================================
# 6️⃣ ENTRY POINT
# ============================================================

def main():
    try:
        app = Application()
        app.run()

    except ValueError as e:
        print(f"\n{e}")
        print("\nConfigura tu GEMINI_API_KEY en el archivo .env")

    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido.")

    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()