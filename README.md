# 🎮 Juego del Ahorcado en Python

Un clásico juego del ahorcado implementado en Python con terminal a color y más de 500 palabras en español.

![Ejemplo de juego](https://via.placeholder.com/400x200?text=Captura+de+pantalla+del+juego)

## ✨ Características

- Interfaz de terminal con colores vibrantes
- Más de 500 palabras en español de diferentes longitudes
- Sistema de detección de tildes (á, é, í, ó, ú)
- Contador de intentos y fallos
- Visualización del estado del ahorcado
- Opción para jugar nuevamente

## 🛠 Requisitos

- Python 3.x
- Terminal que soporte códigos de color ANSI

## ⚙️ Instalación

1. Clona o descarga el repositorio
2. Ejecuta el juego con:
   ```bash
   python ahorcado.py
   ```

## 🎯 Cómo jugar

1. El juego selecciona una palabra aleatoria
2. Adivina letras una por una
3. Tienes 6 intentos antes de que se complete el ahorcado
4. Ganas si adivinas todas las letras antes de agotar los intentos

## 📦 Estructura del código

- **Variables de color**: Define colores ANSI para la terminal
- **Dibujos del ahorcado**: Arte ASCII para cada estado del juego
- **Lista de palabras**: Más de 500 palabras en español
- **Funciones principales**:
  - `randomColor()`: Muestra texto en colores aleatorios
  - `tildes()`: Maneja letras con acentos
  - `rallitas()`: Muestra guiones para las letras no adivinadas
  - `palabras()`: Procesa la palabra a adivinar

## 🚀 Ejecución

El juego se inicia automáticamente al ejecutar el script. Sigue las instrucciones en pantalla:

1. Introduce letras para adivinar la palabra
2. El juego te indicará si la letra es correcta o no
3. Puedes intentar adivinar la palabra completa en cualquier momento

## 📝 Notas

- Las palabras con tildes se manejan automáticamente (por ejemplo, "canción" puede adivinarse como "cancion")
- El juego evita repetir letras ya intentadas
- Al ganar o perder, puedes elegir jugar nuevamente con una palabra diferente

## 📜 Licencia

Este proyecto está bajo la licencia MIT.

---

Hecho con ❤️ por Quique usando Python
