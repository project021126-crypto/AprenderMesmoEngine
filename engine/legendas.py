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
    margem_inferior: float = 0.32,
    margem_horizontal: float = 0.28,
    margem_vertical: float = 0.20,
) -> VGroup:
    """
    Cria uma legenda adaptada automaticamente ao formato
    Short 9:16 ou Long 16:9.
    """

    texto = texto.strip()

    if not texto:
        raise ValueError("O texto da legenda não pode estar vazio.")

    largura_maxima = config.frame_width - 0.75

    legenda = Text(
        texto,
        font_size=tamanho_fonte,
        color=WHITE,
        line_spacing=0.9,
    )

    if legenda.width > largura_maxima:
        legenda.scale_to_fit_width(largura_maxima)

    fundo = RoundedRectangle(
        width=legenda.width + margem_horizontal * 2,
        height=legenda.height + margem_vertical * 2,
        corner_radius=0.14,
        fill_color=BLACK,
        fill_opacity=0.76,
        stroke_opacity=0,
    )

    grupo = VGroup(fundo, legenda)
    legenda.move_to(fundo.get_center())

    grupo.to_edge(DOWN, buff=margem_inferior)
    grupo.set_z_index(100)

    return grupo