from __future__ import annotations

from typing import Literal

from manim import (
    Circle,
    Dot,
    Text,
    VGroup,
    ORIGIN,
)

from engine.config import (
    COR_LUA,
)

from engine.biblioteca.astronomia.efeitos import (
    criar_halo,
)

QualidadeLua = Literal[
    "draft",
    "youtube",
    "cinema",
]


def criar_lua(
    *,
    raio: float = 0.35,
    posicao=ORIGIN,
    qualidade: QualidadeLua = "youtube",
    mostrar_halo: bool = False,
    mostrar_crateras: bool = True,
    mostrar_label: bool = False,
) -> VGroup:

    lua = Circle(
        radius=raio,
        fill_color=COR_LUA,
        fill_opacity=1,
        stroke_color=COR_LUA,
        stroke_width=2,
    )

    grupo = VGroup()

    if mostrar_halo:

        grupo.add(

            criar_halo(
                centro=ORIGIN,
                raio_base=raio,
                quantidade=3,
                espacamento=0.05,
                cor=COR_LUA,
                opacidade_inicial=0.25,
            )

        )

    grupo.add(lua)

    if mostrar_crateras:

        escala = {
            "draft": 2,
            "youtube": 4,
            "cinema": 7,
        }[qualidade]

        for i in range(escala):

            cratera = Dot(
                radius=raio * 0.10,
                color="#C7C7C7",
            )

            if i == 0:
                cratera.move_to(
                    [-raio*0.25, raio*0.18, 0]
                )

            elif i == 1:
                cratera.move_to(
                    [raio*0.18, -raio*0.12, 0]
                )

            elif i == 2:
                cratera.move_to(
                    [0, raio*0.28, 0]
                )

            elif i == 3:
                cratera.move_to(
                    [-raio*0.08, -raio*0.28, 0]
                )

            elif i == 4:
                cratera.move_to(
                    [raio*0.28, raio*0.22, 0]
                )

            elif i == 5:
                cratera.move_to(
                    [-raio*0.30, -raio*0.02, 0]
                )

            else:
                cratera.move_to(
                    [raio*0.10, raio*0.05, 0]
                )

            grupo.add(cratera)

    if mostrar_label:

        label = Text(
            "LUA",
            font_size=28,
            weight="BOLD",
        )

        label.next_to(lua, UP)

        grupo.add(label)

    grupo.move_to(posicao)

    return grupo