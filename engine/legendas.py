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
    margem_inferior: float = 0.58,
    margem_horizontal: float = 0.30,
    margem_vertical: float = 0.24,
) -> VGroup:
    """
    Cria uma legenda intensa, nítida e segura para Short e Long.

    A posição e a largura são calculadas a partir do enquadramento
    real da câmara, evitando texto cortado ou escondido pelos
    controlos das plataformas.
    """

    texto = texto.strip()

    if not texto:
        raise ValueError("O texto da legenda não pode estar vazio.")

    largura_maxima = config.frame_width - 0.65

    legenda = Text(
        texto,
        font_size=tamanho_fonte,
        color=WHITE,
        weight="BOLD",
        line_spacing=0.94,
        fill_opacity=1.0,
        stroke_color=BLACK,
        stroke_width=0.8,
        stroke_opacity=0.95,
    )

    if legenda.width > largura_maxima:
        legenda.scale_to_fit_width(largura_maxima)

    fundo = RoundedRectangle(
        width=legenda.width + margem_horizontal * 2,
        height=legenda.height + margem_vertical * 2,
        corner_radius=0.14,
        fill_color=BLACK,
        fill_opacity=0.97,
        stroke_color=WHITE,
        stroke_opacity=0.40,
        stroke_width=1.5,
    )

    legenda.move_to(fundo.get_center())

    grupo = VGroup(fundo, legenda)
    grupo.to_edge(DOWN, buff=margem_inferior)
    grupo.set_z_index(1000)

    return grupo
