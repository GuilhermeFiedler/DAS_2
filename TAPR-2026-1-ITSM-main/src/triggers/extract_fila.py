from core.base_extractor import BaseExtractor


class FilaExtractor(BaseExtractor):
    TABLE = "fila"
    PRIMARY_KEY = "id_fila"
    COLUMNS = (
        "id_fila", "cd_fila", "nm_fila", "ds_descricao", "fl_ativo",
        "dt_inclusao", "dt_atualizacao", "nm_sistema_origem",
        "cd_registro_origem"
    )
