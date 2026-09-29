from core.base_extractor import BaseExtractor
from core.extraction_strategy import CargaIncremental


class CsatAvaliacaoExtractor(BaseExtractor):
    TABLE = "csat_avaliacao"
    PRIMARY_KEY = "id_csat_avaliacao"
    ESTRATEGIA = CargaIncremental()
    COLUMNS = (
        "id_csat_avaliacao", "id_chamado", "id_analista", "nr_score",
        "ds_comentario", "dt_avaliacao", "dt_inclusao", "dt_atualizacao",
        "nm_sistema_origem", "cd_registro_origem"
    )
