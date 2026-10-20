# Contenido del Taller 1 — Modelos "Open Weights"
### Documento de trabajo — para revisar y corregir antes de pasar a diapositivas

> **Cómo usar este documento:** cada afirmación factual lleva una cita `[n]` que remite a la sección **Fuentes** al final. Las fuentes 1 a 54 se verificaron el 23 y 24 de septiembre de 2026; las fuentes 55 en adelante, el 5 de octubre de 2026. Donde algo estaba impreciso, se marca con **⚠️ Corrección**. Los benchmarks cambian semana a semana: donde aplica, se indica la fecha exacta del dato. La numeración tiene saltos a propósito (fuentes que quedaron sin uso al recortar contenido).

**Notas de estructura y diseño (acordadas):**
- Dos partes: Parte 1, *Breve historia de la galaxia* (30 min), y Parte 2, *Práctica Jedi: usar modelos Open Weights localmente* (60 min).
- Las diapositivas se hacen en **HTML** (fondo espacial, nave que recorre las líneas de tiempo). Para compartir después: exportar a PDF y a PPTX plano (una imagen por diapositiva).
- **Un concepto por diapositiva, con un diagrama animado y el mínimo texto.** El diagrama tiene que explicar el concepto por sí solo.
- La presentación va **de lo general a lo detallado**. La Parte 1 deja muy claro cómo funciona un LLM; los conceptos más técnicos (cuantización, variantes, capacidades, contexto) se explican **durante las demos**, cuando aparecen en pantalla.
- La historia es una anécdota rápida (una sola diapositiva, tres actos) que sirve para el chiste del lado claro y el lado oscuro.
- Humor de Star Wars con moderación.
- DashAI, el caso Samsung y el gancho del "JSON mal formateado" quedaron fuera.
- En la Parte 2 **manda el software en vivo**; las diapositivas resumen un concepto cada una y sirven de guía al speaker (pueden llevar capturas de LM Studio y Ollama) y de respaldo si algo falla.
- Todo lo que se muestre en vivo queda en el **repo de GitHub** para que los asistentes lo repitan en su equipo.

---

## Resumen de temas

**Parte 1 — El origen de la galaxia (~25 min, conceptos) + Interludio: breve historia del Imperio (~5 min, se puede saltar con la tecla S)**
- Temario (Chiletec presenta al speaker antes de empezar)
- El origen: ¿qué es un LLM? (tokens, embeddings, red neuronal, probabilidades, un token a la vez)
- El origen: en realidad, un Transformer (atención + red feed-forward, repetidos decenas de veces)
- El origen: ¿qué es un parámetro? (pesos, tamaño en B y tamaño del archivo)
- El origen: token, embedding, capacidades (herramientas, razonamiento, visión) y ventana de contexto, una diapositiva cada uno
- Bonus al final del deck: ¿cómo aprende? (cómo se entrena un LLM) (adivina, compara, ajusta los pesos; lo que queda es el archivo de pesos)
- El origen: ¿cómo nace un archivo Open Weights? (pre-entrenamiento, post-entrenamiento, publicación; versiones cuantizadas, destiladas y afinadas)
- Tres tipos de modelo: API cerrada, open weights y open source
- Breve historia en tres actos: el lado claro (GPT-2), el lado oscuro (GPT-3 y ChatGPT) y la rebelión (LLaMA se filtra)

**Parte 2 — Práctica Jedi (60 min)** — *estructura preliminar, el detalle se define en la próxima revisión*
- **LM Studio:** anatomía de un modelo usando la interfaz: catálogo, variantes (base, instruct, destiladas, denso contra MoE), cuantización, capacidades (razonamiento, uso de herramientas, visión), ventana de contexto y offload GPU/CPU.
- **Benchmarks: cómo elegir.** Con los conceptos ya vistos en LM Studio: factores de hardware y capacidades del modelo.
- **Ollama + RAG (caso de uso):** notebook interactivo que conecta Ollama con la carpeta de la licitación (bases, anexos, foro). Muestra que el código para una aplicación empresarial es poco, qué hacer cuando la información no cabe en la ventana de contexto, y el uso de herramientas (agente).
- Cierre: qué llevarse, repo y Taller 2.

**Hilo conductor de la Parte 2:** las bases del nuevo Convenio Marco de software de ChileCompra (ID 2239-2-LR26).

---

## Parte 1 — El origen de la galaxia (~25 min) e Interludio (~5 min)

**Orden de la Parte 1 (acordado el 19 oct. 2026):** ¿Qué es un LLM? (chat) → token → embedding → parámetro → Entonces, ¿qué es un LLM? → En realidad, un Transformer → capacidades (razonamiento, herramientas, visión) → ventana de contexto → breve historia → tres tipos de modelo (resumen de la historia). "¿Cómo aprende?" pasa al final del deck como bonus, después de "Gracias". "¿Cómo nace un archivo Open Weights?" se eliminó del deck (su contenido queda abajo como respaldo).

