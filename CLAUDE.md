# CLAUDE.md — Taller 1 Chiletec: Modelos "Open Weights"

Contexto para Claude Code. Léelo completo antes de trabajar en este repo.

## Qué es este proyecto

Material del **Taller 1** de la Mesa de Inteligencia Artificial y Ética de **Chiletec**:
*"Modelos Open Weights: privacidad de tus datos ejecutando LLMs localmente"*.

- **Speaker:** Bastian Carvajal (Master en Tecnologías de la Información, fundador de Afentu SpA).
- **Formato:** 90 minutos, online. Público de empresas socias de Chiletec, **no necesariamente técnico** (no se requiere saber programar).
- **Demo en vivo** en el PC del speaker: **Ubuntu + NVIDIA RTX 3090 (24 GB VRAM)**.
- Habrá un **Taller 2** sobre fine-tuning.
- La propuesta original está en `docs/propuesta-original.md` (quedó desactualizada: DashAI y el gancho del JSON se eliminaron).

**Idioma:** todo el contenido, las diapositivas, los comentarios de código y las respuestas al usuario van en **español de Chile**.

## Estructura del repo

```
CLAUDE.md                  este archivo
README.md                  portada del repo para los asistentes al taller
docs/
  contenido-taller-1.md    DOCUMENTO MAESTRO de contenido, con fuentes citadas [n]
  propuesta-original.md    propuesta enviada a Chiletec (histórica)
slides/
  deck.src.html            FUENTE EDITABLE del deck (marcadores __QR__ y __SHIP__)
  assets/qr.b64            QR del repo en PNG base64 (apunta a una URL PROVISORIA)
  assets/ship.svg          nave original que recorre las líneas de tiempo
  build.py                 compila deck.src.html -> dist/index.html
  shoot.py                 capturas con Playwright para revisión visual
  dist/index.html          deck compilado (lo que se presenta)
demo/                      guías técnicas de la demo  (DESACTUALIZADAS, ver Pendientes)
para-asistentes/           guías no técnicas por sistema operativo + glosario (DESACTUALIZADAS)
notebooks/                 notebooks de JupyterLab (por construir)
benchmarks/                benchmark de hardware y de modelos (por construir)
scripts/                   utilidades, p. ej. medidor de contexto (por construir)
```

## Flujo de trabajo del deck

```bash
python3 slides/build.py                 # compila
python3 slides/shoot.py 4:1 8:5 21:2    # captura diapositiva:pasos en slides/shots/
xdg-open slides/dist/index.html         # o abrir en el navegador
```

- **Edita siempre `slides/deck.src.html`**, nunca `dist/index.html`.
- Después de cada cambio: build + capturas de las diapositivas tocadas + revisar las imágenes antes de dar el trabajo por terminado. Revisa que nada se salga de los márgenes (lienzo 1600×900, padding 64px/96px).
- Navegación del deck: flechas/espacio, tecla **F** pantalla completa, `#n` en la URL para saltar a una diapositiva, swipe en táctil.
- Las fuentes vienen de Google Fonts (Fraunces, IBM Plex Sans, IBM Plex Mono); si no hay red, cae a fuentes del sistema.

