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

from engine.scene import CenaShort


class Episodio001EclipseShort(CenaShort):
    """
    Universo — EP001 — Eclipse Solar

    Short vertical 9:16:
    - todos os objetos dentro da área segura;
    - Sol, Lua e Terra sempre visíveis;
    - eclipse com coroa intensa;
    - legendas fortes;
    - chamada final narrada.
    """

    def construct(self) -> None:
        # =====================================================
        # FUNDO
        # =====================================================

        estrelas = VGroup(
            *[
                Dot(
                    point=[
                        -3.25 + (indice % 8) * 0.92,
                        -5.35 + ((indice * 5) % 12) * 0.88,
                        0,
                    ],
                    radius=0.018,
                    color=WHITE,
                ).set_opacity(0.48)
                for indice in range(72)
            ]
        )

        self.add(estrelas)

        # =====================================================
        # CENA 1 — HOOK
        # =====================================================

        sol_abertura = Circle(
            radius=1.20,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(UP * 2.25)

        lua_abertura = Circle(
            radius=1.14,
            color=GREY_B,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(DOWN * 3.8)

        self.narrar(
            "Durante alguns minutos, o dia pode transformar-se em noite.",
            GrowFromCenter(sol_abertura),
        )

        self.narrar(
            "E tudo acontece porque a Lua passa exatamente à nossa frente.",
            lua_abertura.animate.move_to(
                sol_abertura.get_center()
            ),
        )

        coroa = VGroup(
            *[
                Circle(
                    radius=1.20 + indice * 0.11,
                    stroke_color=WHITE,
                    stroke_opacity=max(
                        0.12,
                        0.72 - indice * 0.10,
                    ),
                    stroke_width=max(
                        1.5,
                        5 - indice * 0.55,
                    ),
                ).move_to(sol_abertura.get_center())
                for indice in range(1, 7)
            ]
        )

        raios_coroa = VGroup(
            *[
                Line(
                    start=sol_abertura.get_center()
                    + [
                        0,
                        1.35 + indice * 0.04,
                        0,
                    ],
                    end=sol_abertura.get_center()
                    + [
                        0,
                        1.75 + indice * 0.08,
                        0,
                    ],
                    color=WHITE,
                    stroke_opacity=0.38,
                    stroke_width=2,
                ).rotate(
                    indice * 0.52,
                    about_point=sol_abertura.get_center(),
                )
                for indice in range(12)
            ]
        )

        self.narrar(
            "Mas como pode a Lua esconder um Sol muito maior do que ela?",
            [
                FadeIn(coroa),
                FadeIn(raios_coroa),
            ],
        )

        pergunta = Text(
            "COMO A LUA\nESCONDE O SOL?",
            font_size=47,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.85,
        ).move_to(DOWN * 2.25)

        self.play(
            Write(pergunta),
            run_time=0.9,
        )

        self.wait(0.45)

        self.play(
            FadeOut(
                VGroup(
                    sol_abertura,
                    lua_abertura,
                    coroa,
                    raios_coroa,
                    pergunta,
                )
            ),
            run_time=0.65,
        )

        # =====================================================
        # CENA 2 — SOL, LUA E TERRA
        # =====================================================

        sol = Circle(
            radius=0.68,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(UP * 4.20)

        lua = Circle(
            radius=0.24,
            color=GREY_B,
            fill_color=GREY_B,
            fill_opacity=1,
            stroke_width=2,
        ).move_to(LEFT * 2.45 + UP * 0.65)

        terra = Circle(
            radius=0.68,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(DOWN * 3.40)

        nome_sol = Text(
            "SOL",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        ).next_to(
            sol,
            DOWN,
            buff=0.18,
        )

        nome_lua = Text(
            "LUA",
            font_size=23,
            color=GREY_B,
            weight="BOLD",
        ).next_to(
            lua,
            UP,
            buff=0.18,
        )

        nome_terra = Text(
            "TERRA",
            font_size=24,
            color=BLUE,
            weight="BOLD",
        ).next_to(
            terra,
            DOWN,
            buff=0.18,
        )

        sistema = VGroup(
            sol,
            lua,
            terra,
            nome_sol,
            nome_lua,
            nome_terra,
        )

        self.narrar(
            "Um eclipse solar acontece quando a Lua passa entre o Sol e a Terra.",
            FadeIn(sistema),
        )

        # =====================================================
        # CENA 3 — ALINHAMENTO COMPLETO
        # =====================================================

        posicao_lua = UP * 0.45

        self.narrar(
            "Nesse momento, os três astros ficam quase perfeitamente alinhados.",
            [
                lua.animate.move_to(posicao_lua),
                nome_lua.animate.move_to(
                    posicao_lua + LEFT * 0.85
                ),
            ],
        )

        linha_sol_lua = Line(
            sol.get_bottom(),
            lua.get_top(),
            color=YELLOW,
            stroke_opacity=0.85,
            stroke_width=4,
        )

        linha_lua_terra = Line(
            lua.get_bottom(),
            terra.get_top(),
            color=GREY_B,
            stroke_opacity=0.85,
            stroke_width=4,
        )

        alinhamento = Text(
            "SOL  →  LUA  →  TERRA",
            font_size=30,
            color=WHITE,
            weight="BOLD",
        ).move_to(DOWN * 5.15)

        self.play(
            FadeIn(linha_sol_lua),
            FadeIn(linha_lua_terra),
            Write(alinhamento),
            run_time=0.8,
        )

        # =====================================================
        # CENA 4 — SOMBRA DA LUA
        # =====================================================

        sombra = Polygon(
            lua.get_center() + LEFT * 0.17 + DOWN * 0.08,
            terra.get_center() + LEFT * 0.23 + UP * 0.54,
            terra.get_center() + RIGHT * 0.23 + UP * 0.54,
            lua.get_center() + RIGHT * 0.17 + DOWN * 0.08,
            fill_color=BLACK,
            fill_opacity=0.90,
            stroke_color=GREY_B,
            stroke_opacity=0.55,
            stroke_width=2,
        )

        sombra.set_z_index(-1)

        zona_total = Dot(
            terra.get_center() + UP * 0.54,
            radius=0.09,
            color=BLACK,
        )

        destaque = Circle(
            radius=0.19,
            stroke_color=WHITE,
            stroke_width=3,
        ).move_to(zona_total)

        self.narrar(
            "A Lua bloqueia parte da luz e projeta uma pequena sombra sobre a Terra.",
            [
                FadeIn(sombra),
                FadeIn(zona_total),
                FadeIn(destaque),
            ],
        )

        self.play(
            FadeOut(
                VGroup(
                    sistema,
                    linha_sol_lua,
                    linha_lua_terra,
                    alinhamento,
                    sombra,
                    zona_total,
                    destaque,
                )
            ),
            run_time=0.65,
        )

        # =====================================================
        # CENA 5 — TAMANHO E DISTÂNCIA
        # =====================================================

        titulo_tamanho = Text(
            "PARECE IMPOSSÍVEL...",
            font_size=37,
            color=WHITE,
            weight="BOLD",
        ).move_to(UP * 5.10)

        sol_grande = Circle(
            radius=1.10,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(UP * 2.15)

        lua_pequena = Circle(
            radius=0.22,
            color=GREY_B,
            fill_color=GREY_B,
            fill_opacity=1,
            stroke_width=2,
        ).move_to(DOWN * 0.85)

        comparacao = Text(
            "O SOL É CERCA DE\n400 VEZES MAIOR",
            font_size=37,
            color=YELLOW,
            weight="BOLD",
            line_spacing=0.88,
        ).move_to(DOWN * 3.50)

        self.narrar(
            "O Sol tem aproximadamente quatrocentas vezes o diâmetro da Lua.",
            [
                Write(titulo_tamanho),
                FadeIn(sol_grande),
                FadeIn(lua_pequena),
                Write(comparacao),
            ],
        )

        distancia = Text(
            "MAS TAMBÉM ESTÁ\nCERCA DE 400 VEZES\nMAIS LONGE",
            font_size=36,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.88,
        ).move_to(DOWN * 3.45)

        self.narrar(
            "Mas também está aproximadamente quatrocentas vezes mais longe da Terra.",
            [
                FadeOut(comparacao),
                Write(distancia),
            ],
        )

        aparente_sol = Circle(
            radius=0.90,
            stroke_color=YELLOW,
            stroke_width=9,
        ).move_to(UP * 1.30)

        aparente_lua = Circle(
            radius=0.85,
            stroke_color=WHITE,
            stroke_width=5,
        ).move_to(UP * 1.30)

        ondas_aparentes = VGroup(
            *[
                Circle(
                    radius=0.95 + indice * 0.12,
                    stroke_color=YELLOW,
                    stroke_opacity=max(
                        0.10,
                        0.60 - indice * 0.09,
                    ),
                    stroke_width=3,
                ).move_to(UP * 1.30)
                for indice in range(1, 6)
            ]
        )

        self.narrar(
            "Por isso, vistos daqui, os dois parecem ter quase exatamente o mesmo tamanho.",
            [
                FadeOut(titulo_tamanho),
                FadeOut(sol_grande),
                FadeOut(lua_pequena),
                FadeOut(distancia),
                FadeIn(aparente_sol),
                FadeIn(aparente_lua),
                FadeIn(ondas_aparentes),
            ],
        )

        self.play(
            FadeOut(
                VGroup(
                    aparente_sol,
                    aparente_lua,
                    ondas_aparentes,
                    estrelas,
                )
            ),
            run_time=0.65,
        )

        # =====================================================
        # CENA 6 — CONCLUSÃO
        # =====================================================

        frase_1 = Text(
            "O SOL NÃO\nDESAPARECE.",
            font_size=44,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.86,
        ).move_to(UP * 2.30)

        frase_2 = Text(
            "A LUA PASSA\nÀ NOSSA FRENTE.",
            font_size=47,
            color=YELLOW,
            weight="BOLD",
            line_spacing=0.85,
        ).move_to(DOWN * 0.75)

        self.narrar(
            "O Sol não desaparece.",
            Write(frase_1),
        )

        self.narrar(
            "É a Lua que passa exatamente à nossa frente.",
            Write(frase_2),
        )

        self.play(
            FadeOut(
                VGroup(
                    frase_1,
                    frase_2,
                )
            ),
            run_time=0.55,
        )

        # =====================================================
        # CENA 7 — CHAMADA FINAL
        # =====================================================

        chamada = Text(
            "SEGUE O NOSSO CANAL",
            font_size=43,
            color=WHITE,
            weight="BOLD",
        ).move_to(UP * 2.25)

        canal = Text(
            "APRENDER MESMO",
            font_size=49,
            color=YELLOW,
            weight="BOLD",
        ).move_to(UP * 0.60)

        complemento = Text(
            "PARA APRENDER CIÊNCIA\nDE FORMA SIMPLES E VISUAL",
            font_size=31,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.90,
        ).move_to(DOWN * 1.75)

        self.narrar(
            "Segue o nosso canal Aprender Mesmo para aprender ciência de forma simples e visual.",
            [
                Write(chamada),
                FadeIn(canal),
                FadeIn(complemento),
            ],
            mostrar_legenda=False,
        )

        self.wait(1)

        self.play(
            FadeOut(
                VGroup(
                    chamada,
                    canal,
                    complemento,
                )
            ),
            run_time=0.65,
        )