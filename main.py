from playwright.sync_api import sync_playwright

from utils import carregar_credenciais, carregar_produtos
from login import fazer_login
from automacao import cadastrar_produtos


def main():
    """
    Função principal que organiza o fluxo da automação.
    """

    email, senha = carregar_credenciais()
    tabela = carregar_produtos()

    with sync_playwright() as playwright:
        navegador = playwright.chromium.launch(
            headless=False
        )

        page = navegador.new_page()

        fazer_login(
            page,
            email,
            senha
        )

        cadastrar_produtos(
            page,
            tabela
        )

        navegador.close()

    print("Automação finalizada com sucesso.")


if __name__ == "__main__":
    main()