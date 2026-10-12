# Instalar Ollama (opcional)

Ollama es la otra herramienta que se muestra en el taller. A diferencia de LM Studio, no tiene una ventana de chat propia — funciona "de fondo" y otras aplicaciones se conectan a él. Si es tu primera vez explorando IA local, **te recomendamos empezar solo con LM Studio** ([ver guía](README.md)) y volver a Ollama después si te interesa el lado más técnico.

## Windows y Mac: instalador con clics, igual que cualquier programa

Buenas noticias: aunque Ollama nació como herramienta de consola, hoy tiene instaladores gráficos normales para Windows y Mac.

### Windows

1. Ve a **[ollama.com/download](https://ollama.com/download)**.
2. Descarga el instalador para Windows (`.exe`).
3. Ábrelo y sigue los pasos — se instala como cualquier programa y queda corriendo silenciosamente con un ícono en la bandeja del sistema (junto al reloj, abajo a la derecha).

### Mac

1. Ve a **[ollama.com/download](https://ollama.com/download)**.
2. Descarga el instalador para Mac.
3. Ábrelo y arrastra la aplicación a tu carpeta de Aplicaciones, igual que cualquier otra app. Aparece un ícono en la barra de menú (arriba).

## ¿Cómo lo uso si no tiene ventana de chat?

Una vez instalado, Ollama queda "escuchando" en tu computador, listo para que otras aplicaciones —como LM Studio, o herramientas de programación— le pidan respuestas. Si quieres chatear directamente con un modelo sin instalar nada más, necesitas abrir una terminal:

- **Windows:** busca "Símbolo del sistema" o "PowerShell" en el menú de inicio.
- **Mac:** busca "Terminal" en Launchpad.

Y escribe:

```
ollama run llama3.2
```

La primera vez descarga el modelo (puede tardar unos minutos); luego puedes escribirle directamente en esa misma ventana. Para salir, escribe `/bye`.

## En resumen

| Quiero... | Instala |
|---|---|
| Chatear con IA local con una ventana visual, sin usar la terminal | **LM Studio** ([guía](README.md)) |
| Entender cómo funciona "el motor" por debajo, o conectarlo a otras herramientas | **Ollama** (esta guía) |
| Las dos cosas | Instala ambos — no interfieren entre sí |

¿Dudas sobre estos términos? Revisa el [glosario](glosario.md).
