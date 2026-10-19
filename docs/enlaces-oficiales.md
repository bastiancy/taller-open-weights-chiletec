# Enlaces oficiales de referencia — Taller 1

Revisado el **18 oct 2026**. Cada URL se comprobó con una petición HTTP (código 200 y título de la página) o,
cuando el sitio bloquea las peticiones automáticas (openai.com responde 403), con búsqueda web.

Notas de verificación:
- **OK**: la URL existe y la página corresponde a lo indicado.
- **OK (indirecto)**: el sitio bloquea la verificación automática, pero la URL aparece indexada con ese contenido o la cita una fuente oficial.
- **dudoso**: probablemente correcta, pero no se pudo confirmar.
- **no encontrado**: no existe un recurso oficial de ese tipo.

---

## Parte 1 — Breve historia de la galaxia

### lm_1b (Google, 2016)
| Recurso | URL | Nota |
|---|---|---|
| Paper: *Exploring the Limits of Language Modeling* | https://arxiv.org/abs/1602.02410 | OK |
| Código y pesos | https://github.com/tensorflow/models/tree/archive/research/lm_1b | OK. Ya no está en `master` (404); solo en la rama `archive`. |

### CoVe (Salesforce, 2017)
| Recurso | URL | Nota |
|---|---|---|
| Paper: *Learned in Translation: Contextualized Word Vectors* | https://arxiv.org/abs/1708.00107 | OK |
| Código y pesos | https://github.com/salesforce/cove | OK (repositorio archivado) |

### ULMFiT (fast.ai, 2018)
| Recurso | URL | Nota |
|---|---|---|
| Paper: *Universal Language Model Fine-tuning for Text Classification* | https://arxiv.org/abs/1801.06146 | OK |
| Anuncio (15 may 2018) | https://nlp.fast.ai/classification/2018/05/15/introducing-ulmfit.html | OK |
| Código (biblioteca fastai) | https://github.com/fastai/fastai | OK. No hay repositorio exclusivo de ULMFiT; vive dentro de fastai. |

### ELMo (AllenAI, 2018)
| Recurso | URL | Nota |
|---|---|---|
| Paper: *Deep contextualized word representations* | https://arxiv.org/abs/1802.05365 | OK |
| Código y pesos (TensorFlow) | https://github.com/allenai/bilm-tf | OK |
| Página antigua de ELMo en allennlp.org | https://allenai.org/allennlp/software/elmo | dudoso: hoy redirige a https://github.com/allenai/allennlp-models |

### Transformer (Google, 2017)
| Recurso | URL | Nota |
|---|---|---|
| Paper: *Attention Is All You Need* | https://arxiv.org/abs/1706.03762 | OK |
| Código de referencia (tensor2tensor) | https://github.com/tensorflow/tensor2tensor | OK (repositorio archivado) |
| Anuncio en el blog de Google Research | https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/ | OK |

### GPT-1 (OpenAI, 11 jun 2018)
| Recurso | URL | Nota |
|---|---|---|
| Anuncio: *Improving language understanding with unsupervised learning* | https://openai.com/index/language-unsupervised/ | OK (indirecto) |
| Paper (PDF) | https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf | OK |
| Código y pesos | https://github.com/openai/finetune-transformer-lm | OK (archivado) |
| Hugging Face | https://huggingface.co/openai-community/openai-gpt | OK |

### BERT (Google, oct 2018)
| Recurso | URL | Nota |
|---|---|---|
| Paper | https://arxiv.org/abs/1810.04805 | OK |
| Código y pesos | https://github.com/google-research/bert | OK (archivado) |
| Anuncio: *Open Sourcing BERT* | https://research.google/blog/open-sourcing-bert-state-of-the-art-pre-training-for-natural-language-processing/ | OK |
| Hugging Face | https://huggingface.co/google-bert/bert-base-uncased | OK |

