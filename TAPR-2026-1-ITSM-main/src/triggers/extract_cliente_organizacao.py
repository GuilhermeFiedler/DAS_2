from core.base_extractor import BaseExtractor


class ClienteOrganizacaoExtractor(BaseExtractor):
    TABLE = "cliente_organizacao"
    PRIMARY_KEY = "id_cliente_organizacao"
    COLUMNS = (
        "id_cliente_organizacao", "cd_cliente_organizacao",
        "nm_cliente_organizacao", "nr_cnpj", "fl_ativo", "dt_inclusao",
        "dt_atualizacao", "nm_sistema_origem", "cd_registro_origem"
    )
