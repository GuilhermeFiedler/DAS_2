from core.base_extractor import BaseExtractor


class CategoriaExtractor(BaseExtractor):
    TABLE = "categoria"
    PRIMARY_KEY = "id_categoria"
    COLUMNS = (
        "id_categoria", "cd_categoria", "nm_categoria", "ds_descricao",
        "fl_ativo", "dt_inclusao", "dt_atualizacao", "nm_sistema_origem",
        "cd_registro_origem"
    )
