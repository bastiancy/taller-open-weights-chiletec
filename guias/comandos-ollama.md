# Comandos de Ollama usados en la demo

Los mismos conceptos que se ven en LM Studio, ahora en la terminal. En la demo se usó `gemma4:26b` (Gemma 4 26B-A4B, un modelo MoE de 17 GB). Si tu equipo tiene menos memoria, cambia el nombre por `llama3.2:3b`.

| En LM Studio | En Ollama |
|---|---|
| Library | `ollama list` |
| Panel de información del modelo | `ollama show gemma4:26b` |
| Chat y estadísticas | `ollama run gemma4:26b --verbose` |
| Pestaña Load (memoria, GPU, contexto) | `ollama ps` |
| Servidor local | API en `http://localhost:11434` |

## 1. Descargar y listar modelos

```bash
ollama pull gemma4:26b
ollama list
```

## 2. Ver la ficha del modelo

```bash
ollama show gemma4:26b
```

Muestra los parámetros (25.8B), la cuantización (Q4_K_M), la ventana de contexto máxima (262.144 tokens) y las capacidades (`vision`, `tools`, `thinking`).

## 3. Conversar y medir la velocidad

```bash
ollama run gemma4:26b --verbose
>>> La capital de Chile es
```

Al final de cada respuesta, `--verbose` muestra el **eval rate**: los tokens por segundo que genera tu equipo. Para salir: `/bye`.

Dentro del chat puedes cambiar la ventana de contexto:

```
/set parameter num_ctx 32768
```

## 4. Ver la memoria y si corre en GPU o CPU

En otra terminal, mientras el modelo está cargado:

```bash
ollama ps
```

- **SIZE:** memoria total (pesos + caché de contexto). Sube si aumentas `num_ctx`.
- **PROCESSOR:** `100% GPU`, `100% CPU` o un reparto como `48%/52% CPU/GPU`.
- **CONTEXT:** la ventana de contexto configurada.

Para descargar el modelo de la memoria: `ollama stop gemma4:26b`.

## 5. Por debajo de todo: el API

Cualquier aplicación puede conversar con el modelo por HTTP:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:26b",
  "messages": [{"role": "user", "content": "La capital de Chile es"}],
  "stream": false
}'
```

La respuesta trae el texto y los contadores: `prompt_eval_count` (tokens de entrada), `eval_count` (tokens generados) y `eval_duration` (nanosegundos). Tokens por segundo = `eval_count ÷ eval_duration × 10⁹`.

Ollama también acepta el formato del API de OpenAI en `http://localhost:11434/v1`, así que una aplicación que hoy usa OpenAI puede apuntar a tu equipo cambiando la URL.

## Referencias

- [CLI de Ollama](https://docs.ollama.com/cli) · [API](https://docs.ollama.com/api) · [Compatibilidad con OpenAI](https://docs.ollama.com/openai) · [FAQ](https://docs.ollama.com/faq) · [Largo de contexto](https://docs.ollama.com/context-length)
