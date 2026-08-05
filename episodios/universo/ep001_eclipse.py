from manim import (
    BLACK,
    BLUE,
    Circle,
    DOWN,
    FadeIn,
    FadeOut,
    GREY_B,
    LEFT,
    Line,
    Polygon,
    RIGHT,
    Scene,
    Text,
    UP,
    VGroup,
    WHITE,
    Write,
    YELLOW,
)


class Episodio001Eclipse(Scene):
    def construct(self):
        titulo = Text(
            "COMO ACONTECE UM ECLIPSE SOLAR?",
            font_size=42,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP)

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
        ).move_to(UP * 1.5)

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
        ).next_to(sol, DOWN)

        nome_lua = Text(
            "LUA",
            font_size=23,
            color=GREY_B,
        ).next_to(lua, UP)

        nome_terra = Text(
            "TERRA",
            font_size=25,
            color=BLUE,
        ).next_to(terra, DOWN)

        self.play(Write(titulo))

        self.play(
            FadeIn(sol),
            FadeIn(lua),
            FadeIn(terra),
            FadeIn(nome_sol),
            FadeIn(nome_lua),
            FadeIn(nome_terra),
        )

        nova_posicao = LEFT * 0.15

        self.play(
            lua.animate.move_to(nova_posicao),
            nome_lua.animate.move_to(nova_posicao + UP * 0.65),
            run_time=2,
        )

        sombra = Polygon(
            nova_posicao + UP * 0.24,
            terra.get_center() + UP * 0.20,
            terra.get_center() + DOWN * 0.20,
            nova_posicao + DOWN * 0.24,
            fill_color=BLACK,
            fill_opacity=0.85,
            stroke_color=GREY_B,
            stroke_opacity=0.4,
        )

        sombra.set_z_index(-1)

        self.play(FadeIn(sombra))

        linha_sol_lua = Line(
            sol.get_right(),
            lua.get_left(),
            color=YELLOW,
        )

        linha_lua_terra = Line(
            lua.get_right(),
            terra.get_left(),
            color=GREY_B,
        )

        alinhamento = Text(
            "SOL  →  LUA  →  TERRA",
            font_size=35,
            color=WHITE,
            weight="BOLD",
        ).move_to(DOWN * 2.5)

        self.play(
            FadeIn(linha_sol_lua),
            FadeIn(linha_lua_terra),
            Write(alinhamento),
        )

        self.wait(2)

        explicacao = Text(
            "A Lua bloqueia a luz do Sol\ne projeta uma sombra sobre a Terra.",
            font_size=29,
            color=WHITE,
            line_spacing=1.2,
        ).move_to(DOWN * 2.35)

        self.play(
            FadeOut(alinhamento),
            FadeIn(explicacao),
        )

        self.wait(2)

        elementos = VGroup(
            titulo,
            sol,
            lua,
            terra,
            nome_sol,
            nome_lua,
            nome_terra,
            sombra,
            linha_sol_lua,
            linha_lua_terra,
            explicacao,
        )

        self.play(FadeOut(elementos))

        final = Text(
            "ISTO É UM ECLIPSE SOLAR",
            font_size=46,
            color=YELLOW,
            weight="BOLD",
        )

        self.play(Write(final))
        self.wait(2)
        self.play(FadeOut(final))