### El origen (0): ¿Qué es un LLM? (la ventana de chat)

Ventana de chat lo más parecida a ChatGPT (sin logos). Paso 0: ventana vacía. Paso 1 (al avanzar): el usuario escribe "¿Cuál es la capital de Chile?" y el asistente responde "La capital de Chile es Santiago." token a token. Paso 2: junto al título aparece "…no, esto es un chatbot": la aplicación no es el modelo; por dentro, un LLM procesa el texto. Corrige el error común de pensar que ChatGPT *es* el modelo.

### El origen (1): Entonces, ¿qué es un LLM?

Un LLM (*Large Language Model*, o modelo de lenguaje de gran escala) recibe texto y **predice qué viene después**. El ejemplo de la diapositiva es *"La capital de Chile es ___"*, y la animación recorre el camino completo:

1. **Tokens.** El texto se corta en pedazos y cada pedazo es un número de un vocabulario fijo. Con el tokenizador de Qwen3, la frase queda en cinco tokens: `La` (8747), `capital` (6722), `de` (409), `Chile` (33000), `es` (1531). El vocabulario de Qwen3 tiene 151.669 tokens [65]. Ojo: no siempre un token es una palabra; "gato" se corta en `g` + `ato`, y "Valparaíso" en cuatro pedazos [65].
2. **Embeddings.** Cada token se convierte en una lista de números que representa su significado.
3. **La red neuronal.** Esos números atraviesan capa tras capa; cada conexión multiplica por un **peso**. *(Simplificación: el diagrama dibuja una red tradicional de capas; la arquitectura real es Transformer [1], pero la idea de pesos y capas es la misma.)*
4. **Probabilidades.** A la salida hay una probabilidad para cada token del vocabulario. Medido con Llama 3.2 3B en el PC del taller: `Santiago` 68 %, `la` 12 %, `una` 10 %, `un` 2 % [66].
5. **Un token a la vez.** Se elige un token, se agrega al texto y se repite todo el proceso. Así escribe un LLM.

*Diapositiva:* animación en seis pasos, una frase de pie por paso.

### El origen (1b): En realidad, un Transformer

La red de la diapositiva anterior es una simplificación. Casi todos los LLM de hoy, abiertos o cerrados, usan la arquitectura **Transformer** [1]. Versión simplificada, sin entrar en detalle:
- **Tokens → embeddings → bloques Transformer → probabilidades.**
- Cada **bloque** tiene dos partes: **atención**, donde cada token mira a los anteriores para entender el contexto (en el ejemplo, "es" mira sobre todo a "Chile" y "capital"), y una **red feed-forward**, que es la red de capas que dibujamos antes.
- El bloque se repite decenas de veces: 28 en Llama 3.2 3B, 30 en Gemma 4 26B, 36 en Qwen3-8B [68]. Todos esos números son los pesos.

*Diapositiva:* la arquitectura Transformer original (Vaswani et al., 2017 [1]), redibujada a partir del video de ByteByteGo "Transformers Step-by-Step Explained", con las etiquetas en inglés como en el paper. Animación en tres pasos: (0) el diagrama completo, pensado para traducir; (1) se marcan las dos mitades: el **codificador** lee la frase completa y el **decodificador** escribe un token a la vez; (2) desaparecen el codificador y la atención cruzada, y el decodificador queda solo: así son los LLM actuales (*decoder-only*: Llama, Qwen, Gemma, DeepSeek, gpt-oss). Notas: Feed Forward = la red de capas; Masked Attention = cada token solo mira hacia atrás; Nx = 28 en Llama 3.2 3B [68].

**Para explicarlo:** el Transformer original tenía dos mitades porque se inventó para traducir. GPT-1 (2018) mostró que para generar texto basta con apilar bloques del decodificador; desde entonces casi todos los LLM son *decoder-only*. La mitad izquierda sobrevive en modelos como BERT, que sirven para clasificar texto o generar embeddings (como los del RAG de la Parte 2), no para conversar.

### El origen (2): ¿Qué es un parámetro?

Cada conexión de la red es un número aprendido: un **peso**. Al total de pesos le llamamos **parámetros**, y "B" significa miles de millones. Si cada número se guarda en 16 bits (2 bytes), el archivo pesa unos 2 GB por cada mil millones de parámetros [39][40]:

| Modelo | Parámetros | Archivo a 16 bits |
|---|---|---|
| Pequeño (p. ej. Llama 3.2 3B) | 3.000 millones | ~6 GB |
| Mediano (p. ej. Qwen3.6-27B [21]) | 27.000 millones | ~54 GB |
| Gigante (p. ej. DeepSeek R1 [18]) | 671.000 millones | ~1,3 TB |

