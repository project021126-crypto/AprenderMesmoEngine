from __future__ import annotations

import math

from manim import (
    BLACK,
    ORIGIN,
    RIGHT,
    UP,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    WHITE,
    YELLOW,
    TAU,
)

from engine.biblioteca.astronomia.CameraRig import (
    CameraRig,
)

from engine.biblioteca.astronomia.LensFlare import (
    LensFlare,
)

from engine.biblioteca.astronomia.SolarGlow import (
    SolarGlow,
)

from engine.biblioteca.astronomia.StarField import (
    StarField,
    animar_entrada_starfield,
)

from engine.biblioteca.astronomia.sol import (
    criar_sol,
)


def criar_coroa_eclipse(
    *,
    raio: float,
) -> VGroup:
    """
    Coroa solar fina, irregular e assimétrica.
    """

    coroa = VGroup()

    quantidade = 96

    for indice in range(
        quantidade
    ):

        angulo = (
            TAU
            * indice
            / quantidade
        )

        # Mistura várias frequências para evitar
        # uma coroa perfeitamente circular.
        onda_1 = math.sin(
            indice * 1.73
        )

        onda_2 = math.sin(
            indice * 3.11 + 0.7
        )

        variacao = (
            0.50
            + 0.28 * onda_1
            + 0.22 * onda_2
        )

        variacao = max(
            0.05,
            min(
                1.0,
                variacao,
            ),
        )

        raio_interno = (
            raio * 1.012
        )

        raio_externo = (
            raio
            * (
                1.09
                + 0.18 * variacao
            )
        )

        opacidade = (
            0.10
            + 0.23 * variacao
        )

        linha = Line(
            start=[
                0,
                raio_interno,
                0,
            ],
            end=[
                0,
                raio_externo,
                0,
            ],
            color=WHITE,
            stroke_opacity=opacidade,
            stroke_width=1.0,
        )

        linha.rotate(
            angulo,
            about_point=ORIGIN,
        )

        coroa.add(
            linha
        )

    coroa.set_z_index(
        47,
        family=True,
    )

    return coroa


