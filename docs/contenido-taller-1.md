# Contenido del Taller 1 — Modelos "Open Weights"
### Documento de trabajo — para revisar y corregir antes de pasar a diapositivas

> **Cómo usar este documento:** cada afirmación factual lleva una cita `[n]` que remite a la sección **Fuentes** al final. Las fuentes 1 a 54 se verificaron el 23 y 24 de septiembre de 2026; las fuentes 55 en adelante, el 5 de octubre de 2026. Donde algo estaba impreciso, se marca con **⚠️ Corrección**. Los benchmarks cambian semana a semana: donde aplica, se indica la fecha exacta del dato. La numeración tiene saltos a propósito (fuentes que quedaron sin uso al recortar contenido).

**Notas de estructura y diseño (acordadas):**
- Dos partes: Parte 1, *Breve historia de la galaxia* (30 min), y Parte 2, *Práctica Jedi: usar modelos Open Weights localmente* (60 min).
- Las diapositivas se hacen en **HTML** (fondo espacial, nave que recorre las líneas de tiempo). Exportar a PowerPoint se evalúa después.
- Menos texto y más diagramas. En la Parte 1, cada sección es una diapositiva.
- Humor de Star Wars con moderación: un par de guiños por sección.
- Ley 21.719: solo una mención de una línea. DashAI, el caso Samsung y el gancho del "JSON mal formateado" quedaron fuera.
- En la Parte 2 **manda el software en vivo**; las diapositivas son puentes cortos y diagramas que se muestran justo después de cada demo (y sirven de respaldo si algo falla).
- Todo lo que se muestre en vivo queda en el **repo de GitHub** (scripts, notebooks, guías) para que los asistentes lo repitan en su equipo.

---

## Resumen de temas

**Parte 1 — Breve historia de la galaxia (30 min)**
- El origen: ¿qué es un LLM?
- El origen: ¿cómo nace un archivo Open Weights? (pre-entrenamiento, post-entrenamiento, publicación; versiones cuantizadas, destiladas y afinadas)
- El lado claro de la Fuerza: Transformer, BERT, GPT-1, GPT-2
- El lado oscuro: GPT-3, ChatGPT, GPT-4 (y una línea sobre regulación)
- La alianza rebelde: la filtración de LLaMA, Mistral 7B, DeepSeek R1, gpt-oss, Qwen3.6
- Resumen: API cerrada, open weights y open source

**Parte 2 — Práctica Jedi (60 min)**
- Bloque A, LM Studio (~22 min): el catálogo y sus variantes (cuantización, instruct, denso contra MoE), qué cabe en la GPU, cómo elegir modelo (rankings y cinco filtros), el PDF de las bases con RAG simple y la lectura de imágenes con un modelo multimodal
- Bloque B, Ollama (~18 min): el API por debajo del chat, de dónde salen los tokens por segundo, ventana de contexto y caché KV, offload GPU contra CPU con el mismo modelo, hardware, costos y benchmark de hardware
- Bloque C, RAG sobre una carpeta (~15 min): notebooks con LangChain que indexan la carpeta de la licitación, inyección en el contexto contra agente con herramientas
- Cierre (~5 min): qué llevarse, repo y Taller 2

**Hilo conductor de la Parte 2:** las bases del nuevo Convenio Marco de software de ChileCompra (ID 2239-2-LR26).

---

## Parte 1 — Breve historia de la galaxia (30 min)

### El origen (1): ¿Qué es un LLM?

Un LLM (*Large Language Model*, o modelo de lenguaje de gran escala) es, en el fondo, un algoritmo entrenado con un objetivo bien simple: **adivinar la palabra que sigue**, dado un pedazo de texto. No hay razonamiento programado a mano: se le entrena una y otra vez, con enormes cantidades de texto, a completar frases.