Cómo achicar ese archivo (cuantización) se explica en la Parte 2, con LM Studio.

### El origen (2b): ¿Qué es un token?

El modelo no lee letras ni palabras: lee **tokens**, pedazos de texto con un número. *Diapositiva:* arriba, "La capital de Chile es Santiago" palabra por palabra (simplificación para mantener el mismo ejemplo en todo el deck). Al avanzar, la frase "La licitación cierra en septiembre" según el tokenizador de tres modelos que se usan en el taller [65][71]:
- **Llama 3.2** (vocabulario de 128.256): 9 tokens — `La` `lic` `it` `ación` `ci` `erra` `en` `sept` `iembre`.
- **Gemma 4** (262.144): 6 tokens — `La` `lic` `itación` `cierra` `en` `septiembre`.
- **Qwen3** (151.669): 9 tokens, con cortes parecidos a Llama pero **otros números**: "La" es 8921 en Llama, 4967 en Gemma y 8747 en Qwen.
Cada tokenizador corta distinto y asigna sus propios IDs. Todo se mide en tokens: el contexto, la velocidad (tokens/s) y el precio de las APIs.

### El origen (2c): ¿Qué es un embedding?

Cada token se convierte en una lista de números que representa su significado: 1.024 números en `qwen3-embedding:0.6b`, 3.072 en Llama 3.2 3B [68]. Significados parecidos quedan cerca. *Diapositiva:* embeddings reales de 12 palabras (lugares, animales, compras públicas) con `qwen3-embedding:0.6b` en Ollama, proyectados a 2D con PCA [70]. Similitud coseno: Santiago–Lima 0,93; Santiago–perro 0,63. Así encuentra un RAG los fragmentos relevantes.

### El origen (2d): Capacidades de un modelo

Tres ejemplos ilustrativos con el caso de la licitación:
- **Uso de herramientas:** el modelo no busca; pide que tu sistema ejecute una función (p. ej. `buscar_licitacion("2239-2-LR26")`) y responde con el resultado.
- **Razonamiento:** escribe sus pasos antes de responder (más tokens, mejores respuestas).
- **Visión:** la imagen se corta en parches y cada parche se vuelve tokens (LLaVA-1.5: 576 tokens visuales por imagen).
No todos los modelos tienen las tres; LM Studio las muestra como íconos en el catálogo.

### El origen (2e): Ventana de contexto

Todo lo que el modelo considera a la vez, medido en tokens: instrucciones, conversación, documentos y respuesta. Lo que no cabe, el modelo no lo ve (por eso existe el RAG). Máximos: Llama 3.2 3B 131.072 tokens; Gemma 4 26B 262.144 [68]. Cada token de contexto ocupa memoria (caché KV): memoria total de Llama 3.2 3B con `num_ctx` 4.096 / 32.768 / 131.072 = 2,6 / 6,1 / 18 GB, columna SIZE de `ollama ps` [70]. *(Esta diapositiva reemplaza a la antigua de caché KV de la Parte 2.)*

### Bonus (al final del deck): ¿Cómo aprende?

Animación con la misma red y la misma frase:
1. Se toma texto real y se tapa la palabra que sigue.
2. Al principio los pesos son números al azar: el modelo adivina mal *(probabilidades ilustrativas)*.
3. Se compara con la respuesta correcta y el error viaja hacia atrás por toda la red.
4. Cada peso se ajusta un poquito para equivocarse menos la próxima vez.
5. Esto se repite con billones de tokens durante meses (Llama 3 se pre-entrenó con más de 15 billones de tokens [67]). Lo que queda al final son **los pesos**: el archivo que vamos a descargar.

### Respaldo (eliminada del deck): ¿Cómo nace un archivo Open Weights?

Cuando el entrenamiento termina, lo que queda es un archivo lleno de números: los **pesos**. No hay servidor ni cuenta: el modelo completo es ese archivo. "Open weights" significa que ese archivo está disponible para descargar.

¿Cómo se llega a ese archivo? En tres etapas:
1. **Pre-entrenamiento:** el modelo lee enormes cantidades de texto y aprende a predecir la palabra que sigue. Toma meses de cómputo. El resultado es un **modelo base**, que completa texto pero no conversa.
2. **Post-entrenamiento:** se ajusta con ejemplos de instrucciones y retroalimentación humana para que siga instrucciones y converse. Así se hizo, por ejemplo, ChatGPT a partir de GPT-3.5 [54]. El resultado es un modelo *instruct* o de chat.
3. **Publicación:** el laboratorio sube los pesos a Hugging Face, en precisión completa. Este es el archivo Open Weights original.

