from core.base_extractor import BaseExtractor


class ChamadoExtractor(BaseExtractor):
    TABLE = "chamado"
    PRIMARY_KEY = "id_chamado"
    COLUMNS = (
        "id_chamado", "nr_chamado", "ds_tipo_chamado", "ds_status_chamado",
        "ds_prioridade", "dt_criacao", "dt_resolucao",
        "dt_ultima_atualizacao", "id_analista_atual", "id_reporter",
        "id_categoria", "id_cliente_organizacao", "id_fila_atual",
        "ds_titulo", "ds_descricao", "dt_inclusao", "dt_atualizacao",
        "nm_sistema_origem", "cd_registro_origem"
    )
