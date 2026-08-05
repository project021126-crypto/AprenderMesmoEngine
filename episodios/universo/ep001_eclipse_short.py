from manim import (
    BLACK,
    BLUE,
    DOWN,
    FadeIn,
    FadeOut,
    GREY_B,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    GrowFromCenter,
    Line,
    Polygon,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
    config,
)

# O formato é definido antes da criação da câmara.
config.frame_width = 8.0
config.frame_height = 14.222

from engine.scene import CenaShort  # noqa: E402


VERSAO_SHORT = "EP001_SHORT_V6"


class Episodio001EclipseShort(CenaShort):
    """
    Short 9:16 sobre eclipse solar.

    V6:
    - etiqueta ECLIPSE visível durante a sobreposição;
    - frase final totalmente dentro do ecrã;
    - Sol, Lua e Terra completos no alinhamento;
    - legenda do rodapé tratada por engine/scene.py.
    """

    def etiqueta(self, texto: str, posicao) -> VGroup:
        palavra = Text(
            texto,
            font_size=38,
            color=YELLOW,
            weight="BOLD",
        )

        fundo = RoundedRectangle(
            width=palavra.width + 0.55,
            height=palavra.height + 0.30,
            corner_radius=0.12,
            fill_color=BLACK,
            fill_opacity=1.0,
            stroke_color=YELLOW,
            stroke_opacity=1.0,
            stroke_width=2.8,
        )

        palavra.move_to(fundo.get_center())
        grupo = VGroup(fundo, palavra)
        grupo.move_to(posicao)
        grupo.set_z_index(900)
        return grupo

    def construct(self) -> None:
        print(f"✅ A renderizar {VERSAO_SHORT}")

        estrelas = VGroup(
            *[
                Dot(
                    point=[
                        -3.35 + (indice % 8) * 0.96,
                        -5.10 + ((indice * 5) % 12) * 0.84,
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
        # 1 — HOOK E ECLIPSE
        # =====================================================

        sol_abertura = Circle(
            radius=0.68,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(UP * 4.20)

        lua_abertura = Circle(
            radius=0.64,
            color=WHITE,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(DOWN * 1.60)

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
                    radius=0.68 + indice * 0.09,
                    stroke_color=WHITE,
                    stroke_opacity=max(0.24, 1.0 - indice * 0.12),
                    stroke_width=max(1.8, 5.8 - indice * 0.58),
                ).move_to(sol_abertura)
                for indice in range(1, 7)
            ]
        )

        raios = VGroup(
            *[
                Line(
                    start=sol_abertura.get_center() + UP * 0.80,
                    end=sol_abertura.get_center() + UP * 1.22,
                    color=WHITE,
                    stroke_opacity=0.95,
                    stroke_width=3.0,
                ).rotate(
                    indice * 0.3927,
                    about_point=sol_abertura.get_center(),
                )
                for indice in range(16)
            ]
        )

        rotulo_eclipse = self.etiqueta(
            "ECLIPSE",
            sol_abertura.get_center() + DOWN * 1.48,
        )

        self.narrar(
            "Mas como pode a Lua esconder um Sol muito maior do que ela?",
            [
                FadeIn(coroa),
                FadeIn(raios),
                FadeIn(rotulo_eclipse),
            ],
        )

        pergunta = Text(
            "COMO A LUA\nESCONDE O SOL?",
            font_size=42,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.86,
        ).move_to(DOWN * 1.75)

        if pergunta.width > 6.6:
            pergunta.scale_to_fit_width(6.6)

        self.play(Write(pergunta), run_time=0.9)
        self.wait(0.4)

        self.play(
            FadeOut(
                VGroup(
                    sol_abertura,
                    lua_abertura,
                    coroa,
                    raios,
                    rotulo_eclipse,
                    pergunta,
                )
            ),
            run_time=0.65,
        )

        # =====================================================
        # 2 — ALINHAMENTO COMPLETO
        # =====================================================

        sol = Circle(
            radius=0.40,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(UP * 4.35)

        lua = Circle(
            radius=0.16,
            color=WHITE,
            fill_color=GREY_B,
            fill_opacity=1,
            stroke_width=2,
        ).move_to(LEFT * 1.40 + UP * 0.50)

        terra = Circle(
            radius=0.46,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(DOWN * 3.25)

        ondas_sol = VGroup(
            *[
                Circle(
                    radius=0.47 + indice * 0.07,
                    stroke_color=YELLOW,
                    stroke_opacity=max(0.22, 0.88 - indice * 0.13),
                    stroke_width=max(1.3, 4.0 - indice * 0.48),
                ).move_to(sol)
                for indice in range(1, 5)
            ]
        )

        ondas_lua = VGroup(
            *[
                Circle(
                    radius=0.21 + indice * 0.05,
                    stroke_color=WHITE,
                    stroke_opacity=max(0.22, 0.85 - indice * 0.15),
                    stroke_width=max(1.1, 3.0 - indice * 0.42),
                ).move_to(lua)
                for indice in range(1, 4)
            ]
        )

        ondas_terra = VGroup(
            *[
                Circle(
                    radius=0.53 + indice * 0.07,
                    stroke_color=BLUE,
                    stroke_opacity=max(0.20, 0.78 - indice * 0.13),
                    stroke_width=max(1.2, 3.5 - indice * 0.45),
                ).move_to(terra)
                for indice in range(1, 4)
            ]
        )

        nome_sol = Text(
            "SOL",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        ).next_to(sol, DOWN, buff=0.12)

        nome_lua = Text(
            "LUA",
            font_size=21,
            color=WHITE,
            weight="BOLD",
        ).next_to(lua, UP, buff=0.12)

        nome_terra = Text(
            "TERRA",
            font_size=22,
            color=BLUE,
            weight="BOLD",
        ).next_to(terra, DOWN, buff=0.12)

        sistema = VGroup(
            sol,
            ondas_sol,
            lua,
            ondas_lua,
            terra,
            ondas_terra,
            nome_sol,
            nome_lua,
            nome_terra,
        )

        self.narrar(
            "Um eclipse solar acontece quando a Lua passa entre o Sol e a Terra.",
            FadeIn(sistema),
        )

        posicao_lua = UP * 0.52

        self.narrar(
            "Nesse momento, os três astros ficam quase perfeitamente alinhados.",
            [
                lua.animate.move_to(posicao_lua),
                ondas_lua.animate.move_to(posicao_lua),
                nome_lua.animate.move_to(posicao_lua + LEFT * 0.58),
            ],
        )

        linha_1 = Line(
            sol.get_bottom(),
            lua.get_top(),
            color=YELLOW,
            stroke_opacity=1.0,
            stroke_width=4,
        )

        linha_2 = Line(
            lua.get_bottom(),
            terra.get_top(),
            color=WHITE,
            stroke_opacity=1.0,
            stroke_width=4,
        )

        alinhamento = Text(
            "SOL  →  LUA  →  TERRA",
            font_size=25,
            color=WHITE,
            weight="BOLD",
        ).move_to(DOWN * 4.62)

        if alinhamento.width > 6.7:
            alinhamento.scale_to_fit_width(6.7)

        self.play(
            FadeIn(linha_1),
            FadeIn(linha_2),
            Write(alinhamento),
            run_time=0.8,
        )

        sombra = Polygon(
            lua.get_center() + LEFT * 0.10 + DOWN * 0.05,
            terra.get_center() + LEFT * 0.16 + UP * 0.38,
            terra.get_center() + RIGHT * 0.16 + UP * 0.38,
            lua.get_center() + RIGHT * 0.10 + DOWN * 0.05,
            fill_color=BLACK,
            fill_opacity=0.96,
            stroke_color=WHITE,
            stroke_opacity=0.78,
            stroke_width=2.4,
        )
        sombra.set_z_index(-1)

        zona_total = Dot(
            terra.get_center() + UP * 0.38,
            radius=0.065,
            color=BLACK,
        )

        ondas_sombra = VGroup(
            *[
                Circle(
                    radius=0.11 + indice * 0.055,
                    stroke_color=WHITE,
                    stroke_width=max(1.3, 3.6 - indice * 0.50),
                    stroke_opacity=max(0.24, 1.0 - indice * 0.16),
                ).move_to(zona_total)
                for indice in range(5)
            ]
        )

        self.narrar(
            "A Lua bloqueia parte da luz e projeta uma pequena sombra sobre a Terra.",
            [
                FadeIn(sombra),
                FadeIn(zona_total),
                FadeIn(ondas_sombra),
            ],
        )

        self.play(
            FadeOut(
                VGroup(
                    sistema,
                    linha_1,
                    linha_2,
                    alinhamento,
                    sombra,
                    zona_total,
                    ondas_sombra,
                )
            ),
            run_time=0.65,
        )

        # =====================================================
        # 3 — TAMANHO APARENTE
        # =====================================================

        titulo = Text(
            "PARECE IMPOSSÍVEL...",
            font_size=34,
            color=WHITE,
            weight="BOLD",
        ).move_to(UP * 4.70)

        sol_grande = Circle(
            radius=0.68,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(UP * 1.65)

        lua_pequena = Circle(
            radius=0.15,
            color=WHITE,
            fill_color=GREY_B,
            fill_opacity=1,
        ).move_to(DOWN * 0.42)

        comparacao = Text(
            "O SOL É CERCA DE\n400 VEZES MAIOR",
            font_size=32,
            color=YELLOW,
            weight="BOLD",
            line_spacing=0.88,
        ).move_to(DOWN * 3.05)

        self.narrar(
            "O Sol tem aproximadamente quatrocentas vezes o diâmetro da Lua.",
            [
                Write(titulo),
                FadeIn(sol_grande),
                FadeIn(lua_pequena),
                Write(comparacao),
            ],
        )

        distancia = Text(
            "MAS TAMBÉM ESTÁ\nCERCA DE 400 VEZES\nMAIS LONGE",
            font_size=31,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.88,
        ).move_to(DOWN * 2.95)

        self.narrar(
            "Mas também está aproximadamente quatrocentas vezes mais longe da Terra.",
            [
                FadeOut(comparacao),
                Write(distancia),
            ],
        )

        centro = UP * 0.90

        aparente_sol = Circle(
            radius=0.58,
            stroke_color=YELLOW,
            stroke_width=9,
        ).move_to(centro)

        aparente_lua = Circle(
            radius=0.54,
            stroke_color=WHITE,
            stroke_width=5,
        ).move_to(centro)

        ondas = VGroup(
            *[
                Circle(
                    radius=0.62 + indice * 0.09,
                    stroke_color=YELLOW,
                    stroke_opacity=max(0.20, 0.94 - indice * 0.13),
                    stroke_width=max(1.5, 4.8 - indice * 0.52),
                ).move_to(centro)
                for indice in range(1, 6)
            ]
        )

        self.narrar(
            "Por isso, vistos daqui, os dois parecem ter quase exatamente o mesmo tamanho.",
            [
                FadeOut(titulo),
                FadeOut(sol_grande),
                FadeOut(lua_pequena),
                FadeOut(distancia),
                FadeIn(aparente_sol),
                FadeIn(aparente_lua),
                FadeIn(ondas),
            ],
        )

        self.play(
            FadeOut(
                VGroup(
                    aparente_sol,
                    aparente_lua,
                    ondas,
                    estrelas,
                )
            ),
            run_time=0.65,
        )

        # =====================================================
        # 4 — FINAL TOTALMENTE ENQUADRADO
        # =====================================================

        frase_1 = Text(
            "O SOL NÃO\nDESAPARECE.",
            font_size=34,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.87,
        ).move_to(UP * 1.45)

        frase_2 = Text(
            "A LUA PASSA\nÀ NOSSA FRENTE.",
            font_size=37,
            color=YELLOW,
            weight="BOLD",
            line_spacing=0.86,
        ).move_to(DOWN * 0.58)

        for frase in (frase_1, frase_2):
            frase.scale_to_fit_width(5.8)

        self.narrar(
            "O Sol não desaparece.",
            Write(frase_1),
        )

        self.narrar(
            "É a Lua que passa exatamente à nossa frente.",
            Write(frase_2),
        )

        self.play(
            FadeOut(VGroup(frase_1, frase_2)),
            run_time=0.55,
        )

        chamada = Text(
            "SEGUE O NOSSO CANAL",
            font_size=36,
            color=WHITE,
            weight="BOLD",
        ).move_to(UP * 1.42)

        canal = Text(
            "APRENDER MESMO",
            font_size=42,
            color=YELLOW,
            weight="BOLD",
        ).move_to(UP * 0.08)

        complemento = Text(
            "PARA APRENDER CIÊNCIA\nDE FORMA SIMPLES E VISUAL",
            font_size=27,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.90,
        ).move_to(DOWN * 1.38)

        for texto in (chamada, canal, complemento):
            if texto.width > 6.4:
                texto.scale_to_fit_width(6.4)

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
            FadeOut(VGroup(chamada, canal, complemento)),
            run_time=0.65,
        )
