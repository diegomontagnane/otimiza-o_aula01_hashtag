import os
import pandas as pd

from dotenv import load_dotenv

from config import (
    ARQUIVO_PRODUTOS,
    CAMPOS_PRODUTO
)


def carregar_credenciais():

    load_dotenv()

    email = os.getenv("EMAIL")
    senha = os.getenv("SENHA")

    if not email or not senha:

        raise ValueError(
            "EMAIL ou SENHA não encontrados no .env"
        )

    return email, senha


def carregar_produtos():

    tabela = pd.read_csv(
        ARQUIVO_PRODUTOS
    )

    colunas_obrigatorias = (
        CAMPOS_PRODUTO.keys()
    )

    for coluna in colunas_obrigatorias:

        if coluna not in tabela.columns:

            raise ValueError(
                f"Coluna ausente: {coluna}"
            )

    return tabela