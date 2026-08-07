from __future__ import annotations

import textwrap
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from manim import (
    BLACK,
    FadeIn,
    FadeOut,
    RoundedRectangle,
    Scene,
    Text,
    VGroup,
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
    Cena base do Aprender Mesmo.
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
        Legenda cinematográfica discreta.

        No Long fica acima da margem inferior,
        sem tocar nos controlos do player.
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
            else config.frame_width - 1.80
        )

        legenda = Text(
            texto_formatado,
            font_size=40 if vertical else 29,
            color="#FFFFFF",
            weight="BOLD",
            line_spacing=0.90,
            fill_opacity=1.0,
            stroke_color=BLACK,
            stroke_width=0.7,
            stroke_opacity=0.85,
        )

        if (
            legenda.width
            > largura_maxima
        ):
            legenda.scale_to_fit_width(
                largura_maxima
            )

        fundo = RoundedRectangle(
            width=min(
                legenda.width + 0.58,
                largura_maxima + 0.08,
            ),
            height=legenda.height + 0.34,
            corner_radius=0.12,
            fill_color=BLACK,
            fill_opacity=0.76,
            stroke_color="#FFFFFF",
            stroke_opacity=0.16,
            stroke_width=0.8,
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
                [0, -4.95, 0]
            )

        else:
            # Antes estava -3.15.
            # Agora fica dentro da área visual segura.
            grupo.move_to(
                [0, -2.55, 0]
            )

        grupo.set_z_index(1000)

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

            self.add(legenda)

        self.add_sound(
            str(caminho_audio)
        )

        if animacoes is None:

            self.wait(
                tempos.audio
            )

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

                self.play(
                    *lista_animacoes,
                    run_time=tempos.animacao,
                )

                restante = (
                    tempos.audio
                    - tempos.animacao
                )

                if restante > 0:
                    self.wait(restante)

            else:
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