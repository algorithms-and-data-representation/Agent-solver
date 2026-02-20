"""
AI Algorithm Solver Agent - Dynamic Programming
ALDA 2026 - Proyecto 20%

VERSIÓN ACTUALIZADA - Con detección automática de modelos Gemini

Autor: [Tu nombre]
Fecha: Febrero 2026
Modelo: Google Gemini (auto-detect)
"""

import google.generativeai as genai
import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


@dataclass
class Solution:
    """
    Estructura de datos para almacenar la solución completa de un problema
    """
    problem_name: str
    analysis: str
    pattern: str
    algorithm: str
    approach: str
    code: str
    time_complexity: str
    space_complexity: str
    explanation: str
    test_cases: Optional[List[Dict]] = None
    
    def to_dict(self) -> Dict:
        """Convierte la solución a diccionario"""
        return asdict(self)
    
    def save_to_file(self, filename: str):
        """Guarda la solución en un archivo JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)


class DPAgent:
    """
    Agent especializado en resolver problemas de Dynamic Programming
    usando Google Gemini API
    """
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        temperature: float = 0.3
    ):
        """
        Inicializa el DP Agent
        
        Args:
            api_key: Gemini API key (usa GEMINI_API_KEY del .env si no se provee)
            model: Modelo de Gemini a usar (auto-detecta si no se especifica)
            temperature: Temperatura para generación (0.0-1.0)
        """
        # Obtener API key
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "❌ API key no encontrada!\n"
                "Por favor:\n"
                "1. Obtén tu key en: https://makersuite.google.com/app/apikey\n"
                "2. Créala en .env: GEMINI_API_KEY=tu-key-aqui"
            )
        
        # Configurar Gemini
        genai.configure(api_key=self.api_key)
        
        # Auto-detectar modelo si no se especifica
        if model is None:
            model = self._detect_best_model()
        
        self.model_name = model
        
        try:
            self.model = genai.GenerativeModel(model)
            print(f"✅ Agent inicializado con {model}")
        except Exception as e:
            print(f"⚠️  Error con modelo {model}: {e}")
            # Intentar con gemini-pro como fallback
            try:
                self.model_name = "gemini-pro"
                self.model = genai.GenerativeModel("gemini-pro")
                print(f"✅ Usando modelo alternativo: gemini-pro")
            except Exception as e2:
                raise ValueError(
                    f"❌ No se pudo inicializar ningún modelo de Gemini.\n"
                    f"Error: {e2}\n"
                    f"Verifica tu API key y conexión a internet."
                )
        
        # Configuración de generación
        self.generation_config = {
            "temperature": temperature,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }
    
    def _detect_best_model(self) -> str:
        """
        Detecta el mejor modelo disponible automáticamente
        """
        # Orden de preferencia de modelos
        preferred_models = [
            "gemini-1.5-flash-latest",
            "gemini-1.5-flash",
            "gemini-1.5-pro-latest", 
            "gemini-1.5-pro",
            "gemini-pro",
            "gemini-1.0-pro"
        ]
        
        try:
            # Obtener lista de modelos disponibles
            available_models = genai.list_models()
            available_names = [m.name.split('/')[-1] for m in available_models 
                             if 'generateContent' in m.supported_generation_methods]
            
            # Buscar el primer modelo preferido que esté disponible
            for model in preferred_models:
                if model in available_names:
                    return model
            
            # Si no encuentra ninguno preferido, usar el primero disponible
            if available_names:
                return available_names[0]
                
        except Exception as e:
            print(f"⚠️  No se pudo auto-detectar modelo: {e}")
        
        # Fallback final
        return "gemini-pro"
    
    def solve(
        self, 
        problem_name: str,
        problem_text: str, 
        include_tests: bool = True,
        verbose: bool = True
    ) -> Solution:
        """
        Resuelve un problema de Dynamic Programming completo
        
        Args:
            problem_name: Nombre del problema (ej: "Fibonacci")
            problem_text: Descripción completa del problema
            include_tests: Si generar casos de prueba
            verbose: Si imprimir progreso
            
        Returns:
            Solution con toda la información
        """
        if verbose:
            print(f"\n{'='*70}")
            print(f"🤖 Resolviendo: {problem_name}")
            print(f"{'='*70}\n")
        
        # Paso 1: Análisis
        if verbose:
            print("📊 Paso 1/3: Analizando problema...")
        analysis = self._analyze_problem(problem_text)
        if verbose:
            print(f"   ✅ Patrón identificado: {analysis['pattern']}")
        
        # Paso 2: Solución
        if verbose:
            print("💻 Paso 2/3: Generando código...")
        solution = self._generate_solution(problem_text, analysis)
        if verbose:
            print(f"   ✅ Código generado ({len(solution['code'].split(chr(10)))} líneas)")
        
        # Paso 3: Tests (opcional)
        test_cases = None
        if include_tests:
            if verbose:
                print("🧪 Paso 3/3: Generando tests...")
            test_cases = self._generate_tests(problem_text, solution['code'])
            if verbose:
                print(f"   ✅ {len(test_cases)} casos de prueba")
        
        if verbose:
            print(f"\n{'='*70}")
            print("✨ ¡Solución completada!")
            print(f"{'='*70}\n")
        
        return Solution(
            problem_name=problem_name,
            analysis=analysis['analysis'],
            pattern=analysis['pattern'],
            algorithm=analysis['algorithm'],
            approach=analysis['approach'],
            code=solution['code'],
            time_complexity=solution['time_complexity'],
            space_complexity=solution['space_complexity'],
            explanation=solution['explanation'],
            test_cases=test_cases
        )
    
    def _analyze_problem(self, problem_text: str) -> Dict:
        """Analiza el problema e identifica patrón DP"""
        
        prompt = f"""Eres un experto en algoritmos de Dynamic Programming.

