import pandas as pd

from config import CAMPOS_PRODUTO


def preencher_campo(page, seletor, valor):
    """
    Preenche um campo do formulário.
    """

    if pd.isna(valor):
        valor = ""

    page.fill(
        seletor,
        str(valor)
    )


def cadastrar_produto(page, produto):
    """
    Realiza o cadastro de um único produto.
    """

    for campo, seletor in CAMPOS_PRODUTO.items():

        valor = produto[campo]

        preencher_campo(
            page,
            seletor,
            valor
        )

    page.click(
        "button[type='submit']"
    )


def cadastrar_produtos(page, tabela):
    """
    Percorre toda a tabela e cadastra os produtos.
    """

    for indice, produto in tabela.iterrows():

        try:

            cadastrar_produto(
                page,
                produto
            )

            print(
                f"Produto {indice + 1} cadastrado: "
                f"{produto['codigo']}"
            )

        except Exception as erro:

            print(
                f"Erro ao cadastrar produto "
                f"{produto['codigo']}: {erro}"
            )