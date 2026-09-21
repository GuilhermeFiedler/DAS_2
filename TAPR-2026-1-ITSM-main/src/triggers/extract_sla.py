from core.base_extractor import BaseExtractor


class SlaExtractor(BaseExtractor):
    TABLE = "sla"
    PRIMARY_KEY = "id_sla"
    COLUMNS = (
        "id_sla", "cd_sla", "nm_sla", "qt_meta_minutos", "ds_descricao",
        "fl_ativo", "dt_inclusao", "dt_atualizacao", "nm_sistema_origem",
        "cd_registro_origem"
    )
