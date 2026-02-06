"""
AI Algorithm Solver Agent - Gemini Version
ALDA - Algorithms and Data Representation
Category: Dynamic Programming

This implementation uses Google's Gemini API instead of OpenAI.
Gemini offers excellent code generation capabilities and a generous free tier.
"""

import google.generativeai as genai
import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Solution:
    """Estructura para almacenar la solución completa"""
    analysis: str
    pattern: str
    algorithm: str
    code: str
    time_complexity: str
    space_complexity: str
    explanation: str
    test_cases: Optional[List[Dict]] = None

class DynamicProgrammingAgent:
    """
    AI Agent especializado en resolver problemas de Dynamic Programming
    Usa Gemini API de Google
    """
    
    def __init__(self, api_key: str = None, model: str = "gemini-1.5-flash"):
        """
        Inicializa el agent con la API key de Gemini
        
        Args:
            api_key: Google Gemini API key (o usa variable de entorno GEMINI_API_KEY)
            model: Modelo a usar (gemini-1.5-flash, gemini-1.5-pro, gemini-2.0-flash-exp)
        
        Modelos disponibles:
        - gemini-1.5-flash: Rápido y eficiente (RECOMENDADO para este proyecto)
        - gemini-1.5-pro: Más potente pero más lento
        - gemini-2.0-flash-exp: Experimental, última versión
        """

        load_dotenv()
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key is required. Set GEMINI_API_KEY env var or pass it directly.\n"
                "Get your free API key at: https://makersuite.google.com/app/apikey"
            )
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        self.model_name = model
        self.model = genai.GenerativeModel(model)
        
        # Configuration for JSON responses
        self.generation_config = {
            "temperature": 0.3,  # Más determinístico para código
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }
        
    def solve_problem(self, problem_text: str, include_tests: bool = True) -> Solution:
        """
        Resuelve un problema algorítmico paso por paso
        
        Args:
            problem_text: Descripción del problema
            include_tests: Si se deben generar casos de prueba
            
        Returns:
            Solution object con toda la información
        """
        print("🤖 Agent iniciando análisis del problema...")
        
        # Paso 1: Analizar el problema
        analysis = self._analyze_problem(problem_text)
        print(f"✅ Análisis completado: {analysis['pattern']}")
        
        # Paso 2: Generar solución
        solution = self._generate_solution(problem_text, analysis)
        print("✅ Solución generada")
        
        # Paso 3: Generar casos de prueba (opcional)
        test_cases = None
        if include_tests:
            test_cases = self._generate_test_cases(problem_text, solution['code'])
            print(f"✅ {len(test_cases)} casos de prueba generados")
        
        return Solution(
            analysis=analysis['analysis'],
            pattern=analysis['pattern'],
            algorithm=analysis['algorithm'],
            code=solution['code'],
            time_complexity=solution['time_complexity'],
            space_complexity=solution['space_complexity'],
            explanation=solution['explanation'],
            test_cases=test_cases
        )
    
    def _analyze_problem(self, problem_text: str) -> Dict:
        """
        Primera fase: Analizar el problema e identificar el patrón
        """
        prompt = f"""You are an expert in Dynamic Programming algorithms.

Analyze this algorithmic problem and identify:
1. The underlying pattern (fibonacci-like, knapsack, subsequence, etc.)
2. The optimal DP approach (memoization vs tabulation)
3. The sub-problem structure

Problem:
{problem_text}

Respond ONLY with valid JSON. No markdown, no code blocks, just raw JSON.
Use this exact format:
{{
  "analysis": "Brief problem analysis",
  "pattern": "Identified DP pattern",
  "algorithm": "Specific algorithm name",
  "approach": "memoization or tabulation or both"
}}"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            
            # Clean response (Gemini sometimes adds markdown)
            text = response.text.strip()
            if text.startswith("```json"):
                text = text.replace("```json", "").replace("```", "").strip()
            elif text.startswith("```"):
                text = text.replace("```", "").strip()
            
            return json.loads(text)
            
        except Exception as e:
            print(f"⚠️ Error en análisis: {e}")
            # Fallback response
            return {
                "analysis": "Error analyzing problem",
                "pattern": "Unknown",
                "algorithm": "Dynamic Programming",
                "approach": "memoization"
            }
    
    def _generate_solution(self, problem_text: str, analysis: Dict) -> Dict:
        """
        Segunda fase: Generar código Python y análisis de complejidad
        """
        prompt = f"""You are an expert Python programmer specializing in Dynamic Programming.

Problem:
{problem_text}

Analysis:
- Pattern: {analysis['pattern']}
- Algorithm: {analysis['algorithm']}
- Approach: {analysis['approach']}

Generate a complete Python solution with:
1. Comprehensive docstrings
2. Type hints
3. Descriptive variable names
4. Inline comments for DP logic
5. Edge case handling
6. Clean, PEP 8 compliant code