**De ese archivo nacen versiones derivadas:**
- **Cuantizadas:** comprimidas para que quepan en tu equipo (formato GGUF, niveles Q8, Q4). Son las que descargas en Ollama o LM Studio [33][39].
- **Destiladas:** un modelo chico que aprende imitando a uno grande. Por ejemplo, DeepSeek publicó versiones destiladas de R1 de 1,5B a 70B [18].
- **Afinadas (fine-tuning):** ajustadas para una tarea o un estilo específico. Es el tema del Taller 2.

### Tres tipos de modelo

Va **después** de la historia, como resumen, con una flecha de "menos control" a "más control":

| Categoría | Qué recibes | Ejemplos |
|---|---|---|
| **API cerrada** | Nada descargable. Tus datos viajan al servidor del proveedor. | GPT, Claude, Gemini |
| **Open weights** | El archivo de pesos, para correrlo en tu equipo. | Llama, Mistral, DeepSeek, Qwen, gpt-oss |
| **Open source** | Pesos, código y datos de entrenamiento. | OLMo (Allen Institute for AI) [23] |

OLMo es de los pocos proyectos que publican las tres cosas a la vez (incluido el dataset Dolma): es la vara más alta de apertura [23].

### Interludio: breve historia del Imperio

Sección propia, con su divisor, entre la teoría y la práctica. Si el speaker va atrasado, la tecla **S** salta directo a la Parte 2.

#### Breve historia en tres actos

Una sola diapositiva con una línea de tiempo de tres hitos; la nave avanza y el título y el color de fondo cambian con cada era: "El lado claro de la Fuerza" → "El lado oscuro" → "La rebelión Open Weights". Cada hito muestra el logo de la empresa (Google y OpenAI, OpenAI, Meta) y su fecha: oct. 2018–nov. 2019, may. 2020–nov. 2022 y mar. 2023. En la rebelión, los modelos que siguieron aparecen con sus logos (Mistral, DeepSeek, Qwen, Llama, GLM, Gemma, gpt-oss, Kimi). Logos: ver `slides/assets/logos/FUENTES.md`.

1. **El lado claro — oct. 2018 a nov. 2019, BERT (Google) y GPT-2 (OpenAI).** Ambos laboratorios publicaban sus modelos completos, con pesos y código [2][3][4]. *(El chiste de "cuando OpenAI era Open" lo cuenta el speaker de palabra; no va escrito en la diapositiva.)*
2. **El lado oscuro — 2020–2022, GPT-3 y ChatGPT.** GPT-3 fue el primer modelo insignia de OpenAI sin pesos públicos, solo por API [53]. ChatGPT (GPT-3.5 ajustado para conversar [54]) llegó a 1 millón de usuarios en 5 días [69] y a 100 millones en dos meses, contra ~9 meses de TikTok y ~30 de Instagram [5]: nace el Imperio. *Diapositiva:* cifra "1 millón en 5 días" y gráfico de barras de meses hasta 100 millones.
3. **La rebelión — 2023, LLaMA se filtra (Meta).** Meta lo compartió solo con investigadores [12]; en una semana los pesos estaban en internet [13][14]. Desde ahí, una galaxia de modelos abiertos: Llama, Mistral, DeepSeek, Qwen, Gemma, gpt-oss, GLM, Kimi.

#### Material de respaldo (no va en las diapositivas; útil para preguntas)

- **2017 — Transformer (Google):** la arquitectura base de casi todos los LLM, publicada abierta desde el primer día [1].
- **2018 — BERT (Google):** modelo entrenado con pesos y código [2]. **⚠️ Corrección:** no fue el primero; ELMo y ULMFiT lo hicieron meses antes [49][50]. Fue el más completo e influyente.
- **2018 — GPT-1 (OpenAI):** primer modelo de OpenAI, con código y pesos, licencia MIT [51][52].
- **2019 — GPT-2:** por temor al mal uso se liberó por partes durante 9 meses (124M, 355M, 774M y 1.500M) y en noviembre de 2019 se publicó completo [3][4].
- **2023 — GPT-4:** su reporte técnico no revela arquitectura, tamaño ni datos de entrenamiento [6].
- **Regulación:** en Chile, la Ley 21.719 de protección de datos personales rige plenamente desde el 1 de diciembre de 2026 [8]. *(Salió de la diapositiva al simplificar la historia; se puede decir de palabra.)*
- **Jul. 2023 — Llama 2**, con licencia comercial [15]. **Sep. 2023 — Mistral 7B**, Apache 2.0 [16][17]. **Ene. 2025 — DeepSeek R1**, 671B, MIT [18]. **Ago. 2025 — gpt-oss**, OpenAI vuelve a publicar pesos [19][20]. **Abr. 2026 — Qwen3.6-27B**, cabe en una GPU de 24 GB y supera a Qwen3.5-397B-A17B en SWE-bench Verified (77,2 contra 76,2) [21][22].

