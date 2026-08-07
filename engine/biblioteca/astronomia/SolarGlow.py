from __future__ import annotations

from manim import (
    Circle,
    VGroup,
    YELLOW,
    ORIGIN,
)


class SolarGlow(VGroup):
    """
    Glow solar multicamada reutilizável.

    Serve para:
    - Sol;
    - estrelas;
    - eclipse;
    - fontes intensas de luz;
    - cenas cinematográficas.

    O glow é composto por várias camadas com
    raios, opacidades e espessuras diferentes.
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
                "camadas": 3,
                "expansao": 0.10,
                "opacidade": 0.24,
                "queda": 0.07,
                "espessura": 4.0,
            },
            "youtube": {
                "camadas": 6,
                "expansao": 0.085,
                "opacidade": 0.34,
                "queda": 0.045,
                "espessura": 5.0,
            },
            "cinema": {
                "camadas": 10,
                "expansao": 0.065,
                "opacidade": 0.42,
                "queda": 0.032,
                "espessura": 6.0,
            },
        }

        cfg = configuracoes[qualidade]

        self.centro = centro
        self.raio_base = raio_base
        self.cor = cor
        self.intensidade = intensidade
        self.qualidade = qualidade

        self.camadas = VGroup()

        for indice in range(cfg["camadas"]):

            raio = (
                raio_base
                + raio_base
                * cfg["expansao"]
                * (indice + 1)
            )

            opacidade = max(
                0.025,
                (
                    cfg["opacidade"]
                    - cfg["queda"] * indice
                )
                * intensidade,
            )

            espessura = max(
                1.0,
                cfg["espessura"] - indice * 0.38,
            )

            camada = Circle(
                radius=raio,
                stroke_color=cor,
                stroke_opacity=min(
                    1.0,
                    opacidade,
                ),
                stroke_width=espessura,
            ).move_to(centro)

            camada.set_z_index(-15 + indice)

            self.camadas.add(camada)

        self.add(self.camadas)


def animar_pulsacao_glow(
    glow: SolarGlow,
    *,
    intensidade: float = 1.025,
    duracao: float = 1.4,
):
    """
    Pulso subtil do glow.

    Mantém o efeito elegante:
    não é uma expansão exagerada,
    apenas uma respiração luminosa.
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
    escala: float = 1.12,
    duracao: float = 2.0,
):
    """
    Expansão mais dramática.

    Útil para:
    - aproximação ao Sol;
    - eclipse;
    - revelação;
    - transições.
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