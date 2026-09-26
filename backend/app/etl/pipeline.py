from pathlib import Path
from app.etl.extractor import ExcelExtractor
from app.etl.transformer import SIUTransformer

def ejecutar_etl_base():
    # Ubicamos el archivo en la carpeta 'files' en la raíz del proyecto
    ruta_excel = Path(__file__).resolve().parent.parent.parent / "files" / "estadisticas_fin_cursada.xlsx"
    
    try:
        # 1. Extracción
        extractor = ExcelExtractor(ruta_excel)
        df_crudo = extractor.extraer()
        
        # 2. Transformación
        transformer = SIUTransformer()
        df_limpio = transformer.limpiar_basico(df_crudo)
        
        # 3. Carga (Temporal: Impresión por consola según el Ticket)
        print("\n--- Primeras 5 filas limpias ---")
        print(df_limpio.head())
        print(f"\n[INFO] Total de registros listos para la base de datos: {len(df_limpio)}")
        
    except Exception as e:
        print(f"[ERROR CRÍTICO] Falló la ejecución del pipeline: {e}")

if __name__ == "__main__":
    ejecutar_etl_base()