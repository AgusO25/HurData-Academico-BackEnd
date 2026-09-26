# HurData - Backend 

Backend del Dashboard Analítico de Gestión Académica para la Universidad Nacional de Hurlingham (UNaHur). Desarrollado con Python, FastAPI y Pandas.

## Requisitos Previos
* Python 3.10 o superior.
* Git.

## Configuración del Entorno Local (Setup)

**1. Clonar el repositorio**
Abrir la terminal y ejecutar:
```bash
git clone [https://github.com/HurData-UNaHur/hurdata-pip-backend.git](https://github.com/HurData-UNaHur/hurdata-pip-backend.git)
cd hurdata-pip-backend
```

**2. Crear el entorno virtual**
Esto aísla las librerías del proyecto del resto de la computadora:
```bash
python -m venv venv
```

**3. Activar el entorno virtual**
* En Windows:
  ```bash
  venv\Scripts\activate
  ```
* En macOS / Linux:
  ```bash
  source venv/bin/activate
  ```
*(Deberían ver un `(venv)` al inicio de la línea en su terminal).*

**4. Instalar las dependencias**
Con el entorno activado, instalen todas las librerías (FastAPI, Pandas, etc.) usando el archivo de requerimientos:
```bash
pip install -r requirements.txt
```

## Gestión de Archivos Sensibles (Inputs)
Los reportes crudos del SIU Guaraní (archivos `.xlsx` o `.csv`) **NO** deben subirse a GitHub por cuestiones de privacidad de datos. 
Para probar los scripts ETL localmente, coloquen sus Excels dentro de la carpeta `files/` en la raíz del proyecto. El archivo `.gitignore` ya está configurado para omitir esta carpeta.