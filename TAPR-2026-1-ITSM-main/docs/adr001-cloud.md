# ADR-001: Utilizar variáveis de ambiente para proteção de dados.

**Status:** Aceito  |  **Data:** 27-08-2026  |  **Autores:** Guilherme T. Fiedler

## Contexto
 CorpTech necessita de uma arquitetura capaz de integrar os dados provenientes do Jira Service Management (JSM), realizar o processamento e sincronização das informações e disponibilizá-las para análise gerencial no Power BI.

O cenário atual depende da exportação manual dos dados do JSM em arquivos CSV, o que dificulta a criação de históricos, aumenta o esforço operacional e limita a capacidade de análise dos indicadores de suporte.

## Decisão


Foi adotada a Microsoft Azure como plataforma de nuvem para hospedar os principais componentes da solução de integração e armazenamento de dados do projeto.

A arquitetura utiliza serviços gerenciados da Azure:

Azure Functions: responsável pela execução das rotinas de integração e sincronização dos dados.
Azure SQL Database: responsável pelo armazenamento estruturado dos dados utilizados pela solução.
A utilização de serviços gerenciados da Azure permite que a solução seja executada sem a necessidade de manter servidores físicos ou máquinas virtuais dedicadas exclusivamente à integração.
## Consequências

(+) Redução da necessidade de infraestrutura física ou servidores próprios para execução da solução.
(+) Utilização de serviços gerenciados, reduzindo atividades de administração e manutenção da infraestrutura.
(-) Indisponibilidade ou problemas nos serviços de nuvem podem afetar a atualização dos dados e, consequentemente, a disponibilidade das informações nos dashboards.
(-) A equipe responsável pela solução precisa possuir conhecimento dos serviços Azure utilizados.

## Alternativas rejeitadas


- Máquinas virtuais hospedadas em infraestrutura própria ou em nuvem: rejeitada para a execução das integrações por exigir maior administração do sistema operacional e da infraestrutura quando comparada ao modelo serverless das Azure Functions.

## Links

 -Substitui: Nenhum.

 -Relacionado: ADR-002 – Implementar Azure SQL Database.

 -Relacionado: ADR-003 – Implementar Azure Functions para extração de dados.

 -Relacionado: ADR-004 – Implementar Dashboards utilizando Power BI para análise de dados.

 -Evidências: Código das Azure Functions, configuração dos bancos Azure SQL Database