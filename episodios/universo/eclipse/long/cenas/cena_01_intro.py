from __future__ import annotations

from manim import (
    BLACK,
    ORIGIN,
    RIGHT,
    Circle,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    WHITE,
    YELLOW,
)

from engine.biblioteca.astronomia.CameraRig import CameraRig

from engine.biblioteca.astronomia.LensFlare import (
    LensFlare,
)

from engine.biblioteca.astronomia.Parallax import (
    animar_aproximacao_espacial,
)

from engine.biblioteca.astronomia.SolarGlow import (
    SolarGlow,
)

from engine.biblioteca.astronomia.StarField import (
    StarField,
    animar_entrada_starfield,
)

from engine.biblioteca.astronomia.sol import criar_sol


def executar_cena_01(cena) -> None:
    """
    Cena 01 — Introdução cinematográfica do eclipse.

    Ordem:
    estrelas → movimento → Sol + glow + flare
    → aproximação → Lua → eclipse → pergunta.
    """

    # ======================================================
    # 1. ESPAÇO — VISÍVEL IMEDIATAMENTE
    # ======================================================

    starfield = StarField(
        seed=101,
        quantidade_distantes=150,
        quantidade_medias=80,
        quantidade_proximas=35,
        camada_azul=True,
    )

    # Apenas o fundo entra primeiro.
    cena.add(starfield.fundo)

    if starfield.camada_azul is not None:
        cena.add(starfield.camada_azul)

    # Estrelas surgem rapidamente.
    cena.play(
        animar_entrada_starfield(
            starfield,
            duracao=0.9,
        )
    )

    # ======================================================
    # 2. SOL + GLOW + LENS FLARE
    # ======================================================

    # O Sol aparece cedo.
    sol = criar_sol(
        raio=0.48,
        posicao=ORIGIN,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_coroa=True,
        intensidade=1.0,
    )

    # Glow EXATAMENTE centrado no Sol.
    glow = SolarGlow(
        centro=ORIGIN,
        raio_base=0.48,
        cor=YELLOW,
        intensidade=0.85,
        qualidade="cinema",
    )

    # Lens flare também nasce no mesmo centro.
    flare = LensFlare(
        centro=ORIGIN,
        raio_base=0.48,
        cor=YELLOW,
        intensidade=0.28,
        qualidade="cinema",
    )

    # ------------------------------------------------------
    # ORDEM DAS CAMADAS
    #
    # estrelas   → fundo
    # glow       → atrás do Sol
    # Sol        → disco principal
    # flare      → por cima, subtil
    # Lua        → por cima de tudo durante o eclipse
    # ------------------------------------------------------

    glow.set_z_index(20, family=True)
    sol.set_z_index(30, family=True)
    flare.set_z_index(40, family=True)

    grupo_sol = VGroup(
        glow,
        sol,
        flare,
    )

    # ======================================================
    # 3. NARRAÇÃO COMEÇA QUASE IMEDIATAMENTE
    # ======================================================

    cena.narrar(
        "No vazio do espaço, uma luz começa a crescer.",
        FadeIn(
            grupo_sol,
            run_time=1.4,
        ),
        mostrar_legenda=True,
    )

    # ======================================================
    # 4. APROXIMAÇÃO CINEMATOGRÁFICA
    # ======================================================

    camera = CameraRig(
        starfield=starfield,
    )

    cena.narrar(
        "É o Sol, uma estrela gigantesca a cento e cinquenta milhões de quilómetros de nós.",
        camera.dolly_in(
            grupo_sol,
            escala=2.15,
            duracao=3.2,
            intensidade_parallax=1.10,
        ),
        mostrar_legenda=True,
    )

    # Pequena respiração conjunta.
    cena.play(
        grupo_sol.animate.scale(1.025),
        run_time=0.65,
    )

    cena.play(
        grupo_sol.animate.scale(1 / 1.025),
        run_time=0.65,
    )

    # Continua a existir movimento no espaço.
    cena.play(
        animar_aproximacao_espacial(
            starfield,
            intensidade=0.35,
            duracao=1.0,
        )
    )

    # ======================================================
    # 5. LUA ENTRA — SÓ DEPOIS DO SOL ESTAR VISÍVEL
    # ======================================================

    # Depois do zoom o Sol está muito maior.
    # A Lua precisa de acompanhar visualmente essa escala.
    lua = Circle(
        radius=0.98,
        fill_color=BLACK,
        fill_opacity=1.0,
        stroke_color="#696969",
        stroke_opacity=0.50,
        stroke_width=1.5,
    )

    lua.move_to(RIGHT * 7.0)
    lua.set_z_index(60)

    cena.add(lua)

    cena.narrar(
        "Então, uma sombra começa lentamente a atravessar o disco solar.",
        lua.animate.move_to(RIGHT * 1.35),
        mostrar_legenda=True,
    )

    # ======================================================
    # 6. ECLIPSE PARCIAL
    # ======================================================

    cena.play(
        lua.animate.move_to(RIGHT * 0.55),

        # O Sol perde intensidade mas NÃO desaparece.
        glow.animate.set_opacity(0.72),

        # O flare reduz à medida que a Lua cobre o Sol.
        flare.animate.set_opacity(0.18),

        run_time=2.3,
    )

    cena.narrar(
        "A luz diminui. O céu muda. E, por alguns instantes, o dia começa a desaparecer.",
        mostrar_legenda=True,
    )

    # ======================================================
    # 7. ECLIPSE TOTAL
    # ======================================================

    cena.play(
        lua.animate.move_to(ORIGIN),

        # No total, a coroa/glow permanece visível.
        glow.animate.set_opacity(1.0),

        # Lens flare quase desaparece.
        flare.animate.set_opacity(0.06),

        run_time=2.2,
    )

    cena.wait(0.35)

    # ======================================================
    # 8. ECLIPSE TOTAL — IDENTIFICAÇÃO
    # ======================================================

    etiqueta = Text(
        "ECLIPSE TOTAL",
        font_size=34,
        color=YELLOW,
        weight="BOLD",
    )

    etiqueta.move_to([0, 2.50, 0])
    etiqueta.set_z_index(200)

    cena.play(
        FadeIn(etiqueta),
        run_time=0.45,
    )

    # ======================================================
    # 9. PERGUNTA PRINCIPAL
    # ======================================================

    linha_1 = Text(
        "COMO É POSSÍVEL",
        font_size=36,
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
        font_size=37,
        color=WHITE,
        weight="BOLD",
    )

    pergunta = VGroup(
        linha_1,
        linha_2,
        linha_3,
    ).arrange(
        direction=[0, -1, 0],
        buff=0.16,
    )

    # Mais alta que anteriormente para não colidir
    # com as legendas/área inferior.
    pergunta.move_to([0, -1.55, 0])
    pergunta.set_z_index(220)

    cena.narrar(
        "Mas como é possível uma Lua tão pequena esconder um Sol gigantesco?",
        [
            FadeIn(linha_1),
            FadeIn(linha_2),
            FadeIn(linha_3),
        ],
        mostrar_legenda=False,
    )

    cena.wait(0.8)

    # ======================================================
    # 10. SAÍDA
    # ======================================================

    cena.play(
        FadeOut(
            VGroup(
                pergunta,
                etiqueta,
                lua,
                grupo_sol,
                starfield,
            )
        ),
        run_time=0.8,
    )