def executar_cena_01(
    cena,
) -> None:
    """
    Cena 01 — Hook cinematográfico do eclipse.
    """

    # ======================================================
    # ESPAÇO
    # ======================================================

    starfield = StarField(
        seed=101,
        quantidade_distantes=170,
        quantidade_medias=90,
        quantidade_proximas=40,
        camada_azul=True,
    )

    cena.add(
        starfield.fundo
    )

    if (
        starfield.camada_azul
        is not None
    ):
        cena.add(
            starfield.camada_azul
        )

    # ======================================================
    # SOL
    # ======================================================

    raio_sol_inicial = 0.50

    sol = criar_sol(
        raio=raio_sol_inicial,
        posicao=ORIGIN,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_coroa=False,
        intensidade=1.0,
    )

    glow = SolarGlow(
        centro=ORIGIN,
        raio_base=raio_sol_inicial,
        cor=YELLOW,
        intensidade=0.80,
        qualidade="cinema",
    )

    flare = LensFlare(
        centro=ORIGIN,
        raio_base=raio_sol_inicial,
        cor=YELLOW,
        intensidade=0.30,
        qualidade="cinema",
    )

    glow.set_z_index(
        20,
        family=True,
    )

    sol.set_z_index(
        30,
        family=True,
    )

    flare.set_z_index(
        40,
        family=True,
    )

    grupo_sol = VGroup(
        glow,
        sol,
        flare,
    )

    # ======================================================
    # PRIMEIRO PLANO
    # ======================================================

    cena.narrar(
        (
            "No vazio do espaço, "
            "uma luz começa a crescer."
        ),
        [
            animar_entrada_starfield(
                starfield,
                duracao=1.20,
            ),
            FadeIn(
                grupo_sol,
                run_time=1.10,
            ),
        ],
        mostrar_legenda=True,
        pausa_final=0.03,
    )

    # ======================================================
    # APROXIMAÇÃO
    # ======================================================

    camera = CameraRig(
        starfield=starfield,
    )

    escala_final = 2.15

    cena.narrar(
        (
            "É o Sol, uma estrela gigantesca "
            "a cento e cinquenta milhões "
            "de quilómetros de nós."
        ),
        camera.dolly_in(
            grupo_sol,
            escala=escala_final,
            duracao=3.0,
            intensidade_parallax=1.05,
        ),
        mostrar_legenda=True,
        pausa_final=0.04,
    )

    cena.play(
        grupo_sol.animate.scale(
            1.012
        ),
        run_time=0.48,
    )

    cena.play(
        grupo_sol.animate.scale(
            1 / 1.012
        ),
        run_time=0.48,
    )

    # ======================================================
    # LUA
    # ======================================================

    raio_sol_final = (
        raio_sol_inicial
        * escala_final
    )

    raio_lua = (
        raio_sol_final
        * 0.965
    )

    lua = Circle(
        radius=raio_lua,
        fill_color=BLACK,
        fill_opacity=1.0,
        stroke_color="#333333",
        stroke_opacity=0.035,
        stroke_width=0.65,
    )

    # Começa imediatamente fora do Sol.
    posicao_inicial_lua = (
        raio_sol_final
        + raio_lua
        + 0.10
    )

    lua.move_to(
        RIGHT
        * posicao_inicial_lua
    )

    lua.set_z_index(
        60,
        family=True,
    )

    cena.add(
        lua
    )

    # ======================================================
    # PRIMEIRO CONTACTO
    # ======================================================

    cena.narrar(
        (
            "Então, uma sombra começa "
            "lentamente a atravessar "
            "o disco solar."
        ),
        lua.animate.move_to(
            RIGHT
            * raio_sol_final
            * 1.10
        ),
        mostrar_legenda=True,
        pausa_final=0.03,
    )

    # ======================================================
    # ECLIPSE PARCIAL
    # ======================================================

    cena.narrar(
        (
            "A luz diminui. "
            "O céu muda. "
            "E o dia começa a desaparecer."
        ),
        [
            lua.animate.move_to(
                RIGHT
                * raio_sol_final
                * 0.44
            ),

            glow.animate.set_opacity(
                0.45
            ),

            flare.animate.set_opacity(
                0.10
            ),
        ],
        mostrar_legenda=True,
        pausa_final=0.04,
    )

    # ======================================================
    # COROA DO ECLIPSE
    # ======================================================

    coroa_total = criar_coroa_eclipse(
        raio=raio_sol_final,
    )

    coroa_total.set_opacity(
        0
    )

    cena.add(
        coroa_total
    )

    # ======================================================
    # TOTALIDADE
    # ======================================================

    cena.narrar(
        (
            "Até que, por alguns instantes, "
            "a Lua cobre completamente o Sol."
        ),
        [
            lua.animate.move_to(
                ORIGIN
            ),

            # O glow normal praticamente desaparece.
            glow.animate.set_opacity(
                0.04
            ),

            # Flare desaparece.
            flare.animate.set_opacity(
                0.0
            ),

            # Agora quem ilumina é a coroa.
            coroa_total.animate.set_opacity(
                1.0
            ),
        ],
        mostrar_legenda=True,
        pausa_final=0.08,
    )

    cena.wait(
        0.40
    )

    # ======================================================
    # COMPOSIÇÃO FINAL
    # ======================================================

    conjunto_eclipse = VGroup(
        grupo_sol,
        coroa_total,
        lua,
    )

    # O eclipse sobe para libertar espaço
    # para a pergunta.
    cena.play(
        conjunto_eclipse.animate.shift(
            UP * 0.68
        ),
        run_time=0.65,
    )

    # ======================================================
    # TÍTULO
    # ======================================================

    etiqueta = Text(
        "ECLIPSE TOTAL",
        font_size=31,
        color=YELLOW,
        weight="BOLD",
    )

    etiqueta.move_to(
        [0, 2.78, 0]
    )

    etiqueta.set_z_index(
        200
    )

    cena.play(
        FadeIn(etiqueta),
        run_time=0.35,
    )

    # ======================================================
    # PERGUNTA
    # ======================================================

    linha_1 = Text(
        "COMO É POSSÍVEL",
        font_size=31,
        color=WHITE,
        weight="BOLD",
    )

    linha_2 = Text(
        "UMA LUA TÃO PEQUENA",
        font_size=38,
        color=YELLOW,
        weight="BOLD",
    )

    linha_3 = Text(
        "ESCONDER UM SOL GIGANTESCO?",
        font_size=31,
        color=WHITE,
        weight="BOLD",
    )

    pergunta = VGroup(
        linha_1,
        linha_2,
        linha_3,
    )

    pergunta.arrange(
        direction=[0, -1, 0],
        buff=0.12,
    )

    pergunta.move_to(
        [0, -2.20, 0]
    )

    pergunta.set_z_index(
        220,
        family=True,
    )

    cena.narrar(
        (
            "Mas como é possível "
            "uma Lua tão pequena "
            "esconder um Sol gigantesco?"
        ),
        [
            FadeIn(
                linha_1,
                run_time=0.25,
            ),
            FadeIn(
                linha_2,
                run_time=0.35,
            ),
            FadeIn(
                linha_3,
                run_time=0.25,
            ),
        ],
        mostrar_legenda=False,
        pausa_final=0.12,
    )

    cena.wait(
        0.65
    )

    # ======================================================
    # SAÍDA
    # ======================================================

    cena.play(
        FadeOut(
            VGroup(
                pergunta,
                etiqueta,
                conjunto_eclipse,
                starfield,
            )
        ),
        run_time=0.70,
    )