from __future__ import annotations

from manim import (
    ORIGIN,
    WHITE,
    Circle,
    Line,
    VGroup,
)


def criar_halo(
    *,
    centro=ORIGIN,
    raio_base: float = 1.0,
    quantidade: int = 5,
    espacamento: float = 0.12,
    cor=WHITE,
    opacidade_inicial: float = 0.60,
    queda_opacidade: float = 0.10,
    espessura_inicial: float = 4.0,
    queda_espessura: float = 0.50,
) -> VGroup:
    """
    Cria um halo concêntrico reutilizável.

    Pode ser usado em:
    - Sol;
    - Lua;
    - planetas;
    - zonas de energia;
    - ondas visuais;
    - destaques.
    """

    if raio_base <= 0:
        raise ValueError("raio_base tem de ser positivo.")

    if quantidade <= 0:
        raise ValueError("quantidade tem de ser superior a zero.")

    if espacamento <= 0:
        raise ValueError("espacamento tem de ser positivo.")

    halo = VGroup()

    for indice in range(1, quantidade + 1):
        opacidade = max(
            0.04,
            opacidade_inicial - indice * queda_opacidade,
        )

        espessura = max(
            0.8,
            espessura_inicial - indice * queda_espessura,
        )

        circulo = Circle(
            radius=raio_base + indice * espacamento,
            stroke_color=cor,
            stroke_opacity=opacidade,
            stroke_width=espessura,
        ).move_to(centro)

        halo.add(circulo)

    return halo


def criar_raios_radiais(
    *,
    centro=ORIGIN,
    raio_interno: float = 1.0,
    raio_externo: float = 1.45,
    quantidade: int = 16,
    cor=WHITE,
    opacidade: float = 0.70,
    espessura: float = 2.2,
) -> VGroup:
    """
    Cria raios distribuídos radialmente à volta de um ponto.

    Útil para:
    - coroa solar;
    - ondas de energia;
    - campos visuais;
    - impacto;
    - pulsações.
    """

    if raio_interno <= 0:
        raise ValueError("raio_interno tem de ser positivo.")

    if raio_externo <= raio_interno:
        raise ValueError(
            "raio_externo tem de ser superior a raio_interno."
        )

    if quantidade <= 0:
        raise ValueError("quantidade tem de ser superior a zero.")

    raios = VGroup()

    for indice in range(quantidade):
        linha = Line(
            start=centro + [0, raio_interno, 0],
            end=centro + [0, raio_externo, 0],
            color=cor,
            stroke_opacity=opacidade,
            stroke_width=espessura,
        )

        linha.rotate(
            indice * (6.283185307179586 / quantidade),
            about_point=centro,
        )

        raios.add(linha)

    return raios


def criar_coroa(
    *,
    centro=ORIGIN,
    raio: float = 1.0,
    cor=WHITE,
    intensidade: float = 1.0,
) -> VGroup:
    """
    Cria uma coroa luminosa completa combinando
    halo concêntrico e raios radiais.

    Ideal para eclipses e estrelas.
    """

    if raio <= 0:
        raise ValueError("raio tem de ser positivo.")

    if intensidade <= 0:
        raise ValueError("intensidade tem de ser positiva.")

    halo = criar_halo(
        centro=centro,
        raio_base=raio,
        quantidade=6,
        espacamento=raio * 0.10,
        cor=cor,
        opacidade_inicial=min(1.0, 0.72 * intensidade),
        queda_opacidade=0.09,
        espessura_inicial=4.8,
        queda_espessura=0.52,
    )

    raios = criar_raios_radiais(
        centro=centro,
        raio_interno=raio * 1.12,
        raio_externo=raio * 1.52,
        quantidade=16,
        cor=cor,
        opacidade=min(1.0, 0.72 * intensidade),
        espessura=2.4,
    )

    return VGroup(
        halo,
        raios,
    )


def criar_ondas(
    *,
    centro=ORIGIN,
    raio_inicial: float = 0.40,
    quantidade: int = 4,
    espacamento: float = 0.10,
    cor=WHITE,
    opacidade_inicial: float = 0.80,
) -> VGroup:
    """
    Cria ondas concêntricas fortes e legíveis.

    Pode ser usado para:
    - impacto;
    - sombra do eclipse;
    - campos visuais;
    - ondas sísmicas;
    - propagação;
    - energia.
    """

    return criar_halo(
        centro=centro,
        raio_base=raio_inicial,
        quantidade=quantidade,
        espacamento=espacamento,
        cor=cor,
        opacidade_inicial=opacidade_inicial,
        queda_opacidade=0.13,
        espessura_inicial=3.8,
        queda_espessura=0.48,
    )