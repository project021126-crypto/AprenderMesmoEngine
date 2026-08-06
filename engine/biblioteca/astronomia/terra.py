from __future__ import annotations

from typing import Literal

from manim import (
    Circle,
    VGroup,
    Text,
    ORIGIN,
)

from engine.config import (
    COR_TERRA,
)

from engine.biblioteca.astronomia.efeitos import (
    criar_halo,
)

QualidadeTerra = Literal[
    "draft",
    "youtube",
    "cinema",
]


def criar_terra(
    *,
    raio: float = 0.55,
    posicao=ORIGIN,
    qualidade: QualidadeTerra = "youtube",
    mostrar_atmosfera: bool = True,
    mostrar_label: bool = False,
) -> VGroup:
    """
    Terra reutilizável do Aprender Mesmo Engine.
    """

    grupo = VGroup()

    planeta = Circle(
        radius=raio,
        fill_color=COR_TERRA,
        fill_opacity=1,
        stroke_color=COR_TERRA,
        stroke_width=2,
    )

    grupo.add(planeta)

    if mostrar_atmosfera:

        atmosfera = criar_halo(
            centro=ORIGIN,
            raio_base=raio,
            quantidade={
                "draft": 2,
                "youtube": 4,
                "cinema": 6,
            }[qualidade],
            espacamento=0.035,
            cor=COR_TERRA,
            opacidade_inicial=0.22,
        )

        grupo.add(atmosfera)

    if mostrar_label:

        label = Text(
            "TERRA",
            font_size=30,
            weight="BOLD",
            color=COR_TERRA,
        )

        label.next_to(planeta, DOWN)

        grupo.add(label)

    grupo.move_to(posicao)

    return grupo