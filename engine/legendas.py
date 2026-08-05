from __future__ import annotations

from manim import (
    BLACK,
    DOWN,
    RoundedRectangle,
    Text,
    VGroup,
    WHITE,
    config,
)


def criar_legenda(
    texto: str,
    tamanho_fonte: int = 34,
    margem_inferior: float = 0.42,
    margem_horizontal: float = 0.30,
    margem_vertical: float = 0.22,
) -> VGroup:
    """
    Cria uma legenda forte e legível para Short e Long.

    - texto branco intenso;
    - fundo preto mais opaco;
    - largura segura;
    - posição acima dos controlos das plataformas.
    """

    texto = texto.strip()

    if not texto:
        raise ValueError("O texto da legenda não pode estar vazio.")

    largura_maxima = config.frame_width - 0.95

    legenda = Text(
        texto,
        font_size=tamanho_fonte,
        color=WHITE,
        line_spacing=0.92,
        weight="BOLD",
    )

    if legenda.width > largura_maxima:
        legenda.scale_to_fit_width(largura_maxima)

    fundo = RoundedRectangle(
        width=legenda.width + margem_horizontal * 2,
        height=legenda.height + margem_vertical * 2,
        corner_radius=0.14,
        fill_color=BLACK,
        fill_opacity=0.92,
        stroke_color=WHITE,
        stroke_opacity=0.15,
        stroke_width=1,
    )

    grupo = VGroup(fundo, legenda)

    legenda.move_to(fundo.get_center())

    grupo.to_edge(
        DOWN,
        buff=margem_inferior,
    )

    grupo.set_z_index(1000)

    return grupo