Analiza este problema e identifica:
1. El patrón DP subyacente (fibonacci-like, knapsack, subsequence, etc.)
2. El enfoque óptimo (memoization, tabulation, o ambos)
3. La estructura del subproblema

Problema:
{problem_text}

IMPORTANTE: Responde SOLO con JSON válido, sin markdown ni bloques de código.
Formato exacto:
{{
  "analysis": "Análisis breve del problema",
  "pattern": "Patrón DP identificado",
  "algorithm": "Nombre del algoritmo específico",
  "approach": "memoization o tabulation"
}}"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            
            # Limpiar respuesta
            text = self._clean_json_response(response.text)
            return json.loads(text)
            
        except Exception as e:
            print(f"⚠️  Error en análisis: {e}")
            return {
                "analysis": "Problema de programación dinámica",
                "pattern": "Dynamic Programming",
                "algorithm": "DP genérico",
                "approach": "memoization"
            }
    
    def _generate_solution(self, problem_text: str, analysis: Dict) -> Dict:
        """Genera código Python y análisis de complejidad"""
        
        prompt = f"""Eres un experto programador Python especializado en Dynamic Programming.

Problema:
{problem_text}

Análisis previo:
- Patrón: {analysis['pattern']}
- Algoritmo: {analysis['algorithm']}
- Enfoque: {analysis['approach']}

Genera una solución completa en Python con:
1. Docstrings comprehensivos
2. Type hints
3. Nombres descriptivos de variables
4. Comentarios explicando la lógica DP
5. Manejo de casos edge
6. Código limpio siguiendo PEP 8

IMPORTANTE: Responde SOLO con JSON válido, sin markdown ni bloques de código.
Formato exacto:
{{
  "code": "Función(es) Python completas como string",
  "time_complexity": "Big-O con explicación breve",
  "space_complexity": "Big-O con explicación breve",
  "explanation": "Explicación paso a paso de la solución"
}}"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            
            text = self._clean_json_response(response.text)
            return json.loads(text)
            
        except Exception as e:
            print(f"⚠️  Error en generación: {e}")
            return {
                "code": f"# Error generando código\n# {str(e)}",
                "time_complexity": "Unknown",
                "space_complexity": "Unknown",
                "explanation": f"Error: {str(e)}"
            }
    
    def _generate_tests(self, problem_text: str, code: str) -> List[Dict]:
        """Genera casos de prueba"""
        
        prompt = f"""Genera casos de prueba comprehensivos para este problema.

Problema:
{problem_text}

Código:
{code}