### Sistema de diseño (mantenerlo consistente)
- Fondo: campo de estrellas en `<canvas>` + nebulosa por "era" que cambia de color con `data-era` en cada `<section>`:
  `neutral` (azulado) · `claro` (dorado #E6B95E) · `oscuro` (rojo #E4493E) · `rebelde` (naranja #F28D3C) · `jedi` (verde-azulado #4AC6B3).
- Tipografía: Fraunces para títulos, IBM Plex Sans para cuerpo, IBM Plex Mono para código.
- Pasos dentro de una diapositiva: `data-steps="N"` en la sección; elementos con `class="frag" data-step="k"` (acumulativos) o `class="only" data-only="k"` (solo en ese paso).
- Líneas de tiempo (`.tl`): la nave viaja al hito del paso actual; los visitados se atenúan.
- Espacios de logo: `<span class="logo" data-logo="openai">OpenAI</span>` — marcadores con borde punteado.
- Estilo: **menos texto, más diagramas**. Nada de "muchas cajas" (fue la razón por la que se descartaron los PPTX). Frases cortas; frases completas sin rellenos.

### Lecciones técnicas
- En SVG, `feGaussianBlur` produce artefactos de recorte → usar `radialGradient`.
- Grillas con texto largo: usar `minmax(0,1fr)` para que no empujen fuera del margen.
- Exportar a PPTX se evaluará después; si se hace, ojo: en pptxgenjs un `\n` dentro de un run centrado rompe el centrado.

## Restricciones (no negociables)

- **No dibujar ni recrear logos de empresas** (OpenAI, Google, Meta, Mistral, DeepSeek, Alibaba/Qwen, etc.). Dejar los marcadores `.logo` y que el usuario aporte los archivos oficiales de los press kits; luego se insertan como `<img>`.
- **No usar arte, personajes, naves ni assets de Star Wars** (Lucasfilm/Disney). El hilo Star Wars es solo verbal y temático; todo el arte espacial es original.
- Datos con fuente: cada afirmación factual nueva en `docs/contenido-taller-1.md` lleva su cita `[n]` y la fuente en la lista. Verificar antes de afirmar; los benchmarks y versiones cambian semana a semana.

## Decisiones del usuario (respetarlas)

- Hilo conductor **Star Wars**, con moderación (un par de guiños por sección). Chiste central: OpenAI nació "Open" y se cerró → el lado oscuro.
- **Eliminados:** DashAI, el caso Samsung, la frase "open weights no es IA gratis…", el gancho del JSON mal formateado. **Ley 21.719**: solo una línea (el público sabe más de regulación que el speaker; evitar polémica).
- Parte 1 abre con **dos preguntas de origen**: "¿Qué es un LLM?" y "¿Cómo nace un archivo Open Weights?" (pre-entrenamiento → post-entrenamiento → publicación; derivadas cuantizadas / destiladas / afinadas).
- Líneas de tiempo reducidas a los hitos más importantes. La tabla "tres tipos de modelo" va como **diapositiva propia al final de la Parte 1**.
- En la Parte 2 **manda el software en vivo**, de lo más simple a lo más complejo. Las diapositivas son **puentes cortos** y diagramas que se muestran justo después de cada demo (y respaldo si la demo falla).
- Orden de la Parte 2: **LM Studio primero** (visual: catálogo, cuantización, instruct, denso vs MoE, qué cabe en GPU, cómo elegir modelo) → **Ollama** (técnico: `curl` al API, tokens/s, contexto y caché KV, offload GPU/CPU, hardware y benchmark) → **RAG sobre una carpeta con notebooks**.
- Caso de uso / hilo conductor: **bases del nuevo Convenio Marco de software de ChileCompra (ID 2239-2-LR26)**.
- RAG con **LangChain** y el mínimo código visible: el usuario define una carpeta, deja sus archivos, y el resto lo hace LangChain. Notebooks de JupyterLab, entregados **ya ejecutados**.
- Todo lo que se muestre en vivo debe quedar en el repo para que los asistentes lo repitan.

## Estado actual del deck (23 diapositivas en `deck.src.html`)

**Parte 1 — Breve historia de la galaxia (30 min):** 1 Portada · 2 Temario (QR) · 3 Divisor · 4 ¿Qué es un LLM? · 5 ¿Cómo nace un archivo Open Weights? · 6 Lado claro (Transformer, BERT, GPT-1, GPT-2) · 7 Lado oscuro (GPT-3, ChatGPT, GPT-4 + Ley 21.719) · 8 Alianza rebelde (LLaMA se filtra, Mistral 7B, DeepSeek R1, gpt-oss, Qwen3.6) · 9 Resumen: tres tipos de modelo.

**Parte 2 — Práctica Jedi (60 min):** 10 Divisor · 11 Ollama · 12 Tabla de hardware (costos "por completar") · 13 Cuantización · 14 Caché KV · 15 LM Studio: el catálogo · 16 Benchmarks · 17 Panorama de hoy · 18 Cinco filtros · 19 Caso de uso Convenio Marco · 20 Camino 1: PDF → texto/RAG · 21 Camino 2: multimodal · 22 Misma pregunta, tres modelos · 23 Cierre.

⚠️ **El orden de la Parte 2 en el deck todavía es el antiguo** (Ollama antes que LM Studio). El orden acordado está en `docs/contenido-taller-1.md` y abajo.

### Parte 2 acordada (reorganización pendiente en el deck)
- **Bloque A — LM Studio (~22 min):** puente → catálogo en vivo → diapositivas de cuantización y **denso vs MoE (nueva)** → rankings, panorama, cinco filtros (+ resultados del benchmark de modelos propio) → PDF de las bases en vivo → Camino 1 → página como imagen con modelo multimodal → Camino 2 → misma pregunta con varios modelos (calidad).
- **Bloque B — Ollama (~18 min):** puente → `curl` al API y **JSON anotado (nueva)** → contexto/caché KV con `nvtop` + `watch ollama ps` + medidor de contexto → mismo modelo en GPU completa / parcial (`num_gpu`) / CPU, llenando la tabla de tokens/s → hardware y costos → resultados del benchmark de hardware.
- **Bloque C — RAG sobre carpeta (~15 min):** puente → notebook LangChain ya ejecutado sobre la carpeta de la licitación (bases, anexos, foro): inyección en el contexto vs agente con herramienta, con fuentes por respuesta.
- **Cierre (~5 min):** qué llevarse, QR, Taller 2.

## Datos verificados clave (detalle y fuentes en docs/contenido-taller-1.md)

- **BERT no fue el primero** en publicar código + pesos: lm_1b (2016), CoVe (2017), ULMFiT (ene/may 2018), ELMo (feb 2018), GPT-1 (11 jun 2018), BERT (oct 2018). BERT fue el más completo e influyente.
- **GPT-2** se liberó por etapas (124M/355M/774M/1.500M, feb–nov 2019) pero terminó completamente abierto. El cierre real empieza con **GPT-3 (2020, solo API)**. **ChatGPT** (30 nov 2022) es GPT-3.5 ajustado con RLHF.
- **Ley 21.719** (Chile): plena vigencia 1 dic 2026. **No** fija "72 horas" (eso es GDPR).
- ChatGPT: 100M usuarios en 2 meses (UBS vía Reuters, feb 2023); TikTok ~9 meses; Instagram ~30 meses.
- LLaMA filtrado el 3 mar 2023; Llama 2 18 jul 2023; Mistral 7B 27 sep 2023 (Apache 2.0); DeepSeek R1 20 ene 2025 (671B, MIT); gpt-oss 5 ago 2025 (Apache 2.0, 120b y 20b); Qwen3.6-27B abr 2026 (supera a Qwen3.5-397B-A17B en SWE-bench Verified 77,2 vs 76,2; ~16,8 GB en Q4_K_M).
- Artificial Analysis Index 7 sep 2026: GLM-5.3 44, Kimi K3 44, GLM-5.3-Flash 42, Qwen3.8 40, DeepSeek V4 Pro 36; mejor cerrado 53. Cambió una semana después → "importa el criterio, no el ranking".
- Convenio Marco **ID 2239-2-LR26**: 3 categorías, 18 tipos de servicios; plazo extendido al 25 sep 2026. Convenio anterior 2239-19-LR23. "~100 páginas" es dato del speaker, **sin verificar**.
- LM Studio con documentos: si cabe en el contexto inyecta el documento completo; si no, usa RAG.
- LLaVA-1.5: 336×336 px → 24×24 parches → **576 tokens visuales**.
- Ollama: `localhost:11434`, API compatible con OpenAI; `ollama ps` (columnas PROCESSOR y SIZE, que incluye caché KV); `--verbose` da tokens/s; `/set parameter num_ctx N`; `num_gpu` limita capas en GPU. **Ollama no expone la ocupación de la caché KV**: el medidor de contexto debe presentarse como estimación.
- LangChain actual: `OllamaEmbeddings` (paquete `langchain-ollama`), `InMemoryVectorStore` (`langchain_core`), agente con `create_agent` + herramienta `@tool`.

## Pendientes

**Del usuario:**
- Logos oficiales de empresas y logo de Afentu (placeholder SVG en la portada, bloque `.brand`).
- URL real del repo de GitHub → regenerar `slides/assets/qr.b64` (hoy apunta a `https://github.com/TU-USUARIO/taller-open-weights-chiletec`). Se puede generar con `qrencode -o qr.png URL && base64 -w0 qr.png > slides/assets/qr.b64`.
- Costos de hardware en Chile (se ofreció buscar precios de referencia).
- PDF de las bases (y anexos) para el dataset del benchmark; confirmar las ~100 páginas.
- Modelo multimodal para el Camino 2; confirmar modelos de la demo (Llama 3.2 3B, Qwen3.6 27B o Gemma 4, y el modelo para GPU vs CPU).
- Confirmar el reparto de tiempos de la Parte 2.

**De trabajo:**
1. Reorganizar la Parte 2 del deck al orden acordado (LM Studio → Ollama → RAG) con diapositivas puente, **denso vs MoE**, **JSON anotado** y resultados de ambos benchmarks.
2. Actualizar `README.md`, `demo/` y `para-asistentes/` al temario nuevo (hoy mencionan DashAI y el orden viejo).
3. Construir `notebooks/` (01 primera petición, 02 benchmark hardware, 03 benchmark modelos, 04 RAG con LangChain), `benchmarks/` y `scripts/medidor-contexto`, más un instalador de un solo comando por sistema operativo.
4. Evaluar exportación del deck HTML a PPTX.

El usuario revisa **por secciones** y da comentarios por partes: no reescribir todo de una vez; mostrar el resultado de cada sección y esperar su revisión.