Respond ONLY with valid JSON. No markdown, no code blocks, just raw JSON.
Use this exact format:
{{
  "code": "Complete Python function(s) as a string",
  "time_complexity": "Big-O notation with brief explanation",
  "space_complexity": "Big-O notation with brief explanation",
  "explanation": "Step-by-step explanation of the solution"
}}"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            
            # Clean response
            text = response.text.strip()
            if text.startswith("```json"):
                text = text.replace("```json", "").replace("```", "").strip()
            elif text.startswith("```"):
                text = text.replace("```", "").strip()
            
            return json.loads(text)
            
        except Exception as e:
            print(f"⚠️ Error en generación: {e}")
            return {
                "code": "# Error generating code",
                "time_complexity": "Unknown",
                "space_complexity": "Unknown",
                "explanation": "Error occurred"
            }
    
    def _generate_test_cases(self, problem_text: str, code: str) -> List[Dict]:
        """
        Tercera fase: Generar casos de prueba
        """
        prompt = f"""Generate comprehensive test cases for this problem and solution.

Problem:
{problem_text}

Solution code:
{code}

Generate 5-7 test cases including:
1. Basic/normal cases
2. Edge cases (empty, single element, etc.)
3. Boundary cases
4. Large cases

Respond ONLY with valid JSON. No markdown, no code blocks, just raw JSON.
Use this exact format:
{{
  "test_cases": [
    {{
      "input": "input description or value",
      "expected_output": "expected result",
      "description": "what this test checks"
    }}
  ]
}}"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            
            # Clean response
            text = response.text.strip()
            if text.startswith("```json"):
                text = text.replace("```json", "").replace("```", "").strip()
            elif text.startswith("```"):
                text = text.replace("```", "").strip()
            
            result = json.loads(text)
            return result.get('test_cases', [])
            
        except Exception as e:
            print(f"⚠️ Error en tests: {e}")
            return []
    
    def explain_solution(self, solution: Solution) -> str:
        """
        Genera una explicación detallada de la solución para presentación
        """
        explanation = f"""
╔══════════════════════════════════════════════════════════════╗
║                    SOLUTION BREAKDOWN                        ║
╚══════════════════════════════════════════════════════════════╝

📊 PROBLEM ANALYSIS
{'-' * 60}
{solution.analysis}

🎯 IDENTIFIED PATTERN
{'-' * 60}
{solution.pattern}

⚙️  ALGORITHM
{'-' * 60}
{solution.algorithm}

💻 CODE IMPLEMENTATION
{'-' * 60}
{solution.code}

⏱️  TIME COMPLEXITY
{'-' * 60}
{solution.time_complexity}

💾 SPACE COMPLEXITY
{'-' * 60}
{solution.space_complexity}

📝 STEP-BY-STEP EXPLANATION
{'-' * 60}
{solution.explanation}
"""
        
        if solution.test_cases:
            explanation += f"""
🧪 TEST CASES
{'-' * 60}
"""
            for i, test in enumerate(solution.test_cases, 1):
                explanation += f"\nTest {i}: {test.get('description', 'N/A')}\n"
                explanation += f"  Input: {test.get('input', 'N/A')}\n"
                explanation += f"  Expected: {test.get('expected_output', 'N/A')}\n"
        
        return explanation


def demo():
    """
    Función de demostración con un problema de ejemplo
    """
    print("=" * 70)
    print("🚀 AI Algorithm Solver - Dynamic Programming Agent (Gemini)")
    print("=" * 70)
    print()
    
    # Ejemplo de problema
    problem = """
    Problem: Fibonacci Number
    
    The Fibonacci numbers, commonly denoted F(n), form a sequence where each 
    number is the sum of the two preceding ones, starting from 0 and 1.
    
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    
    Given n, calculate F(n).
    
    Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1
    
    Example 2:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3
    
    Constraints:
    0 <= n <= 30
    """
    
    print("📌 Configuración:")
    print("   - Modelo: Gemini 1.5 Flash")
    print("   - API: Google Gemini")
    print("   - Categoría: Dynamic Programming")
    print()
    
    # Instrucciones para obtener API key
    print("💡 Para obtener tu API key gratuita:")
    print("   1. Ve a https://makersuite.google.com/app/apikey")
    print("   2. Inicia sesión con tu cuenta Google")
    print("   3. Crea un API key")
    print("   4. Configúralo en .env: GEMINI_API_KEY=tu-key")
    print()
    
    try:
        # Crear agent
        agent = DynamicProgrammingAgent()
        
        print("🔄 Procesando problema...")
        print()
        
        # Resolver problema
        solution = agent.solve_problem(problem, include_tests=True)
        
        # Mostrar resultados
        print(agent.explain_solution(solution))
        
        # Guardar en archivo
        with open("solution_output.txt", "w", encoding="utf-8") as f:
            f.write(agent.explain_solution(solution))
        
        print("\n✅ Solución guardada en 'solution_output.txt'")
        
    except ValueError as e:
        print(f"\n❌ Error de configuración: {e}")
        print("\nPasos para configurar:")
        print("1. Obtén tu API key en https://makersuite.google.com/app/apikey")
        print("2. Crea un archivo .env:")
        print("   GEMINI_API_KEY='tu-key-aqui'")
        print("3. O exporta la variable:")
        print("   export GEMINI_API_KEY='tu-key-aqui'")
        
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("\nSi el problema persiste:")
        print("- Verifica que el API key sea válido")
        print("- Asegúrate de tener conexión a internet")
        print("- Revisa que google-generativeai esté instalado:")
        print("  pip install google-generativeai")


if __name__ == "__main__":
    demo()