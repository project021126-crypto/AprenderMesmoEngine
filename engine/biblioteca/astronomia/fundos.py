from __future__ import annotations

import random

from manim import (
    BLACK,
    BLUE_E,
    Dot,
    Rectangle,
    VGroup,
    WHITE,
    config,
)


def criar_fundo_espaco(
    *,
    quantidade_estrelas: int = 120,
    seed: int = 42,
    cor_fundo=BLACK,
    opacidade_minima: float = 0.22,
    opacidade_maxima: float = 0.85,
    raio_minimo: float = 0.010,
    raio_maximo: float = 0.028,
    margem: float = 0.20,
) -> VGroup:
    """
    Cria um fundo espacial reutilizável.

    O fundo adapta-se automaticamente ao formato atual:
    - Short 9:16
    - Long 16:9

    A utilização de uma seed fixa garante que as estrelas
    aparecem sempre nas mesmas posições entre renderizações.
    """

    if quantidade_estrelas < 0:
        raise ValueError(
            "quantidade_estrelas não pode ser negativa."
        )

    if raio_minimo <= 0 or raio_maximo <= 0:
        raise ValueError(
            "Os raios das estrelas têm de ser positivos."
        )

    if raio_minimo > raio_maximo:
        raise ValueError(
            "raio_minimo não pode ser superior a raio_maximo."
        )

    if not 0 <= opacidade_minima <= 1:
        raise ValueError(
            "opacidade_minima deve estar entre 0 e 1."
        )

    if not 0 <= opacidade_maxima <= 1:
        raise ValueError(
            "opacidade_maxima deve estar entre 0 e 1."
        )

    if opacidade_minima > opacidade_maxima:
        raise ValueError(
            "opacidade_minima não pode ser superior "
            "a opacidade_maxima."
        )

    gerador = random.Random(seed)

    largura = config.frame_width
    altura = config.frame_height

    fundo = Rectangle(
        width=largura,
        height=altura,
        fill_color=cor_fundo,
        fill_opacity=1.0,
        stroke_opacity=0,
    )

    fundo.set_z_index(-1000)

    estrelas = VGroup()

    limite_x = largura / 2 - margem
    limite_y = altura / 2 - margem

    for _ in range(quantidade_estrelas):
        x = gerador.uniform(-limite_x, limite_x)
        y = gerador.uniform(-limite_y, limite_y)

        raio = gerador.uniform(
            raio_minimo,
            raio_maximo,
        )

        opacidade = gerador.uniform(
            opacidade_minima,
            opacidade_maxima,
        )

        estrela = Dot(
            point=[x, y, 0],
            radius=raio,
            color=WHITE,
        ).set_opacity(opacidade)

        estrela.set_z_index(-990)
        estrelas.add(estrela)

    return VGroup(
        fundo,
        estrelas,
    )


def criar_fundo_espaco_profundo(
    *,
    quantidade_estrelas: int = 150,
    seed: int = 84,
) -> VGroup:
    """
    Variante com uma ligeira camada azul escura,
    adequada para cenas mais cinematográficas.
    """

    base = criar_fundo_espaco(
        quantidade_estrelas=quantidade_estrelas,
        seed=seed,
        cor_fundo=BLACK,
        opacidade_minima=0.18,
        opacidade_maxima=0.78,
        raio_minimo=0.009,
        raio_maximo=0.030,
    )

    camada_azul = Rectangle(
        width=config.frame_width,
        height=config.frame_height,
        fill_color=BLUE_E,
        fill_opacity=0.08,
        stroke_opacity=0,
    )

    camada_azul.set_z_index(-995)

    fundo = base[0]
    estrelas = base[1]

    return VGroup(
        fundo,
        camada_azul,
        estrelas,
    )