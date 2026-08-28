# ADR-003: Implementar Azure Functions para extração de dados

**Status:** Aceito  |  **Data:** 27-08-2026  |  **Autores:** Guilherme T. Fiedler

## Contexto

a liderança de TI da CorpTech enfrenta dificuldades para extrair inteligência dos dados de forma ágil. Os relatórios nativos do JSM são limitados e estáticos.

## Decisão

Foram implementadas Azure Functions com a linguagem de programação Python, para fazer integração de dados. Através de Merge, as functions extraem os dados do banco e enviam para um segundo banco, a partir dele o PowerBi extrai os dados e expõe no dashboard.

## Consequências

(+) Automatização da integração dos dados.
(+) Redução de processos manuais.
(-) Necessidade de manutenção da Function e das integrações.
(-) Falhas na execução podem atrasar a atualização dos dados.

## Alternativas rejeitadas

Exportação manual via CSV: maior esforço operacional e risco de erros.

## Links

- Substitui: Nenhum.
- Relacionado: Tendências e volume, Gestão de SLA, Backlog e filas e Performance da equipe.
- Evidências: Dashboard Power BI e código da Azure Function.