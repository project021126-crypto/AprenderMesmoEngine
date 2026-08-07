from __future__ import annotations

import math

from manim import (
    BLACK,
    ORIGIN,
    RIGHT,
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
    Coroa solar irregular.

    Utiliza muitos raios finos de tamanhos diferentes
    para evitar o aspeto de anel geométrico.
    """

    coroa = VGroup()

    quantidade = 72

    for indice in range(
        quantidade
    ):

        angulo = (
            TAU
            * indice
            / quantidade
        )

        variacao = (
            0.5
            + 0.5
            * math.sin(
                indice * 2.17
            )
        )

        raio_interno = (
            raio * 1.015
        )

        raio_externo = (
            raio
            * (
                1.10
                + 0.16 * variacao
            )
        )

        opacidade = (
            0.11
            + 0.20 * variacao
        )

        raio_luz = Line(
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
            stroke_width=1.15,
        )

        raio_luz.rotate(
            angulo,
            about_point=ORIGIN,
        )

        coroa.add(
            raio_luz
        )

    coroa.set_z_index(48)

    return coroa


def executar_cena_01(
    cena,
) -> None:
    """
    Cena 01 — Hook cinematográfico.

    estrelas + Sol
    → aproximação
    → Lua
    → eclipse total
    → pergunta.
    """

    # ======================================================
    # 1. ESPAÇO
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
    # 2. SOL + GLOW + FLARE
    # ======================================================

    raio_sol_inicial = 0.50

    sol = criar_sol(
        raio=raio_sol_inicial,
        posicao=ORIGIN,
        qualidade="cinema",

        # IMPORTANTE:
        # retiramos a antiga coroa geométrica.
        mostrar_halo=False,
        mostrar_coroa=False,

        intensidade=1.0,
    )

    glow = SolarGlow(
        centro=ORIGIN,
        raio_base=raio_sol_inicial,
        cor=YELLOW,
        intensidade=0.90,
        qualidade="cinema",
    )

    flare = LensFlare(
        centro=ORIGIN,
        raio_base=raio_sol_inicial,
        cor=YELLOW,

        # Muito mais subtil.
        intensidade=0.42,

        qualidade="cinema",
    )

    glow.set_z_index(20)
    sol.set_z_index(30)
    flare.set_z_index(40)

    grupo_sol = VGroup(
        glow,
        sol,
        flare,
    )

    # ======================================================
    # 3. NARRAÇÃO COMEÇA IMEDIATAMENTE
    # ======================================================

    cena.narrar(
        (
            "No vazio do espaço, "
            "uma luz começa a crescer."
        ),
        [
            animar_entrada_starfield(
                starfield,
                duracao=1.25,
            ),
            FadeIn(
                grupo_sol
            ),
        ],
        mostrar_legenda=True,
        pausa_final=0.05,
    )

    # ======================================================
    # 4. APROXIMAÇÃO CINEMATOGRÁFICA
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
        pausa_final=0.05,
    )

    # Pulso quase impercetível.
    cena.play(
        grupo_sol.animate.scale(
            1.018
        ),
        run_time=0.55,
    )

    cena.play(
        grupo_sol.animate.scale(
            1 / 1.018
        ),
        run_time=0.55,
    )

    # ======================================================
    # 5. LUA
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

        # Quase sem contorno.
        # No espaço negro praticamente desaparece.
        stroke_color="#444444",
        stroke_opacity=0.08,
        stroke_width=0.8,
    )

    # A Lua começa imediatamente ao lado do Sol.
    # Não atravessa metade do espaço.
    lua.move_to(
        RIGHT * (
            raio_sol_final
            + raio_lua
            + 0.16
        )
    )

    lua.set_z_index(60)

    cena.add(lua)

    # ======================================================
    # 6. PRIMEIRO CONTACTO
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
            * 1.15
        ),
        mostrar_legenda=True,
        pausa_final=0.05,
    )

    # ======================================================
    # 7. ECLIPSE PARCIAL
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
                * 0.46
            ),

            glow.animate.set_opacity(
                0.68
            ),

            flare.animate.set_opacity(
                0.18
            ),
        ],
        mostrar_legenda=True,
        pausa_final=0.05,
    )

    # ======================================================
    # 8. COROA TOTAL
    # ======================================================

    coroa_total = criar_coroa_eclipse(
        raio=raio_sol_final,
    )

    coroa_total.set_opacity(0)

    cena.add(
        coroa_total
    )

    # ======================================================
    # 9. ECLIPSE TOTAL
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

            coroa_total.animate.set_opacity(
                1.0
            ),

            glow.animate.set_opacity(
                0.52
            ),

            flare.animate.set_opacity(
                0.015
            ),
        ],
        mostrar_legenda=True,
        pausa_final=0.10,
    )

    # Pequeno momento para contemplar o eclipse.
    cena.wait(0.45)

    # ======================================================
    # 10. TÍTULO DO FENÓMENO
    # ======================================================

    etiqueta = Text(
        "ECLIPSE TOTAL",
        font_size=33,
        color=YELLOW,
        weight="BOLD",
    )

    etiqueta.move_to(
        [0, 2.55, 0]
    )

    etiqueta.set_z_index(200)

    cena.play(
        FadeIn(etiqueta),
        run_time=0.40,
    )

    # ======================================================
    # 11. PERGUNTA CENTRAL
    # ======================================================

    linha_1 = Text(
        "COMO É POSSÍVEL",
        font_size=35,
        color=WHITE,
        weight="BOLD",
    )

    linha_2 = Text(
        "UMA LUA TÃO PEQUENA",
        font_size=43,
        color=YELLOW,
        weight="BOLD",
    )

    linha_3 = Text(
        "ESCONDER UM SOL GIGANTESCO?",
        font_size=36,
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
        buff=0.14,
    )

    pergunta.move_to(
        [0, -1.65, 0]
    )

    pergunta.set_z_index(
        220
    )

    cena.narrar(
        (
            "Mas como é possível "
            "uma Lua tão pequena "
            "esconder um Sol gigantesco?"
        ),
        [
            FadeIn(linha_1),
            FadeIn(linha_2),
            FadeIn(linha_3),
        ],
        mostrar_legenda=False,
        pausa_final=0.15,
    )

    cena.wait(0.7)

    # ======================================================
    # 12. SAÍDA
    # ======================================================

    cena.play(
        FadeOut(
            VGroup(
                pergunta,
                etiqueta,
                lua,
                coroa_total,
                grupo_sol,
                starfield,
            )
        ),
        run_time=0.75,
    )