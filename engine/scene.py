from __future__ import annotations

import textwrap
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from manim import (
    BLACK,
    AnimationGroup,
    FadeIn,
    FadeOut,
    RoundedRectangle,
    Scene,
    Succession,
    Text,
    VGroup,
    Wait,
    config,
)

from engine.audio import (
    VOZ_PADRAO,
    gerar_audio,
)

from engine.formatos import (
    ConfiguracaoFormato,
    FORMATO_LONG,
    FORMATO_SHORT,
)

from engine.sync import (
    calcular_duracao_narracao,
)


class CenaAprenderMesmo(Scene):
    """
    Cena base do Aprender Mesmo Engine.
    """

    formato: ConfiguracaoFormato = FORMATO_LONG

    pasta_narracoes = Path("narracoes")

    voz_padrao = VOZ_PADRAO

    velocidade_voz = "+0%"

    volume_voz = "+0%"

    def criar_legenda_rodape(
        self,
        texto: str,
    ) -> VGroup:
        """
        Cria legenda cinematográfica dentro da área segura.
        """

        vertical = (
            config.frame_height
            > config.frame_width
        )

        limite = (
            28
            if vertical
            else 64
        )

        linhas = textwrap.wrap(
            texto.strip(),
            width=limite,
            break_long_words=False,
            break_on_hyphens=False,
        )

        texto_formatado = "\n".join(
            linhas
        )

        largura_maxima = (
            config.frame_width - 0.70
            if vertical
            else config.frame_width - 1.70
        )

        legenda = Text(
            texto_formatado,
            font_size=40 if vertical else 27,
            color="#FFFFFF",
            weight="BOLD",
            line_spacing=0.90,
            fill_opacity=1.0,
            stroke_color=BLACK,
            stroke_width=0.65,
            stroke_opacity=0.90,
        )

        if legenda.width > largura_maxima:
            legenda.scale_to_fit_width(
                largura_maxima
            )

        fundo = RoundedRectangle(
            width=min(
                legenda.width + 0.62,
                largura_maxima + 0.08,
            ),
            height=legenda.height + 0.34,
            corner_radius=0.12,
            fill_color=BLACK,
            fill_opacity=0.72,
            stroke_color="#FFFFFF",
            stroke_opacity=0.13,
            stroke_width=0.7,
        )

        legenda.move_to(
            fundo.get_center()
        )

        grupo = VGroup(
            fundo,
            legenda,
        )

        if vertical:
            grupo.move_to(
                [0, -4.80, 0]
            )

        else:
            # Área segura do Long.
            grupo.move_to(
                [0, -2.48, 0]
            )

        grupo.set_z_index(
            1000,
            family=True,
        )

        return grupo

    def narrar(
        self,
        texto: str,
        animacoes: Any
        | Sequence[Any]
        | None = None,
        *,
        mostrar_legenda: bool = True,
        pausa_final: float = 0.12,
        margem_animacao: float = 0.12,
    ) -> None:

        texto = texto.strip()

        if not texto:
            raise ValueError(
                "O texto da narração não pode estar vazio."
            )

        caminho_audio = gerar_audio(
            texto=texto,
            voz=self.voz_padrao,
            pasta=self.pasta_narracoes,
            velocidade=self.velocidade_voz,
            volume=self.volume_voz,
        )

        tempos = calcular_duracao_narracao(
            caminho_audio=caminho_audio,
            margem_animacao=margem_animacao,
            pausa_final=pausa_final,
        )

        legenda = None

        if mostrar_legenda:
            legenda = (
                self.criar_legenda_rodape(
                    texto
                )
            )

        # O áudio começa imediatamente.
        self.add_sound(
            str(caminho_audio)
        )

        # ==================================================
        # SEM ANIMAÇÃO PRINCIPAL
        # ==================================================

        if animacoes is None:

            if legenda is not None:

                atraso_legenda = min(
                    0.12,
                    tempos.audio * 0.10,
                )

                duracao_entrada = min(
                    0.16,
                    tempos.audio * 0.12,
                )

                self.wait(
                    atraso_legenda
                )

                self.play(
                    FadeIn(legenda),
                    run_time=duracao_entrada,
                )

                restante = (
                    tempos.audio
                    - atraso_legenda
                    - duracao_entrada
                )

                if restante > 0:
                    self.wait(restante)

            else:
                self.wait(
                    tempos.audio
                )

        # ==================================================
        # COM ANIMAÇÃO PRINCIPAL
        # ==================================================

        else:

            if isinstance(
                animacoes,
                (list, tuple),
            ):
                lista_animacoes = list(
                    animacoes
                )

            else:
                lista_animacoes = [
                    animacoes
                ]

            if lista_animacoes:

                # Todas as animações principais são
                # coordenadas para durar o tempo calculado.
                animacao_principal = AnimationGroup(
                    *lista_animacoes,
                    lag_ratio=0.0,
                    run_time=tempos.animacao,
                )

                if legenda is not None:

                    # A imagem começa primeiro.
                    # A legenda entra ~120 ms depois.
                    entrada_legenda = Succession(
                        Wait(0.12),
                        FadeIn(
                            legenda,
                            run_time=0.16,
                        ),
                    )

                    self.play(
                        animacao_principal,
                        entrada_legenda,
                    )

                else:
                    self.play(
                        animacao_principal
                    )

                restante = (
                    tempos.audio
                    - tempos.animacao
                )

                if restante > 0:
                    self.wait(
                        restante
                    )

            else:

                if legenda is not None:
                    self.play(
                        Succession(
                            Wait(0.12),
                            FadeIn(
                                legenda,
                                run_time=0.16,
                            ),
                        )
                    )

                self.wait(
                    tempos.audio
                )

        if legenda is not None:

            self.play(
                FadeOut(legenda),
                run_time=0.12,
            )

        if tempos.pausa_final > 0:

            self.wait(
                tempos.pausa_final
            )

    def mostrar_sem_narracao(
        self,
        objeto: Any,
        duracao: float = 0.6,
    ) -> None:

        self.play(
            FadeIn(objeto),
            run_time=duracao,
        )


class CenaShort(CenaAprenderMesmo):
    """Vídeos verticais 9:16."""

    formato = FORMATO_SHORT


class CenaLong(CenaAprenderMesmo):
    """Vídeos horizontais 16:9."""

    formato = FORMATO_LONG