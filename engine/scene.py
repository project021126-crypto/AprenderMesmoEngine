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
    WHITE,
    config,
)

from engine.audio import VOZ_PADRAO, gerar_audio
from engine.formatos import (
    ConfiguracaoFormato,
    FORMATO_LONG,
    FORMATO_SHORT,
)
from engine.sync import calcular_duracao_narracao


class CenaAprenderMesmo(Scene):
    """
    Cena base do Aprender Mesmo.

    A legenda do rodapé é criada diretamente aqui para não
    depender de versões antigas de engine/legendas.py.
    """

    formato: ConfiguracaoFormato = FORMATO_LONG

    pasta_narracoes = Path("narracoes")
    voz_padrao = VOZ_PADRAO
    velocidade_voz = "+0%"
    volume_voz = "+0%"

    def criar_legenda_rodape(self, texto: str) -> VGroup:
        """
        Legenda de rodapé forte:
        - branco puro;
        - fonte grande e em negrito;
        - 2 ou 3 linhas no Short;
        - fundo preto sólido;
        - posição acima dos controlos do vídeo.
        """

        vertical = config.frame_height > config.frame_width
        limite = 28 if vertical else 72

        linhas = textwrap.wrap(
            texto.strip(),
            width=limite,
            break_long_words=False,
            break_on_hyphens=False,
        )
        texto_formatado = "\n".join(linhas)

        largura_maxima = (
            config.frame_width - 0.50
            if vertical
            else config.frame_width - 1.10
        )

        legenda = Text(
            texto_formatado,
            font_size=42 if vertical else 34,
            color="#FFFFFF",
            weight="BOLD",
            line_spacing=0.88,
            fill_opacity=1.0,
            stroke_color=BLACK,
            stroke_width=1.0,
            stroke_opacity=1.0,
        )

        if legenda.width > largura_maxima:
            legenda.scale_to_fit_width(largura_maxima)

        fundo = RoundedRectangle(
            width=min(legenda.width + 0.62, largura_maxima + 0.10),
            height=legenda.height + 0.45,
            corner_radius=0.14,
            fill_color=BLACK,
            fill_opacity=1.0,
            stroke_color=WHITE,
            stroke_opacity=1.0,
            stroke_width=2.2,
        )

        legenda.move_to(fundo.get_center())
        grupo = VGroup(fundo, legenda)

        if vertical:
            grupo.move_to([0, -5.30, 0])
        else:
            grupo.move_to([0, -3.15, 0])

        grupo.set_z_index(1000)
        return grupo

    def narrar(
        self,
        texto: str,
        animacoes: Any | Sequence[Any] | None = None,
        *,
        mostrar_legenda: bool = True,
        pausa_final: float = 0.20,
        margem_animacao: float = 0.15,
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
            legenda = self.criar_legenda_rodape(texto)
            self.add(legenda)

        self.add_sound(str(caminho_audio))

        if animacoes is None:
            self.wait(tempos.audio)
        else:
            if isinstance(animacoes, (list, tuple)):
                lista_animacoes = list(animacoes)
            else:
                lista_animacoes = [animacoes]

            if lista_animacoes:
                self.play(
                    *lista_animacoes,
                    run_time=tempos.animacao,
                )

                restante = tempos.audio - tempos.animacao

                if restante > 0:
                    self.wait(restante)
            else:
                self.wait(tempos.audio)

        if legenda is not None:
            self.play(FadeOut(legenda), run_time=0.15)

        if tempos.pausa_final > 0:
            self.wait(tempos.pausa_final)

    def mostrar_sem_narracao(
        self,
        objeto: Any,
        duracao: float = 0.6,
    ) -> None:
        self.play(FadeIn(objeto), run_time=duracao)


class CenaShort(CenaAprenderMesmo):
    """Base automática para vídeos verticais 9:16."""

    formato = FORMATO_SHORT


class CenaLong(CenaAprenderMesmo):
    """Base automática para vídeos horizontais 16:9."""

    formato = FORMATO_LONG
