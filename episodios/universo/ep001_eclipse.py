from manim import (
    BLACK,
    BLUE,
    DOWN,
    FadeIn,
    FadeOut,
    GREY_B,
    LEFT,
    Line,
    Polygon,
    RIGHT,
    Text,
    UP,
    VGroup,
    WHITE,
    Write,
    YELLOW,
)

from engine.core import FormatoVideo, StudioConfig
from engine.scene import CenaAprenderMesmo
from engine.universo import Lua, Sol, Terra


class Episodio001Eclipse(CenaAprenderMesmo):
    """
    Episódio 001 — Eclipse Solar

    Versão temporária de teste:
    não utiliza narração nem manim-voiceover.
    """

    studio_config = StudioConfig(
        formato=FormatoVideo.LONG,
    )

    def construct(self) -> None:
        self.studio.selecionar_episodio(
            "Universo — EP001 — Eclipse Solar"
        )

        # =====================================================
        # CENA 1 — TÍTULO
        # =====================================================

        titulo = Text(
            "COMO ACONTECE UM ECLIPSE SOLAR?",
            font_size=42,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.5)

        subtitulo = Text(
            "Sol, Lua e Terra perfeitamente alinhados",
            font_size=25,
            color=GREY_B,
        ).next_to(titulo, DOWN, buff=0.25)

        self.play(
            Write(titulo),
            run_time=1.2,
        )

        self.play(
            FadeIn(subtitulo),
            run_time=0.8,
        )

        self.wait(1)

        # =====================================================
        # CENA 2 — APRESENTAR OS ASTROS
        # =====================================================

        sol = Sol(raio=0.95)
        sol.move_to(LEFT * 5)

        lua = Lua(raio=0.28)
        lua.move_to(UP * 1.5)

        terra = Terra(raio=0.68)
        terra.move_to(RIGHT * 4.7)

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

        self.play(
            FadeOut(subtitulo),
            FadeIn(sistema),
            run_time=1.2,
        )

        self.wait(1)

        # =====================================================
        # CENA 3 — LUA MOVE-SE ENTRE O SOL E A TERRA
        # =====================================================

        nova_posicao_lua = LEFT * 0.15

        self.play(
            lua.animate.move_to(nova_posicao_lua),
            nome_lua.animate.move_to(
                nova_posicao_lua + UP * 0.65
            ),
            run_time=2,
        )

        self.wait(0.5)

        # =====================================================
        # CENA 4 — CRIAR A SOMBRA
        # =====================================================

        sombra = Polygon(
            lua.get_center() + UP * 0.24,
            terra.get_center() + UP * 0.20,
            terra.get_center() + DOWN * 0.20,
            lua.get_center() + DOWN * 0.24,
            fill_color=BLACK,
            fill_opacity=0.82,
            stroke_color=GREY_B,
            stroke_opacity=0.45,
            stroke_width=2,
        )

        sombra.set_z_index(-1)

        self.play(
            FadeIn(sombra),
            run_time=1.2,
        )

        self.wait(1)

        # =====================================================
        # CENA 5 — MOSTRAR O ALINHAMENTO
        # =====================================================

        linha_sol_lua = Line(
            sol.get_right(),
            lua.get_left(),
            color=YELLOW,
            stroke_opacity=0.6,
            stroke_width=3,
        )

        linha_lua_terra = Line(
            lua.get_right(),
            terra.get_left(),
            color=GREY_B,
            stroke_opacity=0.6,
            stroke_width=3,
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
            run_time=1.4,
        )

        self.wait(2)

        # =====================================================
        # CENA 6 — EXPLICAÇÃO VISUAL
        # =====================================================

        explicacao_1 = Text(
            "A Lua bloqueia parte da luz do Sol",
            font_size=30,
            color=WHITE,
        ).move_to(DOWN * 2.25)

        explicacao_2 = Text(
            "e projeta uma sombra sobre a Terra.",
            font_size=30,
            color=WHITE,
        ).next_to(explicacao_1, DOWN, buff=0.25)

        self.play(
            FadeOut(alinhamento),
            FadeIn(explicacao_1),
            FadeIn(explicacao_2),
            run_time=1,
        )

        self.wait(2)

        # =====================================================
        # CENA 7 — FINAL
        # =====================================================

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
            explicacao_1,
            explicacao_2,
        )

        self.play(
            FadeOut(elementos),
            run_time=1,
        )

        frase_final = Text(
            "ISTO É UM ECLIPSE SOLAR",
            font_size=47,
            color=YELLOW,
            weight="BOLD",
        )

        assinatura = Text(
            "APRENDER MESMO",
            font_size=27,
            color=GREY_B,
            weight="BOLD",
        ).next_to(frase_final, DOWN, buff=0.5)

        self.play(
            Write(frase_final),
            run_time=1.2,
        )

        self.play(
            FadeIn(assinatura),
            run_time=0.7,
        )

        self.wait(2)

        self.play(
            FadeOut(
                VGroup(
                    frase_final,
                    assinatura,
                )
            ),
            run_time=0.8,
        )