from __future__ import annotations

from manim import (
    BLACK,
    DOWN,
    ORIGIN,
    UP,
    WHITE,
    YELLOW,
    Rectangle,
    RoundedRectangle,
    Text,
    VGroup,
    config,
)

from engine.config import (
    FONTE_PADRAO,
    TAMANHO_TITULO,
)


def ajustar_largura(
    texto: Text,
    largura_maxima: float,
) -> Text:
    """Reduz o texto apenas quando ultrapassa a largura permitida."""

    if texto.width > largura_maxima:
        texto.scale_to_fit_width(largura_maxima)

    return texto


def criar_titulo_secao(
    texto: str,
    *,
    cor=WHITE,
    tamanho: int = TAMANHO_TITULO,
) -> Text:
    """Título superior seguro para Shorts e Longs."""

    titulo = Text(
        texto,
        font=FONTE_PADRAO,
        font_size=tamanho,
        color=cor,
        weight="BOLD",
    )

    largura_segura = config.frame_width - 1.0
    ajustar_largura(titulo, largura_segura)

    titulo.to_edge(UP, buff=0.38)
    titulo.set_z_index(500)

    return titulo


def criar_pergunta_central(
    texto: str,
    *,
    cor=YELLOW,
    tamanho: int = 48,
) -> VGroup:
    """
    Pergunta central com painel próprio.

    O painel cobre os elementos anteriores para impedir
    sobreposições durante a transição.
    """

    painel = Rectangle(
        width=config.frame_width,
        height=config.frame_height,
        fill_color=BLACK,
        fill_opacity=0.97,
        stroke_opacity=0,
    )

    pergunta = Text(
        texto,
        font=FONTE_PADRAO,
        font_size=tamanho,
        color=cor,
        weight="BOLD",
        line_spacing=0.90,
    )

    ajustar_largura(
        pergunta,
        config.frame_width - 1.3,
    )

    pergunta.move_to(ORIGIN)

    painel.set_z_index(700)
    pergunta.set_z_index(710)

    return VGroup(
        painel,
        pergunta,
    )


def criar_etiqueta(
    texto: str,
    *,
    posicao=ORIGIN,
    cor=YELLOW,
    tamanho: int = 28,
) -> VGroup:
    """Etiqueta flutuante com fundo sólido e contorno."""

    palavra = Text(
        texto,
        font=FONTE_PADRAO,
        font_size=tamanho,
        color=cor,
        weight="BOLD",
    )

    ajustar_largura(
        palavra,
        config.frame_width - 1.2,
    )

    fundo = RoundedRectangle(
        width=palavra.width + 0.48,
        height=palavra.height + 0.28,
        corner_radius=0.12,
        fill_color=BLACK,
        fill_opacity=0.96,
        stroke_color=cor,
        stroke_opacity=0.95,
        stroke_width=2.0,
    )

    palavra.move_to(fundo.get_center())

    grupo = VGroup(
        fundo,
        palavra,
    ).move_to(posicao)

    grupo.set_z_index(600)

    return grupo


def criar_texto_explicativo(
    texto: str,
    *,
    posicao=ORIGIN,
    cor=WHITE,
    tamanho: int = 32,
    largura_maxima: float | None = None,
) -> Text:
    """Texto explicativo enquadrado automaticamente."""

    objeto = Text(
        texto,
        font=FONTE_PADRAO,
        font_size=tamanho,
        color=cor,
        weight="BOLD",
        line_spacing=0.90,
    )

    limite = (
        largura_maxima
        if largura_maxima is not None
        else config.frame_width - 1.2
    )

    ajustar_largura(
        objeto,
        limite,
    )

    objeto.move_to(posicao)
    objeto.set_z_index(450)

    return objeto


def criar_chamada_final(
    *,
    titulo: str = "SEGUE O CANAL",
    canal: str = "APRENDER MESMO",
) -> VGroup:
    """Chamada final reutilizável para Shorts e Longs."""

    linha_1 = Text(
        titulo,
        font=FONTE_PADRAO,
        font_size=38,
        color=WHITE,
        weight="BOLD",
    )

    linha_2 = Text(
        canal,
        font=FONTE_PADRAO,
        font_size=48,
        color=YELLOW,
        weight="BOLD",
    )

    grupo = VGroup(
        linha_1,
        linha_2,
    ).arrange(
        DOWN,
        buff=0.35,
    )

    ajustar_largura(
        linha_1,
        config.frame_width - 1.2,
    )

    ajustar_largura(
        linha_2,
        config.frame_width - 1.2,
    )

    grupo.move_to(ORIGIN)
    grupo.set_z_index(600)

    return grupo