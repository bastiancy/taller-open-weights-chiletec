# 2. Instalar LM Studio en Ubuntu (AppImage)

LM Studio en Linux se distribuye como **AppImage** — un solo archivo ejecutable, sin instalador ni gestor de paquetes. No tiene auto-actualización en Linux, así que descarga la versión más reciente manualmente cada cierto tiempo.

## Paso 1 — Descargar el AppImage

Ve a **[lmstudio.ai/download](https://lmstudio.ai/download)** en el navegador, selecciona **Linux** y descarga el `.AppImage` (arquitectura x64, salvo que tu equipo sea ARM64).

Alternativa por consola (ajusta la URL a la versión vigente que veas en la página de descargas):

```bash
cd ~/Descargas
# Reemplaza la URL por el enlace de descarga directa que te entregue lmstudio.ai/download
curl -L -o LM_Studio.AppImage "<URL_DE_DESCARGA_DE_LM_STUDIO>"
```

> LM Studio actualiza sus builds de Linux seguido y no publica una URL fija — por eso conviene descargarlo directamente desde el navegador la primera vez.

## Paso 2 — Dar permisos de ejecución

```bash
chmod +x LM_Studio.AppImage
```

## Paso 3 — Ejecutar

```bash
./LM_Studio.AppImage
```

Si ves un error relacionado con `sandbox` o `AppArmor` (común en Ubuntu 24.04+), ejecuta:

```bash
./LM_Studio.AppImage --no-sandbox
```

## Paso 4 — Confirmar que detecta la GPU

Dentro de LM Studio: **ícono de engranaje (Settings) → Hardware**. Debe listar tu RTX 3090 con 24 GB. Si aparece como "CPU only", revisa `05-troubleshooting.md` — normalmente es un tema de drivers CUDA visibles para la AppImage.

## Paso 5 — Activar el servidor local (opcional para la demo)

Si quieres mostrar que LM Studio también expone un endpoint compatible con OpenAI: pestaña **Developer** (ícono `</>`) → **Start Server**. Por defecto sirve en `http://localhost:1234/v1`.

## Paso 6 (opcional) — Crear un acceso directo en el menú de aplicaciones

Un AppImage no se integra solo al menú de Ubuntu. Si quieres lanzarlo como una app normal durante la demo (más prolijo que abrir la terminal):

```bash
sudo apt install -y libfuse2   # si el AppImage no abre por falta de FUSE
```

Puedes usar una herramienta como [Gear Lever](https://github.com/mijorus/gearlever) (disponible en Flathub) para integrarlo al menú y gestionar actualizaciones automáticamente — opcional, no es necesario para el taller.

Siguiente paso: [03-modelos-y-comandos.md](03-modelos-y-comandos.md)