### GPT-2 (OpenAI, feb–nov 2019)
| Recurso | URL | Nota |
|---|---|---|
| Anuncio: *Better language models and their implications* (14 feb 2019) | https://openai.com/index/better-language-models/ | OK (indirecto) |
| Publicación del modelo de 1.500M (5 nov 2019) | https://openai.com/index/gpt-2-1-5b-release/ | dudoso: Wikipedia cita `openai.com/blog/gpt-2-1-5b-release/`; la ruta `/index/` sigue el patrón actual de OpenAI, pero no se pudo confirmar |
| Paper (PDF) | https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf | OK |
| Código | https://github.com/openai/gpt-2 | OK (archivado) |
| Hugging Face (124M y 1.5B) | https://huggingface.co/openai-community/gpt2 · https://huggingface.co/openai-community/gpt2-xl | OK |

### Lado oscuro (referencia): GPT-3 y ChatGPT
| Recurso | URL | Nota |
|---|---|---|
| Paper GPT-3: *Language Models are Few-Shot Learners* | https://arxiv.org/abs/2005.14165 | OK |
| Anuncio *Introducing ChatGPT* (30 nov 2022) | https://openai.com/index/chatgpt/ | dudoso: openai.com bloquea la verificación y la búsqueda no devolvió la página |

### LLaMA (Meta, feb 2023)
| Recurso | URL | Nota |
|---|---|---|
| Anuncio: *Introducing LLaMA* | https://ai.meta.com/blog/large-language-model-llama-meta-ai/ | OK |
| Paper | https://arxiv.org/abs/2302.13971 | OK |
| Código de inferencia | https://github.com/meta-llama/llama | OK (antes `facebookresearch/llama`, hoy redirige) |
| Hugging Face | — | no encontrado: LLaMA 1 nunca se publicó en HF por Meta (los pesos se entregaban por formulario y se filtraron). |

### Llama 2 (Meta, 18 jul 2023)
| Recurso | URL | Nota |
|---|---|---|
| Anuncio (Meta y Microsoft) | https://about.fb.com/news/2023/07/llama-2/ | OK |
| Paper | https://arxiv.org/abs/2307.09288 | OK |
| Hugging Face | https://huggingface.co/meta-llama/Llama-2-7b-hf | OK (acceso con aceptación de licencia) |
| Código | https://github.com/meta-llama/llama | OK |
| Sitio de Llama | https://www.llama.com/ | dudoso: hoy redirige a https://dev.meta.ai/ |

### Mistral 7B (Mistral AI, 27 sep 2023)
| Recurso | URL | Nota |
|---|---|---|
| Anuncio | https://mistral.ai/news/announcing-mistral-7b/ | OK |
| Paper | https://arxiv.org/abs/2310.06825 | OK |
| Hugging Face | https://huggingface.co/mistralai/Mistral-7B-v0.1 | OK |
| Código de inferencia | https://github.com/mistralai/mistral-inference | OK (archivado) |

### Mixtral 8x7B (Mistral AI, dic 2023)
| Recurso | URL | Nota |
|---|---|---|
| Anuncio: *Mixtral of experts* | https://mistral.ai/news/mixtral-of-experts/ | OK |
| Paper | https://arxiv.org/abs/2401.04088 | OK |
| Hugging Face | https://huggingface.co/mistralai/Mixtral-8x7B-v0.1 | OK |

### DeepSeek R1 (DeepSeek, 20 ene 2025)
| Recurso | URL | Nota |
|---|---|---|
| GitHub | https://github.com/deepseek-ai/DeepSeek-R1 | OK |
| Hugging Face | https://huggingface.co/deepseek-ai/DeepSeek-R1 | OK |
| Paper | https://arxiv.org/abs/2501.12948 | OK |

