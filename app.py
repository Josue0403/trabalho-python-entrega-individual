import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


arquivo = "projecoes_2024_tab1_idade_simples.xlsx"
df = pd.read_excel(arquivo, header=5)


brasil = df[
    (df["LOCAL"] == "Brasil") &
    (df["SEXO"] == "Ambos")
].copy()


brasil["IDADE"] = brasil["IDADE"].astype(str)
brasil["2024"] = pd.to_numeric(
    brasil[2024], errors="coerce"
)

brasil = brasil.dropna(subset=["2024"])


plt.figure(figsize=(12, 6))

plt.bar(brasil["IDADE"], brasil["2024"])

plt.title("População do Brasil por idade — 2024")
plt.xlabel("Idade")
plt.ylabel("População")

plt.xticks(rotation=90)
plt.ticklabel_format(axis="y", style="plain")

plt.grid(axis="y", alpha=0.3)
plt.tight_layout()


plt.savefig("grafico_populacao_2024.png", dpi=180)
plt.show()
