from manim import (
    BLACK,
    BLUE,
    BLUE_B,
    BLUE_D,
    DOWN,
    FadeIn,
    FadeOut,
    GREY_B,
    GREEN,
    LEFT,
    ORANGE,
    ORIGIN,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
    Arrow,
    Circle,
    DashedLine,
    Dot,
    Ellipse,
    GrowArrow,
    GrowFromCenter,
    Line,
    Polygon,
    Rectangle,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
    config,
)

# ==========================================================
# FORMATO LONG — 16:9
# ==========================================================

config.frame_width = 14.222
config.frame_height = 8.0

from engine.scene import CenaLong  # noqa: E402


VERSAO_LONG = "EP001_LONG_V3"


class Episodio001EclipseLong(CenaLong):
    """
    LONG 001 — Eclipse Solar

    Versão V2:
    - duração prevista: 8–9 minutos;
    - perguntas reais do público;
    - pequenas pausas antes das respostas;
    - mais emoção e suspense;
    - explicações visuais;
    - mesma voz aprovada no Short.
    """

    # ======================================================
    # COMPONENTES VISUAIS
    # ======================================================

    def fundo_estrelado(self, quantidade: int = 110) -> VGroup:
        estrelas = VGroup(
            *[
                Dot(
                    point=[
                        -6.8 + (indice % 15) * 0.95,
                        -3.45 + ((indice * 7) % 8) * 0.95,
                        0,
                    ],
                    radius=0.016 + (indice % 3) * 0.004,
                    color=WHITE,
                ).set_opacity(0.28 + (indice % 4) * 0.12)
                for indice in range(quantidade)
            ]
        )
        estrelas.set_z_index(-20)
        return estrelas

    def criar_sol(
        self,
        raio: float,
        posicao=ORIGIN,
        intensidade: float = 1.0,
    ) -> VGroup:
        nucleo = Circle(
            radius=raio,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
            stroke_width=3,
        ).move_to(posicao)

        halo = VGroup(
            *[
                Circle(
                    radius=raio + indice * raio * 0.12,
                    stroke_color=YELLOW,
                    stroke_opacity=max(
                        0.08,
                        intensidade * (0.66 - indice * 0.09),
                    ),
                    stroke_width=max(1.2, 4.8 - indice * 0.55),
                ).move_to(posicao)
                for indice in range(1, 6)
            ]
        )

        raios = VGroup(
            *[
                Line(
                    start=posicao + UP * raio * 1.15,
                    end=posicao + UP * raio * 1.55,
                    color=YELLOW,
                    stroke_opacity=0.68 * intensidade,
                    stroke_width=2.3,
                ).rotate(
                    indice * 0.3927,
                    about_point=posicao,
                )
                for indice in range(16)
            ]
        )

        return VGroup(halo, raios, nucleo)

    def criar_terra(
        self,
        raio: float,
        posicao=ORIGIN,
    ) -> VGroup:
        atmosfera = Circle(
            radius=raio * 1.10,
            stroke_color=BLUE_B,
            stroke_opacity=0.48,
            stroke_width=5,
        ).move_to(posicao)

        planeta = Circle(
            radius=raio,
            color=BLUE,
            fill_color=BLUE_D,
            fill_opacity=1,
            stroke_width=2,
        ).move_to(posicao)

        continentes = VGroup(
            Ellipse(
                width=raio * 0.72,
                height=raio * 0.34,
                color=GREEN,
                fill_color=GREEN,
                fill_opacity=0.85,
                stroke_opacity=0,
            ).move_to(posicao + LEFT * raio * 0.20 + UP * raio * 0.18),
            Ellipse(
                width=raio * 0.55,
                height=raio * 0.26,
                color=GREEN,
                fill_color=GREEN,
                fill_opacity=0.75,
                stroke_opacity=0,
            ).move_to(posicao + RIGHT * raio * 0.24 + DOWN * raio * 0.16),
        )

        brilho = Arc(
            radius=raio * 0.86,
            start_angle=1.85,
            angle=2.20,
            color=WHITE,
            stroke_opacity=0.45,
            stroke_width=3,
        ).move_to(posicao)

        return VGroup(atmosfera, planeta, continentes, brilho)

    def criar_lua(
        self,
        raio: float,
        posicao=ORIGIN,
    ) -> VGroup:
        halo = Circle(
            radius=raio * 1.16,
            stroke_color=WHITE,
            stroke_opacity=0.28,
            stroke_width=3,
        ).move_to(posicao)

        lua = Circle(
            radius=raio,
            color=WHITE,
            fill_color=GREY_B,
            fill_opacity=1,
            stroke_width=2,
        ).move_to(posicao)

        crateras = VGroup(
            Circle(
                radius=raio * 0.16,
                color=BLACK,
                fill_color=BLACK,
                fill_opacity=0.18,
                stroke_opacity=0,
            ).move_to(posicao + LEFT * raio * 0.28 + UP * raio * 0.20),
            Circle(
                radius=raio * 0.11,
                color=BLACK,
                fill_color=BLACK,
                fill_opacity=0.16,
                stroke_opacity=0,
            ).move_to(posicao + RIGHT * raio * 0.25 + DOWN * raio * 0.18),
            Circle(
                radius=raio * 0.08,
                color=BLACK,
                fill_color=BLACK,
                fill_opacity=0.12,
                stroke_opacity=0,
            ).move_to(posicao + RIGHT * raio * 0.05 + UP * raio * 0.34),
        )

        return VGroup(halo, lua, crateras)

    def titulo_secao(self, numero: str, titulo: str) -> Text:
        texto = Text(
            f"{numero}. {titulo}",
            font_size=40,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.35)

        if texto.width > 13.0:
            texto.scale_to_fit_width(13.0)

        return texto

    def pergunta(self, texto: str, cor=YELLOW) -> Text:
        pergunta = Text(
            texto,
            font_size=46,
            color=cor,
            weight="BOLD",
            line_spacing=0.90,
        )

        if pergunta.width > 12.6:
            pergunta.scale_to_fit_width(12.6)

        return pergunta

    def etiqueta(
        self,
        texto: str,
        posicao,
        cor=YELLOW,
        tamanho: int = 28,
    ) -> VGroup:
        palavra = Text(
            texto,
            font_size=tamanho,
            color=cor,
            weight="BOLD",
        )

        fundo = RoundedRectangle(
            width=palavra.width + 0.40,
            height=palavra.height + 0.22,
            corner_radius=0.10,
            fill_color=BLACK,
            fill_opacity=0.96,
            stroke_color=cor,
            stroke_opacity=0.90,
            stroke_width=1.8,
        )

        palavra.move_to(fundo.get_center())
        grupo = VGroup(fundo, palavra).move_to(posicao)
        grupo.set_z_index(200)
        return grupo

    def limpar(self, *objetos, duracao: float = 0.75) -> None:
        self.play(FadeOut(VGroup(*objetos)), run_time=duracao)

    def mostrar_pergunta(
        self,
        texto: str,
        *,
        cor=YELLOW,
        pausa: float = 0.85,
    ) -> VGroup:
        """
        Mostra a pergunta como uma transição independente.

        O painel preto cobre completamente a cena anterior, evitando
        perguntas sobrepostas a planetas, títulos ou etiquetas.
        """
        painel = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,
            fill_opacity=0.98,
            stroke_opacity=0,
        )
        painel.set_z_index(800)

        pergunta = self.pergunta(texto, cor)
        pergunta.move_to(ORIGIN)
        pergunta.set_z_index(810)

        grupo = VGroup(painel, pergunta)

        self.play(
            FadeIn(painel),
            Write(pergunta),
            run_time=0.85,
        )
        self.wait(pausa)
        return grupo

    # ======================================================
    # EPISÓDIO
    # ======================================================

    def construct(self) -> None:
        print(f"✅ A renderizar {VERSAO_LONG}")

        estrelas = self.fundo_estrelado()
        self.add(estrelas)

        # ==================================================
        # CENA 1 — ABERTURA CINEMATOGRÁFICA
        # ==================================================

        sol_hook = self.criar_sol(
            raio=1.18,
            posicao=ORIGIN,
            intensidade=1.0,
        )

        lua_hook = Circle(
            radius=1.12,
            color=WHITE,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=2,
        ).move_to(RIGHT * 5.7)

        self.narrar(
            "Imagina que estás numa praia ao meio-dia. O céu está limpo, o mar reflete a luz e o Sol brilha com toda a força.",
            GrowFromCenter(sol_hook),
        )

        self.narrar(
            "Mas, sem aviso, uma sombra começa a atravessar lentamente o disco solar.",
            lua_hook.animate.move_to(RIGHT * 1.85),
        )

        self.narrar(
            "A luz torna-se estranha. A temperatura começa a descer. Os pássaros calam-se.",
            lua_hook.animate.move_to(RIGHT * 0.70),
        )

        self.narrar(
            "E poucos minutos depois, o dia parece transformar-se em noite.",
            lua_hook.animate.move_to(ORIGIN),
        )

        coroa_hook = VGroup(
            *[
                Circle(
                    radius=1.18 + indice * 0.13,
                    stroke_color=WHITE,
                    stroke_opacity=max(0.10, 0.62 - indice * 0.075),
                    stroke_width=max(1.3, 5.0 - indice * 0.45),
                )
                for indice in range(1, 7)
            ]
        )

        pergunta_abertura = self.mostrar_pergunta(
            "COMO É QUE ISTO É POSSÍVEL?",
            cor=YELLOW,
            pausa=0.95,
        )

        self.narrar(
            "Hoje vamos descobrir não apenas como acontece um eclipse, mas também responder às perguntas que quase toda a gente faz quando o vê pela primeira vez.",
            FadeIn(coroa_hook),
        )

        self.limpar(
            sol_hook,
            lua_hook,
            coroa_hook,
            pergunta_abertura,
        )

        # ==================================================
        # CENA 2 — PROMESSA
        # ==================================================

        titulo_promessa = Text(
            "HOJE VAIS PERCEBER...",
            font_size=48,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.42)

        cartões = VGroup(
            self.etiqueta(
                "PORQUE A LUA CONSEGUE TAPAR O SOL",
                LEFT * 3.9 + UP * 1.55,
                YELLOW,
                26,
            ),
            self.etiqueta(
                "PORQUE NÃO SE VÊ EM TODO O MUNDO",
                RIGHT * 3.7 + UP * 1.55,
                BLUE_B,
                26,
            ),
            self.etiqueta(
                "PORQUE NÃO ACONTECE TODOS OS MESES",
                LEFT * 3.8 + DOWN * 0.25,
                WHITE,
                24,
            ),
            self.etiqueta(
                "SE OS ANIMAIS PENSAM QUE É NOITE",
                RIGHT * 3.7 + DOWN * 0.25,
                ORANGE,
                25,
            ),
            self.etiqueta(
                "E SE UM DIA OS ECLIPSES VÃO ACABAR",
                DOWN * 2.05,
                GREEN,
                26,
            ),
        )

        self.narrar(
            "Vamos começar pelo alinhamento entre o Sol, a Lua e a Terra.",
            [
                Write(titulo_promessa),
                FadeIn(cartões[0]),
                FadeIn(cartões[1]),
            ],
        )

        self.narrar(
            "Depois vamos responder às dúvidas mais curiosas: porque só algumas regiões conseguem ver, porque não acontece todos os meses, o que acontece aos animais e se um dia os eclipses totais vão desaparecer.",
            [
                FadeIn(cartões[2]),
                FadeIn(cartões[3]),
                FadeIn(cartões[4]),
            ],
        )

        self.limpar(titulo_promessa, cartões)

        # ==================================================
        # CENA 3 — O QUE É UM ECLIPSE?
        # ==================================================

        titulo_1 = self.titulo_secao(
            "1",
            "AFINAL, O QUE É UM ECLIPSE SOLAR?",
        )

        sol = self.criar_sol(
            raio=0.72,
            posicao=LEFT * 5.1,
            intensidade=0.85,
        )

        lua = self.criar_lua(
            raio=0.29,
            posicao=UP * 1.55,
        )

        terra = self.criar_terra(
            raio=0.64,
            posicao=RIGHT * 4.8,
        )

        nomes = VGroup(
            Text(
                "SOL",
                font_size=25,
                color=YELLOW,
                weight="BOLD",
            ).next_to(sol, DOWN, buff=0.25),
            Text(
                "LUA",
                font_size=24,
                color=WHITE,
                weight="BOLD",
            ).next_to(lua, UP, buff=0.22),
            Text(
                "TERRA",
                font_size=25,
                color=BLUE_B,
                weight="BOLD",
            ).next_to(terra, DOWN, buff=0.25),
        )

        self.narrar(
            "Um eclipse solar acontece quando a Lua passa entre o Sol e a Terra.",
            [
                Write(titulo_1),
                FadeIn(sol),
                FadeIn(lua),
                FadeIn(terra),
                FadeIn(nomes),
            ],
        )

        self.narrar(
            "Nesse momento, parte da luz que seguia em direção ao nosso planeta é bloqueada.",
            lua.animate.move_to(LEFT * 0.15),
        )

        linha_1 = Line(
            sol.get_right(),
            lua.get_left(),
            color=YELLOW,
            stroke_opacity=0.85,
            stroke_width=3,
        )

        linha_2 = Line(
            lua.get_right(),
            terra.get_left(),
            color=WHITE,
            stroke_opacity=0.78,
            stroke_width=3,
        )

        self.narrar(
            "Visto de lado, o alinhamento parece simples: Sol, Lua e Terra.",
            [
                FadeIn(linha_1),
                FadeIn(linha_2),
            ],
        )

        pergunta_1 = self.mostrar_pergunta(
            "MAS A LUA NÃO É MUITO PEQUENA?",
            cor=YELLOW,
            pausa=0.80,
        )

        self.narrar(
            "É. A Lua é muito menor do que o Sol. Mas o segredo não está apenas no tamanho.",
            FadeOut(pergunta_1),
        )

        self.limpar(
            titulo_1,
            sol,
            lua,
            terra,
            nomes,
            linha_1,
            linha_2,
        )

        # ==================================================
        # CENA 4 — TAMANHO E DISTÂNCIA
        # ==================================================

        titulo_2 = self.titulo_secao(
            "2",
            "COMO A LUA CONSEGUE ESCONDER O SOL?",
        )

        sol_grande = self.criar_sol(
            raio=1.45,
            posicao=LEFT * 3.9,
            intensidade=0.92,
        )

        lua_pequena = self.criar_lua(
            raio=0.24,
            posicao=RIGHT * 3.8,
        )

        self.narrar(
            "O diâmetro do Sol é cerca de quatrocentas vezes maior do que o diâmetro da Lua.",
            [
                Write(titulo_2),
                FadeIn(sol_grande),
                FadeIn(lua_pequena),
            ],
        )

        medidas = VGroup(
            Text(
                "SOL\n≈ 1,39 milhões de km",
                font_size=28,
                color=YELLOW,
                line_spacing=0.90,
            ).next_to(sol_grande, DOWN, buff=0.32),
            Text(
                "LUA\n≈ 3 474 km",
                font_size=28,
                color=WHITE,
                line_spacing=0.90,
            ).next_to(lua_pequena, DOWN, buff=0.32),
        )

        self.narrar(
            "Se os dois estivessem à mesma distância, a Lua pareceria insignificante diante do Sol.",
            FadeIn(medidas),
        )

        pergunta_2 = self.mostrar_pergunta(
            "ENTÃO COMO CONSEGUE TAPÁ-LO?",
            cor=YELLOW,
            pausa=0.90,
        )

        self.play(
            FadeOut(pergunta_2),
            FadeOut(medidas),
            sol_grande.animate.scale(0.40).move_to(LEFT * 5.2),
            lua_pequena.animate.scale(1.45).move_to(LEFT * 0.10),
            run_time=1.1,
        )

        terra_observador = self.criar_terra(
            raio=0.56,
            posicao=RIGHT * 5.0,
        )

        self.narrar(
            "Porque o Sol também está aproximadamente quatrocentas vezes mais longe da Terra do que a Lua.",
            FadeIn(terra_observador),
        )

        linhas_visao = VGroup(
            DashedLine(
                terra_observador.get_center(),
                sol_grande.get_center(),
                color=YELLOW,
                dash_length=0.17,
            ),
            DashedLine(
                terra_observador.get_center(),
                lua_pequena.get_center(),
                color=WHITE,
                dash_length=0.17,
            ),
        )

        self.narrar(
            "Vistos daqui, os dois discos acabam por parecer quase do mesmo tamanho no céu.",
            FadeIn(linhas_visao),
        )

        discos = VGroup(
            Circle(
                radius=0.74,
                stroke_color=YELLOW,
                stroke_width=9,
            ),
            Circle(
                radius=0.70,
                stroke_color=WHITE,
                stroke_width=5,
            ),
        ).move_to(DOWN * 1.90)

        coincidencia = self.etiqueta(
            "UMA COINCIDÊNCIA CÓSMICA",
            DOWN * 3.0,
            YELLOW,
            30,
        )

        self.narrar(
            "É uma coincidência cósmica extraordinária. A Lua parece ter exatamente o tamanho necessário para esconder o Sol.",
            [
                FadeIn(discos),
                FadeIn(coincidencia),
            ],
        )

        self.limpar(
            titulo_2,
            sol_grande,
            lua_pequena,
            terra_observador,
            linhas_visao,
            discos,
            coincidencia,
        )

        # ==================================================
        # CENA 5 — SOMBRA, UMBRA E PENUMBRA
        # ==================================================

        titulo_3 = self.titulo_secao(
            "3",
            "A SOMBRA DA LUA TEM DUAS PARTES",
        )

        sol_sombra = self.criar_sol(
            raio=0.90,
            posicao=LEFT * 5.15,
            intensidade=0.75,
        )

        lua_sombra = self.criar_lua(
            raio=0.31,
            posicao=LEFT * 0.75,
        )

        terra_sombra = self.criar_terra(
            raio=0.78,
            posicao=RIGHT * 4.85,
        )

        self.narrar(
            "A sombra criada pela Lua não é toda igual.",
            [
                Write(titulo_3),
                FadeIn(sol_sombra),
                FadeIn(lua_sombra),
                FadeIn(terra_sombra),
            ],
        )

        umbra = Polygon(
            lua_sombra.get_center() + UP * 0.18,
            terra_sombra.get_center() + UP * 0.13,
            terra_sombra.get_center() + DOWN * 0.13,
            lua_sombra.get_center() + DOWN * 0.18,
            fill_color=BLACK,
            fill_opacity=0.96,
            stroke_color=WHITE,
            stroke_opacity=0.30,
        )

        penumbra_1 = Polygon(
            sol_sombra.get_center() + UP * 0.75,
            lua_sombra.get_center() + UP * 0.22,
            terra_sombra.get_center() + UP * 0.62,
            terra_sombra.get_center() + UP * 0.15,
            fill_color=GREY_B,
            fill_opacity=0.22,
            stroke_opacity=0,
        )

        penumbra_2 = Polygon(
            sol_sombra.get_center() + DOWN * 0.75,
            lua_sombra.get_center() + DOWN * 0.22,
            terra_sombra.get_center() + DOWN * 0.62,
            terra_sombra.get_center() + DOWN * 0.15,
            fill_color=GREY_B,
            fill_opacity=0.22,
            stroke_opacity=0,
        )

        self.narrar(
            "No centro existe uma região muito escura chamada umbra.",
            FadeIn(umbra),
        )

        self.narrar(
            "À volta existe uma zona mais clara chamada penumbra.",
            [
                FadeIn(penumbra_1),
                FadeIn(penumbra_2),
            ],
        )

        pergunta_3 = self.mostrar_pergunta(
            "E O QUE MUDA PARA QUEM ESTÁ EM CADA ZONA?",
            cor=WHITE,
            pausa=0.80,
        )

        etiquetas = VGroup(
            self.etiqueta(
                "UMBRA = ECLIPSE TOTAL",
                DOWN * 2.0,
                WHITE,
                28,
            ),
            self.etiqueta(
                "PENUMBRA = ECLIPSE PARCIAL",
                UP * 2.0,
                GREY_B,
                26,
            ),
        )

        self.narrar(
            "Quem está na umbra vê o Sol totalmente coberto. Quem está na penumbra vê apenas uma parte do Sol desaparecer.",
            [
                FadeOut(pergunta_3),
                FadeIn(etiquetas),
            ],
        )

        self.limpar(
            titulo_3,
            sol_sombra,
            lua_sombra,
            terra_sombra,
            umbra,
            penumbra_1,
            penumbra_2,
            etiquetas,
        )

        # ==================================================
        # CENA 6 — PORQUE NÃO SE VÊ EM TODAS AS REGIÕES?
        # ==================================================

        pergunta_regioes = self.mostrar_pergunta(
            "PORQUE NÃO SE VÊ O ECLIPSE EM TODAS AS REGIÕES?",
            cor=YELLOW,
            pausa=1.0,
        )

        self.play(FadeOut(pergunta_regioes), run_time=0.45)

        titulo_4 = self.titulo_secao(
            "4",
            "A SOMBRA PASSA POR UMA FAIXA MUITO ESTREITA",
        )

        terra_regioes = self.criar_terra(
            raio=2.25,
            posicao=LEFT * 1.55,
        )

        faixa_parcial = Arc(
            radius=2.08,
            start_angle=-0.72,
            angle=1.72,
            color=GREY_B,
            stroke_width=38,
            stroke_opacity=0.34,
        ).move_to(terra_regioes)

        faixa_total = Arc(
            radius=1.98,
            start_angle=-0.50,
            angle=1.32,
            color=BLACK,
            stroke_width=17,
        ).move_to(terra_regioes)

        self.narrar(
            "Porque a umbra chega à Terra como uma mancha muito pequena quando comparada com o tamanho do planeta.",
            [
                Write(titulo_4),
                FadeIn(terra_regioes),
                FadeIn(faixa_parcial),
                FadeIn(faixa_total),
            ],
        )

        cidade_total = Dot(
            terra_regioes.get_center() + RIGHT * 1.45 + UP * 0.42,
            radius=0.10,
            color=YELLOW,
        )

        cidade_parcial = Dot(
            terra_regioes.get_center() + UP * 1.70,
            radius=0.10,
            color=ORANGE,
        )

        cidade_fora = Dot(
            terra_regioes.get_center() + LEFT * 1.42 + DOWN * 1.02,
            radius=0.10,
            color=RED,
        )

        estados_regioes = VGroup(
            self.etiqueta(
                "TOTAL",
                LEFT * 4.35 + UP * 2.55,
                YELLOW,
                27,
            ),
            self.etiqueta(
                "PARCIAL",
                UP * 2.55,
                ORANGE,
                27,
            ),
            self.etiqueta(
                "SEM ECLIPSE",
                RIGHT * 4.35 + UP * 2.55,
                RED,
                25,
            ),
        )

        self.narrar(
            "Uma pessoa dentro da faixa central vê um eclipse total.",
            [
                FadeIn(cidade_total),
                FadeIn(estados_regioes[0]),
            ],
        )

        self.narrar(
            "Outra pessoa, algumas centenas de quilómetros ao lado, pode ver apenas um eclipse parcial.",
            [
                FadeIn(cidade_parcial),
                FadeIn(estados_regioes[1]),
            ],
        )

        self.narrar(
            "E alguém ainda mais afastado pode não notar absolutamente nada.",
            [
                FadeIn(cidade_fora),
                FadeIn(estados_regioes[2]),
            ],
        )

        seta_movimento = Arrow(
            LEFT * 0.3 + DOWN * 2.85,
            RIGHT * 4.8 + DOWN * 2.85,
            color=WHITE,
            buff=0,
        )

        self.narrar(
            "À medida que a Lua avança e a Terra roda, a sombra desloca-se por uma faixa sobre países, continentes e oceanos.",
            GrowArrow(seta_movimento),
        )

        frase_regioes = Text(
            "O ECLIPSE É O MESMO.\n"
            "O QUE MUDA É A POSIÇÃO DO OBSERVADOR.",
            font_size=34,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.90,
        ).move_to(RIGHT * 4.4 + UP * 2.55)

        if frase_regioes.width > 6.0:
            frase_regioes.scale_to_fit_width(6.0)

        self.narrar(
            "O eclipse não pertence a uma região. É o observador que precisa de estar exatamente no caminho da sombra.",
            Write(frase_regioes),
        )

        self.limpar(
            titulo_4,
            terra_regioes,
            faixa_parcial,
            faixa_total,
            cidade_total,
            cidade_parcial,
            cidade_fora,
            estados_regioes,
            seta_movimento,
            frase_regioes,
        )

        # ==================================================
        # CENA 7 — PORQUE NÃO ACONTECE TODOS OS MESES?
        # ==================================================

        pergunta_mensal = self.mostrar_pergunta(
            "SE A LUA DÁ UMA VOLTA TODOS OS MESES...\n"
            "PORQUE NÃO HÁ UM ECLIPSE TODOS OS MESES?",
            cor=YELLOW,
            pausa=1.0,
        )

        self.play(FadeOut(pergunta_mensal), run_time=0.45)

        titulo_5 = self.titulo_secao(
            "5",
            "A ÓRBITA DA LUA ESTÁ INCLINADA",
        )

        terra_orbita = self.criar_terra(
            raio=0.64,
            posicao=ORIGIN,
        )

        plano = Ellipse(
            width=9.4,
            height=2.75,
            color=GREY_B,
            stroke_opacity=0.44,
            stroke_width=3,
        )

        orbita = Ellipse(
            width=9.4,
            height=2.75,
            color=YELLOW,
            stroke_opacity=0.95,
            stroke_width=4,
        ).rotate(0.26)

        lua_orbita = self.criar_lua(
            raio=0.18,
            posicao=RIGHT * 4.05 + UP * 1.08,
        )

        self.narrar(
            "A órbita da Lua está inclinada cerca de cinco graus em relação ao plano da órbita terrestre.",
            [
                Write(titulo_5),
                FadeIn(terra_orbita),
                FadeIn(plano),
                FadeIn(orbita),
                FadeIn(lua_orbita),
            ],
        )

        self.narrar(
            "Por isso, na maioria das luas novas, a Lua passa ligeiramente acima ou abaixo da linha entre o Sol e a Terra.",
        )

        nodos = VGroup(
            Dot(
                point=LEFT * 4.05 + DOWN * 1.08,
                radius=0.11,
                color=RED,
            ),
            Dot(
                point=RIGHT * 4.05 + UP * 1.08,
                radius=0.11,
                color=RED,
            ),
        )

        linha_nodos = DashedLine(
            nodos[0].get_center(),
            nodos[1].get_center(),
            color=RED,
            dash_length=0.16,
        )

        self.narrar(
            "Só quando a Lua passa perto dos pontos onde os dois planos se cruzam é que pode ocorrer um eclipse.",
            [
                FadeIn(nodos),
                FadeIn(linha_nodos),
            ],
        )

        resposta_mensal = self.etiqueta(
            "O ALINHAMENTO PERFEITO É RARO",
            DOWN * 2.55,
            YELLOW,
            30,
        )

        self.narrar(
            "Portanto, não basta existir uma Lua nova. É preciso que o alinhamento aconteça no ponto certo.",
            FadeIn(resposta_mensal),
        )

        self.limpar(
            titulo_5,
            terra_orbita,
            plano,
            orbita,
            lua_orbita,
            nodos,
            linha_nodos,
            resposta_mensal,
        )

        # ==================================================
        # CENA 8 — TIPOS DE ECLIPSE
        # ==================================================

        titulo_6 = self.titulo_secao(
            "6",
            "TODOS OS ECLIPSES SÃO IGUAIS?",
        )

        pergunta_tipos = self.mostrar_pergunta(
            "TOTAL, PARCIAL OU ANULAR...\n"
            "QUAL É A DIFERENÇA?",
            cor=WHITE,
            pausa=0.75,
        )

        self.play(FadeOut(pergunta_tipos), run_time=0.4)

        posicoes = [
            LEFT * 4.8,
            ORIGIN,
            RIGHT * 4.8,
        ]

        sois = VGroup(
            *[
                Circle(
                    radius=0.82,
                    color=YELLOW,
                    fill_color=YELLOW,
                    fill_opacity=1,
                ).move_to(posicao)
                for posicao in posicoes
            ]
        )

        luas = VGroup(
            Circle(
                radius=0.80,
                color=BLACK,
                fill_color=BLACK,
                fill_opacity=1,
            ).move_to(posicoes[0]),
            Circle(
                radius=0.80,
                color=BLACK,
                fill_color=BLACK,
                fill_opacity=1,
            ).move_to(posicoes[1] + RIGHT * 0.42),
            Circle(
                radius=0.60,
                color=BLACK,
                fill_color=BLACK,
                fill_opacity=1,
            ).move_to(posicoes[2]),
        )

        nomes = VGroup(
            Text(
                "TOTAL",
                font_size=28,
                color=WHITE,
                weight="BOLD",
            ).next_to(sois[0], DOWN, buff=0.28),
            Text(
                "PARCIAL",
                font_size=28,
                color=WHITE,
                weight="BOLD",
            ).next_to(sois[1], DOWN, buff=0.28),
            Text(
                "ANULAR",
                font_size=28,
                color=WHITE,
                weight="BOLD",
            ).next_to(sois[2], DOWN, buff=0.28),
        )

        self.narrar(
            "Num eclipse total, a Lua cobre completamente o disco solar para quem está dentro da umbra.",
            [
                Write(titulo_6),
                FadeIn(sois[0]),
                FadeIn(luas[0]),
                FadeIn(nomes[0]),
            ],
        )

        self.narrar(
            "Num eclipse parcial, os discos não ficam totalmente sobrepostos.",
            [
                FadeIn(sois[1]),
                FadeIn(luas[1]),
                FadeIn(nomes[1]),
            ],
        )

        self.narrar(
            "Num eclipse anular, a Lua está mais distante, parece menor e deixa um anel de luz em redor.",
            [
                FadeIn(sois[2]),
                FadeIn(luas[2]),
                FadeIn(nomes[2]),
            ],
        )

        self.limpar(titulo_6, sois, luas, nomes)

        # ==================================================
        # CENA 9 — OS ANIMAIS PENSAM QUE É NOITE?
        # ==================================================

        pergunta_animais = self.mostrar_pergunta(
            "SERÁ QUE OS ANIMAIS PENSAM QUE JÁ É NOITE?",
            cor=ORANGE,
            pausa=1.0,
        )

        self.play(FadeOut(pergunta_animais), run_time=0.45)

        titulo_7 = self.titulo_secao(
            "7",
            "A NATUREZA REAGE À MUDANÇA DA LUZ",
        )

        # Cartão 1 — aves
        passaro_corpo = Ellipse(
            width=1.00,
            height=0.58,
            color=ORANGE,
            fill_color=ORANGE,
            fill_opacity=1,
            stroke_width=2,
        )
        passaro_cabeca = Circle(
            radius=0.22,
            color=ORANGE,
            fill_color=ORANGE,
            fill_opacity=1,
        ).next_to(passaro_corpo, RIGHT, buff=-0.08)
        passaro_bico = Polygon(
            ORIGIN,
            RIGHT * 0.28 + UP * 0.10,
            RIGHT * 0.28 + DOWN * 0.10,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).next_to(passaro_cabeca, RIGHT, buff=0.0)
        passaro_asa = Arc(
            radius=0.35,
            start_angle=0.10,
            angle=2.50,
            color=BLACK,
            stroke_width=4,
        ).move_to(passaro_corpo)
        passaro = VGroup(
            passaro_corpo,
            passaro_cabeca,
            passaro_bico,
            passaro_asa,
        )

        cartao_aves_fundo = RoundedRectangle(
            width=3.75,
            height=3.15,
            corner_radius=0.18,
            fill_color=BLACK,
            fill_opacity=0.92,
            stroke_color=ORANGE,
            stroke_opacity=0.85,
            stroke_width=2,
        )
        passaro.move_to(cartao_aves_fundo.get_center() + UP * 0.42)
        texto_aves = Text(
            "AVES
PROCURAM ABRIGO",
            font_size=27,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.88,
        ).move_to(cartao_aves_fundo.get_center() + DOWN * 0.75)
        cartao_aves = VGroup(
            cartao_aves_fundo,
            passaro,
            texto_aves,
        ).move_to(LEFT * 4.35)

        # Cartão 2 — insetos noturnos
        inseto_corpo = VGroup(
            Circle(
                radius=0.26,
                color=GREEN,
                fill_color=GREEN,
                fill_opacity=1,
            ),
            Circle(
                radius=0.18,
                color=GREEN,
                fill_color=GREEN,
                fill_opacity=1,
            ).shift(UP * 0.36),
            Line(LEFT * 0.24, RIGHT * 0.24, color=WHITE, stroke_width=2),
            Line(LEFT * 0.42 + UP * 0.12, RIGHT * 0.42 + DOWN * 0.12, color=GREEN, stroke_width=3),
            Line(LEFT * 0.42 + DOWN * 0.12, RIGHT * 0.42 + UP * 0.12, color=GREEN, stroke_width=3),
        )

        cartao_insetos_fundo = RoundedRectangle(
            width=3.75,
            height=3.15,
            corner_radius=0.18,
            fill_color=BLACK,
            fill_opacity=0.92,
            stroke_color=GREEN,
            stroke_opacity=0.85,
            stroke_width=2,
        )
        inseto_corpo.move_to(cartao_insetos_fundo.get_center() + UP * 0.42)
        texto_insetos = Text(
            "INSETOS NOTURNOS
FICAM ATIVOS",
            font_size=25,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.88,
        ).move_to(cartao_insetos_fundo.get_center() + DOWN * 0.75)
        cartao_insetos = VGroup(
            cartao_insetos_fundo,
            inseto_corpo,
            texto_insetos,
        ).move_to(ORIGIN)

        # Cartão 3 — descida de temperatura
        termometro = VGroup(
            Rectangle(
                width=0.34,
                height=1.65,
                color=WHITE,
                fill_opacity=0,
            ),
            Rectangle(
                width=0.18,
                height=1.15,
                color=BLUE_B,
                fill_color=BLUE_B,
                fill_opacity=1,
            ).shift(DOWN * 0.24),
            Circle(
                radius=0.28,
                color=BLUE_B,
                fill_color=BLUE_B,
                fill_opacity=1,
            ).shift(DOWN * 0.95),
        )

        seta_frio = Arrow(
            UP * 0.75,
            DOWN * 0.55,
            color=BLUE_B,
            buff=0,
        ).next_to(termometro, RIGHT, buff=0.28)

        cartao_frio_fundo = RoundedRectangle(
            width=3.75,
            height=3.15,
            corner_radius=0.18,
            fill_color=BLACK,
            fill_opacity=0.92,
            stroke_color=BLUE_B,
            stroke_opacity=0.85,
            stroke_width=2,
        )
        VGroup(termometro, seta_frio).move_to(
            cartao_frio_fundo.get_center() + UP * 0.42
        )
        texto_frio = Text(
            "A TEMPERATURA
PODE DESCER",
            font_size=26,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.88,
        ).move_to(cartao_frio_fundo.get_center() + DOWN * 0.75)
        cartao_frio = VGroup(
            cartao_frio_fundo,
            termometro,
            seta_frio,
            texto_frio,
        ).move_to(RIGHT * 4.35)

        cartoes_natureza = VGroup(
            cartao_aves,
            cartao_insetos,
            cartao_frio,
        )

        self.narrar(
            "Muitos animais não compreendem o eclipse como nós. Mas reagem à rápida mudança de luz e temperatura.",
            [
                Write(titulo_7),
                FadeIn(cartoes_natureza),
            ],
        )

        self.narrar(
            "Algumas aves deixam de cantar e procuram abrigo, como fariam ao anoitecer.",
            cartao_aves.animate.scale(1.05),
        )

        self.narrar(
            "Alguns insetos noturnos tornam-se ativos, enquanto outros animais ficam inquietos ou confusos.",
            cartao_insetos.animate.scale(1.05),
        )

        resposta_animais = Text(
            "NÃO PENSAM: «CHEGOU A NOITE».
"
            "REAGEM AOS SINAIS DO AMBIENTE.",
            font_size=31,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.90,
        ).move_to(DOWN * 2.75)

        if resposta_animais.width > 11.8:
            resposta_animais.scale_to_fit_width(11.8)

        self.narrar(
            "Portanto, não é que pensem conscientemente que chegou a noite. O comportamento muda porque os sinais do ambiente mudaram.",
            Write(resposta_animais),
        )

        self.limpar(
            titulo_7,
            cartoes_natureza,
            resposta_animais,
        )

        # ==================================================
        # CENA 10 — PORQUE A TEMPERATURA DESCE?
        # ==================================================

        pergunta_temperatura = self.mostrar_pergunta(
            "PORQUE É QUE A TEMPERATURA DESCE?",
            cor=BLUE_B,
            pausa=0.85,
        )

        self.play(FadeOut(pergunta_temperatura), run_time=0.4)

        sol_calor = self.criar_sol(
            raio=0.90,
            posicao=LEFT * 4.8,
            intensidade=0.85,
        )

        solo = Rectangle(
            width=4.5,
            height=1.05,
            fill_color=ORANGE,
            fill_opacity=0.70,
            stroke_opacity=0,
        ).move_to(RIGHT * 3.8 + DOWN * 1.8)

        raios_calor = VGroup(
            *[
                Arrow(
                    sol_calor.get_right() + UP * deslocamento,
                    solo.get_left() + UP * deslocamento * 0.35,
                    color=YELLOW,
                    buff=0.15,
                )
                for deslocamento in (-0.55, 0, 0.55)
            ]
        )

        self.narrar(
            "Normalmente, o solo recebe continuamente energia do Sol.",
            [
                FadeIn(sol_calor),
                FadeIn(solo),
                FadeIn(raios_calor),
            ],
        )

        lua_bloqueio = Circle(
            radius=0.62,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_color=WHITE,
            stroke_width=2,
        ).move_to(LEFT * 1.7)

        self.narrar(
            "Quando a Lua bloqueia grande parte dessa luz, o solo deixa de receber tanta energia durante alguns minutos.",
            FadeIn(lua_bloqueio),
        )

        seta_descida = Arrow(
            RIGHT * 4.3 + UP * 1.25,
            RIGHT * 4.3 + DOWN * 0.75,
            color=BLUE_B,
        )

        temperatura = Text(
            "TEMPERATURA ↓",
            font_size=39,
            color=BLUE_B,
            weight="BOLD",
        ).next_to(seta_descida, RIGHT, buff=0.25)

        self.narrar(
            "O ar junto ao solo começa a arrefecer, e a descida pode ser sentida pelas pessoas e pelos animais.",
            [
                GrowArrow(seta_descida),
                Write(temperatura),
            ],
        )

        self.limpar(
            sol_calor,
            solo,
            raios_calor,
            lua_bloqueio,
            seta_descida,
            temperatura,
        )

        # ==================================================
        # CENA 11 — É SEGURO OLHAR?
        # ==================================================

        pergunta_segurança = self.mostrar_pergunta(
            "É SEGURO OLHAR DIRETAMENTE PARA UM ECLIPSE?",
            cor=RED,
            pausa=1.0,
        )

        self.play(FadeOut(pergunta_segurança), run_time=0.45)

        sol_seguro = self.criar_sol(
            raio=0.92,
            posicao=LEFT * 3.8,
            intensidade=0.85,
        )

        olho = VGroup(
            Ellipse(
                width=2.3,
                height=1.12,
                color=WHITE,
                stroke_width=3,
            ),
            Circle(
                radius=0.28,
                color=BLUE,
                fill_color=BLUE,
                fill_opacity=1,
            ),
            Circle(
                radius=0.10,
                color=BLACK,
                fill_color=BLACK,
                fill_opacity=1,
            ),
        ).move_to(RIGHT * 3.8)

        seta_perigo = Arrow(
            sol_seguro.get_right(),
            olho.get_left(),
            color=RED,
            buff=0.25,
        )

        self.narrar(
            "Não. Olhar diretamente para o Sol sem proteção adequada pode causar lesões graves nos olhos.",
            [
                FadeIn(sol_seguro),
                FadeIn(olho),
                GrowArrow(seta_perigo),
            ],
        )

        filtro = Rectangle(
            width=1.05,
            height=1.75,
            color=GREEN,
            fill_color=BLACK,
            fill_opacity=0.92,
            stroke_width=3,
        ).move_to(ORIGIN)

        setas_seguras = VGroup(
            Arrow(
                sol_seguro.get_right(),
                filtro.get_left(),
                color=GREEN,
                buff=0.15,
            ),
            Arrow(
                filtro.get_right(),
                olho.get_left(),
                color=GREEN,
                buff=0.15,
            ),
        )

        self.narrar(
            "Durante as fases parciais ou anulares, é necessário usar filtros solares próprios e certificados.",
            [
                FadeOut(seta_perigo),
                FadeIn(filtro),
                GrowArrow(setas_seguras[0]),
                GrowArrow(setas_seguras[1]),
            ],
        )

        aviso = self.etiqueta(
            "ÓCULOS ESCUROS COMUNS NÃO PROTEGEM",
            DOWN * 2.25,
            RED,
            29,
        )

        self.narrar(
            "Óculos escuros comuns não são suficientes.",
            FadeIn(aviso),
        )

        self.narrar(
            "A regra é simples: enquanto qualquer parte brilhante do Sol estiver visível, os olhos precisam de proteção adequada.",
        )

        self.limpar(
            sol_seguro,
            olho,
            filtro,
            setas_seguras,
            aviso,
        )

        # ==================================================
        # CENA 12 — OS ECLIPSES VÃO ACABAR?
        # ==================================================

        pergunta_futuro = self.mostrar_pergunta(
            "SERÁ QUE UM DIA VÃO DEIXAR DE EXISTIR ECLIPSES TOTAIS?",
            cor=GREEN,
            pausa=1.0,
        )

        self.play(FadeOut(pergunta_futuro), run_time=0.45)

        terra_futuro = self.criar_terra(
            raio=0.72,
            posicao=LEFT * 4.4,
        )

        lua_futuro = self.criar_lua(
            raio=0.30,
            posicao=LEFT * 1.7,
        )

        sol_futuro = self.criar_sol(
            raio=0.86,
            posicao=RIGHT * 4.6,
            intensidade=0.75,
        )

        self.narrar(
            "Sim, num futuro muito distante. A Lua está lentamente a afastar-se da Terra.",
            [
                FadeIn(terra_futuro),
                FadeIn(lua_futuro),
                FadeIn(sol_futuro),
            ],
        )

        taxa = self.etiqueta(
            "≈ 3,8 CENTÍMETROS POR ANO",
            DOWN * 2.25,
            YELLOW,
            31,
        )

        self.narrar(
            "A distância aumenta cerca de três vírgula oito centímetros por ano.",
            [
                lua_futuro.animate.shift(RIGHT * 0.95),
                FadeIn(taxa),
            ],
        )

        anel = Circle(
            radius=0.56,
            stroke_color=YELLOW,
            stroke_width=9,
        ).move_to(RIGHT * 1.0)

        lua_menor = Circle(
            radius=0.40,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1,
        ).move_to(RIGHT * 1.0)

        self.narrar(
            "À medida que se afasta, a Lua parece cada vez menor vista daqui.",
            [
                FadeOut(taxa),
                FadeIn(anel),
                FadeIn(lua_menor),
            ],
        )

        futuro = Text(
            "UM DIA, A LUA PARECERÁ\n"
            "PEQUENA DEMAIS PARA COBRIR TODO O SOL.",
            font_size=36,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.90,
        ).move_to(DOWN * 2.20)

        self.narrar(
            "Um dia, já não parecerá suficientemente grande para produzir eclipses totais.",
            Write(futuro),
        )

        alivio = self.etiqueta(
            "AINDA FALTAM CENTENAS DE MILHÕES DE ANOS",
            UP * 2.45,
            GREEN,
            27,
        )

        self.narrar(
            "Mas isso só acontecerá daqui a centenas de milhões de anos.",
            FadeIn(alivio),
        )

        self.limpar(
            terra_futuro,
            lua_futuro,
            sol_futuro,
            anel,
            lua_menor,
            futuro,
            alivio,
            estrelas,
        )

        # ==================================================
        # CENA 13 — RESUMO FINAL
        # ==================================================

        resumo_titulo = Text(
            "AGORA JÁ CONSEGUES EXPLICAR UM ECLIPSE",
            font_size=45,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.45)

        if resumo_titulo.width > 12.8:
            resumo_titulo.scale_to_fit_width(12.8)

        resumo = VGroup(
            Text(
                "A Lua passa entre o Sol e a Terra.",
                font_size=31,
                color=WHITE,
            ),
            Text(
                "A umbra cria o eclipse total.",
                font_size=31,
                color=WHITE,
            ),
            Text(
                "A penumbra cria o eclipse parcial.",
                font_size=31,
                color=WHITE,
            ),
            Text(
                "A sombra só atravessa algumas regiões.",
                font_size=31,
                color=WHITE,
            ),
            Text(
                "A órbita inclinada impede eclipses mensais.",
                font_size=31,
                color=WHITE,
            ),
            Text(
                "A distância faz a Lua parecer do tamanho do Sol.",
                font_size=31,
                color=WHITE,
            ),
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.28,
        ).move_to(DOWN * 0.10)

        self.narrar(
            "Um eclipse não é o desaparecimento do Sol.",
            Write(resumo_titulo),
        )

        self.narrar(
            "É o resultado de tamanhos, distâncias, órbitas e sombras que se combinam de uma forma quase perfeita.",
            FadeIn(resumo),
        )

        self.limpar(resumo_titulo, resumo)

        frase_final = Text(
            "UMA PEQUENA LUA.\n"
            "UMA SOMBRA ESTREITA.\n"
            "UM ESPETÁCULO GIGANTE.",
            font_size=44,
            color=YELLOW,
            weight="BOLD",
            line_spacing=0.90,
        )

        self.narrar(
            "Uma pequena Lua, uma sombra estreita e um dos maiores espetáculos que podemos observar no céu.",
            Write(frase_final),
        )

        self.play(FadeOut(frase_final), run_time=0.6)

        proximo = Text(
            "PRÓXIMO EPISÓDIO:\n"
            "PORQUE A LUA NÃO CAI SOBRE A TERRA?",
            font_size=39,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.90,
        )

        if proximo.width > 12.5:
            proximo.scale_to_fit_width(12.5)

        self.narrar(
            "No próximo episódio, vamos descobrir porque a Lua nunca cai sobre a Terra.",
            Write(proximo),
        )

        assinatura = Text(
            "SEGUE O CANAL APRENDER MESMO",
            font_size=34,
            color=YELLOW,
            weight="BOLD",
        ).next_to(proximo, DOWN, buff=0.55)

        self.narrar(
            "Segue o canal Aprender Mesmo e continua a descobrir o Universo de forma simples e visual.",
            FadeIn(assinatura),
            mostrar_legenda=False,
        )

        self.wait(1.5)

        self.play(
            FadeOut(VGroup(proximo, assinatura)),
            run_time=0.8,
        )