### gpt-oss (OpenAI, 5 ago 2025)
| Recurso | URL | Nota |
|---|---|---|
| Anuncio: *Introducing gpt-oss* | https://openai.com/index/introducing-gpt-oss/ | OK (indirecto) |
| GitHub | https://github.com/openai/gpt-oss | OK |
| Hugging Face 120b | https://huggingface.co/openai/gpt-oss-120b | OK |
| Hugging Face 20b | https://huggingface.co/openai/gpt-oss-20b | OK |
| Ficha técnica (model card) | https://arxiv.org/abs/2508.10925 | OK |

### Qwen3.6-27B (Alibaba Qwen, abr 2026)
| Recurso | URL | Nota |
|---|---|---|
| Hugging Face | https://huggingface.co/Qwen/Qwen3.6-27B | OK (creado el 21 abr 2026, Apache 2.0). Su tabla confirma SWE-bench Verified 77,2 (Qwen3.6-27B) vs 76,2 (Qwen3.5-397B-A17B). |
| Blog | https://qwen.ai/blog?id=qwen3.6-27b | OK (indirecto): lo enlaza la ficha oficial en HF; qwen.ai responde 200 a cualquier `id`, así que no se pudo confirmar de forma automática |
| GitHub | https://github.com/QwenLM/Qwen3.8 | OK. Es el mismo repositorio que antes se llamó Qwen3.5 y Qwen3.6 (esas URLs redirigen ahí). |

### Qwen3.5-397B-A17B (Alibaba Qwen, feb 2026)
| Recurso | URL | Nota |
|---|---|---|
| Hugging Face | https://huggingface.co/Qwen/Qwen3.5-397B-A17B | OK (16 feb 2026, Apache 2.0) |
| GitHub | https://github.com/QwenLM/Qwen3.8 | OK (repositorio renombrado, ver arriba) |

---

## Panorama actual (ranking de Artificial Analysis)

| Recurso | URL | Nota |
|---|---|---|
| Artificial Analysis (ranking de modelos) | https://artificialanalysis.ai/leaderboards/models | OK. El ranking cambia seguido: capturar la fecha al mostrarlo. |

### GLM-5.3 (Z.ai)
| Recurso | URL | Nota |
|---|---|---|
| Hugging Face | https://huggingface.co/zai-org/GLM-5.3 | OK (25 ago 2026; licencia marcada "other" en HF, revisar el archivo LICENSE) |
| Hugging Face (GLM-5.3-Flash) | https://huggingface.co/zai-org/GLM-5.3-Flash | OK |
| GitHub | https://github.com/zai-org/GLM-5 | OK, pero dudoso como fuente de 5.3: el README cubre hasta GLM-5.2; no existe `zai-org/GLM-5.3` |
| Paper GLM-5 | https://arxiv.org/abs/2602.15763 | OK (citado en la ficha de GLM-5.3) |

### Kimi K3 (Moonshot AI)
| Recurso | URL | Nota |
|---|---|---|
| Hugging Face | https://huggingface.co/moonshotai/Kimi-K3 | OK (13 jun 2026; licencia "other", ver LICENSE en HF) |
| GitHub | https://github.com/MoonshotAI/Kimi-K3 | OK |
| Informe técnico | https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf | OK |

### DeepSeek V4 Pro (DeepSeek)
| Recurso | URL | Nota |
|---|---|---|
| Hugging Face | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro | OK (22 abr 2026, MIT). Hay una versión posterior: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813 |
| Paper: *DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence* | https://arxiv.org/abs/2606.19348 | OK |
| GitHub | — | no encontrado: DeepSeek no tiene repositorio propio de V4 (solo HF y ModelScope) |

### Qwen3.8 (Alibaba Qwen)
| Recurso | URL | Nota |
|---|---|---|
| Hugging Face (insignia) | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B | OK (8 ago 2026; licencia "other") |
| Hugging Face (27B) | https://huggingface.co/Qwen/Qwen3.8-27B | OK (Apache 2.0) |
| GitHub | https://github.com/QwenLM/Qwen3.8 | OK |
| Blog | https://qwen.ai/blog?id=qwen3.8 | OK (indirecto): lo enlazan las fichas oficiales en HF |
| Nota | — | dudoso: el ranking dice "Qwen3.8" sin variante. Hay al menos 2.4T-A95B, 27B y Flash-Next; confirmar cuál es. |

