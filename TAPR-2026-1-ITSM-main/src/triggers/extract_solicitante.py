from core.base_extractor import BaseExtractor


class SolicitanteExtractor(BaseExtractor):
    TABLE = "solicitante"
    PRIMARY_KEY = "id_solicitante"
    COLUMNS = (
        "id_solicitante", "cd_solicitante", "id_cliente_organizacao",
        "nm_solicitante", "ds_email", "ds_telefone", "fl_ativo",
        "dt_inclusao", "dt_atualizacao", "nm_sistema_origem",
        "cd_registro_origem"
    )
