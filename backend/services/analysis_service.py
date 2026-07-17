import pandas as pd
import numpy as np
from typing import Dict, Any, List

class DataAnalysisService:
    @staticmethod
    def analyze_csv(file_path: str) -> Dict[str, Any]:
        df = pd.read_csv(file_path)
        summary = {
            "columns": list(df.columns),
            "shape": df.shape,
            "describe": df.describe().to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "correlation": df.select_dtypes(include=[np.number]).corr().to_dict()
        }
        return summary

    @staticmethod
    def calculate_statistics(data: List[float]) -> Dict[str, float]:
        arr = np.array(data)
        return {
            "mean": float(np.mean(arr)),
            "median": float(np.median(arr)),
            "std": float(np.std(arr)),
            "sum": float(np.sum(arr))
        }

analysis_service = DataAnalysisService()
