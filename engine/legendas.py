from __future__ import annotations

from manim import (
    BLACK,
    DOWN,
    RoundedRectangle,
    Text,
    VGroup,
    WHITE,
)


def criar_legenda(
    texto: str,
    largura_maxima: float = 11.5,
    tamanho_fonte: int = 34,
    margem_horizontal: float = 0.35,
    margem_vertical: float = 0.22,
) -> VGroup:
    """
    Cria uma legenda centralizada na parte inferior do vídeo.

    A legenda inclui:
    - texto branco;
    - fundo preto semitransparente;
    - cantos arredondados;
    - largura máxima controlada.
    """

    texto = texto.strip()

    if not texto:
        raise ValueError("O texto da legenda não pode estar vazio.")

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
        corner_radius=0.16,
        fill_color=BLACK,
        fill_opacity=0.72,
        stroke_opacity=0,
    )

    grupo = VGroup(fundo, legenda)
    legenda.move_to(fundo.get_center())

    grupo.to_edge(DOWN, buff=0.28)
    grupo.set_z_index(100)

    return grupo