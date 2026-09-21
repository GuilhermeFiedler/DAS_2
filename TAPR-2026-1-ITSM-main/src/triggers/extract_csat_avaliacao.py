from core.base_extractor import BaseExtractor


class CsatAvaliacaoExtractor(BaseExtractor):
    TABLE = "csat_avaliacao"
    PRIMARY_KEY = "id_csat_avaliacao"
    COLUMNS = (
        "id_csat_avaliacao", "id_chamado", "id_analista", "nr_score",
        "ds_comentario", "dt_avaliacao", "dt_inclusao", "dt_atualizacao",
        "nm_sistema_origem", "cd_registro_origem"
    )