Incluye:
1. Casos básicos/normales
2. Casos edge (vacío, un elemento, etc.)
3. Casos de frontera
4. Casos grandes

IMPORTANTE: Responde SOLO con JSON válido.
Formato exacto:
{{
  "test_cases": [
    {{
      "input": "descripción o valor del input",
      "expected_output": "resultado esperado",
      "description": "qué verifica este test"
    }}
  ]
}}"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            
            text = self._clean_json_response(response.text)
            result = json.loads(text)
            return result.get('test_cases', [])
            
        except Exception as e:
            print(f"⚠️  Error en tests: {e}")
            return []
    
    def _clean_json_response(self, text: str) -> str:
        """Limpia la respuesta para obtener JSON válido"""
        text = text.strip()
        
        # Remover markdown
        if text.startswith("```json"):
            text = text.replace("```json", "", 1)
        if text.startswith("```"):
            text = text.replace("```", "", 1)
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0]
        
        return text.strip()
    
    def format_solution(self, solution: Solution) -> str:
        """Formatea la solución para impresión bonita"""
        
        output = f"""
╔══════════════════════════════════════════════════════════════╗
║  {solution.problem_name.center(60)}  ║
╚══════════════════════════════════════════════════════════════╝

📊 ANÁLISIS DEL PROBLEMA
{'-'*64}
{solution.analysis}

🎯 PATRÓN IDENTIFICADO
{'-'*64}
{solution.pattern}

⚙️  ALGORITMO
{'-'*64}
{solution.algorithm} ({solution.approach})

💻 CÓDIGO PYTHON
{'-'*64}
{solution.code}

⏱️  COMPLEJIDAD TEMPORAL
{'-'*64}
{solution.time_complexity}

💾 COMPLEJIDAD ESPACIAL
{'-'*64}
{solution.space_complexity}

📝 EXPLICACIÓN
{'-'*64}
{solution.explanation}
"""
        
        if solution.test_cases:
            output += f"""
🧪 CASOS DE PRUEBA
{'-'*64}
"""
            for i, test in enumerate(solution.test_cases, 1):
                output += f"""
Test {i}: {test.get('description', 'N/A')}
  Input:    {test.get('input', 'N/A')}
  Expected: {test.get('expected_output', 'N/A')}
"""
        
        return output
    
    def list_available_models(self):
        """Lista los modelos disponibles en tu API key"""
        try:
            print("\n📋 Modelos Gemini disponibles:")
            print("-" * 60)
            
            models = genai.list_models()
            for model in models:
                if 'generateContent' in model.supported_generation_methods:
                    print(f"✅ {model.name.split('/')[-1]}")
            
            print("-" * 60)
        except Exception as e:
            print(f"❌ Error listando modelos: {e}")


def main():
    """Función principal de demostración"""
    
    print("="*70)
    print("🚀 AI Algorithm Solver - Dynamic Programming Agent")
    print("="*70)
    print()
    
    # Problema de ejemplo
    problema_fibonacci = """
Problem: Fibonacci Number

The Fibonacci numbers form a sequence where each number is the sum of 
the two preceding ones, starting from 0 and 1.

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
    
    try:
        # Crear agent
        agent = DPAgent()
        
        # Mostrar modelos disponibles
        agent.list_available_models()
        
        # Resolver problema
        solution = agent.solve(
            problem_name="Fibonacci Number",
            problem_text=problema_fibonacci,
            include_tests=True
        )
        
        # Mostrar solución
        print(agent.format_solution(solution))
        
        # Guardar en archivo
        os.makedirs("results", exist_ok=True)
        solution.save_to_file("results/fibonacci_solution.json")
        print(f"\n✅ Solución guardada en: results/fibonacci_solution.json")
        
    except ValueError as e:
        print(f"\n{e}")
        print("\n💡 Configuración rápida:")
        print("1. Ve a: https://makersuite.google.com/app/apikey")
        print("2. Crea un API key")
        print("3. Ejecuta: echo 'GEMINI_API_KEY=tu-key' > .env")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n🔧 Debugging:")
        print("1. Verifica tu API key en .env")
        print("2. Verifica tu conexión a internet")
        print("3. Intenta de nuevo en unos segundos")


if __name__ == "__main__":
    main()