---

## Herramientas

### Ollama
| Recurso | URL | Nota |
|---|---|---|
| Sitio | https://ollama.com/ | OK |
| Catálogo de modelos | https://ollama.com/library | OK |
| Documentación | https://docs.ollama.com/ | OK |
| GitHub | https://github.com/ollama/ollama | OK |
| Referencia de la API | https://docs.ollama.com/api | OK (también https://github.com/ollama/ollama/blob/main/docs/api.md) |
| API: generate / chat / ps | https://docs.ollama.com/api/generate · https://docs.ollama.com/api/chat · https://docs.ollama.com/api/ps | OK |
| Compatibilidad con la API de OpenAI | https://docs.ollama.com/openai | OK |
| FAQ | https://docs.ollama.com/faq | OK (la versión en GitHub `docs/faq.md` ya no existe: 404) |
| Modelfile y parámetros (`num_ctx`, `num_gpu`, etc.) | https://docs.ollama.com/modelfile | OK (`docs/modelfile.md` en GitHub: 404) |
| Largo de contexto | https://docs.ollama.com/context-length | OK |
| GPU | https://docs.ollama.com/gpu | OK |
| CLI | https://docs.ollama.com/cli | OK |

### LM Studio
| Recurso | URL | Nota |
|---|---|---|
| Sitio | https://lmstudio.ai/ | OK |
| Documentación (app) | https://lmstudio.ai/docs/app | OK (`/docs` redirige) |
| Descargar modelos | https://lmstudio.ai/docs/app/basics/download-model | OK |
| Chat con documentos (RAG) | https://lmstudio.ai/docs/app/basics/rag | OK |
| CLI `lms` | https://lmstudio.ai/docs/cli | OK |
| CLI: `lms load` / `lms server start` | https://lmstudio.ai/docs/cli/local-models/load · https://lmstudio.ai/docs/cli/serve/server-start | OK |
| GitHub de la CLI | https://github.com/lmstudio-ai/lms | OK |
| Servidor local | https://lmstudio.ai/docs/developer/core/server | OK |
| API compatible con OpenAI | https://lmstudio.ai/docs/developer/openai-compat | OK |
| Catálogo de modelos | https://lmstudio.ai/models | OK |

### LangChain
| Recurso | URL | Nota |
|---|---|---|
| Documentación | https://docs.langchain.com/ | OK |
| Instalación | https://docs.langchain.com/oss/python/langchain/install | OK |
| `OllamaEmbeddings` | https://docs.langchain.com/oss/python/integrations/text_embedding/ollama | OK |
| `ChatOllama` | https://docs.langchain.com/oss/python/integrations/chat/ollama | OK |
| Proveedor Ollama (resumen) | https://docs.langchain.com/oss/python/integrations/providers/ollama | OK |
| Paquete `langchain-ollama` | https://pypi.org/project/langchain-ollama/ · https://reference.langchain.com/python/integrations/langchain_ollama/ | OK |
| `InMemoryVectorStore` | https://docs.langchain.com/oss/python/integrations/vectorstores/in_memory | OK |
| Agentes (`create_agent`) | https://docs.langchain.com/oss/python/langchain/agents | OK (referencia: https://reference.langchain.com/python/langchain/agents) |
| Herramientas (`@tool`) | https://docs.langchain.com/oss/python/langchain/tools | OK |
| Tutorial RAG | https://docs.langchain.com/oss/python/langchain/rag | OK |
| GitHub | https://github.com/langchain-ai/langchain | OK |

### JupyterLab
| Recurso | URL | Nota |
|---|---|---|
| Proyecto Jupyter | https://jupyter.org/ | OK |
| Documentación | https://jupyterlab.readthedocs.io/en/stable/ | OK |
| Instalación | https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html | OK |
| GitHub | https://github.com/jupyterlab/jupyterlab | OK |

