from __future__ import annotations

from manim import (
    Circle,
    ORIGIN,
    VGroup,
    WHITE,
    YELLOW,
)


class SolarGlow(VGroup):
    """
    Halo solar cinematográfico multicamada.

    Construído com muitas camadas extremamente suaves
    para evitar círculos/anéis claramente visíveis.
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
                "qualidade inválida."
            )

        quantidade_camadas = {
            "draft": 8,
            "youtube": 14,
            "cinema": 22,
        }[qualidade]

        self.centro = centro
        self.raio_base = raio_base
        self.cor = cor
        self.intensidade = intensidade
        self.qualidade = qualidade

        self.camadas = VGroup()

        # ==================================================
        # GLOW DIFUSO
        # ==================================================

        for indice in range(
            quantidade_camadas
        ):

            progresso = (
                indice
                / max(
                    1,
                    quantidade_camadas - 1,
                )
            )

            # Camadas cada vez maiores.
            multiplicador = (
                1.06
                + progresso * 0.82
            )

            # Muito transparente.
            # Quanto mais longe do Sol, menor a intensidade.
            opacidade = (
                0.040
                * (1.0 - progresso) ** 2
                * intensidade
            )

            camada = Circle(
                radius=(
                    raio_base
                    * multiplicador
                ),
                fill_color=cor,
                fill_opacity=opacidade,
                stroke_opacity=0,
            ).move_to(
                centro
            )

            camada.set_z_index(
                -50 + indice
            )

            self.camadas.add(
                camada
            )

        # ==================================================
        # BORDA LUMINOSA MUITO FINA
        # ==================================================

        self.borda_luminosa = Circle(
            radius=raio_base * 1.025,
            fill_opacity=0,
            stroke_color=WHITE,
            stroke_opacity=min(
                0.24,
                0.18 * intensidade,
            ),
            stroke_width=1.15,
        ).move_to(
            centro
        )

        self.borda_luminosa.set_z_index(
            -20
        )

        self.add(
            self.camadas,
            self.borda_luminosa,
        )


def animar_pulsacao_glow(
    glow: SolarGlow,
    *,
    intensidade: float = 1.012,
    duracao: float = 1.2,
):

    if intensidade <= 1.0:
        raise ValueError(
            "intensidade deve ser superior a 1."
        )

    if duracao <= 0:
        raise ValueError(
            "duracao tem de ser positiva."
        )

    return glow.animate.scale(
        intensidade
    ).set_run_time(
        duracao
    )


def animar_expansao_glow(
    glow: SolarGlow,
    *,
    escala: float = 1.06,
    duracao: float = 1.8,
):

    if escala <= 1.0:
        raise ValueError(
            "escala deve ser superior a 1."
        )

    if duracao <= 0:
        raise ValueError(
            "duracao tem de ser positiva."
        )

    return glow.animate.scale(
        escala
    ).set_run_time(
        duracao
    )