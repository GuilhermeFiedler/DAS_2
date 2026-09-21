from core.base_extractor import BaseExtractor


class ChamadoSlaExtractor(BaseExtractor):
    TABLE = "chamado_sla"
    PRIMARY_KEY = "id_chamado_sla"
    COLUMNS = (
        "id_chamado_sla", "id_chamado", "id_sla", "fl_breach",
        "qt_tempo_restante_minutos", "qt_tempo_decorrido_minutos",
        "qt_meta_minutos", "dt_referencia", "dt_inclusao", "dt_atualizacao",
        "nm_sistema_origem", "cd_registro_origem"
    )
