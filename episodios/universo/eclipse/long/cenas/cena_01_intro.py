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
    animar_entrada_flare,
)
from engine.biblioteca.astronomia.Parallax import (
    animar_aproximacao_espacial,
)
from engine.biblioteca.astronomia.SolarGlow import (
    SolarGlow,
    animar_pulsacao_glow,
)
from engine.biblioteca.astronomia.StarField import (
    StarField,
    animar_entrada_starfield,
)
from engine.biblioteca.astronomia.sol import criar_sol


def executar_cena_01(cena) -> None:
    """
    Ato 1 — O Mistério.

    Objetivo:
    - prender imediatamente;
    - dar profundidade;
    - mostrar o Sol como presença viva;
    - criar trânsito real da Lua;
    - terminar numa pergunta forte.
    """

    # ======================================================
    # 1. CAMPO ESTELAR
    # ======================================================

    starfield = StarField(
        seed=101,
        quantidade_distantes=150,
        quantidade_medias=80,
        quantidade_proximas=35,
        camada_azul=True,
    )

    cena.add(starfield.fundo)

    if starfield.camada_azul is not None:
        cena.add(starfield.camada_azul)

    cena.play(
        animar_entrada_starfield(
            starfield,
            duracao=1.8,
        )
    )

    cena.add(
        starfield.distantes,
        starfield.medias,
        starfield.proximas,
    )

    # ======================================================
    # 2. PARALLAX — COMEÇA LOGO A DAR PROFUNDIDADE
    # ======================================================

    cena.play(
        animar_aproximacao_espacial(
            starfield,
            intensidade=0.85,
            duracao=1.8,
        )
    )

    # ======================================================
    # 3. SOL DISTANTE
    # ======================================================

    sol = criar_sol(
        raio=0.42,
        posicao=ORIGIN,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_coroa=True,
        intensidade=1.0,
    )

    glow = SolarGlow(
        centro=ORIGIN,
        raio_base=0.42,
        cor=YELLOW,
        intensidade=1.0,
        qualidade="cinema",
    )

    flare = LensFlare(
        centro=ORIGIN,
        raio_base=0.42,
        cor=YELLOW,
        intensidade=0.85,
        qualidade="cinema",
    )

    cena.add(
        glow,
        sol,
        flare,
    )

    glow.set_opacity(0)
    sol.set_opacity(0)
    flare.set_opacity(0)

    cena.play(
        FadeIn(sol),
        FadeIn(glow),
        animar_entrada_flare(
            flare,
            escala_inicial=0.30,
            duracao=1.4,
        ),
        run_time=1.4,
    )

    # ======================================================
    # 4. CÂMARA APROXIMA DO SOL
    # ======================================================

    camera = CameraRig(
        starfield=starfield,
    )

    grupo_sol = VGroup(
        glow,
        sol,
        flare,
    )

    cena.narrar(
        "No vazio do espaço, uma luz cresce diante de nós.",
        camera.dolly_in(
            grupo_sol,
            escala=2.25,
            duracao=3.2,
            intensidade_parallax=1.15,
        ),
        mostrar_legenda=True,
    )

    # ======================================================
    # 5. SOL VIVO
    # ======================================================

    cena.play(
        animar_pulsacao_glow(
            glow,
            intensidade=1.035,
            duracao=0.9,
        )
    )

    cena.play(
        glow.animate.scale(1 / 1.035),
        run_time=0.9,
    )

    # ======================================================
    # 6. LUA ENTRA
    # ======================================================

    raio_lua = 0.90

    lua = Circle(
        radius=raio_lua,
        fill_color=BLACK,
        fill_opacity=1.0,
        stroke_color="#707070",
        stroke_opacity=0.75,
        stroke_width=2.0,
    )

    lua.move_to(RIGHT * 6.0)
    lua.set_z_index(100)

    cena.add(lua)

    cena.narrar(
        "Então, sem aviso, a Lua começa a atravessar o disco solar.",
        lua.animate.move_to(RIGHT * 1.15),
        mostrar_legenda=True,
    )

    # ======================================================
    # 7. ECLIPSE PARCIAL
    # ======================================================

    cena.play(
        lua.animate.move_to(RIGHT * 0.48),
        starfield.distantes.animate.set_opacity(0.38),
        starfield.medias.animate.set_opacity(0.48),
        starfield.proximas.animate.set_opacity(0.58),
        glow.animate.set_opacity(0.70),
        flare.animate.set_opacity(0.55),
        run_time=2.5,
    )

    cena.narrar(
        "A luz diminui. O céu muda. E por alguns instantes, o dia parece desaparecer.",
        mostrar_legenda=True,
    )

    # ======================================================
    # 8. ECLIPSE TOTAL
    # ======================================================

    cena.play(
        lua.animate.move_to(ORIGIN),
        glow.animate.set_opacity(1.0),
        flare.animate.set_opacity(0.32),
        run_time=2.4,
    )

    cena.wait(0.6)

    # ======================================================
    # 9. ETIQUETA
    # ======================================================

    etiqueta = Text(
        "ECLIPSE TOTAL",
        font_size=34,
        color=YELLOW,
        weight="BOLD",
    )

    etiqueta.move_to([0, 2.45, 0])
    etiqueta.set_z_index(300)

    cena.play(
        FadeIn(etiqueta),
        run_time=0.5,
    )

    cena.wait(0.5)

    # ======================================================
    # 10. PERGUNTA
    # ======================================================

    linha_1 = Text(
        "COMO É POSSÍVEL",
        font_size=38,
        color=WHITE,
        weight="BOLD",
    )

    linha_2 = Text(
        "UMA LUA TÃO PEQUENA",
        font_size=45,
        color=YELLOW,
        weight="BOLD",
    )

    linha_3 = Text(
        "ESCONDER UM SOL GIGANTESCO?",
        font_size=40,
        color=WHITE,
        weight="BOLD",
    )

    pergunta = VGroup(
        linha_1,
        linha_2,
        linha_3,
    ).arrange(
        direction=[0, -1, 0],
        buff=0.18,
    )

    pergunta.move_to([0, -2.05, 0])
    pergunta.set_z_index(350)

    cena.narrar(
        "Como é possível uma Lua tão pequena esconder um Sol gigantesco?",
        [
            FadeIn(linha_1),
            FadeIn(linha_2),
            FadeIn(linha_3),
        ],
        mostrar_legenda=False,
    )

    cena.wait(1.0)

    # ======================================================
    # 11. SAÍDA
    # ======================================================

    cena.play(
        FadeOut(
            VGroup(
                pergunta,
                etiqueta,
                lua,
                glow,
                sol,
                flare,
                starfield,
            )
        ),
        run_time=0.9,
    )