Lo interesante es que, con suficientes datos y parámetros, empieza a mostrar capacidades que nadie le programó: traducir, resumir, responder preguntas, escribir código. Aparecen como efecto secundario de ser muy bueno prediciendo la siguiente palabra.

**¿Qué tan "grande"?** El tamaño se mide en parámetros, y "B" significa miles de millones:
- **3B**: corre en un notebook.
- **27B**: cabe en una GPU de 24 GB (por ejemplo, Qwen3.6-27B [21]).
- **671B**: requiere un centro de datos (por ejemplo, DeepSeek R1 [18]).

Por dentro, casi todos los LLM usan la arquitectura **Transformer**, publicada por Google en 2017 [1]. El detalle técnico queda para otro taller.

*Diapositiva:* diagrama de "El gato se subió al ___" con las probabilidades de la siguiente palabra, y una escala visual 3B / 27B / 671B.

### El origen (2): ¿Cómo nace un archivo Open Weights?

Cuando el entrenamiento termina, lo que queda es un archivo lleno de números: los **pesos**, los parámetros que el modelo ajustó y que codifican todo lo que aprendió. No hay servidor ni cuenta: el modelo completo es ese archivo. "Open weights" significa que ese archivo está disponible para descargar.

¿Cómo se llega a ese archivo? En tres etapas:
1. **Pre-entrenamiento:** el modelo lee enormes cantidades de texto y aprende a predecir la palabra que sigue. Toma meses de cómputo. El resultado es un **modelo base**, que completa texto pero no conversa.
2. **Post-entrenamiento:** se ajusta con ejemplos de instrucciones y retroalimentación humana para que siga instrucciones y converse. Así se hizo, por ejemplo, ChatGPT a partir de GPT-3.5 [54]. El resultado es un modelo *instruct* o de chat.
3. **Publicación:** el laboratorio sube los pesos a Hugging Face, en precisión completa. Este es el archivo Open Weights original.

**De ese archivo nacen versiones derivadas:**
- **Cuantizadas:** comprimidas para que quepan en tu equipo (formato GGUF, niveles Q8, Q4). Son las que descargas en Ollama o LM Studio [33][39].
- **Destiladas:** un modelo chico que aprende imitando a uno grande. Por ejemplo, DeepSeek publicó versiones destiladas de R1 de 1,5B a 70B [18].
- **Afinadas (fine-tuning):** ajustadas para una tarea o un estilo específico. Es el tema del Taller 2.

### El lado claro de la Fuerza: cuando "Open" significaba algo (2017–2019)

La época en que los laboratorios compartían sus descubrimientos sin pensarlo dos veces. Cuatro hitos:

- **2017 — Transformer (Google):** la arquitectura base de casi todos los LLM, publicada abierta desde el primer día [1].
- **2018 — BERT (Google):** el modelo ya entrenado, con pesos y código, listo para descargar [2]. Se volvió la base de medio mundo del procesamiento de lenguaje.
  **⚠️ Corrección:** BERT no fue el primero en publicar código y pesos; ELMo (AllenAI) y ULMFiT (fast.ai) lo hicieron meses antes [49][50]. BERT fue el más completo e influyente.
- **2018 — GPT-1 (OpenAI):** en junio de 2018, OpenAI publicó su primer modelo con código y pesos, bajo licencia MIT [51][52]. No por nada se llamaba "Open"AI: todavía era un Jedi.
- **2019 — GPT-2 (OpenAI), la primera duda:** por temor al mal uso lo liberó por partes durante 9 meses (124M, 355M, 774M y 1.500M de parámetros) y en noviembre de 2019 lo publicó completo [3][4]. Siguió siendo abierto, pero fue la primera vez que dudaron en voz alta.

*Diapositiva:* línea de tiempo con la nave que avanza hito por hito; cada hito con el logo de la empresa (pendiente) y un diagrama breve.

### El lado oscuro: OpenAI se convierte en Imperio (2020–2023)

Tres hitos:

- **2020 — GPT-3:** por primera vez, el modelo insignia de OpenAI nunca tuvo pesos públicos; solo acceso pagado por API [53].
- **Noviembre de 2022 — ChatGPT:** es GPT-3.5 ajustado con retroalimentación humana para conversar [54]. **Aclaración:** ChatGPT no es GPT-2 ni GPT-3 a secas. Llegó a 100 millones de usuarios en dos meses, contra ~9 de TikTok y ~30 de Instagram (UBS vía Reuters) [5]. Gigante y cerrado a la vez: nace el Imperio.
- **2023 — GPT-4:** su reporte técnico no revela arquitectura, tamaño ni datos de entrenamiento, citando "el panorama competitivo" [6]. Contraste total con los papers de GPT-1, 2 y 3.

**Una línea sobre regulación:** con el Imperio llegó la regulación. En Chile, la Ley 21.719 de protección de datos personales rige plenamente desde el 1 de diciembre de 2026 [8]. Da para otra charla.

### La alianza rebelde de Open Weights (2023–2026)

*"El Imperio pensó que había apagado las luces para siempre. Se equivocó."* Cinco hitos:

- **Marzo de 2023 — LLaMA se filtra (Meta):** Meta lo lanzó solo para investigadores [12]; una semana después alguien publicó los pesos completos en internet y ya no hubo vuelta atrás [13][14]. Meta respondió en julio de 2023 con **Llama 2**, con licencia comercial [15].
- **Septiembre de 2023 — Mistral 7B (Mistral AI):** el laboratorio francés publica sus modelos con Apache 2.0, la licencia más permisiva [16][17].
- **Enero de 2025 — DeepSeek R1:** 671B parámetros, razonamiento comparable a OpenAI o1, licencia MIT [18]. Hoy la rebelión la lideran laboratorios chinos.
- **Agosto de 2025 — gpt-oss (OpenAI):** OpenAI vuelve a publicar pesos, seis años después de GPT-2 [19][20]. Hasta el Imperio cambia de bando.
- **Abril de 2026 — Qwen3.6-27B (Alibaba):** cabe en una sola GPU de 24 GB y supera en programación a su predecesor 15 veces más grande (SWE-bench Verified 77,2 contra 76,2) [21][22].

### En resumen: tres tipos de modelo

Diapositiva propia al cierre de la Parte 1, con una flecha de "menos control" a "más control":

| Categoría | Qué recibes | Ejemplos |
|---|---|---|
| **API cerrada** | Nada descargable. Tus datos viajan al servidor del proveedor. | GPT, Claude, Gemini |
| **Open weights** | El archivo de pesos, para correrlo en tu equipo. | Llama, Mistral, DeepSeek, Qwen, gpt-oss |
| **Open source** | Pesos, código y datos de entrenamiento. | OLMo (Allen Institute for AI) [23] |

OLMo es de los pocos proyectos que publican las tres cosas a la vez (incluido el dataset Dolma): es la vara más alta de apertura [23].

---

## Parte 2 — Práctica Jedi: usar modelos Open Weights localmente (60 min)

**Principio:** se muestra el software funcionando en vivo, de lo más simple a lo más complejo. Cada concepto se explica justo cuando aparece en pantalla. Las diapositivas son puentes entre bloques y diagramas de apoyo.

**Hilo conductor — el caso de uso:** las bases de licitación del **nuevo Convenio Marco de Servicios de Desarrollo y Mantención de Software, Servicios Profesionales TI y Cloud Computing** de ChileCompra (ID 2239-2-LR26) [55]. Datos clave:
- 3 categorías y 18 tipos de servicios, incluyendo desarrollo de software, IA, automatización, datos, ciberseguridad y cloud [55].
- El convenio vigente anterior es el ID 2239-19-LR23 [55].
- El plazo para ofertar se extendió al 25 de septiembre de 2026 por modificaciones a las bases [56].
- El PDF tiene cerca de 100 páginas (dato del speaker, por confirmar).