---

## Parte 2 — Práctica Jedi: usar modelos Open Weights localmente (60 min)

**Principio:** se muestran en vivo los mismos conceptos de la Parte 1, de lo más visual a lo más técnico. El speaker comparte la pantalla entera del PC Ubuntu (no se explica la instalación). Cada diapositiva resume un concepto y sirve de guía; las de LM Studio usan capturas reales con llamadas numeradas que aparecen en el orden de la demo. Las notas del presentador (tecla P) tienen los pasos exactos.

**Hilo conductor — el caso de uso:** las bases de licitación del **nuevo Convenio Marco de Servicios de Desarrollo y Mantención de Software, Servicios Profesionales TI y Cloud Computing** de ChileCompra (ID 2239-2-LR26) [55]. 3 categorías y 18 tipos de servicios [55]; convenio anterior ID 2239-19-LR23 [55]; plazo para ofertar extendido al 25 de septiembre de 2026 [56]; "~100 páginas" es dato del speaker, por confirmar.

**Antes de empezar:** VRAM libre (`ollama ps` vacío; ningún modelo cargado en LM Studio), modelos precalentados, LM Studio abierto en Library.

### Bloque A — LM Studio: los conceptos en la interfaz (~22 min)

| # | Diapositiva | Qué se hace en vivo | Concepto de la Parte 1 |
|---|---|---|---|
| A1 | LM Studio: la biblioteca (captura) | Library → LLMs: columna Params (26B-A4B, 30B-A3B), íconos de capacidades, Size, panel Info (Quantization Q4_K_M, Format GGUF) | parámetros, capacidades, cuantización |
| A2 | El nombre lo dice todo | Model Search: buscar una familia y ver variantes | instruct (post-entrenamiento), MoE, QAT, destilado (DeepSeek-R1-0528 → Qwen3-8B), formato GGUF |
| A3 | Cuantizar: comprimir los pesos | Columna Size | Llama 3.1 8B: ~16 GB en FP16 (estimado) → 4,9 GB en Q4_K_M (archivo real) |
| A4 | Denso contra MoE | Comparar 26B-A4B con un denso | Gemma 4 26B: 25,8B parámetros, 128 expertos [68]; solo CPU: 19 tok/s vs 27 tok/s de Llama 3.2 3B (medido) |
| A5 | ¿No cabe? Una parte va a la CPU | Pestaña Load: Context Length y GPU Offload | ventana de contexto; los 30 bloques de Gemma 4 26B: 125 / 41 / 19 tok/s con todo en GPU / mitad / solo CPU (medido) |
| A6 | LM Studio: el chat (captura) | "La capital de Chile es" → Santiago; estadísticas (tok/s); Think; System Prompt | token a token, razonamiento |

*(A7–A9 —caso de uso, PDF e imágenes— pasaron al bonus; ver abajo.)*

### Bloque B — Ollama: lo mismo, en la terminal (~9 min)

No se vuelven a explicar los conceptos: solo la equivalencia con LM Studio, con el mismo modelo (`gemma4:26b`) y la misma pregunta. Antes: expulsar el modelo de LM Studio.
- `ollama list` = Library · `ollama show gemma4:26b` = panel Info (25.8B, Q4_K_M, contexto 262.144, capacidades vision/tools/thinking) · `ollama run --verbose` = chat + estadísticas (eval rate) · `ollama ps` = pestaña Load (SIZE, PROCESSOR, CONTEXT) [60b][61].
- **Por debajo de todo, un API:** `curl` a `/api/chat`; la respuesta trae el texto y los contadores (`prompt_eval_count` 18, `eval_count` 17, `eval_duration` en ns; medición real del 20 oct. 2026). Ollama en `localhost:11434` y LM Studio en `localhost:1234`, ambos compatibles con el API de OpenAI. *(Pendiente técnico: el servicio de Ollama del PC escucha hoy en el puerto 1234; volver a 11434.)*

### Bloque C — ¿Qué modelo elijo? (~10 min)

Rankings (votación humana, exámenes, tareas reales) [35]–[38], panorama de hoy (Artificial Analysis, 7 sep. 2026) [24]–[26], memoria y hardware (costos por completar), los cinco filtros y "Misma pregunta, tres modelos" (Llama 3.1 8B, Gemma 4 26B-A4B, Qwen3.8 27B; resultados pendientes del benchmark propio).

### Cierre (~3 min)

Qué llevarse (tokens, contexto y memoria deciden qué puedes correr; los cinco filtros), QR al repo y Taller 2 (fine-tuning).

### Gancho para el Taller 2 (antes de "Gracias")

