# 🤖 AI Algorithm Solver - Dynamic Programming

> Proyecto ALDA 2026 - 20% de la nota final

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Gemini-API-green.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-Academic-yellow.svg)]()

---

## 👨‍💻 Autor

**Julian David Castiblanco Real**  
Escuela de Ingenieros  
Universidad Escuela Colombiana ingenieria Julio Garavito Armero

---

## 📚 Descripción

AI Agent que resuelve problemas de **Dynamic Programming** usando Google Gemini API. El agent analiza problemas algorítmicos, identifica patrones DP, genera código Python optimizado y proporciona análisis de complejidad completo.

### 🎯 Características

- ✅ Identificación automática de patrones DP
- ✅ Generación de código Python con type hints
- ✅ Análisis de complejidad temporal y espacial
- ✅ Generación automática de casos de prueba
- ✅ Interfaz interactiva fácil de usar

---

## ✅ Problemas Resueltos

### Básicos
- [x] **Fibonacci Number**
  - Patrón: Fibonacci-like / Overlapping subproblems
  - Algoritmo: DP con Tabulación
  - Complejidad: O(n) tiempo, O(n) espacio
  - Estado: ✅ Completado
  - [Ver solución](results/fibonacci_number_solution.json)

### Pendientes
- [ ] Climbing Stairs (Básico)
- [ ] Coin Change (Medio)
- [ ] Longest Common Subsequence (Medio)
- [ ] 0/1 Knapsack (Medio)

**Meta:** Resolver 8-10 problemas de diferentes dificultades

---

## 🚀 Instalación

### Requisitos Previos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Cuenta de Google (para API key gratuita)

### Pasos de Instalación

```bash
# 1. Clonar repositorio
git clone https://github.com/TU-USUARIO/ai-algorithm-solver.git
cd ai-algorithm-solver

# 2. Crear virtual environment
python -m venv venv

# 3. Activar virtual environment
# Windows (Git Bash):
source venv/Scripts/activate
# Windows (CMD):
venv\Scripts\activate.bat
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Configurar API key
cp .env.example .env
# Editar .env y agregar tu GEMINI_API_KEY
```

---

## 🔑 Obtener API Key de Gemini (100% GRATIS)

1. Ve a: https://makersuite.google.com/app/apikey
2. Inicia sesión con tu cuenta Google
3. Click en **"Create API Key"**
4. Copia el key (empieza con `AIzaSy...`)
5. Pégalo en tu archivo `.env`:
   ```
   GEMINI_API_KEY=tu-key-aqui
   ```

**Límites gratuitos:**
- 1,500 requests por día
- Más que suficiente para el proyecto

---

## 💻 Uso

### Programa Interactivo

```bash
python main.py
```

### Menú Principal

```
📋 MENÚ PRINCIPAL
1. 🎯 Resolver problema predefinido
2. ✍️  Resolver problema personalizado
3. 📊 Ver resultados guardados
4. ℹ️  Información del proyecto
0. 🚪 Salir
```

### Ejemplo de Uso

```python
# También puedes usar el agent directamente en código
from src.agent import DPAgent

agent = DPAgent()

problema = """
Problem: Fibonacci Number
[descripción del problema]
"""

solution = agent.solve(
    problem_name="Fibonacci",
    problem_text=problema,
    include_tests=True
)

print(solution.code)
print(f"Complejidad: {solution.time_complexity}")
```

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| **Python 3.13** | Lenguaje principal |
| **Google Gemini API** | Modelo de IA (gemini-pro) |
| **google-generativeai** | Cliente de API |
| **python-dotenv** | Gestión de variables de entorno |

---

## 📁 Estructura del Proyecto

```
ai-algorithm-solver/
│
├── main.py                 # 🎯 Programa principal interactivo
├── src/
│   └── agent.py           # 🤖 Clase DPAgent (core del proyecto)
│
├── results/               # 💾 Soluciones generadas (JSON)
│   └── fibonacci_number_solution.json
│
├── problems/              # 📚 Problemas de prueba
│   ├── test/             # Para desarrollo
│   └── evidence/         # Para evidencia final
│
├── docs/                  # 📖 Documentación adicional
│
├── requirements.txt       # 📦 Dependencias Python
├── .env.example          # 🔐 Template de configuración
├── .gitignore            # 🚫 Archivos a ignorar
└── README.md             # 📄 Este archivo
```

---

## 📊 Resultados y Estadísticas

### Fibonacci Number - Análisis Detallado

**Métricas:**
- ✅ Código generado: 45 líneas
- ✅ Casos de prueba: 10
- ✅ Complejidad temporal: O(n)
- ✅ Complejidad espacial: O(n)
- ✅ Tiempo de generación: ~3 segundos

