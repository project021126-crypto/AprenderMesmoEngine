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
    Halo solar cinematográfico suave.

    Em vez de anéis desenhados com contorno grosso,
    utiliza discos transparentes sobrepostos.

    Resultado:
    - brilho difuso;
    - transição gradual;
    - sem efeito de "donut";
    - continua visível como halo durante o eclipse.
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
            "draft": [
                (1.45, 0.045),
                (1.25, 0.070),
                (1.12, 0.110),
            ],
            "youtube": [
                (1.70, 0.025),
                (1.48, 0.040),
                (1.30, 0.060),
                (1.18, 0.090),
                (1.10, 0.130),
            ],
            "cinema": [
                (1.95, 0.018),
                (1.72, 0.026),
                (1.52, 0.038),
                (1.36, 0.052),
                (1.24, 0.070),
                (1.15, 0.095),
                (1.09, 0.135),
            ],
        }

        self.centro = centro
        self.raio_base = raio_base
        self.cor = cor
        self.intensidade = intensidade
        self.qualidade = qualidade

        self.camadas = VGroup()

        for indice, (
            multiplicador,
            opacidade,
        ) in enumerate(
            configuracoes[qualidade]
        ):
            camada = Circle(
                radius=raio_base * multiplicador,
                fill_color=cor,
                fill_opacity=min(
                    0.40,
                    opacidade * intensidade,
                ),
                stroke_opacity=0,
            ).move_to(centro)

            camada.set_z_index(
                -30 + indice
            )

            self.camadas.add(camada)

        # Linha luminosa extremamente fina junto ao Sol.
        # Durante o eclipse ajuda a criar a borda da coroa.
        self.borda_luminosa = Circle(
            radius=raio_base * 1.045,
            fill_opacity=0,
            stroke_color=WHITE,
            stroke_opacity=min(
                0.32,
                0.22 * intensidade,
            ),
            stroke_width=1.5,
        ).move_to(centro)

        self.borda_luminosa.set_z_index(-15)

        self.add(
            self.camadas,
            self.borda_luminosa,
        )


def animar_pulsacao_glow(
    glow: SolarGlow,
    *,
    intensidade: float = 1.018,
    duracao: float = 1.2,
):
    """
    Respiração luminosa muito subtil.
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
    escala: float = 1.08,
    duracao: float = 1.8,
):
    """
    Expansão luminosa controlada.
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