- **¿Cuáles son los límites del modelo? ¿Se puede mejorar?** Solo sabe lo que vio al entrenarse. Sí: dándole más datos, por dos caminos para casos distintos.
- **RAG:** le muestras tus documentos al preguntar (fragmentos → embeddings → búsqueda → contexto). Sirve para información propia o que cambia; no cambia el modelo.
- **Fine-tuning:** ajustas los pesos con tus ejemplos (modelo base + pares pregunta/respuesta → entrenamiento → nuevo GGUF). Sirve para cambiar formato, tono o una tarea específica; no para datos que cambian. Se pueden combinar.

*(El caso de uso del Convenio Marco, el PDF, las imágenes, el notebook de RAG y "¿Cómo aprende?" salieron del deck el 20 oct. 2026; su contenido queda en este documento como respaldo.)*

---

## Recursos del repo de GitHub

Pensados para personas que no programan: instalación de un solo comando por sistema operativo y guía paso a paso.

- **Guías:** instalación de Ollama y LM Studio, comandos usados en la demo, solución de problemas.
- **Medidor de contexto:** script que muestra el llenado de la ventana de contexto y estima la caché KV.
- **Notebooks de JupyterLab** (ejecutados, con gráficos guardados):
  1. Primera conexión y primera petición al modelo.
  2. Benchmark de hardware: modelos fijos en GPU completa, parcial y solo CPU, con contexto corto y largo. Mide velocidad de prompt, velocidad de generación, tiempo hasta el primer token y VRAM. Genera CSV y gráficos.
  3. Benchmark de modelos: 20 a 30 tareas sobre las bases (extracción de datos, clasificación de servicios, resumen, respuesta en JSON y preguntas trampa cuya respuesta no está en el texto, para medir alucinación). Cada tarea incluye el fragmento relevante en el prompt para medir al modelo y no a la búsqueda. Corrección automática, sin usar otro LLM como juez.
  4. RAG sobre tu propia carpeta, con LangChain.

---

## Pendientes

- Logos oficiales (Google, OpenAI, Meta, Mistral AI, DeepSeek, Alibaba Qwen) y logo de Afentu.
- URL real del repo, para regenerar el QR.
- Costos de la tabla de hardware.
- Confirmar las ~100 páginas del PDF de las bases.
- Definir el modelo multimodal para el Camino 2.
- Confirmar los modelos de la demo (Llama 3.2 3B, Qwen3.6 27B o Gemma 4, y el modelo para la comparación GPU contra CPU).
- PDF de las bases (y anexos), para construir el dataset del benchmark de modelos.
- Diapositivas nuevas de la Parte 2: puentes de cada bloque, denso contra MoE, JSON anotado del API y resultados de los dos benchmarks.

---

## Fuentes

**Historia y contexto**
1. Vaswani et al., "Attention Is All You Need", arXiv:1706.03762 (2017). https://arxiv.org/abs/1706.03762
2. BERT (Google AI, 2018) — referencia general. https://en.wikipedia.org/wiki/BERT_(language_model)
3. TheNextWeb, "Remember that scary AI text-generator..." (5 nov. 2019). https://thenextweb.com/artificial-intelligence/2019/11/05/remember-that-scary-ai-text-generator-that-was-too-dangerous-to-release-its-out-now/
4. Gigazine, cronología del release por etapas de GPT-2. https://gigazine.net/gsc_news/en/20191106-gpt-2-final-model-release
5. Reuters, "ChatGPT sets record for fastest-growing user base" (1 feb. 2023). https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/
6. OpenAI, "GPT-4 Technical Report", arXiv:2303.08774. https://arxiv.org/pdf/2303.08774.pdf
8. Biblioteca del Congreso Nacional, Ley 21.719 (texto oficial). https://www.bcn.cl/leychile/navegar?idNorma=1209272

**La rebelión open weights**
12. Wikipedia, "LLaMA (language model)". https://en.wikipedia.org/wiki/LLaMA
13. The Verge vía Computing.co.uk, filtración de LLaMA. https://www.computing.co.uk/news/4077275/metas-language-model-llama-leaks-online
14. Wikipedia, cronología detallada de la filtración. https://en.wikipedia.org/wiki/LLaMA
15. Meta AI, "Meta and Microsoft Introduce the Next Generation of Llama" (18 jul. 2023). https://ai.meta.com/blog/llama-2/
16. Simon Willison, anuncios Mistral 7B / Mixtral 8x7B. https://simonwillison.net/2023/Dec/18/mistral
17. Systems Analysis Wiki, ficha técnica Mixtral 8x7B. https://systems-analysis.ru/eng/Mixtral_(Mistral_AI)
18. DeepSeek, "DeepSeek-R1 Release" (20 ene. 2025). https://www.deepseek.com/en/news/deepseek-r1/
19. OpenAI, "Introducing gpt-oss" (5 ago. 2025). https://openai.com/index/introducing-gpt-oss/
20. YourStory, detalles técnicos gpt-oss-120b/20b. https://yourstory.com/ai-story/openai-gpt-oss-120b-20b-models-release
21. Qwen (Alibaba), model card Qwen3.6-27B (abr. 2026). https://qwen.ai/blog?id=qwen3.6-27b
22. Implicator.ai, cobertura técnica Qwen3.6-27B. https://www.implicator.ai/alibaba-ships-qwen3-6-27b-an-open-weight-coding-model-that-beats-its-397b-moe/
23. Wikipedia, "Allen Institute for AI" — OLMo / Dolma. https://en.wikipedia.org/wiki/Allen_Institute_for_AI

