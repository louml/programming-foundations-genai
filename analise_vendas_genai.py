import pandas as pd

# Leitura da base de dados
df = pd.read_csv("dados_ecommerce_vendas.csv")

# Análises básicas
crescimento_faturamento = df["faturamento"].iloc[-1] - df["faturamento"].iloc[0]
taxa_conversao = df["pedidos"].sum() / df["visitas_site"].sum()

# Insight gerado (simulação de Gen AI)
insight = f"""
O faturamento apresentou crescimento ao longo do período analisado.
O crescimento total foi de R$ {crescimento_faturamento}.
A taxa média de conversão do site foi de {taxa_conversao:.2%}.
Recomenda-se manter os investimentos em marketing digital.
"""

print(insight)

