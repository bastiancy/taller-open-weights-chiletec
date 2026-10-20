# Instalar Ollama

Ollama es el "motor" para correr modelos locales desde la terminal. Corre de fondo como un servicio y expone un API local en `http://localhost:11434` al que se puede conectar cualquier aplicación (es compatible con el API de OpenAI).

Si es tu primera vez con IA local, parte por [LM Studio](instalar-lmstudio.md) y vuelve a Ollama cuando quieras ver lo que hay debajo.

## Instalación

- **Windows y macOS:** descarga el instalador desde **[ollama.com/download](https://ollama.com/download)** e instálalo como cualquier programa. Queda corriendo con un ícono en la bandeja (Windows) o en la barra de menú (macOS).
- **Linux:**
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

Comprueba que funciona abriendo una terminal (PowerShell en Windows, Terminal en macOS):

```bash
ollama --version
```

## Tu primer modelo

```bash
ollama run llama3.2:3b
```

La primera vez descarga el modelo (2 GB). Luego escribe tu pregunta; para salir, `/bye`.

Siguiente paso: los [comandos de la demo](comandos-ollama.md).

Documentación oficial: [docs.ollama.com](https://docs.ollama.com/)
