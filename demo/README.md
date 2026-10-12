> ⚠️ **Desactualizado:** esta carpeta refleja el temario antiguo (incluye DashAI y el orden Ollama → LM Studio). Pendiente de actualizar; ver `CLAUDE.md`.

# Demo técnica — para el speaker

Instrucciones para preparar y ejecutar la demostración práctica del taller en tu equipo Ubuntu con la RTX 3090.

**Sigue este orden**, idealmente unos días antes del taller, no el mismo día:

1. **[01-instalar-ollama.md](01-instalar-ollama.md)** — instalar el motor Ollama por consola y verificar que usa la GPU
2. **[02-instalar-lmstudio.md](02-instalar-lmstudio.md)** — instalar LM Studio (AppImage) para la parte visual de la demo
3. **[03-modelos-y-comandos.md](03-modelos-y-comandos.md)** — qué modelos descargar, cuánto pesan, y los comandos exactos
4. **[04-guion-demo.md](04-guion-demo.md)** — el guion minuto a minuto de los 60 minutos de demo en vivo
5. **[05-troubleshooting.md](05-troubleshooting.md)** — qué hacer si algo falla el día del taller

## Checklist de la noche anterior

- [ ] `nvidia-smi` corre sin errores y muestra la RTX 3090
- [ ] Los modelos de la sección 3 ya están descargados (`ollama list` los muestra)
- [ ] LM Studio abre y detecta la GPU (Settings → Hardware)
- [ ] El documento corporativo de ejemplo para la demo de RAG está listo y a mano
- [ ] Probaste el guion completo una vez, cronómetro en mano
- [ ] Tienes una segunda pestaña de terminal lista con `nvidia-smi -l 1` para mostrar consumo en vivo
- [ ] Cerraste aplicaciones que compitan por VRAM (navegador con muchas pestañas, otros juegos/apps de GPU)

## Hardware de referencia

- GPU: NVIDIA RTX 3090, 24 GB VRAM
- OS: Ubuntu (22.04 o superior recomendado)
- Driver NVIDIA propietario instalado y funcionando (`nvidia-smi` debe correr antes de seguir)
