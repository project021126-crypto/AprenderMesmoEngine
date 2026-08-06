from __future__ import annotations

from manim import (
    FadeIn,
    FadeOut,
    Transform,
    VGroup,
    Write,
    YELLOW,
)

from engine.biblioteca.astronomia.eclipse import (
    criar_eclipse_frontal,
)
from engine.biblioteca.astronomia.fundos import (
    criar_fundo_espaco_profundo,
)
from engine.biblioteca.astronomia.textos import (
    criar_pergunta_central,
)


def executar_cena_01(cena) -> None:
    """
    Cena 01 — Introdução cinematográfica.

    Mostra:
    - o Sol inicialmente descoberto;
    - a Lua a avançar progressivamente;
    - o eclipse total;
    - a pergunta principal do episódio.
    """

    # ======================================================
    # FUNDO
    # ======================================================

    fundo = criar_fundo_espaco_profundo(
        quantidade_estrelas=150,
        seed=101,
    )

    cena.add(fundo)

    # ======================================================
    # ESTADO INICIAL — SOL DESCOBERTO
    # ======================================================

    eclipse = criar_eclipse_frontal(
        raio_sol=1.20,
        cobertura=0.0,
        qualidade="youtube",
    )

    cena.narrar(
        (
            "Imagina que estás ao ar livre, em pleno meio-dia. "
            "O céu está limpo e o Sol brilha com toda a força."
        ),
        FadeIn(eclipse),
    )

    # ======================================================
    # A LUA COMEÇA A COBRIR O SOL
    # ======================================================

    eclipse_inicio = criar_eclipse_frontal(
        raio_sol=1.20,
        cobertura=0.28,
        qualidade="youtube",
    )

    cena.narrar(
        (
            "Mas, sem aviso, uma sombra começa lentamente "
            "a atravessar o disco solar."
        ),
        Transform(
            eclipse,
            eclipse_inicio,
        ),
    )

    # ======================================================
    # ECLIPSE PARCIAL
    # ======================================================

    eclipse_parcial = criar_eclipse_frontal(
        raio_sol=1.20,
        cobertura=0.62,
        qualidade="youtube",
    )

    cena.narrar(
        (
            "A luz muda. A temperatura começa a descer. "
            "E os pássaros ficam estranhamente silenciosos."
        ),
        Transform(
            eclipse,
            eclipse_parcial,
        ),
    )

    # ======================================================
    # ECLIPSE TOTAL
    # ======================================================

    eclipse_total = criar_eclipse_frontal(
        raio_sol=1.20,
        cobertura=1.0,
        qualidade="youtube",
    )

    cena.narrar(
        (
            "Poucos minutos depois, parece que a noite "
            "chegou no meio do dia."
        ),
        Transform(
            eclipse,
            eclipse_total,
        ),
    )

    # ======================================================
    # PERGUNTA PRINCIPAL
    # ======================================================

    pergunta = criar_pergunta_central(
        "COMO É QUE ISTO É POSSÍVEL?",
        cor=YELLOW,
        tamanho=50,
    )

    cena.play(
        FadeIn(pergunta[0]),
        Write(pergunta[1]),
        run_time=0.9,
    )

    cena.wait(0.9)

    cena.narrar(
        (
            "Para perceber um eclipse, temos de começar "
            "por três astros: o Sol, a Lua e a Terra."
        ),
        mostrar_legenda=True,
    )

    # ======================================================
    # LIMPEZA PARA A CENA 2
    # ======================================================

    cena.play(
        FadeOut(
            VGroup(
                pergunta,
                eclipse,
                fundo,
            )
        ),
        run_time=0.8,
    )