from __future__ import annotations

from manim import (
    BLACK,
    DOWN,
    Scene,
    Text,
    VGroup,
    config,
)

from engine.biblioteca.astronomia.sol import criar_sol


config.pixel_width = 1280
config.pixel_height = 720
config.frame_width = 14.222
config.frame_height = 8.0
config.background_color = BLACK


class TesteSol(Scene):
    def construct(self) -> None:
        sol_draft = criar_sol(
            raio=0.75,
            posicao=[-4.4, 0.55, 0],
            qualidade="draft",
            mostrar_halo=True,
            mostrar_coroa=True,
        )

        sol_youtube = criar_sol(
            raio=0.75,
            posicao=[0, 0.55, 0],
            qualidade="youtube",
            mostrar_halo=True,
            mostrar_coroa=True,
        )

        sol_cinema = criar_sol(
            raio=0.75,
            posicao=[4.4, 0.55, 0],
            qualidade="cinema",
            mostrar_halo=True,
            mostrar_coroa=True,
            intensidade=1.15,
        )

        labels = VGroup(
            Text(
                "DRAFT",
                font_size=28,
                weight="BOLD",
            ).next_to(sol_draft, DOWN, buff=0.75),

            Text(
                "YOUTUBE",
                font_size=28,
                weight="BOLD",
            ).next_to(sol_youtube, DOWN, buff=0.75),

            Text(
                "CINEMA",
                font_size=28,
                weight="BOLD",
            ).next_to(sol_cinema, DOWN, buff=0.75),
        )

        titulo = Text(
            "TESTE DO SOL",
            font_size=42,
            weight="BOLD",
        ).to_edge([0, 1, 0], buff=0.35)

        self.add(
            titulo,
            sol_draft,
            sol_youtube,
            sol_cinema,
            labels,
        )

        self.wait(2)