El documento aparece en cada bloque y el modelo recibe cada vez más información: un PDF en LM Studio, un fragmento por API en Ollama, la carpeta completa de la licitación en los notebooks, y además el dataset del benchmark de modelos.

**Preguntas de ejemplo para el documento:**
- ¿Qué categorías y servicios incluye?
- ¿Cuáles son los criterios de evaluación de las ofertas?
- ¿Qué garantías se exigen a los proveedores?

### Bloque A — LM Studio: qué es un modelo y cómo elegirlo (~22 min)

LM Studio es una aplicación de escritorio para explorar, descargar y conversar con modelos, con interfaz gráfica. Desde la versión 0.4.0 (enero de 2026) también corre sin interfaz, como servidor [31][32]. Se parte por aquí porque el catálogo permite explicar los conceptos de forma visual, a medida que se seleccionan en la aplicación.

**1. El catálogo (en vivo).** Al buscar un modelo se ven:
- **Proveedor y modelo:** quién lo entrenó y cuántos parámetros tiene.
- **Variantes de un mismo modelo:** distintas cuantizaciones; versiones *instruct* (conecta con el post-entrenamiento de la Parte 1); modelos **densos** contra **MoE**.
- **Si cabe o no:** el catálogo indica qué modelos caben completos en la GPU y cuáles necesitan offload parcial a CPU.

**Concepto: cuantización.** Entrenar produce pesos "pesados" (2 bytes por parámetro). Cuantizar los comprime: el formato más usado, **Q4_K_M**, deja un modelo en cerca de una cuarta parte de su tamaño, con una pérdida de calidad mínima [39][40]. Analogía: pasar una foto de RAW a JPEG.

**Concepto: denso contra MoE.** Un modelo denso usa todos sus parámetros para cada palabra. Un modelo MoE (*Mixture of Experts*) se divide en "expertos" y activa solo algunos por palabra: es más rápido de lo que su tamaño sugiere, pero igual necesita memoria para todo el modelo. Ejemplos: Mixtral 8x7B [17] o Qwen3.5-397B-A17B, que activa 17B de sus 397B [22].

**2. ¿Cómo elijo qué modelo descargar?** Ningún ranking te dice qué usar, solo a quién mirar:
- **Votación humana (LMArena):** la gente vota a ciegas la respuesta que prefiere [35]. Mide lo que gusta, no lo que es correcto; el estudio *"The Leaderboard Illusion"* documenta sesgos [36].
- **Exámenes automáticos:** la primera versión del ranking de Hugging Face se saturó y se retiró en junio de 2024 [37][38].
- **Tareas reales (SWE-bench y similares):** miden si el modelo resuelve el trabajo. Son las más útiles para una empresa.

**El panorama de hoy** (Artificial Analysis Intelligence Index, 7 de septiembre de 2026) [24]:

| Modelo | Puntaje | Tipo |
|---|---|---|
| GLM-5.3 (Z.ai) | 44 | Open weight |
| Kimi K3 (Moonshot AI) | 44 | Open weight |
| GLM-5.3-Flash | 42 | Open weight |
| Qwen3.8 | 40 | Open weight |
| DeepSeek V4 Pro | 36 | Open weight |
| Mejor cerrado (Claude Fable 5.1 / GPT-6 Astra) | 53 | Cerrado |

Solo 9 puntos separan al mejor abierto del mejor cerrado [24]. Una semana después los números ya habían cambiado [25][26]: importa el criterio, no el ranking.

**La licencia importa tanto como el benchmark.** Meta permite uso comercial libre de Llama 4 solo bajo 700 millones de usuarios activos al mes [27], y sus modelos multimodales excluyen a la Unión Europea [28].

