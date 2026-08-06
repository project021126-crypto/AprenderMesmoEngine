from __future__ import annotations

from typing import Literal

from manim import (
    ORIGIN,
    YELLOW,
    Circle,
    VGroup,
)

from engine.biblioteca.astronomia.efeitos import (
    criar_coroa,
    criar_halo,
)


QualidadeSol = Literal[
    "draft",
    "youtube",
    "cinema",
]


def criar_sol(
    *,
    raio: float = 1.0,
    posicao=ORIGIN,
    qualidade: QualidadeSol = "youtube",
    cor=YELLOW,
    mostrar_halo: bool = True,
    mostrar_coroa: bool = True,
    intensidade: float = 1.0,
) -> VGroup:
    """
    Cria um Sol reutilizável para vídeos do Aprender Mesmo.

    Parâmetros principais:
    - raio: tamanho do Sol;
    - posicao: posição no ecrã;
    - qualidade: draft, youtube ou cinema;
    - mostrar_halo: ativa o brilho exterior;
    - mostrar_coroa: ativa os raios e a coroa;
    - intensidade: força visual dos efeitos.

    O componente adapta automaticamente o número e a força
    dos efeitos ao nível de qualidade escolhido.
    """

    if raio <= 0:
        raise ValueError(
            "O raio do Sol tem de ser positivo."
        )

    if intensidade <= 0:
        raise ValueError(
            "A intensidade tem de ser positiva."
        )

    if qualidade not in {
        "draft",
        "youtube",
        "cinema",
    }:
        raise ValueError(
            "qualidade deve ser 'draft', 'youtube' ou 'cinema'."
        )

    configuracoes = {
        "draft": {
            "quantidade_halo": 2,
            "espacamento_halo": raio * 0.10,
            "opacidade_halo": 0.36,
            "espessura_halo": 2.6,
            "mostrar_coroa_real": False,
        },
        "youtube": {
            "quantidade_halo": 5,
            "espacamento_halo": raio * 0.10,
            "opacidade_halo": 0.62,
            "espessura_halo": 4.2,
            "mostrar_coroa_real": True,
        },
        "cinema": {
            "quantidade_halo": 8,
            "espacamento_halo": raio * 0.085,
            "opacidade_halo": 0.78,
            "espessura_halo": 5.2,
            "mostrar_coroa_real": True,
        },
    }

    configuracao = configuracoes[qualidade]

    nucleo = Circle(
        radius=raio,
        color=cor,
        fill_color=cor,
        fill_opacity=1.0,
        stroke_color=cor,
        stroke_width=3.0,
    ).move_to(posicao)

    camadas = VGroup()

    if mostrar_halo:
        halo = criar_halo(
            centro=posicao,
            raio_base=raio,
            quantidade=configuracao[
                "quantidade_halo"
            ],
            espacamento=configuracao[
                "espacamento_halo"
            ],
            cor=cor,
            opacidade_inicial=min(
                1.0,
                configuracao[
                    "opacidade_halo"
                ]
                * intensidade,
            ),
            queda_opacidade=0.09,
            espessura_inicial=configuracao[
                "espessura_halo"
            ],
            queda_espessura=0.45,
        )

        camadas.add(halo)

    if (
        mostrar_coroa
        and configuracao["mostrar_coroa_real"]
    ):
        coroa = criar_coroa(
            centro=posicao,
            raio=raio,
            cor=cor,
            intensidade=intensidade,
        )

        camadas.add(coroa)

    camadas.add(nucleo)

    sol = VGroup(*camadas)
    sol.move_to(posicao)

    return sol