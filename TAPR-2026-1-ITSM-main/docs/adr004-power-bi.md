# ADR-004: Implementar Dashboards utilizando PowerBi para análise de dados

**Status:** Aceito  |  **Data:** 27-08-2026  |  **Autores:** Guilherme T. Fiedler

## Contexto

Não existe análise histórica de volume de chamados por período, picos de abertura ou sazonalidade. Decisões de dimensionamento são baseadas em percepção.

## Decisão

Através da tecnologia PowerBi, foi implementado um dashboard de Chamados, com conexão direta ao banco de dados via Azure, registrando contagem total, por analista, por categoria, por status e períodos.

## Consequências

(+) Análise estatística de dados de fácil visualização.

(+) Controle de chamados registrados.

(-) Dependência de sincronização com o banco de dados Azure.

## Alternativas rejeitadas

- Planihas Excel convencionais&#58; Atualização manual.

## Links

- Substitui: Nenhum.

- Relacionado: Problema relatado via documentação: Tendências e volume.

- Evidências: Imagem do dashboard no repositório, link de acesso do powerBi.