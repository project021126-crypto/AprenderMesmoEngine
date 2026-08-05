from manim import (
    BLACK,
    WHITE,
    YELLOW,
    BLUE,
    GREY_B,
    ORIGIN,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    GrowFromCenter,
    Line,
    Polygon,
    Text,
    VGroup,
    Write,
)

from engine.core import FormatoVideo, StudioConfig
from engine.scene import CenaAprenderMesmo
from engine.universo import Sol, Terra, Lua


class Episodio001Eclipse(CenaAprenderMesmo):
    """
    Episódio 001 — O Dia em Que o Sol Desapareceu
    Série: Universo
    Formato: Long 16:9
    """

    studio_config = StudioConfig(
        formato=FormatoVideo.LONG,
    )

    def construct(self) -> None:
        self.studio.selecionar_episodio(
            "Universo — EP001 — O Eclipse Solar"
        )

        # =====================================================
        # CENA 1 — ABERTURA
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

        sol_abertura = Sol(raio=1.8)
        sol_abertura.move_to(ORIGIN)

        lua_abertura = Lua(raio=1.72)
        lua_abertura.set_fill(BLACK, opacity=1)
        lua_abertura.set_stroke(GREY_B, width=2)
        lua_abertura.move_to(RIGHT * 4.8)

        self.add(estrelas)

        self.narrar(
            "Imagina que são duas da tarde...",
            [
                GrowFromCenter(sol_abertura),
            ],
        )

        self.narrar(
            "E, sem aviso, o Sol começa lentamente a desaparecer.",
            [
                lua_abertura.animate.move_to(ORIGIN),
            ],
        )

        coroa = VGroup(
            *[
                Circle(
                    radius=1.8 + indice * 0.12,
                    stroke_color=WHITE,
                    stroke_opacity=max(
                        0.05,
                        0.30 - indice * 0.04,
                    ),
                    stroke_width=2,
                )
                for indice in range(1, 7)
            ]
        )

        self.play(
            FadeIn(coroa),
            run_time=1,
        )

        self.narrar(
            "Como é possível o dia transformar-se em noite?"
        )

        titulo = self.mostrar_titulo(
            "O DIA EM QUE O SOL DESAPARECEU",
            tamanho=45,
            duracao=1.2,
        )

        self.wait(0.6)

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
        # CENA 2 — SOL, LUA E TERRA
        # =====================================================

        sol = Sol(raio=0.9)
        sol.move_to(LEFT * 5)

        terra = Terra(raio=0.65)
        terra.move_to(RIGHT * 4.8)

        lua = Lua(raio=0.27)
        lua.move_to(UP * 1.4)

        nome_sol = Text(
            "SOL",
            font_size=26,
            color=YELLOW,
            weight="BOLD",
        ).next_to(sol, DOWN, buff=0.3)

        nome_lua = Text(
            "LUA",
            font_size=24,
            color=GREY_B,
            weight="BOLD",
        ).next_to(lua, UP, buff=0.25)

        nome_terra = Text(
            "TERRA",
            font_size=26,
            color=BLUE,
            weight="BOLD",
        ).next_to(terra, DOWN, buff=0.3)

        sistema = VGroup(
            sol,
            terra,
            lua,
            nome_sol,
            nome_lua,
            nome_terra,
        )

        self.play(
            FadeIn(sistema),
            run_time=1.2,
        )

        self.narrar(
            "Para perceber este fenómeno, precisamos de olhar para tudo a partir do espaço."
        )

        self.narrar(
            "Um eclipse solar acontece quando a Lua passa exatamente entre o Sol e a Terra.",
            [
                lua.animate.move_to(LEFT * 0.1),
            ],
        )

        # =====================================================
        # CENA 3 — SOMBRA DA LUA
        # =====================================================

        sombra = Polygon(
            lua.get_center() + UP * 0.24,
            terra.get_center() + UP * 0.18,
            terra.get_center() + DOWN * 0.18,
            lua.get_center() + DOWN * 0.24,
            fill_color=BLACK,
            fill_opacity=0.80,
            stroke_color=GREY_B,
            stroke_opacity=0.45,
            stroke_width=2,
        )

        sombra.set_z_index(-1)

        self.narrar(
            "A Lua bloqueia parte da luz e projeta uma sombra estreita sobre o nosso planeta.",
            [
                FadeIn(sombra),
            ],
        )

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
            "Quem estiver dentro desta pequena região consegue observar um eclipse total.",
            [
                FadeIn(zona_total),
                FadeIn(destaque),
            ],
        )

        self.play(
            FadeOut(
                VGroup(
                    sistema,
                    sombra,
                    zona_total,
                    destaque,
                )
            ),
            run_time=0.8,
        )

        # =====================================================
        # CENA 4 — O MISTÉRIO DO TAMANHO
        # =====================================================

        sol_comparacao = Sol(raio=1.55)
        sol_comparacao.move_to(LEFT * 3.3)

        lua_comparacao = Lua(raio=0.24)
        lua_comparacao.move_to(RIGHT * 3.2)

        self.play(
            FadeIn(sol_comparacao),
            FadeIn(lua_comparacao),
            run_time=1,
        )

        pergunta = Text(
            "Como consegue a Lua esconder o Sol?",
            font_size=38,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.55)

        self.narrar(
            "Mas espera. Se o Sol é tão gigantesco, como consegue a Lua escondê-lo?",
            [
                Write(pergunta),
            ],
        )

        numero_sol = Text(
            "1 390 000 km",
            font_size=27,
            color=YELLOW,
        ).next_to(sol_comparacao, DOWN, buff=0.3)

        numero_lua = Text(
            "3 474 km",
            font_size=27,
            color=GREY_B,
        ).next_to(lua_comparacao, DOWN, buff=0.3)

        quatrocentas = Text(
            "CERCA DE 400 VEZES MAIOR",
            font_size=36,
            color=YELLOW,
            weight="BOLD",
        ).move_to(UP * 2.2)

        self.play(
            FadeOut(pergunta),
            run_time=0.3,
        )

        self.narrar(
            "O Sol tem aproximadamente quatrocentas vezes o diâmetro da Lua.",
            [
                FadeIn(numero_sol),
                FadeIn(numero_lua),
                Write(quatrocentas),
            ],
        )

        self.play(
            FadeOut(
                VGroup(
                    numero_sol,
                    numero_lua,
                    quatrocentas,
                )
            ),
            sol_comparacao.animate.scale(0.5).move_to(LEFT * 5),
            lua_comparacao.animate.scale(1.4).move_to(RIGHT * 0.5),
            run_time=1.1,
        )

        # =====================================================
        # CENA 5 — A DISTÂNCIA
        # =====================================================

        terra_observador = Terra(raio=0.55)
        terra_observador.move_to(RIGHT * 5.2)

        linha_sol = Line(
            terra_observador.get_center(),
            sol_comparacao.get_center(),
            color=YELLOW,
            stroke_opacity=0.55,
        )

        linha_lua = Line(
            terra_observador.get_center(),
            lua_comparacao.get_center(),
            color=GREY_B,
            stroke_opacity=0.55,
        )

        self.play(
            FadeIn(terra_observador),
            FadeIn(linha_sol),
            FadeIn(linha_lua),
            run_time=0.8,
        )

        self.narrar(
            "A resposta está na distância."
        )

        self.narrar(
            "O Sol também está aproximadamente quatrocentas vezes mais longe da Terra do que a Lua."
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
            "Por isso, quando os observamos da Terra, parecem ter quase exatamente o mesmo tamanho.",
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
            "É esta coincidência cósmica que torna possível um eclipse total.",
            [
                Write(coincidencia),
            ],
        )

        self.play(
            FadeOut(
                VGroup(
                    sol_comparacao,
                    lua_comparacao,
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
        # FINAL
        # =====================================================

        frase_1 = Text(
            "O UNIVERSO NÃO FAZ MAGIA...",
            font_size=47,
            color=WHITE,
            weight="BOLD",
        ).move_to(UP * 0.4)

        frase_2 = Text(
            "MAS, ÀS VEZES, PARECE.",
            font_size=52,
            color=YELLOW,
            weight="BOLD",
        ).next_to(frase_1, DOWN, buff=0.4)

        self.narrar(
            "O Universo não faz magia.",
            [
                Write(frase_1),
            ],
        )

        self.narrar(
            "Mas, às vezes, parece.",
            [
                Write(frase_2),
            ],
        )

        assinatura = Text(
            "APRENDER MESMO",
            font_size=27,
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