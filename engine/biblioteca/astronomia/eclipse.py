from __future__ import annotations

from manim import (
    BLACK,
    GREY_B,
    ORIGIN,
    RIGHT,
    WHITE,
    YELLOW,
    Circle,
    Line,
    Polygon,
    VGroup,
)

from engine.biblioteca.astronomia.astros import (
    criar_lua,
    criar_sol,
    criar_terra,
)
from engine.biblioteca.astronomia.efeitos import criar_coroa


def criar_eclipse_frontal(
    *,
    centro=ORIGIN,
    raio_sol: float = 1.20,
    cobertura: float = 1.0,
    qualidade: str = "youtube",
) -> VGroup:
    """
    Cria a visão frontal de um eclipse solar.

    cobertura:
    - 0.0 = Lua afastada do Sol;
    - 0.5 = eclipse parcial;
    - 1.0 = eclipse total.
    """

    if raio_sol <= 0:
        raise ValueError("raio_sol tem de ser positivo.")

    if not 0.0 <= cobertura <= 1.0:
        raise ValueError("cobertura deve estar entre 0 e 1.")

    sol = criar_sol(
        raio=raio_sol,
        posicao=centro,
        qualidade=qualidade,
        mostrar_halo=True,
        mostrar_coroa=False,
    )

    raio_lua = raio_sol * 0.96

    deslocamento = (1.0 - cobertura) * raio_sol * 2.15

    lua = criar_lua(
        raio=raio_lua,
        posicao=centro + RIGHT * deslocamento,
        qualidade=qualidade,
        mostrar_halo=False,
        mostrar_crateras=False,
        mostrar_label=False,
    )

    # Para o eclipse, a face da Lua voltada para o observador
    # deve aparecer escura.
    disco_escuro = Circle(
        radius=raio_lua,
        fill_color=BLACK,
        fill_opacity=1.0,
        stroke_color=GREY_B,
        stroke_width=2.0,
    ).move_to(lua.get_center())

    coroa = criar_coroa(
        centro=centro,
        raio=raio_sol,
        cor=WHITE,
        intensidade=1.0,
    )
    coroa.set_opacity(cobertura)

    return VGroup(
        sol,
        coroa,
        lua,
        disco_escuro,
    )


def criar_alinhamento_eclipse(
    *,
    centro=ORIGIN,
    escala: float = 1.0,
    qualidade: str = "youtube",
    mostrar_linhas: bool = True,
    mostrar_labels: bool = True,
) -> VGroup:
    """
    Cria o alinhamento horizontal completo:

    SOL → LUA → TERRA

    Todos os astros ficam integralmente dentro de uma cena Long.
    """

    if escala <= 0:
        raise ValueError("escala tem de ser positiva.")

    sol = criar_sol(
        raio=0.72 * escala,
        posicao=centro + [-5.0 * escala, 0, 0],
        qualidade=qualidade,
        mostrar_halo=True,
        mostrar_coroa=True,
        intensidade=0.85,
    )

    lua = criar_lua(
        raio=0.27 * escala,
        posicao=centro,
        qualidade=qualidade,
        mostrar_halo=False,
        mostrar_crateras=True,
        mostrar_label=mostrar_labels,
    )

    terra = criar_terra(
        raio=0.58 * escala,
        posicao=centro + [5.0 * escala, 0, 0],
        qualidade=qualidade,
        mostrar_atmosfera=True,
        mostrar_label=mostrar_labels,
    )

    elementos = VGroup(sol, lua, terra)

    if mostrar_labels:
        # O Sol ainda não possui label interno.
        from manim import Text

        label_sol = Text(
            "SOL",
            font_size=28,
            color=YELLOW,
            weight="BOLD",
        ).next_to(sol, direction=[0, -1, 0], buff=0.28)

        elementos.add(label_sol)

    if mostrar_linhas:
        linha_sol_lua = Line(
            sol.get_right(),
            lua.get_left(),
            color=YELLOW,
            stroke_opacity=0.80,
            stroke_width=3,
        )

        linha_lua_terra = Line(
            lua.get_right(),
            terra.get_left(),
            color=WHITE,
            stroke_opacity=0.75,
            stroke_width=3,
        )

        elementos.add(
            linha_sol_lua,
            linha_lua_terra,
        )

    return elementos


def criar_cone_sombra(
    *,
    inicio,
    fim,
    largura_inicio: float = 0.36,
    largura_fim: float = 0.10,
    cor=BLACK,
    opacidade: float = 0.90,
) -> Polygon:
    """Cria a umbra entre a Lua e a Terra."""

    if largura_inicio <= 0 or largura_fim <= 0:
        raise ValueError("As larguras têm de ser positivas.")

    return Polygon(
        inicio + [0, largura_inicio, 0],
        fim + [0, largura_fim, 0],
        fim + [0, -largura_fim, 0],
        inicio + [0, -largura_inicio, 0],
        fill_color=cor,
        fill_opacity=opacidade,
        stroke_color=WHITE,
        stroke_opacity=0.22,
        stroke_width=1.5,
    )


def criar_penumbra(
    *,
    origem_sol,
    centro_lua,
    centro_terra,
    abertura: float = 0.70,
    opacidade: float = 0.18,
) -> VGroup:
    """Cria as regiões superior e inferior da penumbra."""

    superior = Polygon(
        origem_sol + [0, abertura, 0],
        centro_lua + [0, 0.24, 0],
        centro_terra + [0, 0.62, 0],
        centro_terra + [0, 0.14, 0],
        fill_color=GREY_B,
        fill_opacity=opacidade,
        stroke_opacity=0,
    )

    inferior = Polygon(
        origem_sol + [0, -abertura, 0],
        centro_lua + [0, -0.24, 0],
        centro_terra + [0, -0.62, 0],
        centro_terra + [0, -0.14, 0],
        fill_color=GREY_B,
        fill_opacity=opacidade,
        stroke_opacity=0,
    )

    return VGroup(superior, inferior)