from manim import (
    BLACK, BLUE, BLUE_B, BLUE_D, DOWN, FadeIn, FadeOut, GREY_B,
    GREEN, LEFT, ORANGE, ORIGIN, RED, RIGHT, UP, WHITE, YELLOW,
    Arc, Arrow, Circle, DashedLine, Dot, Ellipse, GrowArrow,
    GrowFromCenter, Line, Polygon, Rectangle, Text, VGroup, Write
)

from engine.scene import CenaLong


class Episodio001EclipseLong(CenaLong):
    """
    Vídeo horizontal 16:9 sobre eclipses solares.
    Estrutura preparada para ultrapassar 6 minutos.
    """

    def titulo_secao(self, texto: str) -> Text:
        return Text(
            texto,
            font_size=40,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.4)

    def limpar(self, *objetos) -> None:
        self.play(
            FadeOut(VGroup(*objetos)),
            run_time=0.8,
        )

    def construct(self) -> None:
        estrelas = VGroup(
            *[
                Dot(
                    point=[
                        -6.7 + (indice % 14),
                        -3.5 + ((indice * 7) % 8),
                        0,
                    ],
                    radius=0.018,
                    color=WHITE,
                ).set_opacity(0.40)
                for indice in range(90)
            ]
        )

        sol_abertura = Circle(
            radius=1.65,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        )

        lua_abertura = Circle(
            radius=1.58,
            color=GREY_B,
            fill_color=BLACK,
            fill_opacity=1,
        ).move_to(RIGHT * 5.7)

        self.add(estrelas)

        self.narrar(
            "Durante alguns minutos, o dia pode transformar-se em noite.",
            GrowFromCenter(sol_abertura),
        )

        self.narrar(
            "A temperatura desce, as sombras mudam e muitos animais comportam-se como se a noite tivesse chegado de repente.",
            lua_abertura.animate.move_to(sol_abertura.get_center()),
        )

        coroa = VGroup(
            *[
                Circle(
                    radius=1.65 + indice * 0.12,
                    stroke_color=WHITE,
                    stroke_opacity=max(0.05, 0.34 - indice * 0.045),
                    stroke_width=2,
                )
                for indice in range(1, 7)
            ]
        )

        self.narrar(
            "Mas como consegue a pequena Lua esconder uma estrela gigantesca?",
            FadeIn(coroa),
        )

        titulo = Text(
            "ECLIPSE SOLAR",
            font_size=58,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.5)

        subtitulo = Text(
            "Como acontece, porque só algumas regiões o veem\n"
            "e porque não ocorre todos os meses",
            font_size=29,
            color=GREY_B,
            line_spacing=0.95,
        ).next_to(titulo, DOWN, buff=0.35)

        self.play(
            Write(titulo),
            FadeIn(subtitulo),
            run_time=1.3,
        )
        self.wait(1)

        self.limpar(
            sol_abertura,
            lua_abertura,
            coroa,
            titulo,
            subtitulo,
        )

        # 1 — O QUE É UM ECLIPSE
        titulo_1 = self.titulo_secao("1. O QUE É UM ECLIPSE SOLAR?")

        sol = Circle(
            radius=0.95,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(LEFT * 5.2)

        lua = Circle(
            radius=0.29,
            color=GREY_B,
            fill_color=GREY_B,
            fill_opacity=1,
        ).move_to(UP * 1.4)

        terra = Circle(
            radius=0.72,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
        ).move_to(RIGHT * 4.8)

        nomes = VGroup(
            Text("SOL", font_size=24, color=YELLOW).next_to(sol, DOWN),
            Text("LUA", font_size=23, color=GREY_B).next_to(lua, UP),
            Text("TERRA", font_size=24, color=BLUE).next_to(terra, DOWN),
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
            "Ao entrar nessa posição, a Lua bloqueia parte da luz solar que seguiria em direção ao nosso planeta.",
            lua.animate.move_to(LEFT * 0.15),
        )

        linha_1 = Line(
            sol.get_right(),
            lua.get_left(),
            color=YELLOW,
            stroke_opacity=0.65,
            stroke_width=3,
        )

        linha_2 = Line(
            lua.get_right(),
            terra.get_left(),
            color=GREY_B,
            stroke_opacity=0.65,
            stroke_width=3,
        )

        self.narrar(
            "Visto de lado, parece simples: Sol, Lua e Terra quase alinhados.",
            [
                FadeIn(linha_1),
                FadeIn(linha_2),
            ],
        )

        alinhamento = Text(
            "SOL  →  LUA  →  TERRA",
            font_size=38,
            color=WHITE,
            weight="BOLD",
        ).move_to(DOWN * 2.4)

        self.narrar(
            "Mas a palavra quase é importante, porque um pequeno desvio muda completamente o que vemos.",
            Write(alinhamento),
        )

        self.limpar(
            titulo_1,
            sol,
            lua,
            terra,
            nomes,
            linha_1,
            linha_2,
            alinhamento,
        )

        # 2 — TAMANHO APARENTE
        titulo_2 = self.titulo_secao(
            "2. COMO PODE A LUA TAPAR O SOL?"
        )

        sol_grande = Circle(
            radius=1.65,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(LEFT * 3.7)

        lua_pequena = Circle(
            radius=0.25,
            color=GREY_B,
            fill_color=GREY_B,
            fill_opacity=1,
        ).move_to(RIGHT * 3.5)

        self.narrar(
            "A Lua é muito menor do que o Sol. O diâmetro solar é aproximadamente quatrocentas vezes maior.",
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
                line_spacing=0.9,
            ).next_to(sol_grande, DOWN, buff=0.35),
            Text(
                "LUA\n≈ 3 474 km",
                font_size=28,
                color=GREY_B,
                line_spacing=0.9,
            ).next_to(lua_pequena, DOWN, buff=0.35),
        )

        self.narrar(
            "Se estivessem à mesma distância, a Lua pareceria minúscula e nunca conseguiria cobrir o Sol.",
            FadeIn(medidas),
        )

        terra_observador = Circle(
            radius=0.58,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
        ).move_to(RIGHT * 5.1)

        self.narrar(
            "O detalhe decisivo é a distância. O Sol também está aproximadamente quatrocentas vezes mais longe da Terra do que a Lua.",
            [
                FadeOut(medidas),
                sol_grande.animate.scale(0.42).move_to(LEFT * 5.2),
                lua_pequena.animate.scale(1.35).move_to(ORIGIN),
                FadeIn(terra_observador),
            ],
        )

        raios = VGroup(
            DashedLine(
                terra_observador.get_center(),
                sol_grande.get_center(),
                color=YELLOW,
                dash_length=0.18,
            ),
            DashedLine(
                terra_observador.get_center(),
                lua_pequena.get_center(),
                color=GREY_B,
                dash_length=0.18,
            ),
        )

        self.narrar(
            "Por causa desta relação entre tamanho e distância, os dois discos parecem quase iguais no céu.",
            FadeIn(raios),
        )

        aparente_sol = Circle(
            radius=0.67,
            stroke_color=YELLOW,
            stroke_width=8,
        ).move_to(DOWN * 1.9)

        aparente_lua = Circle(
            radius=0.64,
            stroke_color=GREY_B,
            stroke_width=5,
        ).move_to(DOWN * 1.9)

        self.narrar(
            "É uma coincidência cósmica extraordinária: a Lua parece ter precisamente o tamanho necessário para cobrir o Sol.",
            [
                FadeIn(aparente_sol),
                FadeIn(aparente_lua),
            ],
        )

        self.limpar(
            titulo_2,
            sol_grande,
            lua_pequena,
            terra_observador,
            raios,
            aparente_sol,
            aparente_lua,
        )

        # 3 — UMBRA E PENUMBRA
        titulo_3 = self.titulo_secao(
            "3. A SOMBRA DA LUA NÃO É TODA IGUAL"
        )

        sol_sombra = Circle(
            radius=1.05,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(LEFT * 5.3)

        lua_sombra = Circle(
            radius=0.32,
            color=GREY_B,
            fill_color=GREY_B,
            fill_opacity=1,
        ).move_to(LEFT * 0.7)

        terra_sombra = Circle(
            radius=0.82,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
        ).move_to(RIGHT * 4.9)

        self.narrar(
            "A sombra criada pela Lua divide-se em regiões diferentes.",
            [
                Write(titulo_3),
                FadeIn(sol_sombra),
                FadeIn(lua_sombra),
                FadeIn(terra_sombra),
            ],
        )

        umbra = Polygon(
            lua_sombra.get_center() + UP * 0.18,
            terra_sombra.get_center() + UP * 0.16,
            terra_sombra.get_center() + DOWN * 0.16,
            lua_sombra.get_center() + DOWN * 0.18,
            fill_color=BLACK,
            fill_opacity=0.92,
            stroke_color=WHITE,
            stroke_opacity=0.25,
        )

        penumbra_superior = Polygon(
            sol_sombra.get_center() + UP * 0.85,
            lua_sombra.get_center() + UP * 0.22,
            terra_sombra.get_center() + UP * 0.62,
            terra_sombra.get_center() + UP * 0.18,
            fill_color=GREY_B,
            fill_opacity=0.22,
            stroke_opacity=0,
        )

        penumbra_inferior = Polygon(
            sol_sombra.get_center() + DOWN * 0.85,
            lua_sombra.get_center() + DOWN * 0.22,
            terra_sombra.get_center() + DOWN * 0.62,
            terra_sombra.get_center() + DOWN * 0.18,
            fill_color=GREY_B,
            fill_opacity=0.22,
            stroke_opacity=0,
        )

        self.narrar(
            "No centro está a umbra, onde a Lua tapa completamente o disco solar.",
            FadeIn(umbra),
        )

        self.narrar(
            "À volta existe a penumbra, onde apenas parte do Sol fica escondida.",
            [
                FadeIn(penumbra_superior),
                FadeIn(penumbra_inferior),
            ],
        )

        rotulos = VGroup(
            Text(
                "UMBRA\nECLIPSE TOTAL",
                font_size=26,
                color=WHITE,
                line_spacing=0.85,
            ).move_to(DOWN * 2.0),
            Text(
                "PENUMBRA\nECLIPSE PARCIAL",
                font_size=26,
                color=GREY_B,
                line_spacing=0.85,
            ).move_to(UP * 2.0),
        )

        self.narrar(
            "Por isso, duas pessoas em cidades diferentes podem observar eclipses muito diferentes no mesmo instante.",
            FadeIn(rotulos),
        )

        self.limpar(
            titulo_3,
            sol_sombra,
            lua_sombra,
            terra_sombra,
            umbra,
            penumbra_superior,
            penumbra_inferior,
            rotulos,
        )

        # 4 — REGIÕES
        titulo_4 = self.titulo_secao(
            "4. PORQUE SÓ ALGUMAS REGIÕES CONSEGUEM VER?"
        )

        terra_grande = Circle(
            radius=2.45,
            color=BLUE,
            fill_color=BLUE_D,
            fill_opacity=1,
        ).move_to(LEFT * 1.8)

        faixa_total = Arc(
            radius=2.15,
            start_angle=-0.45,
            angle=1.25,
            color=BLACK,
            stroke_width=16,
        ).move_to(terra_grande)

        faixa_parcial = Arc(
            radius=2.28,
            start_angle=-0.65,
            angle=1.65,
            color=GREY_B,
            stroke_width=34,
            stroke_opacity=0.35,
        ).move_to(terra_grande)

        self.narrar(
            "Quando a umbra chega à Terra, cobre apenas uma faixa estreita da superfície.",
            [
                Write(titulo_4),
                FadeIn(terra_grande),
                FadeIn(faixa_total),
                FadeIn(faixa_parcial),
            ],
        )

        cidade_total = Dot(
            terra_grande.get_center() + RIGHT * 1.6 + UP * 0.4,
            radius=0.10,
            color=YELLOW,
        )

        cidade_parcial = Dot(
            terra_grande.get_center() + RIGHT * 0.1 + UP * 1.75,
            radius=0.10,
            color=ORANGE,
        )

        cidade_fora = Dot(
            terra_grande.get_center() + LEFT * 1.4 + DOWN * 1.1,
            radius=0.10,
            color=RED,
        )

        self.narrar(
            "Quem estiver dentro da faixa central vê um eclipse total.",
            FadeIn(cidade_total),
        )

        self.narrar(
            "Quem estiver mais afastado, mas ainda dentro da penumbra, vê apenas um eclipse parcial.",
            FadeIn(cidade_parcial),
        )

        self.narrar(
            "E quem estiver fora de toda a sombra não vê eclipse nenhum.",
            FadeIn(cidade_fora),
        )

        seta_movimento = Arrow(
            LEFT * 0.8 + DOWN * 2.8,
            RIGHT * 3.3 + DOWN * 2.8,
            color=WHITE,
            buff=0,
        )

        texto_movimento = Text(
            "A sombra desloca-se sobre a Terra",
            font_size=30,
            color=WHITE,
        ).next_to(seta_movimento, UP, buff=0.2)

        self.narrar(
            "Como a Lua continua a mover-se e a Terra também roda, essa faixa atravessa diferentes regiões ao longo do tempo.",
            [
                GrowArrow(seta_movimento),
                Write(texto_movimento),
            ],
        )

        self.limpar(
            titulo_4,
            terra_grande,
            faixa_total,
            faixa_parcial,
            cidade_total,
            cidade_parcial,
            cidade_fora,
            seta_movimento,
            texto_movimento,
        )

        # 5 — TIPOS
        titulo_5 = self.titulo_secao(
            "5. TOTAL, PARCIAL OU ANULAR?"
        )

        total_sol = Circle(
            radius=1.05,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(LEFT * 4.5)

        total_lua = Circle(
            radius=1.02,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1,
        ).move_to(total_sol)

        parcial_sol = Circle(
            radius=1.05,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(ORIGIN)

        parcial_lua = Circle(
            radius=1.02,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1,
        ).move_to(ORIGIN + RIGHT * 0.55)

        anular_sol = Circle(
            radius=1.05,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(RIGHT * 4.5)

        anular_lua = Circle(
            radius=0.78,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1,
        ).move_to(anular_sol)

        rotulos_tipos = VGroup(
            Text("TOTAL", font_size=28, color=WHITE).next_to(total_sol, DOWN),
            Text("PARCIAL", font_size=28, color=WHITE).next_to(parcial_sol, DOWN),
            Text("ANULAR", font_size=28, color=WHITE).next_to(anular_sol, DOWN),
        )

        self.narrar(
            "Num eclipse total, a Lua cobre completamente o Sol para quem está na umbra.",
            [
                Write(titulo_5),
                FadeIn(total_sol),
                FadeIn(total_lua),
                FadeIn(rotulos_tipos[0]),
            ],
        )

        self.narrar(
            "Num eclipse parcial, apenas uma parte do Sol desaparece.",
            [
                FadeIn(parcial_sol),
                FadeIn(parcial_lua),
                FadeIn(rotulos_tipos[1]),
            ],
        )

        self.narrar(
            "Num eclipse anular, a Lua parece menor e deixa um anel brilhante à volta.",
            [
                FadeIn(anular_sol),
                FadeIn(anular_lua),
                FadeIn(rotulos_tipos[2]),
            ],
        )

        self.limpar(
            titulo_5,
            total_sol,
            total_lua,
            parcial_sol,
            parcial_lua,
            anular_sol,
            anular_lua,
            rotulos_tipos,
        )

        # 6 — PORQUE NÃO TODOS OS MESES
        titulo_6 = self.titulo_secao(
            "6. PORQUE NÃO HÁ ECLIPSE TODOS OS MESES?"
        )

        terra_orbita = Circle(
            radius=0.72,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
        )

        orbita_horizontal = Ellipse(
            width=8.2,
            height=2.8,
            color=GREY_B,
            stroke_opacity=0.45,
        )

        orbita_inclinada = Ellipse(
            width=8.2,
            height=2.8,
            color=YELLOW,
            stroke_opacity=0.9,
        ).rotate(0.28)

        lua_orbita = Dot(
            point=RIGHT * 3.7 + UP * 0.95,
            radius=0.15,
            color=GREY_B,
        )

        self.narrar(
            "Se a Lua completa uma volta à Terra todos os meses, porque não existe um eclipse mensal?",
            [
                Write(titulo_6),
                FadeIn(terra_orbita),
                FadeIn(orbita_horizontal),
                FadeIn(orbita_inclinada),
                FadeIn(lua_orbita),
            ],
        )

        self.narrar(
            "Porque a órbita da Lua está inclinada cerca de cinco graus em relação ao plano da órbita terrestre.",
        )

        acima = Text(
            "A LUA PASSA\nACIMA OU ABAIXO",
            font_size=36,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.9,
        ).move_to(DOWN * 2.5)

        self.narrar(
            "Na maioria das luas novas, ela passa ligeiramente acima ou abaixo da linha entre o Sol e a Terra.",
            Write(acima),
        )

        nodo_1 = Dot(
            point=LEFT * 3.7 + DOWN * 0.95,
            radius=0.11,
            color=RED,
        )

        nodo_2 = Dot(
            point=RIGHT * 3.7 + UP * 0.95,
            radius=0.11,
            color=RED,
        )

        linha_nodos = DashedLine(
            nodo_1.get_center(),
            nodo_2.get_center(),
            color=RED,
            dash_length=0.15,
        )

        self.narrar(
            "Os eclipses só acontecem perto dos pontos em que as duas órbitas se cruzam, chamados nós.",
            [
                FadeOut(acima),
                FadeIn(nodo_1),
                FadeIn(nodo_2),
                FadeIn(linha_nodos),
            ],
        )

        self.limpar(
            titulo_6,
            terra_orbita,
            orbita_horizontal,
            orbita_inclinada,
            lua_orbita,
            nodo_1,
            nodo_2,
            linha_nodos,
        )

        # 7 — DURAÇÃO
        titulo_7 = self.titulo_secao(
            "7. PORQUE A TOTALIDADE DURA TÃO POUCO?"
        )

        faixa = Rectangle(
            width=10.5,
            height=0.65,
            fill_color=GREY_B,
            fill_opacity=0.25,
            stroke_color=GREY_B,
            stroke_opacity=0.4,
        )

        sombra_movel = Circle(
            radius=0.33,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1,
        ).move_to(LEFT * 5.0)

        observador = Dot(
            point=ORIGIN,
            radius=0.11,
            color=YELLOW,
        )

        self.narrar(
            "A umbra é pequena e desloca-se rapidamente sobre a superfície terrestre.",
            [
                Write(titulo_7),
                FadeIn(faixa),
                FadeIn(sombra_movel),
                FadeIn(observador),
            ],
        )

        self.narrar(
            "Para uma pessoa num único lugar, a sombra passa e vai embora em poucos minutos.",
            sombra_movel.animate.move_to(RIGHT * 5.0),
        )

        relogio = Text(
            "TOTALIDADE:\nAPENAS ALGUNS MINUTOS",
            font_size=38,
            color=YELLOW,
            weight="BOLD",
            line_spacing=0.9,
        ).move_to(DOWN * 2.1)

        self.narrar(
            "Por isso, mesmo durante um grande eclipse, a fase total é breve.",
            Write(relogio),
        )

        self.limpar(
            titulo_7,
            faixa,
            sombra_movel,
            observador,
            relogio,
        )

        # 8 — NATUREZA
        titulo_8 = self.titulo_secao(
            "8. O QUE MUDA DURANTE A TOTALIDADE?"
        )

        termometro = VGroup(
            Rectangle(
                width=0.45,
                height=3.1,
                color=WHITE,
                fill_opacity=0,
            ),
            Rectangle(
                width=0.25,
                height=2.5,
                color=RED,
                fill_color=RED,
                fill_opacity=1,
            ).align_to(ORIGIN, DOWN),
            Circle(
                radius=0.38,
                color=RED,
                fill_color=RED,
                fill_opacity=1,
            ).shift(DOWN * 1.7),
        ).move_to(LEFT * 4.5)

        ceu_dia = Rectangle(
            width=4.2,
            height=3.2,
            fill_color=BLUE_B,
            fill_opacity=1,
            stroke_opacity=0,
        ).move_to(ORIGIN)

        ceu_noite = Rectangle(
            width=4.2,
            height=3.2,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_opacity=0,
        ).move_to(ORIGIN)

        animal = Circle(
            radius=0.45,
            color=ORANGE,
            fill_color=ORANGE,
            fill_opacity=1,
        ).move_to(RIGHT * 4.5)

        self.narrar(
            "Quando a luz solar diminui rapidamente, a temperatura pode descer e o ambiente muda de forma percetível.",
            [
                Write(titulo_8),
                FadeIn(termometro),
                FadeIn(ceu_dia),
                FadeIn(animal),
            ],
        )

        self.narrar(
            "O céu escurece o suficiente para revelar estrelas e planetas brilhantes.",
            FadeIn(ceu_noite),
        )

        comportamento = Text(
            "ALGUNS ANIMAIS\nCOMPORTAM-SE COMO SE FOSSE NOITE",
            font_size=32,
            color=WHITE,
            weight="BOLD",
            line_spacing=0.9,
        ).move_to(DOWN * 2.3)

        self.narrar(
            "Alguns animais regressam aos locais onde dormem, enquanto outros iniciam atividades noturnas.",
            Write(comportamento),
        )

        self.limpar(
            titulo_8,
            termometro,
            ceu_dia,
            ceu_noite,
            animal,
            comportamento,
        )

        # 9 — SEGURANÇA
        titulo_9 = self.titulo_secao(
            "9. COMO OBSERVAR EM SEGURANÇA?"
        )

        sol_seguranca = Circle(
            radius=1.15,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        ).move_to(LEFT * 3.2)

        olho = VGroup(
            Ellipse(
                width=2.2,
                height=1.1,
                color=WHITE,
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
        ).move_to(RIGHT * 3.2)

        seta_perigo = Arrow(
            sol_seguranca.get_right(),
            olho.get_left(),
            color=RED,
            buff=0.2,
        )

        self.narrar(
            "Olhar diretamente para o Sol sem proteção adequada pode causar lesões graves nos olhos.",
            [
                Write(titulo_9),
                FadeIn(sol_seguranca),
                FadeIn(olho),
                GrowArrow(seta_perigo),
            ],
        )

        filtro = Rectangle(
            width=1.0,
            height=1.7,
            color=GREEN,
            fill_color=BLACK,
            fill_opacity=0.75,
        ).move_to(ORIGIN)

        setas_seguras = VGroup(
            Arrow(
                sol_seguranca.get_right(),
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
            "Durante as fases parciais, devem ser usados filtros solares próprios, e não óculos escuros comuns.",
            [
                FadeOut(seta_perigo),
                FadeIn(filtro),
                GrowArrow(setas_seguras[0]),
                GrowArrow(setas_seguras[1]),
            ],
        )

        aviso = Text(
            "PROTEÇÃO CERTIFICADA\nSEMPRE QUE O SOL AINDA É VISÍVEL",
            font_size=34,
            color=GREEN,
            weight="BOLD",
            line_spacing=0.9,
        ).move_to(DOWN * 2.4)

        self.narrar(
            "Se alguma parte brilhante do Sol ainda estiver visível, os olhos precisam de proteção.",
            Write(aviso),
        )

        self.limpar(
            titulo_9,
            sol_seguranca,
            olho,
            filtro,
            setas_seguras,
            aviso,
            estrelas,
        )

        # 10 — RESUMO
        resumo_titulo = Text(
            "AGORA JÁ SABES",
            font_size=50,
            color=WHITE,
            weight="BOLD",
        ).to_edge(UP, buff=0.5)

        resumo = VGroup(
            Text(
                "1. A Lua passa entre o Sol e a Terra.",
                font_size=31,
                color=WHITE,
            ),
            Text(
                "2. A umbra cria a faixa do eclipse total.",
                font_size=31,
                color=WHITE,
            ),
            Text(
                "3. A penumbra cria o eclipse parcial.",
                font_size=31,
                color=WHITE,
            ),
            Text(
                "4. A órbita inclinada impede eclipses mensais.",
                font_size=31,
                color=WHITE,
            ),
            Text(
                "5. A proteção ocular continua essencial.",
                font_size=31,
                color=WHITE,
            ),
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.35,
        ).move_to(DOWN * 0.3)

        self.narrar(
            "Um eclipse solar não é o desaparecimento do Sol.",
            Write(resumo_titulo),
        )

        self.narrar(
            "É o resultado de tamanhos, distâncias, órbitas e sombras que, durante alguns minutos, se combinam de forma quase perfeita.",
            FadeIn(resumo),
        )

        frase_final = Text(
            "UMA PEQUENA LUA.\n"
            "UMA SOMBRA ESTREITA.\n"
            "UM ESPETÁCULO GIGANTE.",
            font_size=42,
            color=YELLOW,
            weight="BOLD",
            line_spacing=0.9,
        )

        self.limpar(resumo_titulo, resumo)

        self.narrar(
            "Uma pequena Lua, uma sombra estreita e um dos maiores espetáculos que podemos observar no céu.",
            Write(frase_final),
        )

        assinatura = Text(
            "APRENDER MESMO",
            font_size=30,
            color=GREY_B,
            weight="BOLD",
        ).next_to(frase_final, DOWN, buff=0.65)

        self.play(FadeIn(assinatura), run_time=0.7)
        self.wait(2)

        self.play(
            FadeOut(VGroup(frase_final, assinatura)),
            run_time=0.8,
        )
