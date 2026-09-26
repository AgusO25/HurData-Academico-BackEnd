import pandas as pd

class ExcelTransformer:
    def limpiar_basico(self, df: pd.DataFrame) -> pd.DataFrame:
        print("[TRANSFORM] Iniciando limpieza básica de datos...")
        
        # 1. Crear una copia para no mutar el DataFrame original
        df_limpio = df.copy()
        
        # 2. Eliminar filas y columnas completamente vacías
        df_limpio.dropna(how='all', inplace=True)
        df_limpio.dropna(axis=1, how='all', inplace=True)
        
        # 3. Normalizar nombres de columnas (minúsculas, sin espacios)
        df_limpio.columns = [str(c).strip().lower().replace(" ", "_") for c in df_limpio.columns]
        
        return df_limpio