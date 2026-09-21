from core.base_extractor import BaseExtractor


class AnalistaExtractor(BaseExtractor):
    TABLE = "analista"
    PRIMARY_KEY = "id_analista"
    COLUMNS = (
        "id_analista", "cd_analista", "nm_analista", "ds_email", "ds_nivel",
        "id_fila_atual", "fl_ativo", "dt_inclusao", "dt_atualizacao",
        "nm_sistema_origem", "cd_registro_origem"
    )
