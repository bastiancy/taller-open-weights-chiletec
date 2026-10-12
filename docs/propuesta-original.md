## **Propuesta de Webinar / Taller 1: **
**Modelos “Open Weights”: privacidad de tus datos ejecutando LLMs localmente** 

**Organiza:** Mesa de Inteligencia Artificial & Ética de Chiletec 
**Duración:** 90 minutos
**Modalidad:** Online
**Speaker:** Bastian Carvajal, Master en Tecnologias de la Informacion, y fundador de [Afentu](https://afentu.com/)

**Público Objetivo:** Profesionales técnicos, líderes de proyectos y empresas que buscan adoptar IA sin comprometer la confidencialidad de sus datos (No se requieren conocimientos de programación).

**Objetivo del Taller:** Desmitificar el uso de la Inteligencia Artificial local. El asistente comprenderá la importancia de la soberanía de los datos y aprenderá, mediante una demostración práctica guiada, a ejecutar un modelo de lenguaje en su propio equipo para analizar documentos corporativos de forma 100% privada usando herramientas de interfaz gráfica (No-Code).

**Estructura y Temario (90 minutos):**

**Parte 1: El Contexto y la Historia del Ecosistema (30 minutos)**

- **La Promesa Original (2018-2019):** Breve contexto de los inicios de la IA generativa moderna.

- **El Cierre y el Efecto ChatGPT (2022):** Cómo la industria migró hacia modelos privativos de caja negra (APIs) y los riesgos de seguridad y privacidad que esto implica para el sector corporativo.

- **La Rebelión ****"****Open Weights****"**** (2023-2026):** El contraataque de la comunidad y empresas (Meta, Mistral, DeepSeek) al liberar los "pesos" pre-entrenados de los modelos, devolviendo el control a los usuarios.

**Parte 2: Demostración Práctica - Usando Ollama y LM Studio (60 minutos)**

- **Servir modelos con Ollama y LM Studio:** Levantaremos el modelo seleccionado desde la consola usando Ollama, demostrando su agilidad como motor de fondo y servidor local. Luego, utilizaremos la interfaz gráfica de LM Studio para interactuar con la IA de manera visual y amigable.

- **Benchmarks y Selección de Modelos:** ¿Cómo elegir el modelo correcto entre miles de opciones? Revisión rápida de los estándares de evaluación de la industria (como *LMSYS Chatbot Arena* o *Hugging Face Leaderboard*) para entender cómo comparar modelos *Open Weights* frente a alternativas cerradas según el caso de uso corporativo.

- **Eligiendo el Hardware:** Uso de una GPU de alto rendimiento (NVIDIA RTX 3090 de 24GB VRAM) para visualizar el consumo de recursos en tiempo real. Explicaremos cómo dimensionar el equipo necesario (cálculo de VRAM requerida según el tamaño del modelo y su nivel de cuantización) y mencionaremos las diferencias frente a arquitecturas como la memoria unificada de Apple (Mac M1/M2/M3).

- **Cierre y el Ecosistema (DashAI y Taller 2):** Mención a cómo estos modelos pueden conectarse con herramientas visuales de la comunidad (como DashAI) para entrenamientos No-Code. Finalmente, dejaremos planteado el "gancho" para el Taller 2: mostraremos las limitaciones de formato que aún tiene el modelo (incluso usando RAG), justificando la necesidad del *Fine-Tuning* para modificar definitivamente su comportamiento.