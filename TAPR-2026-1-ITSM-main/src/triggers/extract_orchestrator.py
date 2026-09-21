import logging

import azure.functions as func

from core.base_extractor import BaseExtractor
from triggers.extract_analista import AnalistaExtractor
from triggers.extract_categoria import CategoriaExtractor
from triggers.extract_chamado import ChamadoExtractor
from triggers.extract_chamado_sla import ChamadoSlaExtractor
from triggers.extract_chamado_status_historico import ChamadoStatusHistoricoExtractor
from triggers.extract_cliente_organizacao import ClienteOrganizacaoExtractor
from triggers.extract_csat_avaliacao import CsatAvaliacaoExtractor
from triggers.extract_fila import FilaExtractor
from triggers.extract_sla import SlaExtractor
from triggers.extract_solicitante import SolicitanteExtractor

app = func.Blueprint()

PIPELINE: list[tuple[str, list[type[BaseExtractor]]]] = [
    ("Nível 1", [
        FilaExtractor,
        CategoriaExtractor,
        SlaExtractor,
        ClienteOrganizacaoExtractor,
    ]),
    ("Nível 2", [
        AnalistaExtractor,
        SolicitanteExtractor,
    ]),
    ("Nível 3", [
        ChamadoExtractor,
    ]),
    ("Nível 4", [
        ChamadoSlaExtractor,
        ChamadoStatusHistoricoExtractor,
        CsatAvaliacaoExtractor,
    ]),
]


@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer",
                   run_on_startup=False, use_monitor=False)
def extract_all(myTimer: func.TimerRequest) -> None:
    logging.info("Iniciando pipeline EL")
    total = 0

    for nivel, extractors in PIPELINE:
        logging.info(nivel)
        for extractor_cls in extractors:
            total += extractor_cls().run()

    logging.info("Pipeline EL concluída — %d linhas carregadas", total)
