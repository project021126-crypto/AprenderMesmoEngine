from __future__ import annotations

import math

from manim import (
    BLACK,
    ORIGIN,
    RIGHT,
    UP,
    DOWN,
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

from engine.biblioteca.astronomia.CameraRig import CameraRig
from engine.biblioteca.astronomia.LensFlare import LensFlare
from engine.biblioteca.astronomia.SolarGlow import SolarGlow
from engine.biblioteca.astronomia.StarField import (
    StarField,
    animar_entrada_starfield,
)
from engine.biblioteca.astronomia.sol import criar_sol


# ==========================================================
# COROA SOLAR
# ==========================================================

def criar_coroa_eclipse(
    *,
    raio: float,
) -> VGroup:
    """
    Coroa solar fina e irregular.
    """

    coroa = VGroup()

    quantidade = 96

    for indice in range(quantidade):

        angulo = (
            TAU
            * indice
            / quantidade
        )

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
            min(1.0, variacao),
        )

        raio_interno = (
            raio * 1.012
        )

        raio_externo = (
            raio
            * (
                1.08
                + 0.18 * variacao
            )
        )

        opacidade = (
            0.10
            + 0.24 * variacao
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

        coroa.add(linha)

    coroa.set_z_index(
        47,
        family=True,
    )

    return coroa


# ==========================================================
# CENA 01
# ==========================================================

def executar_cena_01(cena) -> None:
    """
    PARTE 1 — O MISTÉRIO

    Não explica ainda o eclipse.
    Cria perguntas que serão respondidas
    nas cenas seguintes do Long.
    """

    # ======================================================
    # 1 — ESPAÇO
    # ======================================================

    starfield = StarField(
        seed=101,
        quantidade_distantes=180,
        quantidade_medias=95,
        quantidade_proximas=42,
        camada_azul=True,
    )

    cena.add(
        starfield.fundo
    )

    if starfield.camada_azul is not None:
        cena.add(
            starfield.camada_azul
        )

    # ======================================================
    # 2 — SOL
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

    # Glow deliberadamente discreto.
    glow = SolarGlow(
        centro=ORIGIN,
        raio_base=raio_sol_inicial,
        cor=YELLOW,
        intensidade=0.30,
        qualidade="cinema",
    )

    flare = LensFlare(
        centro=ORIGIN,
        raio_base=raio_sol_inicial,
        cor=YELLOW,
        intensidade=0.24,
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
    # 3 — PRIMEIRO GANCHO
    # ======================================================

    cena.narrar(
        (
            "Há um fenómeno na Terra "
            "que parece quase impossível."
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
        pausa_final=0.05,
    )

    # ======================================================
    # 4 — APROXIMAÇÃO AO SOL
    # ======================================================

    camera = CameraRig(
        starfield=starfield
    )

    escala_final = 2.15

    cena.narrar(
        (
            "Uma esfera muito mais pequena "
            "consegue esconder por completo "
            "uma estrela gigantesca."
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

    raio_sol_final = (
        raio_sol_inicial
        * escala_final
    )

    # ======================================================
    # 5 — LUA
    # ======================================================

    raio_lua = (
        raio_sol_final
        * 0.965
    )

    lua = Circle(
        radius=raio_lua,
        fill_color=BLACK,
        fill_opacity=1.0,
        stroke_color="#333333",
        stroke_opacity=0.025,
        stroke_width=0.5,
    )

    # Começa mesmo ao lado do Sol.
    posicao_lua = (
        raio_sol_final
        + raio_lua
        + 0.08
    )

    lua.move_to(
        RIGHT * posicao_lua
    )

    lua.set_z_index(
        60,
        family=True,
    )

    cena.add(lua)

    # ======================================================
    # 6 — PRIMEIRA PERGUNTA
    # ======================================================

    cena.narrar(
        (
            "E o mais estranho..."
            " nem sequer é isso."
        ),
        lua.animate.move_to(
            RIGHT
            * raio_sol_final
            * 1.10
        ),
        mostrar_legenda=True,
        pausa_final=0.18,
    )

    # ======================================================
    # 7 — ECLIPSE PARCIAL
    # ======================================================

    cena.narrar(
        (
            "Por alguns minutos, "
            "o dia começa literalmente "
            "a desaparecer."
        ),
        [
            lua.animate.move_to(
                RIGHT
                * raio_sol_final
                * 0.44
            ),

            glow.animate.set_opacity(
                0.35
            ),

            flare.animate.set_opacity(
                0.08
            ),
        ],
        mostrar_legenda=True,
        pausa_final=0.08,
    )

    # ======================================================
    # 8 — PREPARAR COROA
    # ======================================================

    coroa = criar_coroa_eclipse(
        raio=raio_sol_final
    )

    coroa.set_opacity(0)

    cena.add(coroa)

    # ======================================================
    # 9 — TOTALIDADE
    # ======================================================

    cena.narrar(
        (
            "E então acontece isto."
        ),
        [
            lua.animate.move_to(
                ORIGIN
            ),

            # Glow normal desaparece.
            glow.animate.set_opacity(
                0.0
            ),

            flare.animate.set_opacity(
                0.0
            ),

            # Só permanece a coroa.
            coroa.animate.set_opacity(
                1.0
            ),
        ],
        mostrar_legenda=True,
        pausa_final=0.20,
    )

    # Momento para observar.
    cena.wait(0.70)

    # ======================================================
    # 10 — SEGUNDO GANCHO
    # ======================================================

    texto_coincidencia = Text(
        "UMA COINCIDÊNCIA EXTRAORDINÁRIA",
        font_size=31,
        color=YELLOW,
        weight="BOLD",
    )

    texto_coincidencia.to_edge(
        UP,
        buff=0.55,
    )

    texto_coincidencia.set_z_index(
        200
    )

    cena.narrar(
        (
            "Isto só é possível por causa "
            "de uma coincidência extraordinária."
        ),
        FadeIn(
            texto_coincidencia
        ),
        mostrar_legenda=True,
        pausa_final=0.15,
    )

    cena.play(
        FadeOut(
            texto_coincidencia
        ),
        run_time=0.35,
    )

    # ======================================================
    # 11 — TERCEIRO GANCHO
    # ======================================================

    texto_desaparecer = Text(
        "MAS NÃO VAI DURAR PARA SEMPRE",
        font_size=32,
        color=WHITE,
        weight="BOLD",
    )

    texto_desaparecer.to_edge(
        UP,
        buff=0.55,
    )

    texto_desaparecer.set_z_index(
        200
    )

    cena.narrar(
        (
            "E há outro problema: "
            "esta coincidência não vai durar para sempre."
        ),
        FadeIn(
            texto_desaparecer
        ),
        mostrar_legenda=True,
        pausa_final=0.15,
    )

    # ======================================================
    # 12 — LUA COMEÇA A AFASTAR-SE
    # ======================================================

    cena.play(
        FadeOut(
            texto_desaparecer
        ),
        run_time=0.30,
    )

    cena.narrar(
        (
            "A Lua afasta-se da Terra "
            "um pouco mais todos os anos."
        ),
        [
            lua.animate.scale(
                0.94
            ),

            coroa.animate.set_opacity(
                0.82
            ),
        ],
        mostrar_legenda=True,
        pausa_final=0.10,
    )

    # ======================================================
    # 13 — CONSEQUÊNCIA
    # ======================================================

    cena.narrar(
        (
            "No futuro, ela já não será "
            "grande o suficiente no nosso céu "
            "para esconder totalmente o Sol."
        ),
        lua.animate.scale(
            0.93
        ),
        mostrar_legenda=True,
        pausa_final=0.15,
    )

    # Agora vemos uma pequena borda do Sol.
    cena.wait(0.45)

    # ======================================================
    # 14 — NOVAS PERGUNTAS
    # ======================================================

    conjunto_eclipse = VGroup(
        grupo_sol,
        coroa,
        lua,
    )

    cena.play(
        conjunto_eclipse.animate.shift(
            UP * 0.72
        ),
        run_time=0.60,
    )

    pergunta_1 = Text(
        "PORQUÊ AGORA?",
        font_size=35,
        color=YELLOW,
        weight="BOLD",
    )

    pergunta_2 = Text(
        "PORQUÊ SÓ EM ALGUNS LUGARES?",
        font_size=31,
        color=WHITE,
        weight="BOLD",
    )

    pergunta_3 = Text(
        "E PORQUE NÃO ACONTECE TODOS OS MESES?",
        font_size=29,
        color=WHITE,
        weight="BOLD",
    )

    perguntas = VGroup(
        pergunta_1,
        pergunta_2,
        pergunta_3,
    ).arrange(
        DOWN,
        buff=0.18,
    )

    perguntas.move_to(
        [0, -2.05, 0]
    )

    perguntas.set_z_index(
        220,
        family=True,
    )

    cena.narrar(
        (
            "Então porque conseguimos ver "
            "eclipses totais agora?"
        ),
        FadeIn(
            pergunta_1
        ),
        mostrar_legenda=False,
        pausa_final=0.08,
    )

    cena.narrar(
        (
            "Porque só algumas regiões "
            "da Terra conseguem vê-los?"
        ),
        FadeIn(
            pergunta_2
        ),
        mostrar_legenda=False,
        pausa_final=0.08,
    )

    cena.narrar(
        (
            "E porque não acontece "
            "um eclipse todos os meses?"
        ),
        FadeIn(
            pergunta_3
        ),
        mostrar_legenda=False,
        pausa_final=0.18,
    )

    # ======================================================
    # 15 — TÍTULO / TRANSIÇÃO PARA PARTE 2
    # ======================================================

    cena.play(
        FadeOut(
            perguntas
        ),
        run_time=0.40,
    )

    titulo = Text(
        "O SEGREDO DOS ECLIPSES",
        font_size=42,
        color=YELLOW,
        weight="BOLD",
    )

    subtitulo = Text(
        "começa com dois números",
        font_size=27,
        color=WHITE,
    )

    titulo_final = VGroup(
        titulo,
        subtitulo,
    ).arrange(
        DOWN,
        buff=0.22,
    )

    titulo_final.move_to(
        [0, -1.95, 0]
    )

    titulo_final.set_z_index(
        250,
        family=True,
    )

    cena.narrar(
        (
            "A resposta começa "
            "com dois números surpreendentes."
        ),
        FadeIn(
            titulo_final
        ),
        mostrar_legenda=False,
        pausa_final=0.20,
    )

    cena.wait(0.75)

    # ======================================================
    # 16 — SAÍDA PARA CENA 2
    # ======================================================

    cena.play(
        FadeOut(
            VGroup(
                titulo_final,
                conjunto_eclipse,
                starfield,
            )
        ),
        run_time=0.75,
    )