### llama.cpp y formato GGUF
| Recurso | URL | Nota |
|---|---|---|
| GitHub llama.cpp | https://github.com/ggml-org/llama.cpp | OK |
| Especificación GGUF | https://github.com/ggml-org/ggml/blob/master/docs/gguf.md | OK |
| PR que introdujo GGUF (#2398, ago 2023) | https://github.com/ggml-org/llama.cpp/pull/2398 | OK |
| PR de las cuantizaciones "k-quants", origen de Q4_K_M (#1684, jun 2023) | https://github.com/ggml-org/llama.cpp/pull/1684 | OK |
| Herramienta `quantize` (tipos de cuantización) | https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md | OK |
| GGUF en Hugging Face | https://huggingface.co/docs/hub/gguf | OK |
| Usar GGUF de HF con Ollama | https://huggingface.co/docs/hub/ollama | OK |

---

## Cuentas y organizaciones oficiales

Todas verificadas (HTTP 200 en la API de GitHub y en la de Hugging Face).

| Empresa | GitHub | Hugging Face |
|---|---|---|
| Google | https://github.com/google · https://github.com/google-research · https://github.com/google-deepmind | https://huggingface.co/google · https://huggingface.co/google-bert |
| OpenAI | https://github.com/openai | https://huggingface.co/openai · https://huggingface.co/openai-community (modelos antiguos: GPT-1, GPT-2) |
| Meta | https://github.com/facebookresearch · https://github.com/meta-llama | https://huggingface.co/meta-llama · https://huggingface.co/facebook |
| Mistral AI | https://github.com/mistralai | https://huggingface.co/mistralai |
| DeepSeek | https://github.com/deepseek-ai | https://huggingface.co/deepseek-ai |
| Alibaba Qwen | https://github.com/QwenLM | https://huggingface.co/Qwen |
| Z.ai (GLM) | https://github.com/zai-org | https://huggingface.co/zai-org |
| Moonshot AI (Kimi) | https://github.com/MoonshotAI | https://huggingface.co/moonshotai |
| Ollama | https://github.com/ollama | — |
| LM Studio | https://github.com/lmstudio-ai | https://huggingface.co/lmstudio-community (cuantizaciones GGUF/MLX) |
| Hugging Face | https://github.com/huggingface | https://huggingface.co/huggingface |
| LangChain | https://github.com/langchain-ai | — |
| llama.cpp / ggml | https://github.com/ggml-org | https://huggingface.co/ggml-org |
| Jupyter | https://github.com/jupyter · https://github.com/jupyterlab | — |
| AllenAI (ELMo) | https://github.com/allenai | — |
| Salesforce (CoVe) | https://github.com/salesforce | — |
| fast.ai (ULMFiT) | https://github.com/fastai | — |
| TensorFlow (lm_1b, tensor2tensor) | https://github.com/tensorflow | — |

## Hallazgos que conviene revisar en el deck o en el documento maestro

- **Chiletec:** el dominio `chiletec.cl` no existe (NXDOMAIN en DNS); el sitio oficial es **https://chiletec.org/**.
- **Qwen en GitHub:** `QwenLM/Qwen3.5` y `QwenLM/Qwen3.6` redirigen a `QwenLM/Qwen3.8` (es el mismo repositorio renombrado).
- **GLM-5.3, Kimi K3 y Qwen3.8-2.4T** tienen licencia "other" en Hugging Face (no MIT ni Apache): leer el LICENSE antes de llamarlos "abiertos" sin matices. DeepSeek V4 Pro es MIT; Qwen3.8-27B y Qwen3.6-27B, Apache 2.0.
- **Ollama:** la documentación se movió a docs.ollama.com; los enlaces antiguos a `docs/faq.md` y `docs/modelfile.md` en GitHub ya dan 404.
