from manim import (
    BLACK, BLUE, DOWN, FadeIn, FadeOut, GREY_B, LEFT, ORIGIN, RIGHT,
    UP, WHITE, YELLOW, Circle, Dot, GrowFromCenter, Line, Polygon,
    Text, VGroup, Write
)

from engine.scene import CenaShort


class Episodio001EclipseShort(CenaShort):
    """Short vertical 9:16 sobre eclipses solares."""

    def construct(self) -> None:
        estrelas = VGroup(
            *[
                Dot(
                    point=[
                        -3.5 + (indice % 8),
                        -6.2 + ((indice * 5) % 13),
                        0,
                    ],
                    radius=0.018,
                    color=WHITE,
                ).set_opacity(0.42)
                for indice in range(72)
            ]
        )

        sol_abertura = Circle(
            radius=1.55,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(UP * 1.5)

        lua_abertura = Circle(
            radius=1.48,
            color=GREY_B,
            fill_color=BLACK,
            fill_opacity=1,
        ).move_to(DOWN * 5.7)

        self.add(estrelas)

        self.narrar(
            "Durante alguns minutos, o dia pode transformar-se em noite.",
            GrowFromCenter(sol_abertura),
        )

        self.narrar(
            "E tudo acontece porque a Lua passa exatamente à nossa frente.",
            lua_abertura.animate.move_to(sol_abertura.get_center()),
        )

        coroa = VGroup(
            *[
                Circle(
                    radius=1.55 + indice * 0.11,
                    stroke_color=WHITE,
                    stroke_opacity=max(0.05, 0.32 - indice * 0.045),
                    stroke_width=2,
                ).move_to(sol_abertura)
                for indice in range(1, 7)
            ]
        )

        self.narrar(
            "Mas como pode a Lua esconder um Sol muito maior do que ela?",
            FadeIn(coroa),
        )

        titulo = Text(
            "COMO A LUA\nESCONDE O SOL?",
            font_size=54,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.85,
        ).move_to(UP * 4.8)

        self.play(Write(titulo), run_time=1)
        self.wait(0.45)

        self.play(
            FadeOut(VGroup(sol_abertura, lua_abertura, coroa, titulo)),
            run_time=0.7,
        )

        sol = Circle(
            radius=0.85,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(UP * 4.1)

        lua = Circle(
            radius=0.25,
            color=GREY_B,
            fill_color=GREY_B,
            fill_opacity=1,
        ).move_to(LEFT * 2.4 + DOWN * 0.3)

        terra = Circle(
            radius=0.70,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
        ).move_to(DOWN * 4.2)

        nome_sol = Text(
            "SOL", font_size=27, color=YELLOW, weight="BOLD"
        ).next_to(sol, UP, buff=0.25)

        nome_lua = Text(
            "LUA", font_size=25, color=GREY_B, weight="BOLD"
        ).next_to(lua, UP, buff=0.20)

        nome_terra = Text(
            "TERRA", font_size=27, color=BLUE, weight="BOLD"
        ).next_to(terra, DOWN, buff=0.25)

        sistema = VGroup(sol, lua, terra, nome_sol, nome_lua, nome_terra)

        self.narrar(
            "Um eclipse solar acontece quando a Lua passa entre o Sol e a Terra.",
            FadeIn(sistema),
        )

        posicao_lua = ORIGIN

        self.narrar(
            "Nesse momento, os três astros ficam quase perfeitamente alinhados.",
            [
                lua.animate.move_to(posicao_lua),
                nome_lua.animate.move_to(
                    posicao_lua + LEFT * 0.85 + UP * 0.25
                ),
            ],
        )

        linha_sol_lua = Line(
            sol.get_bottom(),
            lua.get_top(),
            color=YELLOW,
            stroke_opacity=0.65,
            stroke_width=3,
        )

        linha_lua_terra = Line(
            lua.get_bottom(),
            terra.get_top(),
            color=GREY_B,
            stroke_opacity=0.65,
            stroke_width=3,
        )

        self.play(
            FadeIn(linha_sol_lua),
            FadeIn(linha_lua_terra),
            run_time=0.8,
        )

        sombra = Polygon(
            lua.get_center() + LEFT * 0.22 + DOWN * 0.18,
            terra.get_center() + LEFT * 0.25 + UP * 0.55,
            terra.get_center() + RIGHT * 0.25 + UP * 0.55,
            lua.get_center() + RIGHT * 0.22 + DOWN * 0.18,
            fill_color=BLACK,
            fill_opacity=0.86,
            stroke_color=GREY_B,
            stroke_opacity=0.42,
            stroke_width=2,
        )
        sombra.set_z_index(-1)

        zona_total = Dot(
            terra.get_center() + UP * 0.55,
            radius=0.10,
            color=BLACK,
        )

        destaque = Circle(
            radius=0.20,
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

        self.play(
            FadeOut(
                VGroup(
                    sistema,
                    linha_sol_lua,
                    linha_lua_terra,
                    sombra,
                    zona_total,
                    destaque,
                )
            ),
            run_time=0.7,
        )

        sol_grande = Circle(
            radius=1.55,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(UP * 2.7)

        lua_pequena = Circle(
            radius=0.24,
            color=GREY_B,
            fill_color=GREY_B,
            fill_opacity=1,
        ).move_to(DOWN * 1.2)

        comparacao = Text(
            "O SOL É CERCA DE\n400 VEZES MAIOR",
            font_size=42,
            color=YELLOW,
            weight="BOLD",
            line_spacing=0.88,
        ).move_to(DOWN * 4.1)

        self.narrar(
            "O Sol tem aproximadamente quatrocentas vezes o diâmetro da Lua.",
            [
                FadeIn(sol_grande),
                FadeIn(lua_pequena),
                Write(comparacao),
            ],
        )

        distancia = Text(
            "MAS TAMBÉM ESTÁ\nCERCA DE 400 VEZES\nMAIS LONGE",
            font_size=42,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.88,
        ).move_to(DOWN * 3.9)

        self.narrar(
            "Mas também está aproximadamente quatrocentas vezes mais longe da Terra.",
            [
                FadeOut(comparacao),
                Write(distancia),
            ],
        )

        aparente_sol = Circle(
            radius=0.86,
            stroke_color=YELLOW,
            stroke_width=8,
        ).move_to(UP * 1.5)

        aparente_lua = Circle(
            radius=0.82,
            stroke_color=GREY_B,
            stroke_width=5,
        ).move_to(UP * 1.5)

        self.narrar(
            "Por isso, vistos daqui, os dois parecem ter quase exatamente o mesmo tamanho.",
            [
                FadeOut(sol_grande),
                FadeOut(lua_pequena),
                FadeOut(distancia),
                FadeIn(aparente_sol),
                FadeIn(aparente_lua),
            ],
        )

        self.play(
            FadeOut(VGroup(aparente_sol, aparente_lua, estrelas)),
            run_time=0.7,
        )

        frase_1 = Text(
            "O SOL NÃO DESAPARECE.",
            font_size=47,
            color=WHITE,
            weight="BOLD",
        ).move_to(UP * 1.0)

        frase_2 = Text(
            "A LUA PASSA\nÀ NOSSA FRENTE.",
            font_size=51,
            color=YELLOW,
            weight="BOLD",
            line_spacing=0.85,
        ).next_to(frase_1, DOWN, buff=0.55)

        self.narrar(
            "O Sol não desaparece.",
            Write(frase_1),
        )

        self.narrar(
            "É a Lua que passa exatamente à nossa frente.",
            Write(frase_2),
        )

        assinatura = Text(
            "APRENDER MESMO",
            font_size=29,
            color=GREY_B,
            weight="BOLD",
        ).move_to(DOWN * 4.8)

        self.play(FadeIn(assinatura), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(frase_1, frase_2, assinatura)),
            run_time=0.7,
        )
