# Instalar LM Studio

LM Studio es un programa gratuito para descargar modelos y conversar con ellos en tu computador, sin que tus datos salgan de tu equipo. Es la forma más simple de partir: no necesitas usar la terminal.

## Requisitos aproximados

- Windows 10/11 (64 bits), macOS con chip Apple (M1 o superior) o Linux (x64).
- 16 GB de RAM recomendado. Con 8 GB funcionan modelos chicos.
- 20 GB libres en disco o más (cada modelo pesa entre 2 y 20 GB).

## Instalación

1. Entra a **[lmstudio.ai](https://lmstudio.ai)** y descarga el instalador para tu sistema (la página lo detecta sola).
2. Instálalo como cualquier programa:
   - **Windows:** abre el `.exe`. Si aparece "Windows protegió tu PC", elige *Más información → Ejecutar de todas formas*.
   - **macOS:** abre el `.dmg` y arrastra LM Studio a *Aplicaciones*.
   - **Linux:** descarga el `.AppImage` (o el `.deb`), dale permisos de ejecución y ábrelo.
3. Abre LM Studio.

## Lo que mostramos en la demo

1. **Buscar y descargar un modelo** (ícono de lupa, *Model Search*). Por ejemplo, busca `gemma 4`. Fíjate en:
   - **Parámetros** (por ejemplo `26B-A4B`: 26 mil millones en total, 4 mil millones activos; es un modelo MoE).
   - **Cuantización** (`Q4_K_M`, `Q8_0`…): menos bits, menos memoria.
   - El aviso de si **cabe completo en tu GPU** o necesita usar la CPU.
2. **Library:** los modelos descargados, con su tamaño y los íconos de **capacidades** (visión, uso de herramientas, razonamiento).
3. **Cargar el modelo** (pestaña *Load*): ajusta la **ventana de contexto** (*Context Length*) y cuántas capas van a la GPU (*GPU Offload*).
4. **Chat:** elige el modelo abajo, escribe tu pregunta y mira las estadísticas bajo la respuesta (tokens por segundo).

## ¿Qué modelo descargo?

Como referencia (modelos cuantizados en Q4):

| Tu equipo | Prueba con |
|---|---|
| Notebook sin GPU, 16 GB de RAM | Gemma 4 12B o un modelo de 3–8B |
| GPU de 8 GB | Modelos de 7–8B (Llama 3.1 8B, Qwen3 8B) |
| GPU de 12–16 GB | Gemma 4 12B, modelos de 12–14B |
| GPU de 24 GB | Gemma 4 26B-A4B (rápido) o Qwen3.8 27B (más inteligente) |
| Mac con 32–64 GB de memoria unificada | Modelos de 27B a 70B, más lento que una GPU dedicada |

Más contexto en el [glosario](glosario.md) y en la diapositiva "Tu memoria decide el tamaño del modelo".

Documentación oficial: [lmstudio.ai/docs](https://lmstudio.ai/docs/app)
