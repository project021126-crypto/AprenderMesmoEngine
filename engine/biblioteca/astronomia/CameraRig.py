from __future__ import annotations

from manim import AnimationGroup, Mobject

from engine.biblioteca.astronomia.Parallax import (
    animar_aproximacao_espacial,
)
from engine.biblioteca.astronomia.StarField import StarField


class CameraRig:
    """
    Controlador cinematográfico do AprenderMesmo Engine.

    Não representa uma câmara física.
    Coordena movimentos visuais entre:
    - alvo principal;
    - campo estelar;
    - elementos de fundo.

    Objetivo:
    criar sensação de dolly, aproximação,
    afastamento e revelação sem repetir código.
    """

    def __init__(
        self,
        *,
        starfield: StarField | None = None,
    ) -> None:
        self.starfield = starfield

    def dolly_in(
        self,
        alvo: Mobject,
        *,
        escala: float = 1.35,
        deslocamento=(0.0, 0.0, 0.0),
        duracao: float = 3.0,
        intensidade_parallax: float = 1.0,
    ) -> AnimationGroup:
        """
        Aproximação cinematográfica ao alvo.
        """

        if escala <= 0:
            raise ValueError(
                "escala tem de ser positiva."
            )

        if duracao <= 0:
            raise ValueError(
                "duracao tem de ser positiva."
            )

        animacoes = [
            alvo.animate
            .scale(escala)
            .shift(deslocamento)
        ]

        if self.starfield is not None:
            animacoes.append(
                animar_aproximacao_espacial(
                    self.starfield,
                    intensidade=intensidade_parallax,
                    duracao=duracao,
                )
            )

        return AnimationGroup(
            *animacoes,
            lag_ratio=0.0,
            run_time=duracao,
        )

    def dolly_out(
        self,
        alvo: Mobject,
        *,
        escala: float = 0.75,
        deslocamento=(0.0, 0.0, 0.0),
        duracao: float = 3.0,
    ) -> AnimationGroup:
        """
        Afastamento cinematográfico do alvo.
        """

        if escala <= 0:
            raise ValueError(
                "escala tem de ser positiva."
            )

        if duracao <= 0:
            raise ValueError(
                "duracao tem de ser positiva."
            )

        return AnimationGroup(
            alvo.animate
            .scale(escala)
            .shift(deslocamento),
            lag_ratio=0.0,
            run_time=duracao,
        )

    def pan(
        self,
        alvo: Mobject,
        *,
        deslocamento=(0.6, 0.0, 0.0),
        duracao: float = 2.5,
    ) -> AnimationGroup:
        """
        Movimento lateral suave do enquadramento.
        """

        if duracao <= 0:
            raise ValueError(
                "duracao tem de ser positiva."
            )

        animacoes = [
            alvo.animate.shift(deslocamento)
        ]

        if self.starfield is not None:
            dx, dy, dz = deslocamento

            animacoes.append(
                self.starfield.distantes.animate.shift(
                    [
                        dx * 0.12,
                        dy * 0.12,
                        dz,
                    ]
                )
            )

            animacoes.append(
                self.starfield.medias.animate.shift(
                    [
                        dx * 0.32,
                        dy * 0.32,
                        dz,
                    ]
                )
            )

            animacoes.append(
                self.starfield.proximas.animate.shift(
                    [
                        dx * 0.60,
                        dy * 0.60,
                        dz,
                    ]
                )
            )

        return AnimationGroup(
            *animacoes,
            lag_ratio=0.0,
            run_time=duracao,
        )

    def reveal(
        self,
        alvo: Mobject,
        *,
        escala_inicial: float = 0.35,
        escala_final: float = 1.0,
        duracao: float = 3.0,
    ) -> AnimationGroup:
        """
        Revelação cinematográfica:
        o alvo começa pequeno e cresce suavemente.
        """

        if escala_inicial <= 0:
            raise ValueError(
                "escala_inicial tem de ser positiva."
            )

        if escala_final <= 0:
            raise ValueError(
                "escala_final tem de ser positiva."
            )

        if duracao <= 0:
            raise ValueError(
                "duracao tem de ser positiva."
            )

        alvo.scale(escala_inicial)

        fator = escala_final / escala_inicial

        animacoes = [
            alvo.animate.scale(fator)
        ]

        if self.starfield is not None:
            animacoes.append(
                animar_aproximacao_espacial(
                    self.starfield,
                    intensidade=0.8,
                    duracao=duracao,
                )
            )

        return AnimationGroup(
            *animacoes,
            lag_ratio=0.0,
            run_time=duracao,
        )