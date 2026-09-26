import pandas as pd
from pathlib import Path

class ExcelExtractor:
    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def extraer(self) -> pd.DataFrame:
        if not self.file_path.exists():
            raise FileNotFoundError(f"No se encontró el archivo de origen en: {self.file_path}")
        
        print(f"[EXTRACT] Leyendo datos desde: {self.file_path.name}")

        return pd.read_excel(self.file_path)