# 5. Troubleshooting — qué hacer si algo falla

## `nvidia-smi` no muestra nada / comando no encontrado

El driver NVIDIA no está instalado o no cargó correctamente.

```bash
sudo ubuntu-drivers devices        # ver qué driver recomienda Ubuntu
sudo ubuntu-drivers autoinstall    # instalar el recomendado
sudo reboot
```

Después del reinicio, `nvidia-smi` debe funcionar antes de tocar Ollama o LM Studio.

## Ollama corre pero usa CPU en vez de GPU

Confirma que el driver es visible para Ollama:

```bash
nvidia-smi                 # ¿ves la GPU aquí?
journalctl -u ollama -n 50 # busca líneas mencionando CUDA o GPU
```

Si `nvidia-smi` funciona pero Ollama no detecta la GPU, reinicia el servicio:

```bash
sudo systemctl restart ollama
```

Si persiste, revisa que no haya una versión vieja de `nvidia-container-toolkit` o librerías CUDA conflictivas instaladas.

## LM Studio (AppImage) no abre o se cierra inmediatamente

Prueba ejecutarlo desde la terminal para ver el error:

```bash
./LM_Studio.AppImage --no-sandbox
```

Errores comunes:
- **Falta FUSE**: `sudo apt install -y libfuse2`
- **AppArmor bloquea el sandbox de Chromium** (Ubuntu 24.04+): usa `--no-sandbox` como arriba.

## LM Studio dice "CPU only" y no ve la GPU

- Confirma versión del driver NVIDIA: `nvidia-smi` debe reportar CUDA 12.x o superior.
- Ve a **Settings → Hardware** dentro de LM Studio y fuerza la detección de GPU manualmente si existe esa opción en tu versión.
- Como último recurso, descarga la build más reciente del AppImage — versiones viejas a veces tienen peor detección de hardware.

## El modelo no carga / error de memoria (OOM)

Síntoma clásico del "error clásico" que se explica en la charla: el archivo cabe, pero el archivo + caché KV no.

```bash
ollama ps        # ver qué hay cargado y cuánta memoria usa
ollama stop <modelo>
```

Soluciones, en orden de preferencia:
1. Usa una cuantización más agresiva del mismo modelo (Q4 en vez de Q6/Q8).
2. Reduce el contexto que le estás pidiendo (menos texto pegado, documento más corto).
3. Baja a un modelo más chico (`gpt-oss:20b` en vez de `qwen2.5:32b`).

## Todo funciona pero muy lento (menos de ~5 tokens/segundo)

Probablemente el modelo no entró completo en VRAM y Ollama está repartiendo entre GPU y RAM del sistema (swap). Revisa con `nvidia-smi` si la VRAM usada es menor a lo esperado — si es así, aplica las soluciones de la sección anterior.

## Plan de respaldo si nada de esto se resuelve a tiempo

1. Ten `llama3.2:1b` descargado siempre — es tan chico que corre en casi cualquier condición.
2. Ten capturas de pantalla o un screen recording de una corrida exitosa previa, por si necesitas mostrar el resultado sin poder ejecutar en vivo.
3. Si la GPU falla por completo, Ollama puede correr en CPU (lento, pero funcional) — suficiente para mostrar el concepto con el modelo de 1B.
