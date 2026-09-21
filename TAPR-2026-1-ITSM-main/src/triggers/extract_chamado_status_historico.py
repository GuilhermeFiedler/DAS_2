from core.base_extractor import BaseExtractor


class ChamadoStatusHistoricoExtractor(BaseExtractor):
    TABLE = "chamado_status_historico"
    PRIMARY_KEY = "id_chamado_status_historico"
    COLUMNS = (
        "id_chamado_status_historico", "id_chamado", "ds_status_chamado",
        "dt_inicio_status", "dt_fim_status", "qt_tempo_status_minutos",
        "id_analista_responsavel", "id_fila", "dt_inclusao",
        "dt_atualizacao", "nm_sistema_origem", "cd_registro_origem"
    )
