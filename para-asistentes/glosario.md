# Glosario del taller (en lenguaje simple)

Términos que vas a escuchar durante la charla, explicados sin jerga técnica.

**Peso (o "weight")**
Un modelo de IA es, en el fondo, un archivo con millones de números. Esos números son los "pesos": el resultado de todo el entrenamiento. Cuando descargas un modelo, lo que descargas son sus pesos.

**Open weights ("pesos abiertos")**
Modelos cuyo archivo de pesos puedes descargar y usar en tu propio computador, en vez de tener que usarlo únicamente a través de internet en la página de una empresa.

**API cerrada**
Lo opuesto a open weights: un servicio al que le mandas tu pregunta por internet (por ejemplo ChatGPT o Claude en su versión web) y te responde desde un servidor de la empresa. No puedes descargarlo ni ejecutarlo tú mismo.

**LLM (Large Language Model / Modelo de Lenguaje)**
El tipo de IA detrás de herramientas como ChatGPT, Claude o los modelos que se muestran en este taller — programas entrenados con enormes cantidades de texto para responder preguntas, escribir y razonar.

**Ejecutar localmente / IA local**
Usar un modelo de IA que corre físicamente en tu propio computador, sin que tus preguntas o documentos viajen a internet.

**GPU / VRAM**
La GPU es la tarjeta gráfica de tu computador (originalmente para videojuegos). VRAM es su memoria propia — mientras más VRAM tiene, más grandes son los modelos de IA que puede correr rápido. Sin GPU dedicada, los modelos también funcionan, pero más lento.

**Cuantización**
Una forma de "comprimir" un modelo para que ocupe menos espacio y memoria, a cambio de una pequeña pérdida de precisión — parecido a guardar una foto en menor calidad para que pese menos. Es lo que permite que modelos grandes quepan en computadores normales.

**Contexto / ventana de contexto**
Cuánto texto puede "recordar" el modelo de una sola vez en la conversación — incluye tu pregunta, el historial del chat, y cualquier documento que le hayas dado. Modelos con contexto más grande pueden analizar documentos más largos de una sola vez.

**RAG (Retrieval-Augmented Generation)**
La técnica que usa LM Studio cuando le adjuntas un documento: busca los fragmentos relevantes del documento y se los muestra al modelo junto con tu pregunta, para que responda basándose en ese contenido específico.

**Fine-tuning**
Entrenar más a un modelo ya existente con tus propios datos, para cambiar cómo se comporta (su tono, formato de respuesta, o el tipo de tareas que hace mejor) — distinto de RAG, que solo le da información nueva sin cambiar cómo actúa. Este es el tema del Taller 2.

**Licencia (Apache 2.0, MIT, etc.)**
Las reglas legales bajo las cuales puedes usar un modelo. Algunas permiten cualquier uso, incluido comercial (Apache 2.0, MIT); otras tienen restricciones específicas. Se explica con más detalle durante la charla.

**Benchmark**
Una prueba estandarizada que mide qué tan bien responde un modelo a cierto tipo de tareas, usada para comparar modelos entre sí.