**Patrón identificado:** Fibonacci-like sequence with overlapping subproblems

**Enfoque:** Tabulación (bottom-up DP)

**Calidad del código:**
- Type hints completos ✅
- Docstrings detallados ✅
- Comentarios explicativos ✅
- Manejo de edge cases ✅

---

## 🎓 Para el Curso ALDA

### Objetivos del Proyecto
- ✅ Implementar AI Agent funcional
- ⏳ Resolver 5-10 problemas DP (1/5 completado)
- ⏳ Demostrar solución de problemas nuevos
- ⏳ Documentar proceso y resultados
- ⏳ Repositorio público en GitHub

### Criterios de Evaluación

| Criterio | Peso | Estado |
|----------|------|--------|
| Funcionalidad del Agent | 40% | ✅ Implementado |
| Sofisticación (prompts, lógica) | 30% | ✅ Implementado |
| Evidencia (problemas nuevos) | 20% | ⏳ Pendiente |
| Documentación | 10% | ⏳ En progreso |

---

## 🔬 Metodología

### Arquitectura del Agent

1. **Análisis del Problema**
   - Identificación de patrón DP
   - Determinación de enfoque (memoization/tabulation)
   - Análisis de estructura de subproblemas

2. **Generación de Solución**
   - Código Python optimizado
   - Type hints y documentación
   - Manejo de casos especiales

3. **Análisis de Complejidad**
   - Cálculo de Big-O temporal
   - Cálculo de Big-O espacial
   - Justificación detallada

4. **Generación de Tests**
   - Casos base
   - Casos normales
   - Casos de frontera

---

## 🧪 Testing

### Ejecutar Tests

```bash
# Usar el menú interactivo
python main.py
# Seleccionar opción 1 y resolver problemas

# O ejecutar diagnóstico
python diagnostico_gemini.py
```

### Estructura de Tests

Cada solución incluye:
- ✅ Mínimo 5 casos de prueba
- ✅ Casos base (n=0, n=1)
- ✅ Casos normales
- ✅ Casos de frontera

---

## 📈 Roadmap

### Semana 1 (Actual) ✅
- [x] Setup del proyecto
- [x] Configuración de Gemini API
- [x] Implementación del DPAgent
- [x] Primer problema resuelto (Fibonacci)

### Semana 2
- [ ] Resolver 4 problemas adicionales
- [ ] Documentar cada solución
- [ ] Ajustar prompts según necesidad

### Semana 3
- [ ] Resolver problemas nuevos (evidencia)
- [ ] Grabar video de demostración
- [ ] Screenshots de resultados

### Semana 4
- [ ] Documentación final completa
- [ ] Revisión de código
- [ ] Preparación de presentación

---

## 🤝 Contribuciones

Este es un proyecto académico individual para el curso ALDA 2026.

---

## 📝 Licencia

Este proyecto es con fines académicos exclusivamente.

**Universidad de Los Andes - ALDA 2026**

---

## 🙏 Agradecimientos

- **Google Gemini Team** - Por proporcionar API gratuita
- **Profesor del curso ALDA** - Por la guía del proyecto
- **Universidad de Los Andes** - Escuela de Ingenieros

---

## 📞 Contacto

**Julian David Castiblanco Real**  
Escuela de Ingenieros  
Universidad de Los Andes

---

## ⚠️ Notas Importantes

1. ✅ El repositorio DEBE ser público (requisito del curso)
2. ❌ NUNCA subir el archivo `.env` con tu API key
3. ✅ Usar `.gitignore` para proteger información sensible
4. ✅ Documentar todo el proceso
5. ✅ Poder explicar cada línea de código generado

---

## 🔍 Troubleshooting

### Problema: Error de API key
```bash
# Verifica que .env existe y tiene tu key
cat .env

# Debe contener:
GEMINI_API_KEY=AIzaSy...
```

### Problema: Modelo no disponible
```bash
# Ejecuta diagnóstico
python diagnostico_gemini.py

# Esto te dirá qué modelos tienes disponibles
```

### Problema: Import errors
```bash
# Reinstala dependencias
pip install -r requirements.txt
```

---

## 📚 Recursos Adicionales

- [Documentación Gemini API](https://ai.google.dev/)
- [Dynamic Programming - CLRS](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)
- [LeetCode DP Problems](https://leetcode.com/tag/dynamic-programming/)

---

**Última actualización:** Febrero 2026  
**Versión:** 1.0.0  
**Estado:** 🚧 En desarrollo activo

---

<div align="center">

**⭐ Si este proyecto te fue útil, dale una estrella ⭐**

Hecho con ❤️ para ALDA 2026

</div>