**Benchmarks**
24. 24/7 Wall St., citando @artificialanlys (7 sep. 2026). https://247wallst.com/cards/xpost-01m1yj852p230gg5tksfn4q7bh
25. Interconnects.ai, "The current balance of power in open models" (14 sep. 2026). https://www.interconnects.ai/p/the-current-balance-of-power-in-open
26. Artificial Analysis, leaderboard en vivo. https://artificialanalysis.ai/leaderboards/models
27. Meta, Llama 4 Community License — umbral de 700M MAU. https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Original
28. ioplus.nl, exclusión de la UE en Llama 4 multimodal. https://ioplus.nl/en/posts/european-union-excluded-from-llama-4-multimodal-models
35. Chiang et al., "Chatbot Arena", arXiv:2403.04132. https://arxiv.org/abs/2403.04132
36. Singh et al., "The Leaderboard Illusion", arXiv:2504.20879.
37. Hugging Face, doc. oficial "Open LLM Leaderboard v1" (archivado jun. 2024). https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive
38. DeepLearning.AI, "Hugging Face overhauls open LLM leaderboard". https://www.deeplearning.ai/the-batch/hugging-face-overhauls-open-llm-leaderboard-with-tougher-benchmarks

**Herramientas y conceptos técnicos**
29. Ollama, "Ollama's new engine for multimodal models" (15 may. 2025). https://registry.ollama.ai/blog/multimodal-models
30. Cybernews, cobertura del nuevo motor de Ollama. https://cybernews.com/news/ollama-adds-multimodal-llm-support/
31. LM Studio, "Introducing LM Studio 0.4.0" (28 ene. 2026). https://lmstudio.ai/blog/0.4.0
32. LM Studio, release notes oficiales v0.4.0. https://lmstudio.ai/changelog/lmstudio-v0.4.0
33. Wikipedia, "GGUF". https://en.wikipedia.org/wiki/GGUF
34. Wikipedia, "Llama.cpp". https://en.wikipedia.org/wiki/Llama.cpp
39. DataCamp, "GGUF Format: A Complete Guide". https://www.datacamp.com/tutorial/gguf-format-a-complete-guide
40. Kaitchup (Substack), cuantización GGUF. https://kaitchup.substack.com/p/gguf-quantization-for-fast-and-memory
41. "KVCompose", arXiv:2509.05165 — fórmula de la caché KV.
42. Ainslie et al., "GQA", EMNLP 2023 / arXiv:2305.13245. https://arxiv.org/abs/2305.13245
43. ZeroEntropy, explicación visual de GQA. https://www.zeroentropy.dev/concepts/grouped-query-attention/
44. TechSpot, ficha oficial NVIDIA RTX 3090. https://www.techspot.com/specs/gpu/224809-nvidia-geforce-rtx-3090.html

**RAG**
48. Lewis et al., "Retrieval-Augmented Generation...", NeurIPS 2020 / arXiv:2005.11401. https://arxiv.org/abs/2005.11401

**Historia temprana (revisión del 24 de septiembre)**
49. Peters et al. (AllenAI), "Deep contextualized word representations" (ELMo), arXiv:1802.05365 (feb. 2018). https://arxiv.org/abs/1802.05365
50. Howard & Ruder (fast.ai), "Universal Language Model Fine-tuning" (ULMFiT), arXiv:1801.06146 y anuncio oficial (15 may. 2018). https://nlp.fast.ai/classification/2018/05/15/introducing-ulmfit.html
51. OpenAI, "Improving language understanding with unsupervised learning" (11 jun. 2018) — anuncio de GPT-1. https://openai.com/index/language-unsupervised/
52. OpenAI, repositorio oficial de GPT-1 — código y pesos, licencia MIT. https://github.com/openai/finetune-transformer-lm
53. TechCrunch, "OpenAI makes an all-purpose API for its text-based AI capabilities" (11 jun. 2020). https://techcrunch.com/2020/06/11/openai-makes-an-all-purpose-api-for-its-text-based-ai-capabilities/
54. OpenAI, "Introducing ChatGPT" (30 nov. 2022) — ChatGPT es un ajuste fino de un modelo de la serie GPT-3.5. https://openai.com/index/chatgpt/

