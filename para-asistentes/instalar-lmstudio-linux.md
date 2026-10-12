# Instalar LM Studio en Linux

En Linux, LM Studio se distribuye como un archivo **AppImage**: un solo archivo que ejecutas directamente, sin proceso de instalación tradicional. Requiere dos pasos por terminal (copiar y pegar), el resto es todo con clics.

## Requisitos

- Ubuntu 20.04 o superior (u otra distribución moderna)
- Al menos 16 GB de RAM recomendado
- Al menos 20 GB de espacio libre en disco

## Pasos

1. **Abre tu navegador** y ve a **[lmstudio.ai](https://lmstudio.ai)**.
2. Haz clic en el botón de descarga y elige **Linux**. Se descarga un archivo `.AppImage`.
3. Abre una terminal (en Ubuntu: busca "Terminal" en tus aplicaciones, o presiona `Ctrl+Alt+T`).
4. Ve a tu carpeta de Descargas y dale permiso de ejecución al archivo (copia y pega esto, ajustando el nombre del archivo si es distinto):

   ```bash
   cd ~/Descargas
   chmod +x LM-Studio-*.AppImage
   ```

5. Haz doble clic en el archivo desde tu explorador de archivos, o ejecútalo desde la terminal:

   ```bash
   ./LM-Studio-*.AppImage
   ```

6. Si no abre y ves un mensaje sobre "sandbox", ejecuta en su lugar:

   ```bash
   ./LM-Studio-*.AppImage --no-sandbox
   ```

## Primeros pasos dentro de LM Studio

1. Al abrir por primera vez, LM Studio te va a sugerir descargar un modelo. Elige uno recomendado o busca por nombre (por ejemplo, "gpt-oss").
2. Haz clic en **Download** y espera a que termine.
3. Ve a la pestaña de chat y empieza a escribir.

## Para analizar un documento (como en el taller)

1. En la ventana de chat, busca el ícono de **clip o "+"** junto a la caja de texto.
2. Selecciona un documento de tu computador (PDF o Word).
3. Hazle preguntas sobre su contenido — responde basándose en el documento, sin que salga de tu equipo.

## Nota sobre actualizaciones

A diferencia de Windows y Mac, la versión de Linux no se actualiza sola. Cuando quieras la versión más reciente, repite el paso 2 y reemplaza el archivo `.AppImage` anterior.

¿Dudas sobre estos términos? Revisa el [glosario](glosario.md).
