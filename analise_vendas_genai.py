import pandas as pd

# Dados de vendas simulados
data = {
    "mes": ["Jan", "Fev", "Mar", "Abr"],
    "vendas": [12000, 15000, 18000, 22000]
}

df = pd.DataFrame(data)

# Insight gerado (simulação de Gen AI)
insight = """
As vendas apresentaram crescimento contínuo ao longo dos meses.
O maior volume de vendas ocorreu em Abril.
Recomenda-se investir mais em marketing nesse período.
"""

print(insight)
