from __future__ import annotations

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    Arrow,
    Circle,
    DecimalNumber,
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
    - o Sol é aproximadamente 400x maior que a Lua;
    - o Sol está aproximadamente 400x mais distante;
    - por isso os dois podem parecer quase do mesmo tamanho no céu.

    Termina abrindo a próxima pergunta:
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
            duracao=0.75,
        )
    )

    # ======================================================
    # 2 — GANCHO: DOIS NÚMEROS
    # ======================================================

    numero_1 = Text(
        "400×",
        font_size=92,
        color=YELLOW,
        weight="BOLD",
    )

    numero_2 = Text(
        "400×",
        font_size=92,
        color=WHITE,
        weight="BOLD",
    )

    numeros = VGroup(
        numero_1,
        numero_2,
    ).arrange(
        RIGHT,
        buff=2.2,
    )

    numeros.move_to(
        ORIGIN
    )

    cena.narrar(
        (
            "Lembras-te dos dois números? "
            "Curiosamente... são quase iguais."
        ),
        [
            FadeIn(numero_1),
            FadeIn(numero_2),
        ],
        mostrar_legenda=True,
        pausa_final=0.10,
    )

    # ======================================================
    # 3 — PRIMEIRO 400: TAMANHO
    # ======================================================

    cena.play(
        numero_2.animate.set_opacity(0.18),
        numero_1.animate.move_to(
            [0, 2.35, 0]
        ),
        run_time=0.65,
    )

    titulo_tamanho = Text(
        "TAMANHO",
        font_size=30,
        color=WHITE,
        weight="BOLD",
    )

    titulo_tamanho.next_to(
        numero_1,
        DOWN,
        buff=0.16,
    )

    cena.play(
        FadeIn(titulo_tamanho),
        run_time=0.30,
    )

    # ======================================================
    # 4 — SOL E LUA LADO A LADO
    # ======================================================

    sol_grande = criar_sol(
        raio=1.55,
        posicao=LEFT * 3.2,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_coroa=False,
        intensidade=1.0,
    )

    lua_pequena = criar_lua(
        raio=0.26,
        posicao=RIGHT * 3.25,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_crateras=True,
        mostrar_label=False,
    )

    label_sol = Text(
        "SOL",
        font_size=26,
        color=YELLOW,
        weight="BOLD",
    ).next_to(
        sol_grande,
        DOWN,
        buff=0.28,
    )

    label_lua = Text(
        "LUA",
        font_size=26,
        color=WHITE,
        weight="BOLD",
    ).next_to(
        lua_pequena,
        DOWN,
        buff=0.28,
    )

    cena.narrar(
        (
            "O Sol tem cerca de quatrocentas vezes "
            "o diâmetro da Lua."
        ),
        [
            FadeIn(sol_grande),
            FadeIn(lua_pequena),
            FadeIn(label_sol),
            FadeIn(label_lua),
        ],
        mostrar_legenda=True,
        pausa_final=0.08,
    )

    # ======================================================
    # 5 — COMPARAÇÃO VISUAL
    # ======================================================

    linha_sol = Line(
        sol_grande.get_left(),
        sol_grande.get_right(),
        color=YELLOW,
        stroke_width=4,
    )

    linha_lua = Line(
        lua_pequena.get_left(),
        lua_pequena.get_right(),
        color=WHITE,
        stroke_width=4,
    )

    cena.play(
        FadeIn(linha_sol),
        FadeIn(linha_lua),
        run_time=0.45,
    )

    texto_400_tamanho = Text(
        "≈ 400× MAIOR",
        font_size=36,
        color=YELLOW,
        weight="BOLD",
    )

    texto_400_tamanho.move_to(
        [0, -2.30, 0]
    )

    cena.play(
        FadeIn(texto_400_tamanho),
        run_time=0.40,
    )

    cena.wait(0.45)

    # ======================================================
    # 6 — MAS HÁ UM PROBLEMA
    # ======================================================

    cena.narrar(
        (
            "Só que existe um detalhe fundamental: "
            "o Sol também está muito mais longe."
        ),
        FadeOut(
            VGroup(
                linha_sol,
                linha_lua,
                texto_400_tamanho,
                titulo_tamanho,
                numero_1,
                numero_2,
                label_sol,
                label_lua,
            )
        ),
        mostrar_legenda=True,
        pausa_final=0.08,
    )

    # ======================================================
    # 7 — DISTÂNCIA
    # ======================================================

    sol_distancia = sol_grande.copy()

    sol_distancia.scale(0.58)
    sol_distancia.move_to(
        LEFT * 5.2
    )

    lua_distancia = lua_pequena.copy()

    lua_distancia.scale(1.35)
    lua_distancia.move_to(
        RIGHT * 0.6
    )

    observador = Circle(
        radius=0.16,
        fill_color=WHITE,
        fill_opacity=1.0,
        stroke_opacity=0,
    )

    observador.move_to(
        RIGHT * 5.3
    )

    label_observador = Text(
        "TERRA",
        font_size=24,
        color=WHITE,
        weight="BOLD",
    ).next_to(
        observador,
        DOWN,
        buff=0.20,
    )

    cena.play(
        FadeOut(sol_grande),
        FadeOut(lua_pequena),
        FadeIn(sol_distancia),
        FadeIn(lua_distancia),
        FadeIn(observador),
        FadeIn(label_observador),
        run_time=0.70,
    )

    # ======================================================
    # 8 — LINHAS DE DISTÂNCIA
    # ======================================================

    seta_sol = Arrow(
        start=observador.get_left(),
        end=sol_distancia.get_right(),
        buff=0.10,
        color=YELLOW,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.035,
    )

    seta_lua = Arrow(
        start=observador.get_left(),
        end=lua_distancia.get_right(),
        buff=0.10,
        color=WHITE,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.07,
    )

    texto_distancia_sol = Text(
        "≈ 150 milhões km",
        font_size=25,
        color=YELLOW,
        weight="BOLD",
    )

    texto_distancia_sol.move_to(
        [-2.0, 1.25, 0]
    )

    texto_distancia_lua = Text(
        "≈ 384 mil km",
        font_size=25,
        color=WHITE,
        weight="BOLD",
    )

    texto_distancia_lua.move_to(
        [2.8, -1.20, 0]
    )

    cena.narrar(
        (
            "O Sol está aproximadamente "
            "quatrocentas vezes mais distante da Terra "
            "do que a Lua."
        ),
        [
            GrowArrow(seta_sol),
            GrowArrow(seta_lua),
            FadeIn(texto_distancia_sol),
            FadeIn(texto_distancia_lua),
        ],
        mostrar_legenda=True,
        pausa_final=0.10,
    )

    # ======================================================
    # 9 — SEGUNDO 400
    # ======================================================

    segredo = Text(
        "≈ 400× MAIS DISTANTE",
        font_size=42,
        color=YELLOW,
        weight="BOLD",
    )

    segredo.to_edge(
        UP,
        buff=0.55,
    )

    cena.play(
        FadeIn(segredo),
        run_time=0.40,
    )

    cena.wait(0.50)

    # ======================================================
    # 10 — A COINCIDÊNCIA
    # ======================================================

    cena.narrar(
        (
            "E é aqui que acontece a coincidência."
        ),
        FadeOut(
            VGroup(
                sol_distancia,
                lua_distancia,
                observador,
                label_observador,
                seta_sol,
                seta_lua,
                texto_distancia_sol,
                texto_distancia_lua,
                segredo,
            )
        ),
        mostrar_legenda=True,
        pausa_final=0.08,
    )

    # ======================================================
    # 11 — APARENTEMENTE IGUAIS
    # ======================================================

    sol_aparente = criar_sol(
        raio=1.10,
        posicao=LEFT * 2.25,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_coroa=False,
        intensidade=1.0,
    )

    lua_aparente = criar_lua(
        raio=1.07,
        posicao=RIGHT * 2.25,
        qualidade="cinema",
        mostrar_halo=False,
        mostrar_crateras=True,
        mostrar_label=False,
    )

    igual = Text(
        "≈",
        font_size=78,
        color=WHITE,
        weight="BOLD",
    )

    cena.narrar(
        (
            "Vistos daqui da Terra, "
            "os dois ocupam quase o mesmo tamanho no céu."
        ),
        [
            FadeIn(sol_aparente),
            FadeIn(lua_aparente),
            FadeIn(igual),
        ],
        mostrar_legenda=True,
        pausa_final=0.10,
    )

    # ======================================================
    # 12 — SOBREPOSIÇÃO
    # ======================================================

    cena.play(
        sol_aparente.animate.move_to(
            ORIGIN
        ),
        lua_aparente.animate.move_to(
            ORIGIN
        ),
        FadeOut(igual),
        run_time=2.0,
    )

    texto_perfeito = Text(
        "QUASE O MESMO TAMANHO APARENTE",
        font_size=31,
        color=YELLOW,
        weight="BOLD",
    )

    texto_perfeito.to_edge(
        UP,
        buff=0.60,
    )

    cena.play(
        FadeIn(texto_perfeito),
        run_time=0.45,
    )

    cena.narrar(
        (
            "Por isso, quando ficam perfeitamente alinhados, "
            "a Lua consegue esconder o Sol."
        ),
        mostrar_legenda=True,
        pausa_final=0.12,
    )

    # ======================================================
    # 13 — REVELAÇÃO 400 + 400
    # ======================================================

    cena.play(
        FadeOut(
            VGroup(
                sol_aparente,
                lua_aparente,
                texto_perfeito,
            )
        ),
        run_time=0.55,
    )

    quatrocentos_1 = Text(
        "400× MAIOR",
        font_size=48,
        color=YELLOW,
        weight="BOLD",
    )

    mais = Text(
        "+",
        font_size=52,
        color=WHITE,
        weight="BOLD",
    )

    quatrocentos_2 = Text(
        "400× MAIS LONGE",
        font_size=48,
        color=YELLOW,
        weight="BOLD",
    )

    formula_visual = VGroup(
        quatrocentos_1,
        mais,
        quatrocentos_2,
    ).arrange(
        DOWN,
        buff=0.30,
    )

    formula_visual.move_to(
        ORIGIN
    )

    cena.narrar(
        (
            "Quatrocentas vezes maior. "
            "Quatrocentas vezes mais longe."
        ),
        [
            FadeIn(quatrocentos_1),
            FadeIn(mais),
            FadeIn(quatrocentos_2),
        ],
        mostrar_legenda=False,
        pausa_final=0.15,
    )

    # ======================================================
    # 14 — MAS NÃO TERMINÁMOS
    # ======================================================

    cena.play(
        FadeOut(
            formula_visual
        ),
        run_time=0.45,
    )

    nova_pergunta = Text(
        "ENTÃO PORQUE NÃO HÁ UM ECLIPSE TODOS OS MESES?",
        font_size=34,
        color=YELLOW,
        weight="BOLD",
    )

    nova_pergunta.move_to(
        ORIGIN
    )

    cena.narrar(
        (
            "Mas se o encaixe é tão perfeito... "
            "porque não temos um eclipse todos os meses?"
        ),
        FadeIn(
            nova_pergunta
        ),
        mostrar_legenda=False,
        pausa_final=0.25,
    )

    cena.wait(
        0.80
    )

    # ======================================================
    # 15 — TRANSIÇÃO
    # ======================================================

    proximo = Text(
        "O ALINHAMENTO NÃO É TÃO SIMPLES",
        font_size=29,
        color=WHITE,
        weight="BOLD",
    )

    proximo.next_to(
        nova_pergunta,
        DOWN,
        buff=0.55,
    )

    cena.play(
        FadeIn(proximo),
        run_time=0.40,
    )

    cena.wait(
        0.75
    )

    cena.play(
        FadeOut(
            VGroup(
                nova_pergunta,
                proximo,
                starfield,
            )
        ),
        run_time=0.70,
    )