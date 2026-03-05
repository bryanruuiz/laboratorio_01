from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, time

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="API de Reservas de Salas",
    description="Microservicio para la gestión de reservas de salas universitarias."
)

# Base de datos temporal en memoria (Punto 5 de la Actividad 3)
reservas_db = []

# Definición del modelo de datos con Pydantic (Actividad 2 y Punto 2 de la Actividad 3)
class Reserva(BaseModel):
    id_reserva: int
    id_sala: int
    id_usuario: int
    fecha: date
    hora_inicio: time
    hora_fin: time
    personas: int
    estado: str