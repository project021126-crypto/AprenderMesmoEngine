from __future__ import annotations

from manim import (
    Circle,
    Line,
    ORIGIN,
    VGroup,
    WHITE,
    YELLOW,
)


class LensFlare(VGroup):
    """
    Lens flare cinematográfico subtil.

    Não deve parecer um objeto desenhado.
    Deve ser quase impercetível e apenas sugerir
    uma fonte luminosa intensa.
    """

    def __init__(
        self,
        *,
        centro=ORIGIN,
        raio_base: float = 1.0,
        cor=YELLOW,
        intensidade: float = 1.0,
        qualidade: str = "cinema",
    ) -> None:
        super().__init__()

        if raio_base <= 0:
            raise ValueError(
                "raio_base tem de ser positivo."
            )

        if intensidade <= 0:
            raise ValueError(
                "intensidade tem de ser positiva."
            )

        self.centro = centro
        self.raio_base = raio_base
        self.intensidade = intensidade

        # ==================================================
        # CENTRO LUMINOSO
        # ==================================================

        nucleo = Circle(
            radius=raio_base * 0.055,
            fill_color=WHITE,
            fill_opacity=min(
                0.45,
                0.24 * intensidade,
            ),
            stroke_opacity=0,
        ).move_to(centro)

        # ==================================================
        # RAIOS MUITO SUBTIS
        # ==================================================

        horizontal = Line(
            start=[
                centro[0] - raio_base * 2.1,
                centro[1],
                0,
            ],
            end=[
                centro[0] + raio_base * 2.1,
                centro[1],
                0,
            ],
            color=cor,
            stroke_opacity=min(
                0.12,
                0.075 * intensidade,
            ),
            stroke_width=1.2,
        )

        vertical = Line(
            start=[
                centro[0],
                centro[1] - raio_base * 1.25,
                0,
            ],
            end=[
                centro[0],
                centro[1] + raio_base * 1.25,
                0,
            ],
            color=WHITE,
            stroke_opacity=min(
                0.08,
                0.045 * intensidade,
            ),
            stroke_width=0.9,
        )

        # ==================================================
        # REFLEXOS ÓTICOS QUASE INVISÍVEIS
        # ==================================================

        reflexos = VGroup()

        dados_reflexos = [
            (-1.35, 0.035, 0.045),
            (-0.72, 0.025, 0.035),
            (0.88, 0.030, 0.040),
            (1.55, 0.020, 0.055),
        ]

        for (
            distancia,
            opacidade,
            tamanho,
        ) in dados_reflexos:

            reflexo = Circle(
                radius=raio_base * tamanho,
                fill_color=cor,
                fill_opacity=min(
                    0.08,
                    opacidade * intensidade,
                ),
                stroke_opacity=0,
            )

            reflexo.move_to(
                [
                    centro[0]
                    + raio_base * distancia,
                    centro[1],
                    0,
                ]
            )

            reflexos.add(reflexo)

        self.add(
            reflexos,
            horizontal,
            vertical,
            nucleo,
        )


def animar_entrada_flare(
    flare: LensFlare,
    *,
    escala_inicial: float = 0.65,
    duracao: float = 1.0,
):
    if escala_inicial <= 0:
        raise ValueError(
            "escala_inicial tem de ser positiva."
        )

    flare.scale(escala_inicial)

    return flare.animate.scale(
        1 / escala_inicial
    ).set_run_time(
        duracao
    )


def animar_respiracao_flare(
    flare: LensFlare,
    *,
    escala: float = 1.015,
    duracao: float = 1.0,
):
    if escala <= 1:
        raise ValueError(
            "escala deve ser superior a 1."
        )

    return flare.animate.scale(
        escala
    ).set_run_time(
        duracao
    )