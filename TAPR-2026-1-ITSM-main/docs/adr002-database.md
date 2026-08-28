# ADR-002: Implementar Azure SQL database

**Status:** Aceito  |  **Data:** 27-08-2026  |  **Autores:** Guilherme T. Fiedler

## Contexto

A solução necessita de uma base de dados para armazenar os dados extraídos do ITSM e disponibilizá-los de forma estruturada para consultas e análises no Power BI.

## Decisão

Foi adotado o Azure SQL Database como banco de dados de destino da solução. Essa base armazenará os sincronizados por meio das Azure Functions.

## Consequências

(+) Integração com Azure Functions e Power BI.
(+) Escalabilidade conforme a necessidade da aplicação.
(-) Dependência dos serviços Azure.
(-) Custos relacionados ao uso do banco.

## Alternativas rejeitadas

SQL Server em Servidor Próprio: Manutenção difícil comparado à manutenção em nuvem.

## Links

- Substitui: Nenhum.
- Relacionado: ADR de integração com Azure Functions.
- Evidências: Azure SQL Database utilizado pela solução