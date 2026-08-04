from manim import (
    BLACK,
    WHITE,
    DOWN,
    UP,
    FadeIn,
    FadeOut,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
)


class TextoMixin:
    """
    Ferramentas reutilizáveis para títulos, perguntas,
    destaques e legendas.
    """

    def criar_titulo(
        self,
        texto: str,
        tamanho: int = 48,
        cor=WHITE,
    ) -> Text:
        titulo = Text(
            texto,
            font="DejaVu Sans",
            font_size=tamanho,
            color=cor,
            weight="BOLD",
        )

        titulo.to_edge(UP, buff=0.45)
        return titulo

    def mostrar_titulo(
        self,
        texto: str,
        tamanho: int = 48,
        cor=WHITE,
        duracao: float = 1.0,
    ) -> Text:
        titulo = self.criar_titulo(
            texto=texto,
            tamanho=tamanho,
            cor=cor,
        )

        self.play(
            Write(titulo),
            run_time=duracao,
        )

        return titulo

    def criar_legenda(
        self,
        texto: str,
        tamanho: int = 30,
    ) -> VGroup:
        caixa = RoundedRectangle(
            width=12.8,
            height=1.0,
            corner_radius=0.18,
            fill_color=BLACK,
            fill_opacity=0.78,
            stroke_opacity=0,
        )

        legenda = Text(
            texto,
            font="DejaVu Sans",
            font_size=tamanho,
            color=WHITE,
        )

        legenda.scale_to_fit_width(11.8)
        legenda.move_to(caixa.get_center())

        grupo = VGroup(caixa, legenda)
        grupo.to_edge(DOWN, buff=0.22)
        grupo.set_z_index(100)

        return grupo

    def mostrar_legenda(
        self,
        texto: str,
        tamanho: int = 30,
        duracao_entrada: float = 0.2,
    ) -> VGroup:
        legenda = self.criar_legenda(
            texto=texto,
            tamanho=tamanho,
        )

        self.play(
            FadeIn(legenda),
            run_time=duracao_entrada,
        )

        return legenda

    def esconder_texto(
        self,
        objeto,
        duracao: float = 0.3,
    ) -> None:
        self.play(
            FadeOut(objeto),
            run_time=duracao,
        )