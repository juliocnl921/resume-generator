CONTEXT = """Genera un CV optimizado para la vacante.

OBJETIVO:
- Maximizar compatibilidad con ATS usando keywords relevantes.
- Mantener solo información relevante al puesto.

REGLAS:
- Elimina habilidades y experiencias no relacionadas.
- Prioriza tecnologías y tareas de la vacante.
- Ordena skills por relevancia.
- Máximo 4 experiencias.
- Máximo 4 bullets por experiencia.
- Cada bullet corto (1–2 líneas) con impacto y keywords.
- Redacta en el mismo idioma que la posicion

FORMATO:
- Responde SOLO en JSON válido.
- Usa EXACTAMENTE los mismos campos del input.
- No agregues texto fuera del JSON.
"""
MODEL = "gpt-4o-mini" 
MODEL_MINI = "gpt-5-mini"
MODEL_NANO = "gpt-5.4-nano"
MODEL_FULL = "gpt-5.4"