**Caso de uso y Parte 2 (revisión del 5 de octubre de 2026)**
55. Dirección ChileCompra, "Oferta en la licitación para el nuevo Convenio Marco de Servicios de Desarrollo y Mantención de Software" (15 jul. 2026). https://www.chilecompra.cl/2026/07/oferta-en-la-licitacion-para-el-nuevo-convenio-marco-de-servicios-de-desarrollo-y-mantencion-de-software/
56. Dirección ChileCompra, "Nuevo plazo para ofertar en la licitación..." (31 ago. 2026). https://www.chilecompra.cl/2026/08/nuevo-plazo-para-ofertar-en-la-licitacion-para-el-nuevo-convenio-marco-de-servicios-de-desarrollo-y-mantencion-de-software/
57. LM Studio, documentación "Chat with Documents". https://lmstudio.ai/docs/basics/rag
58. Dosovitskiy et al. (Google), "An Image is Worth 16x16 Words" (Vision Transformer), arXiv:2010.11929. https://arxiv.org/abs/2010.11929
59. Detalle de LLaVA-1.5 (336×336 px, 24×24 parches, 576 tokens visuales), en arXiv:2603.26731, apéndice A. https://arxiv.org/pdf/2603.26731 — paper original: Liu et al., "Improved Baselines with Visual Instruction Tuning", arXiv:2310.03744. https://arxiv.org/abs/2310.03744
60. Arquitectura de modelos visión-lenguaje (encoder de visión, proyector, LLM), arXiv:2601.16615. https://arxiv.org/pdf/2601.16615
60b. Ollama, FAQ oficial (`ollama ps`, columna PROCESSOR, `num_ctx`). https://docs.ollama.com/faq.md
61. MLJourney, "How to Benchmark Ollama: Tokens Per Second, GPU Usage and Flash Attention" (`--verbose`, columna SIZE con caché KV). https://mljourney.com/?p=6435
62. DEV Community, "Ollama Not Using GPU?" (`num_gpu` limita las capas en GPU). https://dev.to/mrsaynothing/ollama-not-using-gpu-fix-it-on-linux-windows-and-wsl-3jb8
63. LangChain, documentación de `OllamaEmbeddings` e `InMemoryVectorStore`. https://docs.langchain.com/oss/python/integrations/text_embedding/ollama
64. LangChain, ejemplo de RAG con `create_agent` y herramientas. https://docs.langchain.com/oss/python/langchain/multi-agent/custom-workflow
65. Qwen, tokenizador de Qwen3-8B (`tokenizer.json`, vocabulario de 151.669 tokens); tokenización de la frase de ejemplo calculada con la librería `tokenizers` el 18 oct. 2026. https://huggingface.co/Qwen/Qwen3-8B/blob/main/tokenizer.json
66. Medición propia: Ollama 0.31.2, modelo `llama3.2:3b`, `/api/generate` con `raw: true`, `logprobs: true`, `top_logprobs: 6`, prompt "La capital de Chile es", 18 oct. 2026, RTX 3090. Documentación del parámetro: https://docs.ollama.com/api/generate
67. Meta, "Introducing Meta Llama 3" (abr. 2024): "Llama 3 is pretrained on over 15T tokens". https://ai.meta.com/blog/meta-llama-3/
68. Número de bloques: `ollama show --verbose` (`llama.block_count` 28 para llama3.2:3b, `gemma4.block_count` 30 para gemma4:26b), 18 oct. 2026; Qwen3-8B, `num_hidden_layers` 36 en https://huggingface.co/Qwen/Qwen3-8B/blob/main/config.json
69. Sam Altman (@sama), publicación del 5 dic. 2022: "ChatGPT launched on wednesday. today it crossed 1 million users!" (lanzamiento el 30 nov. 2022). Reproducida en https://techstartups.com/2022/12/05/chatgpt-crosses-1-million-users-five-days-launch/
70. Mediciones propias, 19 oct. 2026, Ollama 0.31.2, RTX 3090: embeddings de `qwen3-embedding:0.6b` (`/api/embed`) proyectados con PCA; memoria por contexto con `ollama ps` tras cargar `llama3.2:3b` con distintos `num_ctx`.
71. Tokenizadores oficiales (`tokenizer.json`) de Llama 3.2 3B Instruct (https://huggingface.co/unsloth/Llama-3.2-3B-Instruct) y Gemma 4 26B A4B (https://huggingface.co/google/gemma-4-26b-a4b-it), procesados con la librería `tokenizers` el 19 oct. 2026.
