from __future__ import annotations

from manim import (
    BLACK,
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    GrowArrow,
    Line,
    Text,
    VGroup,
    WHITE,
    YELLOW,
)

from engine.biblioteca.astronomia.StarField import (
    StarField,
    animar_entrada_starfield,
)

from engine.biblioteca.astronomia.sol import (
    criar_sol,
)

from engine.biblioteca.astronomia.astros import (
    criar_lua,
)


def executar_cena_02(cena) -> None:
    """
    PARTE 2 — O SEGREDO DOS 400

    Revela:
    - Sol ≈ 400x maior que a Lua;
    - Sol ≈ 400x mais distante;
    - por isso ambos têm tamanho aparente semelhante.

    Termina com:
    porque não acontece um eclipse todos os meses?
    """

    # ======================================================
    # 1 — FUNDO
    # ======================================================

    starfield = StarField(
        seed=202,
        quantidade_distantes=150,
        quantidade_medias=70,
        quantidade_proximas=25,
        camada_azul=True,
    )

    cena.add(
        starfield.fundo
    )

    if starfield.camada_azul is not None:
        cena.add(
            starfield.camada_azul
        )

    cena.play(
        animar_entrada_starfield(
            starfield,
            duracao=0.70,
        )
    )

    # ======================================================
    # 2 — OS DOIS NÚMEROS
    # ======================================================

    numero_1 = Text(
        "400×",
        font_size=84,
        color=YELLOW,
        weight="BOLD",
    )

    numero_2 = Text(
        "400×",
        font_size=84,
        color=WHITE,
        weight="BOLD",
    )

    numeros = VGroup(
        numero_1,
        numero_2,
    ).arrange(
        RIGHT,
        buff=2.8,
    )

    numeros.move_to(
        ORIGIN
    )

    cena.narrar(
        (
            "Lembras-te dos dois números? "
            "Curiosamente, são quase iguais."
        ),
        [
            FadeIn(numero_1),
            FadeIn(numero_2),
        ],
        mostrar_legenda=True,
        pausa_final=0.08,
    )

    # ======================================================
    # 3 — 400× MAIOR
    # ======================================================

    cena.play(
        FadeOut(numero_2),
        numero_1.animate
        .scale(0.78)
        .move_to([0, 2.65, 0]),
        run_time=0.60,
    )

    titulo_tamanho = Text(
        "O PRIMEIRO 400",
        font_size=25,
        color=WHITE,
        weight="BOLD",
    )

    titulo_tamanho.next_to(
        numero_1,
        DOWN,
        buff=0.12,
    )

    cena.play(
        FadeIn(titulo_tamanho),
        run_time=0.25,
    )

    # ======================================================
    # 4 — SOL E LUA
    # ======================================================

    sol_grande = criar_sol(
        raio=1.45,
        posicao=LEFT * 3.1,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_coroa=False,
        intensidade=1.0,
    )

    lua_pequena = criar_lua(
        raio=0.24,
        posicao=RIGHT * 3.15,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_crateras=True,
        mostrar_label=False,
    )

    label_sol = Text(
        "SOL",
        font_size=24,
        color=YELLOW,
        weight="BOLD",
    ).next_to(
        sol_grande,
        DOWN,
        buff=0.22,
    )

    label_lua = Text(
        "LUA",
        font_size=24,
        color=WHITE,
        weight="BOLD",
    ).next_to(
        lua_pequena,
        DOWN,
        buff=0.22,
    )

    cena.narrar(
        (
            "O Sol tem aproximadamente "
            "quatrocentas vezes o diâmetro da Lua."
        ),
        [
            FadeIn(sol_grande),
            FadeIn(lua_pequena),
            FadeIn(label_sol),
            FadeIn(label_lua),
        ],
        mostrar_legenda=True,
        pausa_final=0.05,
    )

    # ======================================================
    # 5 — MEDIDA VISUAL MAIS LIMPA
    # ======================================================

    linha_sol = Line(
        sol_grande.get_left(),
        sol_grande.get_right(),
        color=YELLOW,
        stroke_width=3,
    )

    linha_lua = Line(
        lua_pequena.get_left(),
        lua_pequena.get_right(),
        color=WHITE,
        stroke_width=3,
    )

    linha_sol.next_to(
        sol_grande,
        UP,
        buff=0.18,
    )

    linha_lua.next_to(
        lua_pequena,
        UP,
        buff=0.18,
    )

    texto_400_tamanho = Text(
        "≈ 400× MAIOR",
        font_size=31,
        color=YELLOW,
        weight="BOLD",
    )

    texto_400_tamanho.move_to(
        [0, -2.20, 0]
    )

    cena.play(
        FadeIn(linha_sol),
        FadeIn(linha_lua),
        FadeIn(texto_400_tamanho),
        run_time=0.40,
    )

    cena.wait(0.40)

    # ======================================================
    # 6 — TRANSIÇÃO PARA DISTÂNCIA
    # ======================================================

    cena.narrar(
        (
            "Mas o tamanho é apenas metade da história."
        ),
        FadeOut(
            VGroup(
                numero_1,
                titulo_tamanho,
                linha_sol,
                linha_lua,
                texto_400_tamanho,
                label_sol,
                label_lua,
            )
        ),
        mostrar_legenda=True,
        pausa_final=0.04,
    )

    # ======================================================
    # 7 — SEGUNDO 400: DISTÂNCIA
    # ======================================================

    sol_distancia = sol_grande.copy()
    sol_distancia.scale(0.52)
    sol_distancia.move_to(
        LEFT * 5.05
    )

    lua_distancia = lua_pequena.copy()
    lua_distancia.scale(1.15)
    lua_distancia.move_to(
        RIGHT * 1.25
    )

    terra = Circle(
        radius=0.18,
        fill_color="#4A7BD0",
        fill_opacity=1.0,
        stroke_color=WHITE,
        stroke_opacity=0.35,
        stroke_width=1.0,
    )

    terra.move_to(
        RIGHT * 5.25
    )

    label_terra = Text(
        "TERRA",
        font_size=22,
        color=WHITE,
        weight="BOLD",
    ).next_to(
        terra,
        DOWN,
        buff=0.18,
    )

    cena.play(
        FadeOut(sol_grande),
        FadeOut(lua_pequena),
        FadeIn(sol_distancia),
        FadeIn(lua_distancia),
        FadeIn(terra),
        FadeIn(label_terra),
        run_time=0.65,
    )

    # ======================================================
    # 8 — DISTÂNCIA SOL/TERRA
    # ======================================================

    seta_sol = Arrow(
        start=terra.get_left(),
        end=sol_distancia.get_right(),
        buff=0.12,
        color=YELLOW,
        stroke_width=2.5,
        max_tip_length_to_length_ratio=0.035,
    )

    texto_distancia_sol = Text(
        "≈ 150 milhões km",
        font_size=23,
        color=YELLOW,
        weight="BOLD",
    )

    texto_distancia_sol.move_to(
        [-2.10, 1.20, 0]
    )

    # ======================================================
    # 9 — DISTÂNCIA LUA/TERRA
    # ======================================================

    seta_lua = Arrow(
        start=terra.get_left(),
        end=lua_distancia.get_right(),
        buff=0.10,
        color=WHITE,
        stroke_width=2.5,
        max_tip_length_to_length_ratio=0.09,
    )

    texto_distancia_lua = Text(
        "≈ 384 mil km",
        font_size=23,
        color=WHITE,
        weight="BOLD",
    )

    texto_distancia_lua.move_to(
        [3.05, -1.20, 0]
    )

    cena.narrar(
        (
            "O Sol também está aproximadamente "
            "quatrocentas vezes mais distante da Terra."
        ),
        [
            GrowArrow(seta_sol),
            GrowArrow(seta_lua),
            FadeIn(texto_distancia_sol),
            FadeIn(texto_distancia_lua),
        ],
        mostrar_legenda=True,
        pausa_final=0.07,
    )

    # ======================================================
    # 10 — REVELAR O SEGUNDO 400
    # ======================================================

    segredo = Text(
        "≈ 400× MAIS DISTANTE",
        font_size=35,
        color=YELLOW,
        weight="BOLD",
    )

    segredo.to_edge(
        UP,
        buff=0.50,
    )

    cena.play(
        FadeIn(segredo),
        run_time=0.35,
    )

    cena.wait(0.45)

    # ======================================================
    # 11 — LIMPAR
    # ======================================================

    cena.narrar(
        (
            "E é aí que os dois números se encontram."
        ),
        FadeOut(
            VGroup(
                sol_distancia,
                lua_distancia,
                terra,
                label_terra,
                seta_sol,
                seta_lua,
                texto_distancia_sol,
                texto_distancia_lua,
                segredo,
            )
        ),
        mostrar_legenda=True,
        pausa_final=0.05,
    )

    # ======================================================
    # 12 — TAMANHO APARENTE
    # ======================================================

    sol_aparente = criar_sol(
        raio=1.08,
        posicao=LEFT * 2.2,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_coroa=False,
        intensidade=1.0,
    )

    # Aqui NÃO usamos criar_lua().
    # Queremos mostrar o disco escuro que realmente
    # vemos durante um eclipse solar.
    lua_aparente = Circle(
        radius=1.045,
        fill_color=BLACK,
        fill_opacity=1.0,
        stroke_color="#686868",
        stroke_opacity=0.35,
        stroke_width=1.1,
    )

    lua_aparente.move_to(
        RIGHT * 2.2
    )

    igual = Text(
        "≈",
        font_size=68,
        color=WHITE,
        weight="BOLD",
    )

    label_aparente = Text(
        "VISTOS DA TERRA",
        font_size=25,
        color=WHITE,
        weight="BOLD",
    )

    label_aparente.to_edge(
        UP,
        buff=0.55,
    )

    cena.narrar(
        (
            "Vistos daqui da Terra, "
            "os dois ocupam quase o mesmo tamanho no céu."
        ),
        [
            FadeIn(label_aparente),
            FadeIn(sol_aparente),
            FadeIn(lua_aparente),
            FadeIn(igual),
        ],
        mostrar_legenda=True,
        pausa_final=0.06,
    )

    # ======================================================
    # 13 — SOBREPOR
    # ======================================================

    cena.play(
        sol_aparente.animate.move_to(
            ORIGIN
        ),
        lua_aparente.animate.move_to(
            ORIGIN
        ),
        FadeOut(igual),
        FadeOut(label_aparente),
        run_time=1.8,
    )

    # Agora fica muito mais parecido com eclipse.
    texto_perfeito = Text(
        "QUASE O MESMO TAMANHO APARENTE",
        font_size=29,
        color=YELLOW,
        weight="BOLD",
    )

    texto_perfeito.to_edge(
        UP,
        buff=0.52,
    )

    cena.play(
        FadeIn(texto_perfeito),
        run_time=0.35,
    )

    cena.narrar(
        (
            "É por isso que, quando ficam alinhados, "
            "a Lua consegue cobrir quase exatamente o disco solar."
        ),
        mostrar_legenda=True,
        pausa_final=0.08,
    )

    # ======================================================
    # 14 — A EQUAÇÃO VISUAL DOS 400
    # ======================================================

    cena.play(
        FadeOut(
            VGroup(
                sol_aparente,
                lua_aparente,
                texto_perfeito,
            )
        ),
        run_time=0.45,
    )

    quatrocentos_1 = Text(
        "400× MAIOR",
        font_size=43,
        color=YELLOW,
        weight="BOLD",
    )

    mais = Text(
        "↕",
        font_size=42,
        color=WHITE,
        weight="BOLD",
    )

    quatrocentos_2 = Text(
        "400× MAIS DISTANTE",
        font_size=43,
        color=YELLOW,
        weight="BOLD",
    )

    formula_visual = VGroup(
        quatrocentos_1,
        mais,
        quatrocentos_2,
    ).arrange(
        DOWN,
        buff=0.24,
    )

    formula_visual.move_to(
        ORIGIN
    )

    cena.narrar(
        (
            "Quatrocentas vezes maior. "
            "Quatrocentas vezes mais distante."
        ),
        [
            FadeIn(quatrocentos_1),
            FadeIn(mais),
            FadeIn(quatrocentos_2),
        ],
        mostrar_legenda=False,
        pausa_final=0.12,
    )

    # ======================================================
    # 15 — NOVO MISTÉRIO
    # ======================================================

    cena.play(
        FadeOut(
            formula_visual
        ),
        run_time=0.40,
    )

    nova_pergunta = Text(
        "ENTÃO PORQUE NÃO HÁ",
        font_size=35,
        color=WHITE,
        weight="BOLD",
    )

    nova_pergunta_2 = Text(
        "UM ECLIPSE TODOS OS MESES?",
        font_size=41,
        color=YELLOW,
        weight="BOLD",
    )

    pergunta = VGroup(
        nova_pergunta,
        nova_pergunta_2,
    ).arrange(
        DOWN,
        buff=0.18,
    )

    pergunta.move_to(
        ORIGIN
    )

    cena.narrar(
        (
            "Mas se o encaixe é tão perfeito, "
            "porque não temos um eclipse todos os meses?"
        ),
        [
            FadeIn(nova_pergunta),
            FadeIn(nova_pergunta_2),
        ],
        mostrar_legenda=False,
        pausa_final=0.18,
    )

    # ======================================================
    # 16 — GANCHO PARA CENA 3
    # ======================================================

    proximo = Text(
        "PORQUE A LUA NÃO VIAJA NUMA LINHA PERFEITA.",
        font_size=27,
        color=WHITE,
        weight="BOLD",
    )

    proximo.next_to(
        pergunta,
        DOWN,
        buff=0.55,
    )

    cena.play(
        FadeIn(proximo),
        run_time=0.35,
    )

    cena.wait(0.70)

    cena.play(
        FadeOut(
            VGroup(
                pergunta,
                proximo,
                starfield,
            )
        ),
        run_time=0.65,
    )