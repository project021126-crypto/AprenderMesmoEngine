from __future__ import annotations

import random

from manim import (
    BLACK,
    BLUE_E,
    Dot,
    FadeIn,
    LaggedStart,
    Rectangle,
    VGroup,
    WHITE,
    config,
)


class StarField(VGroup):
    """
    Campo estelar cinematográfico em múltiplas profundidades.

    Camadas:
    - fundo espacial;
    - estrelas distantes;
    - estrelas médias;
    - estrelas próximas.

    A separação por profundidade permite aplicar Parallax
    posteriormente sem reconstruir o campo estelar.
    """

    def __init__(
        self,
        *,
        seed: int = 42,
        quantidade_distantes: int = 150,
        quantidade_medias: int = 75,
        quantidade_proximas: int = 30,
        margem: float = 0.25,
        camada_azul: bool = True,
    ) -> None:
        super().__init__()

        self.seed = seed
        self.gerador = random.Random(seed)

        largura = float(config.frame_width)
        altura = float(config.frame_height)

        # ==================================================
        # FUNDO
        # ==================================================

        self.fundo = Rectangle(
            width=largura,
            height=altura,
            fill_color=BLACK,
            fill_opacity=1.0,
            stroke_opacity=0,
        )

        self.fundo.set_z_index(-1000)
        self.add(self.fundo)

        # ==================================================
        # CAMADA AZUL SUBTIL
        # ==================================================

        self.camada_azul = None

        if camada_azul:
            self.camada_azul = Rectangle(
                width=largura,
                height=altura,
                fill_color=BLUE_E,
                fill_opacity=0.055,
                stroke_opacity=0,
            )

            self.camada_azul.set_z_index(-999)
            self.add(self.camada_azul)

        # ==================================================
        # LIMITES
        # ==================================================

        limite_x = largura / 2 - margem
        limite_y = altura / 2 - margem

        # ==================================================
        # ESTRELAS DISTANTES
        # ==================================================

        self.distantes = self._criar_camada(
            quantidade=quantidade_distantes,
            limite_x=limite_x,
            limite_y=limite_y,
            raio_minimo=0.006,
            raio_maximo=0.015,
            opacidade_minima=0.20,
            opacidade_maxima=0.55,
            z_index=-980,
        )

        # ==================================================
        # ESTRELAS MÉDIAS
        # ==================================================

        self.medias = self._criar_camada(
            quantidade=quantidade_medias,
            limite_x=limite_x,
            limite_y=limite_y,
            raio_minimo=0.012,
            raio_maximo=0.026,
            opacidade_minima=0.40,
            opacidade_maxima=0.82,
            z_index=-970,
        )

        # ==================================================
        # ESTRELAS PRÓXIMAS
        # ==================================================

        self.proximas = self._criar_camada(
            quantidade=quantidade_proximas,
            limite_x=limite_x,
            limite_y=limite_y,
            raio_minimo=0.020,
            raio_maximo=0.042,
            opacidade_minima=0.65,
            opacidade_maxima=1.0,
            z_index=-960,
        )

        self.add(
            self.distantes,
            self.medias,
            self.proximas,
        )

    def _criar_camada(
        self,
        *,
        quantidade: int,
        limite_x: float,
        limite_y: float,
        raio_minimo: float,
        raio_maximo: float,
        opacidade_minima: float,
        opacidade_maxima: float,
        z_index: int,
    ) -> VGroup:
        camada = VGroup()

        for _ in range(quantidade):
            x = self.gerador.uniform(-limite_x, limite_x)
            y = self.gerador.uniform(-limite_y, limite_y)

            raio = self.gerador.uniform(
                raio_minimo,
                raio_maximo,
            )

            opacidade = self.gerador.uniform(
                opacidade_minima,
                opacidade_maxima,
            )

            estrela = Dot(
                point=[x, y, 0.0],
                radius=raio,
                color=WHITE,
            )

            estrela.set_opacity(opacidade)
            estrela.set_z_index(z_index)

            estrela.opacidade_base = opacidade

            camada.add(estrela)

        return camada


def animar_entrada_starfield(
    starfield: StarField,
    *,
    duracao: float = 1.8,
) -> LaggedStart:
    """
    Faz as estrelas aparecerem em profundidade.
    """

    if duracao <= 0:
        raise ValueError(
            "duracao tem de ser positiva."
        )

    animacoes = []

    for estrela in starfield.distantes:
        animacoes.append(
            FadeIn(estrela)
        )

    for estrela in starfield.medias:
        animacoes.append(
            FadeIn(estrela)
        )

    for estrela in starfield.proximas:
        animacoes.append(
            FadeIn(estrela)
        )

    return LaggedStart(
        *animacoes,
        lag_ratio=0.006,
        run_time=duracao,
    )