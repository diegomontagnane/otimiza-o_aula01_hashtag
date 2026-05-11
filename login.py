from config import URL_LOGIN


def fazer_login(page, email, senha):
    """
    Realiza login no sistema.
    """

    page.goto(
        URL_LOGIN,
        wait_until="domcontentloaded"
    )

    page.fill(
        "#email",
        email
    )

    page.fill(
        "#password",
        senha
    )

    page.click(
        "button"
    )

    page.wait_for_load_state(
        "domcontentloaded"
    )