**Cinco filtros para elegir:** ¿la licencia me sirve? → ¿cabe en mi equipo? → ¿rinde en español? → ¿rinde en mi tipo de tarea? → **pruébalo con 20 a 30 casos reales**. El quinto filtro se remata con los resultados del **benchmark de modelos propio** (ver Bloque C y Recursos del repo).

**3. Caso de uso, Camino 1: el PDF como texto (en vivo).** Se adjunta el PDF de las bases al chat de LM Studio y se le pregunta. Si el documento cabe en el contexto del modelo, LM Studio lo agrega completo a la conversación; si es muy largo, usa RAG para extraer solo las partes relevantes [57].
*Diapositiva después de la demo:* PDF → texto o Markdown → fragmentos → índice de vectores → búsqueda de los fragmentos más parecidos a la pregunta. Dos formas de que el modelo reciba esos fragmentos:
- **Inyección en el contexto:** se pegan en el mensaje junto a la pregunta (lo que hace LM Studio).
- **Uso de herramientas:** el modelo decide cuándo buscar y llama a una función de búsqueda, como un agente (se muestra en el Bloque C).

El concepto de RAG fue propuesto por Lewis et al. en 2020 [48].

**4. Caso de uso, Camino 2: modelos que leen imágenes (en vivo).** Tablas, firmas y páginas escaneadas se pierden al pasar a texto. Un modelo multimodal las lee directamente como imagen: se adjunta una página (por ejemplo, la tabla de criterios de evaluación) y se le pregunta.
*Diapositiva después de la demo — cómo se codifica la imagen:*
1. La imagen se corta en **parches** de tamaño fijo, como propuso el Vision Transformer [58].
2. Un **encoder de visión** convierte cada parche en un vector.
3. Un **proyector** lleva esos vectores al espacio del modelo de lenguaje: se vuelven **tokens de imagen** que el LLM lee junto a los tokens de texto [59][60].

Ejemplo concreto: LLaVA-1.5 lleva la imagen a 336×336 píxeles, la divide en 24×24 parches y genera **576 tokens visuales** por imagen [59].

**¿Cuándo usar cada camino?** Texto y RAG para documentos largos con texto digital. Imagen para tablas, gráficos y escaneos; cada imagen ocupa cientos de tokens del contexto.

**5. Misma pregunta, varios modelos (en vivo).** Se compara la **calidad** de la respuesta entre un modelo pequeño y uno mediano que caben en la GPU (por ejemplo, Llama 3.2 3B y Qwen3.6 27B o Gemma 4), anotando si la respuesta es correcta.

### Bloque B — Ollama: lo que hay debajo del chat (~18 min)

Ollama es el motor: corre como un servicio en tu equipo (`localhost:11434`) y expone un API compatible con el de OpenAI, así que migrar de la nube a local puede ser cambiar una URL. Desde mayo de 2025 usa un motor propio para dar soporte de primera clase a modelos multimodales [29][30]. Lee modelos en formato **GGUF**, que empaqueta pesos, configuración y vocabulario en un solo archivo; lo creó Georgi Gerganov en agosto de 2023 [33][34].

**1. El API por dentro (en vivo).** Un `curl` al API de Ollama muestra lo que realmente se envía y lo que el modelo responde: un JSON con el texto, cuántos tokens procesó, cuántos generó y cuánto se demoró cada etapa. **De ahí salen los tokens por segundo**, y un benchmark no es más que esa misma petición repetida en distintas condiciones.
*Diapositiva nueva:* el JSON de respuesta anotado.

