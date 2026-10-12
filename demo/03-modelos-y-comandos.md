# 3. Modelos recomendados y comandos

## Importante: verifica los nombres exactos antes del taller

Los proveedores actualizan y renombran versiones seguido. Unos días antes del taller, confirma el nombre exacto del tag en la [librería de Ollama](https://ollama.com/library) o con:

```bash
ollama search qwen
ollama search gpt-oss
ollama search deepseek
```

Los comandos de abajo usan los nombres más estables a la fecha de escritura de este repo. Si un tag ya no existe, `ollama.com/library/<modelo>` te muestra las variantes vigentes.

## Modelo principal recomendado para la demo: gpt-oss:20b

Es la apuesta más segura para un 24 GB de VRAM: licencia Apache 2.0 sin restricciones, ~16 GB en su cuantización nativa (deja margen cómodo en la 3090), y pensado explícitamente para equipos con recursos moderados.

```bash
ollama pull gpt-oss:20b
```

## Alternativa de mayor calidad (si tu conexión y tiempo lo permiten)

Un modelo denso de ~27-32B en Q4 aprovecha mejor los 24 GB y da mejores respuestas para la demo de análisis de documentos:

```bash
ollama pull qwen2.5:32b-instruct-q4_K_M
```

> Al momento del taller puede existir una versión más nueva de la línea Qwen (revisa `ollama search qwen`). El comando de arriba es el punto de partida seguro; si hay una versión posterior con licencia Apache 2.0, prefiérela.

## Modelo chico para pruebas rápidas / respaldo

Si algo falla con los modelos grandes en vivo, ten este como plan B — pesa ~1.3 GB y responde casi instantáneo:

```bash
ollama pull llama3.2:1b
```

## Tabla de referencia para explicar en vivo (RTX 3090, 24 GB)

| Modelo | Parámetros | Cuantización | Tamaño aprox. | Cabe en 24 GB con contexto largo |
|---|---|---|---|---|
| llama3.2:1b | 1B | Q8 | ~1.3 GB | Sí, sobra mucho margen |
| gpt-oss:20b | 20B (MoE) | nativa (~4 bits) | ~13-16 GB | Sí, cómodo |
| qwen2.5:32b-instruct-q4_K_M | 32B | Q4_K_M | ~19-20 GB | Ajustado — reduce el contexto si hace swap |

## Descargar todo de una vez (la noche anterior, no el día del taller)

```bash
ollama pull llama3.2:1b
ollama pull gpt-oss:20b
ollama pull qwen2.5:32b-instruct-q4_K_M
ollama list
```

## Preparar el documento para la demo de RAG

1. Ten a mano un documento corporativo de ejemplo (PDF o Word, 3-10 páginas) que **no** contenga información sensible real — usa un contrato de plantilla, un informe ficticio, o anonimiza uno real.
2. En **LM Studio**: pestaña de chat → ícono de clip/adjuntar → selecciona el documento. LM Studio lo indexa localmente y responde con RAG sin que el archivo salga de tu equipo.
3. Prepara 2-3 preguntas de contenido (que sí va a responder bien) y **una pregunta de formato estricto** para la demo de fracaso planeada (ver el guion): pídele que devuelva la respuesta en un JSON con campos específicos. Va a fallar en la forma, no en el fondo — ese es exactamente el gancho hacia el Taller 2.

Siguiente paso: [04-guion-demo.md](04-guion-demo.md)
