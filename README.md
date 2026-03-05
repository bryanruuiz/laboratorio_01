# API de Reservas de Salas - ITM

## 1. Descripción del proyecto
Este proyecto es un microservicio web desarrollado con **FastAPI** y **Python** para gestionar las reservas de salas utilizadas en actividades académicas. Permite registrar nuevas reservas y consultar las existentes, validando que la estructura de los datos sea correcta mediante **Pydantic**. Los datos se almacenan temporalmente en la memoria del servidor.

## 2. Instrucciones de instalación
Para ejecutar este proyecto en un entorno local, sigue estos pasos:
en consola git bash
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu_usuario/laboratorio_01.git](https://github.com/tu_usuario/laboratorio_01.git)

   Entra a la carpeta del proyecto:
   cd laboratorio_01

   Crea y activa un entorno virtual:
   
   python -m venv venv
   source venv/Scripts/activate  # En Windows (Git Bash)

   Instala las dependencias requeridas:

   pip install -r requirements.txt

   Instrucciones de ejecución
Con el entorno virtual activado, inicia el servidor local ejecutando el siguiente comando

uvicorn main:app --reload


El servidor estará disponible en: http://127.0.0.1:8000



4. Ejemplos de uso de los endpoints
Puedes probar la API directamente desde la interfaz interactiva (Swagger UI) ingresando a: http://127.0.0.1:8000/docs

GET /reservas: Retorna una lista en formato JSON con todas las reservas registradas en memoria.

POST /reservas: Permite crear una nueva reserva enviando un JSON en el cuerpo de la petición.

Ejemplo de JSON válido para el POST:


{
  "id_reserva": 1,
  "id_sala": 101,
  "id_usuario": 100456,
  "fecha": "2026-03-10",
  "hora_inicio": "14:00:00",
  "hora_fin": "16:00:00",
  "personas": 20,
  "estado": "confirmada"
}