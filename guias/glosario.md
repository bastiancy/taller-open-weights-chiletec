# Glosario del taller

Los conceptos de la charla, en lenguaje simple.

**LLM (Large Language Model)**
Un modelo que recibe texto y predice qué viene después, un token a la vez. ChatGPT no es un LLM: es una aplicación de chat que usa un LLM por dentro.

**Token**
El modelo no lee letras ni palabras, sino tokens: pedazos de texto con un número. Cada modelo corta distinto ("licitación" son 3 tokens en Llama 3.2 y 2 en Gemma 4). El contexto, la velocidad y el precio de las APIs se miden en tokens.

**Embedding**
Una lista de números que representa el significado de un token o de un texto. Significados parecidos quedan cerca ("Santiago" cerca de "Lima"). Así encuentra un RAG los fragmentos relevantes.

**Parámetro / peso**
Cada conexión de la red neuronal es un número aprendido: un peso. Al total le llamamos parámetros; "27B" significa 27 mil millones. El archivo que descargas es, literalmente, una lista de esos números.

**Transformer**
La arquitectura de casi todos los LLM actuales (Google, 2017). Cada bloque tiene atención (cada token mira a los anteriores) y una red feed-forward; el bloque se repite decenas de veces.

**Open weights**
Modelos cuyo archivo de pesos puedes descargar y correr en tu equipo. Distinto de una **API cerrada** (tus datos viajan al proveedor) y de **open source** completo (además publican el código y los datos de entrenamiento).

**Instruct / base**
Un modelo *base* solo completa texto. Uno *instruct* (o *it*) fue post-entrenado para seguir instrucciones y conversar.

**Destilado**
Un modelo chico entrenado para imitar a uno grande (por ejemplo, DeepSeek-R1-0528-Qwen3-8B aprendió de DeepSeek R1).

**Cuantización**
Comprimir los pesos usando menos bits por número (Q8, Q4_K_M…). Un modelo de 8B pasa de ~16 GB a ~5 GB con una pérdida de calidad pequeña. Como pasar una foto de RAW a JPEG.

**GGUF**
El formato de archivo de los modelos cuantizados que usan LM Studio y Ollama.

**Denso / MoE (Mixture of Experts)**
Un modelo denso usa todos sus parámetros para cada token. Uno MoE activa solo algunos "expertos": `26B-A4B` ocupa memoria como uno de 26B, pero trabaja como uno de 4B, por eso es mucho más rápido.

**Capacidades**
*Razonamiento* (escribe sus pasos antes de responder), *uso de herramientas* (pide que tu sistema ejecute una función) y *visión* (lee imágenes). No todos los modelos tienen las tres.

**Ventana de contexto**
Todo lo que el modelo considera a la vez, medido en tokens: instrucciones, conversación, documentos y respuesta. Lo que no cabe, no lo ve. Cada token de contexto ocupa memoria (la caché KV).

**GPU / VRAM / offload**
La VRAM es la memoria de la tarjeta gráfica. Si el modelo no cabe, una parte de las capas va a la CPU (*offload*): funciona, pero mucho más lento.

**Tokens por segundo**
La velocidad a la que el modelo genera texto. Depende del modelo y de tu hardware.

**Benchmark / índice de inteligencia / Elo**
Formas de comparar modelos. El índice de Artificial Analysis es un examen automático (mide si acierta); el Elo de LMArena es una votación humana a ciegas (mide qué prefiere la gente). Ninguno conoce tu tarea: pruébalo con tus propios casos.

**RAG (Retrieval-Augmented Generation)**
Buscar fragmentos relevantes de tus documentos y mostrárselos al modelo junto con la pregunta. Sirve para que sepa cosas nuevas sin cambiar el modelo.

**Fine-tuning**
Ajustar los pesos de un modelo con tus propios ejemplos para cambiar cómo se comporta (formato, tono, una tarea específica). Tema de un próximo taller.

**Licencia**
Las reglas de uso del modelo. Apache 2.0 y MIT permiten uso comercial libre; otras tienen restricciones propias. Revísala antes de usar un modelo en tu empresa.
