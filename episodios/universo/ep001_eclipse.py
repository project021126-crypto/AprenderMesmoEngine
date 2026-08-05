from manim import (
    BLACK,
    BLUE,
    DOWN,
    FadeIn,
    FadeOut,
    GREY_B,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    GrowFromCenter,
    Line,
    Polygon,
    Text,
    VGroup,
    Write,
)

from engine.scene import CenaAprenderMesmo


class Episodio001Eclipse(CenaAprenderMesmo):
    """
    Universo — EP001 — Eclipse Solar

    Versão com:
    - narração em português europeu;
    - legendas automáticas;
    - animações sincronizadas;
    - entrada forte;
    - explicação visual progressiva.
    """

    def construct(self) -> None:
        # =====================================================
        # CENA 1 — ENTRADA FORTE
        # =====================================================

        estrelas = VGroup(
            *[
                Dot(
                    point=[
                        -6.5 + (indice % 13),
                        -3.2 + ((indice * 7) % 7),
                        0,
                    ],
                    radius=0.018,
                    color=WHITE,
                ).set_opacity(0.45)
                for indice in range(70)
            ]
        )

        sol_abertura = Circle(
            radius=1.75,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        )

        lua_abertura = Circle(
            radius=1.68,
            color=GREY_B,
            fill_color=BLACK,
            fill_opacity=1,
        ).move_to(RIGHT * 5)

        self.add(estrelas)

        self.narrar(
            "Durante alguns minutos, o dia pode transformar-se em noite.",
            [
                GrowFromCenter(sol_abertura),
            ],
        )

        self.narrar(
            "E tudo acontece porque a Lua passa exatamente à nossa frente.",
            [
                lua_abertura.animate.move_to(ORIGIN),
            ],
        )

        coroa = VGroup(
            *[
                Circle(
                    radius=1.75 + indice * 0.11,
                    stroke_color=WHITE,
                    stroke_opacity=max(
                        0.05,
                        0.32 - indice * 0.045,
                    ),
                    stroke_width=2,
                )
                for indice in range(1, 7)
            ]
        )

        self.narrar(
            "Mas como pode a Lua esconder um Sol muito maior do que ela?",
            [
                FadeIn(coroa),
            ],
        )

        titulo = Text(
            "O DIA EM QUE O SOL DESAPARECE",
            font_size=44,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.45)

        self.play(
            Write(titulo),
            run_time=1,
        )

        self.wait(0.7)

        self.play(
            FadeOut(
                VGroup(
                    sol_abertura,
                    lua_abertura,
                    coroa,
                    titulo,
                )
            ),
            run_time=0.8,
        )

        # =====================================================
        # CENA 2 — APRESENTAR SOL, LUA E TERRA
        # =====================================================

        sol = Circle(
            radius=0.95,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(LEFT * 5)

        lua = Circle(
            radius=0.28,
            color=GREY_B,
            fill_color=GREY_B,
            fill_opacity=1,
        ).move_to(UP * 1.6)

        terra = Circle(
            radius=0.68,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
        ).move_to(RIGHT * 4.7)

        nome_sol = Text(
            "SOL",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        ).next_to(sol, DOWN, buff=0.25)

        nome_lua = Text(
            "LUA",
            font_size=23,
            color=GREY_B,
            weight="BOLD",
        ).next_to(lua, UP, buff=0.22)

        nome_terra = Text(
            "TERRA",
            font_size=25,
            color=BLUE,
            weight="BOLD",
        ).next_to(terra, DOWN, buff=0.25)

        sistema = VGroup(
            sol,
            lua,
            terra,
            nome_sol,
            nome_lua,
            nome_terra,
        )

        self.narrar(
            "Para perceber o eclipse, precisamos de observar os três astros a partir do espaço.",
            [
                FadeIn(sistema),
            ],
        )

        # =====================================================
        # CENA 3 — ALINHAMENTO
        # =====================================================

        nova_posicao_lua = LEFT * 0.15

        self.narrar(
            "Um eclipse solar acontece quando a Lua passa entre o Sol e a Terra.",
            [
                lua.animate.move_to(nova_posicao_lua),
                nome_lua.animate.move_to(
                    nova_posicao_lua + UP * 0.65
                ),
            ],
        )

        linha_sol_lua = Line(
            sol.get_right(),
            lua.get_left(),
            color=YELLOW,
            stroke_opacity=0.65,
            stroke_width=3,
        )

        linha_lua_terra = Line(
            lua.get_right(),
            terra.get_left(),
            color=GREY_B,
            stroke_opacity=0.65,
            stroke_width=3,
        )

        alinhamento = Text(
            "SOL  →  LUA  →  TERRA",
            font_size=35,
            color=WHITE,
            weight="BOLD",
        ).move_to(DOWN * 2.45)

        self.narrar(
            "Nesse momento, os três astros ficam quase perfeitamente alinhados.",
            [
                FadeIn(linha_sol_lua),
                FadeIn(linha_lua_terra),
                Write(alinhamento),
            ],
        )

        # =====================================================
        # CENA 4 — SOMBRA DA LUA
        # =====================================================

        sombra = Polygon(
            lua.get_center() + UP * 0.24,
            terra.get_center() + UP * 0.20,
            terra.get_center() + DOWN * 0.20,
            lua.get_center() + DOWN * 0.24,
            fill_color=BLACK,
            fill_opacity=0.85,
            stroke_color=GREY_B,
            stroke_opacity=0.45,
            stroke_width=2,
        )

        sombra.set_z_index(-1)

        zona_total = Dot(
            terra.get_center() + LEFT * 0.54,
            radius=0.10,
            color=BLACK,
        )

        destaque = Circle(
            radius=0.18,
            stroke_color=WHITE,
            stroke_width=2,
        ).move_to(zona_total)

        self.narrar(
            "A Lua bloqueia parte da luz e projeta uma pequena sombra sobre a Terra.",
            [
                FadeIn(sombra),
                FadeIn(zona_total),
                FadeIn(destaque),
            ],
        )

        self.narrar(
            "Quem estiver dentro desta região consegue ver o Sol completamente tapado.",
        )

        self.play(
            FadeOut(
                VGroup(
                    alinhamento,
                    linha_sol_lua,
                    linha_lua_terra,
                    sombra,
                    zona_total,
                    destaque,
                    sistema,
                )
            ),
            run_time=0.8,
        )

        # =====================================================
        # CENA 5 — O MISTÉRIO DO TAMANHO
        # =====================================================

        sol_grande = Circle(
            radius=1.55,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(LEFT * 3.3)

        lua_pequena = Circle(
            radius=0.24,
            color=GREY_B,
            fill_color=GREY_B,
            fill_opacity=1,
        ).move_to(RIGHT * 3.2)

        pergunta = Text(
            "COMO CONSEGUE A LUA ESCONDER O SOL?",
            font_size=38,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.5)

        self.narrar(
            "A Lua parece pequena ao lado do Sol. E é mesmo.",
            [
                FadeIn(sol_grande),
                FadeIn(lua_pequena),
                Write(pergunta),
            ],
        )

        numero_sol = Text(
            "1 390 000 km",
            font_size=28,
            color=YELLOW,
        ).next_to(sol_grande, DOWN, buff=0.3)

        numero_lua = Text(
            "3 474 km",
            font_size=28,
            color=GREY_B,
        ).next_to(lua_pequena, DOWN, buff=0.3)

        comparacao = Text(
            "CERCA DE 400 VEZES MAIOR",
            font_size=37,
            color=YELLOW,
            weight="BOLD",
        ).move_to(UP * 2.1)

        self.narrar(
            "O Sol tem aproximadamente quatrocentas vezes o diâmetro da Lua.",
            [
                FadeOut(pergunta),
                FadeIn(numero_sol),
                FadeIn(numero_lua),
                Write(comparacao),
            ],
        )

        # =====================================================
        # CENA 6 — A DISTÂNCIA EXPLICA TUDO
        # =====================================================

        self.play(
            FadeOut(
                VGroup(
                    numero_sol,
                    numero_lua,
                    comparacao,
                )
            ),
            sol_grande.animate.scale(0.48).move_to(LEFT * 5),
            lua_pequena.animate.scale(1.4).move_to(RIGHT * 0.4),
            run_time=1.1,
        )

        terra_observador = Circle(
            radius=0.55,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
        ).move_to(RIGHT * 5.2)

        linha_sol = Line(
            terra_observador.get_center(),
            sol_grande.get_center(),
            color=YELLOW,
            stroke_opacity=0.5,
        )

        linha_lua = Line(
            terra_observador.get_center(),
            lua_pequena.get_center(),
            color=GREY_B,
            stroke_opacity=0.5,
        )

        self.narrar(
            "Mas o Sol também está aproximadamente quatrocentas vezes mais longe da Terra.",
            [
                FadeIn(terra_observador),
                FadeIn(linha_sol),
                FadeIn(linha_lua),
            ],
        )

        aparente_sol = Circle(
            radius=0.58,
            stroke_color=YELLOW,
            stroke_width=7,
        ).move_to(LEFT * 1.0)

        aparente_lua = Circle(
            radius=0.56,
            stroke_color=GREY_B,
            stroke_width=5,
        ).move_to(LEFT * 1.0)

        self.narrar(
            "Por isso, vistos daqui, os dois parecem ter quase exatamente o mesmo tamanho.",
            [
                FadeIn(aparente_sol),
                FadeIn(aparente_lua),
            ],
        )

        coincidencia = Text(
            "UMA COINCIDÊNCIA CÓSMICA",
            font_size=44,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.5)

        self.narrar(
            "É uma coincidência cósmica rara, e é ela que torna possível um eclipse total.",
            [
                Write(coincidencia),
            ],
        )

        self.play(
            FadeOut(
                VGroup(
                    sol_grande,
                    lua_pequena,
                    terra_observador,
                    linha_sol,
                    linha_lua,
                    aparente_sol,
                    aparente_lua,
                    coincidencia,
                    estrelas,
                )
            ),
            run_time=1,
        )

        # =====================================================
        # CENA 7 — FINAL
        # =====================================================

        frase_1 = Text(
            "O SOL NÃO DESAPARECE.",
            font_size=47,
            color=WHITE,
            weight="BOLD",
        ).move_to(UP * 0.45)

        frase_2 = Text(
            "A LUA PASSA À NOSSA FRENTE.",
            font_size=48,
            color=YELLOW,
            weight="BOLD",
        ).next_to(frase_1, DOWN, buff=0.4)

        self.narrar(
            "O Sol não desaparece.",
            [
                Write(frase_1),
            ],
        )

        self.narrar(
            "É a Lua que passa exatamente à nossa frente.",
            [
                Write(frase_2),
            ],
        )

        assinatura = Text(
            "APRENDER MESMO",
            font_size=28,
            color=GREY_B,
            weight="BOLD",
        ).next_to(frase_2, DOWN, buff=0.8)

        self.play(
            FadeIn(assinatura),
            run_time=0.7,
        )

        self.wait(2)

        self.play(
            FadeOut(
                VGroup(
                    frase_1,
                    frase_2,
                    assinatura,
                )
            ),
            run_time=0.8,
        )