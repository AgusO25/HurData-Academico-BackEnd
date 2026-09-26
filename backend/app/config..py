import os
from dotenv import load_dotenv

# Carga las variables físicas del archivo .env al entorno de Python
load_dotenv()

# Centralizamos la configuración
class Config:
    # Busca la variable, y si el archivo .env falla, usa un valor por defecto
    SIU_FILENAME = os.getenv("EXCEL_SIU_FILENAME", "estadisticas_fin_cursada.xlsx")

config = Config()