from __future__ import annotations

from abc import ABC, abstractmethod

from core.connection import source_connection, target_connection


class ExtractionStrategy(ABC):
    @abstractmethod
    def extract(self, extractor) -> list[tuple]:
        ...


class CargaCompleta(ExtractionStrategy):
    def extract(self, extractor) -> list[tuple]:
        sql = extractor.build_select_sql()
        with source_connection() as src:
            cursor = src.cursor()
            cursor.execute(sql)
            return [tuple(row) for row in cursor.fetchall()]


class CargaIncremental(ExtractionStrategy):
    def __init__(self, watermark_column: str = "dt_atualizacao") -> None:
        self.watermark_column = watermark_column

    def _watermark(self, extractor):
        with target_connection() as dst:
            cursor = dst.cursor()
            cursor.execute(
                f"SELECT MAX({self.watermark_column}) FROM {extractor.full_table}"
            )
            row = cursor.fetchone()
            return row[0] if row else None

    def extract(self, extractor) -> list[tuple]:
        marca = self._watermark(extractor)
        base_sql = extractor.build_select_sql()

        with source_connection() as src:
            cursor = src.cursor()
            if marca is None:
                cursor.execute(base_sql)
            else:
                cursor.execute(
                    f"{base_sql} WHERE {self.watermark_column} > ?", marca
                )
            return [tuple(row) for row in cursor.fetchall()]
