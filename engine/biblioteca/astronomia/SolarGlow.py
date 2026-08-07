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
    Glow solar discreto e cinematográfico.

    Objetivo:
    - iluminar subtilmente o Sol;
    - não aumentar visualmente demasiado o seu tamanho;
    - evitar anéis visíveis;
    - desaparecer quase por completo no eclipse total.
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
            "draft": 5,
            "youtube": 8,
            "cinema": 12,
        }[qualidade]

        self.centro = centro
        self.raio_base = raio_base
        self.cor = cor
        self.intensidade = intensidade
        self.qualidade = qualidade

        self.camadas = VGroup()

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

            # Antes chegava perto de 1.88x o raio.
            # Agora o glow termina apenas ~30% fora do Sol.
            multiplicador = (
                1.025
                + progresso * 0.30
            )

            # Muito menos luminosidade.
            opacidade = (
                0.018
                * (1.0 - progresso) ** 2.2
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
                -40 + indice
            )

            self.camadas.add(
                camada
            )

        # Borda mínima junto ao disco.
        self.borda_luminosa = Circle(
            radius=raio_base * 1.012,
            fill_opacity=0,
            stroke_color=WHITE,
            stroke_opacity=min(
                0.10,
                0.07 * intensidade,
            ),
            stroke_width=0.7,
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
    intensidade: float = 1.006,
    duracao: float = 1.2,
):
    """
    Pulsação quase impercetível.
    """

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
    escala: float = 1.025,
    duracao: float = 1.8,
):
    """
    Expansão muito subtil.
    """

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