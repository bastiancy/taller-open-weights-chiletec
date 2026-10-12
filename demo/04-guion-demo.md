# 4. Guion de la demo en vivo (60 minutos)

Basado en la sugerencia de reordenar el temario original: hardware primero (breve), luego la demo, benchmarks y cierre al final. Todos los modelos deben estar **ya descargados** antes de empezar — nunca descargues un modelo de varios GB en vivo.

## Minuto 0-5 — Antes de compartir pantalla

- Cierra pestañas y apps innecesarias.
- Abre dos terminales: una para comandos, otra con `nvidia-smi -l 1` corriendo (refresca cada segundo) para mostrar consumo de VRAM en tiempo real.
- Ten LM Studio ya abierto de fondo (sin compartir pantalla todavía).
- Ten el documento de ejemplo de la demo de RAG ya guardado y ubicable rápido.

## Minuto 5-15 — Dimensionamiento rápido (mover antes de la demo)

- Muestra `nvidia-smi` limpio (sin nada corriendo): 24 GB libres.
- Explica la regla: `VRAM ≈ pesos + KV cache + 15-20% overhead`.
- Menciona la tabla de la slide 19 (dimensionamiento por VRAM) — solo un vistazo, el detalle ya está en la charla.

## Minuto 15-30 — Ollama por consola: el motor

```bash
ollama list
ollama run gpt-oss:20b
```

- Mientras carga, cambia a la terminal con `nvidia-smi -l 1` — la audiencia ve la VRAM subir en tiempo real. Este es el momento más visual de la charla.
- Haz una pregunta simple en el chat de consola para mostrar que responde.
- Sal con `/bye`.
- Punto clave a decir en voz alta: *"Esto que acaban de ver corriendo en mi terminal es exactamente el mismo modelo que van a usar con clic en LM Studio — es el mismo motor por debajo."*

## Minuto 30-45 — LM Studio: la cara amigable + RAG

- Abre LM Studio, carga el mismo modelo (o el de mayor calidad si la conexión y el tiempo lo permitieron: `qwen2.5:32b-instruct-q4_K_M`).
- Muestra el explorador de modelos y el slider de parámetros — remarca que es la misma potencia sin terminal.
- Adjunta el documento corporativo de ejemplo.
- Haz 2 preguntas de contenido que respondan bien (demuestra que el RAG funciona y que el documento nunca salió del equipo — puedes mostrar que no hay conexión de red activa, o mostrarlo en modo avión si tu setup lo permite).

## Minuto 45-52 — Benchmarks en 2 minutos

- Muestra la slide del framework de decisión (licencia → hardware → español → benchmark de tarea → eval propia).
- No profundices mucho aquí — ya se vio en la Parte 1. Es un recordatorio antes de la demo de fracaso.

## Minuto 52-58 — La demo de fracaso (el gancho al Taller 2)

Este es el momento más importante del cierre. Pide al modelo, sobre el mismo documento:

> "Devuélveme el análisis en un JSON con exactamente estos campos: `resumen`, `riesgos`, `monto_total`. Sin texto adicional, sin markdown, solo el JSON."

- El modelo va a acertar el **contenido** pero va a fallar la **forma**: agrega texto antes o después, usa bloques de markdown, cambia nombres de campos, o anida mal el JSON.
- Muéstralo sin editar nada — el fallo real es más convincente que cualquier slide.
- Cierra con la frase ancla: *"El RAG le dio los datos correctos. Pero no puedo hacer que se comporte exactamente como necesito. Para eso hay que tocar los pesos del modelo — y eso es exactamente el Taller 2."*

## Minuto 58-60 — Cierre

- Menciona DashAI como el puente natural (mismo argumento de soberanía, capa de entrenamiento).
- Agradece y comparte el link del repo para que los asistentes instalen por su cuenta si quieren (`para-asistentes/`).

---

### Frases ancla para memorizar (una por sección)

- *"Open weights no es IA gratis: es IA que corre en fierro que tú controlas."*
- *"Tus documentos y tus prompts nunca salen del equipo."* (no digas "100% privado" a secas — ver nota de honestidad en la slide 3 de troubleshooting)
- *"Cambiar de la nube a local puede ser cambiar una URL."*
- *"El RAG le dio los datos correctos. Pero no puedo hacer que se comporte como necesito."*
