# 1. Instalar Ollama en Ubuntu (con GPU NVIDIA)

## Paso 0 — Confirmar que el driver NVIDIA funciona

Antes de instalar Ollama, confirma que Ubuntu ve tu RTX 3090:

```bash
nvidia-smi
```

Deberías ver una tabla con el nombre de la GPU, la versión del driver, y `24576MiB` de memoria total. Si este comando falla, instala el driver propietario de NVIDIA primero (`sudo ubuntu-drivers autoinstall` seguido de un reinicio) — Ollama no lo hace por ti.

## Paso 1 — Instalar Ollama

Un solo comando. El script detecta tu arquitectura, descarga el binario, instala el servicio y detecta la GPU automáticamente:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Al finalizar, el instalador te dirá si detectó tu GPU NVIDIA. Busca una línea como `NVIDIA GPU installed`.

## Paso 2 — Verificar que el servicio está corriendo

Ollama se instala como un servicio systemd que arranca automáticamente:

```bash
systemctl status ollama
```

Deberías ver `active (running)`. Si no, arráncalo manualmente:

```bash
sudo systemctl start ollama
sudo systemctl enable ollama
```

## Paso 3 — Confirmar la versión y el endpoint

```bash
ollama --version
curl http://localhost:11434
```

El segundo comando debe responder `Ollama is running`. Este es el servidor local que vas a mostrar en la demo — anota la URL, la vas a usar para explicar el endpoint compatible con OpenAI.

## Paso 4 — Probar con un modelo pequeño

Antes de descargar los modelos grandes de la demo (ver `03-modelos-y-comandos.md`), prueba que todo funciona con un modelo chico:

```bash
ollama run llama3.2:1b "Responde en una frase: ¿qué es un modelo open weight?"
```

Si esto responde en un par de segundos, Ollama y la GPU están funcionando correctamente.

## Paso 5 — Confirmar que Ollama usa la GPU y no la CPU

Mientras corres cualquier modelo, en otra terminal:

```bash
nvidia-smi
```

Deberías ver un proceso `ollama` en la lista de procesos con memoria GPU asignada. Si `nvidia-smi` no muestra nada usando la GPU, revisa `05-troubleshooting.md`.

---

**Comandos útiles que vas a usar seguido durante la preparación:**

```bash
ollama list                 # modelos descargados localmente
ollama ps                   # modelos actualmente cargados en memoria/VRAM
ollama rm <modelo>          # liberar espacio en disco
ollama stop <modelo>        # descargar un modelo de la VRAM sin borrarlo del disco
journalctl -u ollama -f     # ver logs del servicio en vivo (útil para debug)
```

Siguiente paso: [02-instalar-lmstudio.md](02-instalar-lmstudio.md)