**2. Ventana de contexto y caché KV (en vivo).** Terminal dividida en paneles: `ollama run modelo --verbose` a un lado, y `nvtop` (uso de VRAM y GPU en vivo) y `watch -n1 ollama ps` al otro.
- `--verbose` muestra después de cada respuesta la velocidad de generación, la velocidad de procesamiento del prompt y el tiempo de carga [61].
- El contexto se cambia en vivo con `/set parameter num_ctx 8192` [60b].
- En `ollama ps`, la columna SIZE incluye la caché KV [61]: se ve crecer al agrandar el contexto.
- **El error clásico:** ver que el archivo cabe en la GPU y asumir que el modelo cabe. Hay que sumar la memoria de la conversación (la caché KV), que crece con el largo del contexto [41]. *Grouped-Query Attention* ayuda a que no se dispare [42][43].
- Un script del repo (el **medidor de contexto**) dibuja una barra de tokens usados contra `num_ctx` y estima el tamaño de la caché KV. Se presenta como **estimación calculada**: Ollama no expone la ocupación de la caché KV directamente.
*Diapositiva después de la demo:* barras de VRAM de 24 GB con pesos + caché KV, en pregunta corta contra documento largo (esquema ilustrativo con Qwen3.6-27B Q4_K_M de 16,8 GB).

**3. GPU contra CPU con el mismo modelo (en vivo).** El parámetro `num_gpu` limita cuántas capas se cargan en la GPU [62]. Se corre **el mismo modelo con la misma tarea** en tres modos (todas las capas en GPU, la mitad, ninguna), así la única variable es el hardware. La columna PROCESSOR de `ollama ps` muestra "100% GPU", "100% CPU" o un reparto como "48%/52% CPU/GPU" [60b]. Se llena en vivo la tabla de tokens por segundo.

**4. Hardware y costos.** La RTX 3090 tiene 24 GB de VRAM, de sobra para modelos de 14B a 32B bien cuantizados [44].

| Equipo | Memoria para el modelo | Qué corre bien | Costo aprox. |
|---|---|---|---|
| Notebook sin GPU dedicada | RAM del sistema | Modelos pequeños, lento | por completar |
| GPU de 8 GB | 8 GB | 7 a 8B en Q4 | por completar |
| GPU de 12 GB | 12 GB | 12 a 14B en Q4 | por completar |
| **RTX 3090 (equipo del speaker)** | 24 GB | 14 a 32B en Q4 | por completar |
| RTX 5090 | 32 GB | 27B en Q6 u Q8 | por completar |
| Mac con memoria unificada | 64 GB compartidos | 70B o más, más lento | por completar |

GPU dedicada: más velocidad con un techo fijo de memoria. Mac: más techo, menos velocidad.

**5. Benchmark de hardware.** Se muestran los resultados del notebook ya ejecutado en la RTX 3090, como referencia para que cada asistente lo corra en su equipo y se compare.

### Bloque C — RAG sobre una carpeta completa (~15 min)

**Notebook ya ejecutado (en vivo se corren solo una o dos celdas).** El asistente define una carpeta, deja ahí sus archivos (PDF, Word, texto) y el resto lo hace **LangChain**, con el mínimo código visible.
- Embeddings locales con `OllamaEmbeddings` y vectores en `InMemoryVectorStore`, sin instalar una base de datos aparte [63].
- Los dos caminos sobre el mismo índice: **inyección en el contexto** (buscar y luego preguntar) y **agente con herramienta de búsqueda** (`create_agent` con una herramienta definida con `@tool`) [64].
- Funciona con Ollama o LM Studio cambiando un parámetro, porque ambos exponen un API compatible con OpenAI.
- Cada respuesta muestra de qué archivo y página salió.
- Para el caso de uso, la carpeta es la licitación completa: bases, anexos y respuestas del foro de preguntas.
- **Limitación a mencionar:** el RAG de texto no funciona con PDF escaneados; para eso están los modelos multimodales del Bloque A.

### Cierre (~5 min)

- Qué llevarse: los tres tipos de modelo, los cinco filtros, y que el hardware y el contexto deciden qué puedes correr.
- QR al repo con todo el material.
- **Taller 2:** RAG le da al modelo información nueva, pero no cambia cómo se comporta. Para cambiar el comportamiento (formato, tono, estructura) hay que ajustar los pesos: eso es fine-tuning.

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
