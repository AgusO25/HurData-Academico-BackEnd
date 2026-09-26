from pathlib import Path
from app.etl.extractor import ExcelExtractor
from app.etl.transformer import SIUTransformer # (O ExcelTransformer según como lo hayas llamado)
from app.config import config  # Importamos el archivo que creamos arriba

def ejecutar_etl_base():
    # Variable de configuración para armar la ruta
    ruta_excel = Path(__file__).resolve().parent.parent.parent / "files" / config.EXCEL_SIU_FILENAME
    
    try:
        # 1. Extracción
        extractor = ExcelExtractor(ruta_excel)
        df_crudo = extractor.extraer()
        
        # 2. Transformación
        transformer = SIUTransformer()
        df_limpio = transformer.limpiar_basico(df_crudo)
        
        # 3. Carga
        print("\n--- Primeras 5 filas limpias ---")
        print(df_limpio.head())
        
    except Exception as e:
        print(f"Error en el pipeline: {e}")

if __name__ == "__main__":
    ejecutar_etl_base()