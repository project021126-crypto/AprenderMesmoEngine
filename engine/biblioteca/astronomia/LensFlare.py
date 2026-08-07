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
    Lens flare cinematográfico reutilizável.

    Não tenta imitar fotografia real de forma literal.
    Cria uma assinatura visual elegante para:
    - Sol;
    - estrelas;
    - eclipses;
    - fontes intensas de luz.

    Componentes:
    - núcleo luminoso;
    - anéis suaves;
    - raios horizontais/verticais;
    - reflexos secundários.
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

        if qualidade not in {
            "draft",
            "youtube",
            "cinema",
        }:
            raise ValueError(
                "qualidade deve ser "
                "'draft', 'youtube' ou 'cinema'."
            )

        configuracoes = {
            "draft": {
                "aneis": 2,
                "reflexos": 1,
            },
            "youtube": {
                "aneis": 4,
                "reflexos": 3,
            },
            "cinema": {
                "aneis": 6,
                "reflexos": 5,
            },
        }

        cfg = configuracoes[qualidade]

        self.centro = centro
        self.raio_base = raio_base
        self.cor = cor
        self.intensidade = intensidade
        self.qualidade = qualidade

        # ==================================================
        # NÚCLEO
        # ==================================================

        nucleo = Circle(
            radius=raio_base * 0.08,
            fill_color=WHITE,
            fill_opacity=min(
                1.0,
                0.85 * intensidade,
            ),
            stroke_opacity=0,
        ).move_to(centro)

        nucleo.set_z_index(100)

        # ==================================================
        # ANÉIS
        # ==================================================

        aneis = VGroup()

        for indice in range(cfg["aneis"]):

            raio = raio_base * (
                0.18 + indice * 0.11
            )

            opacidade = max(
                0.03,
                0.26
                - indice * 0.035,
            ) * intensidade

            anel = Circle(
                radius=raio,
                stroke_color=cor,
                stroke_opacity=min(
                    1.0,
                    opacidade,
                ),
                stroke_width=max(
                    1.0,
                    3.0 - indice * 0.25,
                ),
            ).move_to(centro)

            anel.set_z_index(90 - indice)

            aneis.add(anel)

        # ==================================================
        # RAIOS PRINCIPAIS
        # ==================================================

        comprimento_horizontal = (
            raio_base * 2.8
        )

        comprimento_vertical = (
            raio_base * 1.8
        )

        raio_horizontal = Line(
            start=[
                centro[0]
                - comprimento_horizontal,
                centro[1],
                0,
            ],
            end=[
                centro[0]
                + comprimento_horizontal,
                centro[1],
                0,
            ],
            color=cor,
            stroke_opacity=min(
                1.0,
                0.24 * intensidade,
            ),
            stroke_width=2.0,
        )

        raio_vertical = Line(
            start=[
                centro[0],
                centro[1]
                - comprimento_vertical,
                0,
            ],
            end=[
                centro[0],
                centro[1]
                + comprimento_vertical,
                0,
            ],
            color=cor,
            stroke_opacity=min(
                1.0,
                0.14 * intensidade,
            ),
            stroke_width=1.4,
        )

        raio_horizontal.set_z_index(80)
        raio_vertical.set_z_index(80)

        # ==================================================
        # REFLEXOS SECUNDÁRIOS
        # ==================================================

        reflexos = VGroup()

        for indice in range(
            cfg["reflexos"]
        ):

            distancia = (
                raio_base
                * (0.80 + indice * 0.52)
            )

            lado = (
                -1
                if indice % 2 == 0
                else 1
            )

            posicao_reflexo = [
                centro[0]
                + distancia * lado,
                centro[1]
                + raio_base
                * 0.07
                * (indice - 1),
                0,
            ]

            reflexo = Circle(
                radius=raio_base
                * (
                    0.055
                    + 0.012 * indice
                ),
                fill_color=cor,
                fill_opacity=max(
                    0.035,
                    (
                        0.17
                        - indice * 0.022
                    )
                    * intensidade,
                ),
                stroke_color=WHITE,
                stroke_opacity=max(
                    0.02,
                    0.10
                    - indice * 0.012,
                ),
                stroke_width=1.0,
            ).move_to(
                posicao_reflexo
            )

            reflexo.set_z_index(
                70 - indice
            )

            reflexos.add(
                reflexo
            )

        self.add(
            reflexos,
            raio_horizontal,
            raio_vertical,
            aneis,
            nucleo,
        )


def animar_entrada_flare(
    flare: LensFlare,
    *,
    escala_inicial: float = 0.35,
    duracao: float = 1.4,
):
    """
    Entrada progressiva do lens flare.
    """

    if escala_inicial <= 0:
        raise ValueError(
            "escala_inicial tem de ser positiva."
        )

    if duracao <= 0:
        raise ValueError(
            "duracao tem de ser positiva."
        )

    flare.scale(
        escala_inicial
    )

    fator = (
        1.0
        / escala_inicial
    )

    return flare.animate.scale(
        fator
    ).set_run_time(
        duracao
    )


def animar_respiracao_flare(
    flare: LensFlare,
    *,
    escala: float = 1.035,
    duracao: float = 1.2,
):
    """
    Pequena expansão luminosa.

    Deve ser usada de forma subtil.
    """

    if escala <= 1.0:
        raise ValueError(
            "escala deve ser superior a 1."
        )

    if duracao <= 0:
        raise ValueError(
            "duracao tem de ser positiva."
        )

    return flare.animate.scale(
        escala
    ).set_run_time(
        duracao
    )