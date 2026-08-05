from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import Any

from manim import FadeIn, FadeOut, Scene

from engine.audio import VOZ_PADRAO, gerar_audio
from engine.formatos import (
    ConfiguracaoFormato,
    FORMATO_LONG,
    FORMATO_SHORT,
)
from engine.legendas import criar_legenda
from engine.sync import calcular_duracao_narracao


class CenaAprenderMesmo(Scene):
    """
    Cena base do Aprender Mesmo.

    O formato da imagem é aplicado pelo renderizador antes
    de o Manim criar a câmara. Esta classe trata da narração,
    legendas, animações e pausas.
    """

    formato: ConfiguracaoFormato = FORMATO_LONG

    pasta_narracoes = Path("narracoes")
    voz_padrao = VOZ_PADRAO
    velocidade_voz = "+0%"
    volume_voz = "+0%"

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
            legenda = criar_legenda(
                texto=texto,
                tamanho_fonte=self.formato.tamanho_legenda,
                margem_inferior=self.formato.margem_legenda,
            )
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

                tempo_restante = tempos.audio - tempos.animacao

                if tempo_restante > 0:
                    self.wait(tempo_restante)
            else:
                self.wait(tempos.audio)

        if legenda is not None:
            self.play(
                FadeOut(legenda),
                run_time=0.15,
            )

        if tempos.pausa_final > 0:
            self.wait(tempos.pausa_final)

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
    """Base para vídeos verticais 9:16."""

    formato = FORMATO_SHORT


class CenaLong(CenaAprenderMesmo):
    """Base para vídeos horizontais 16:9."""

    formato = FORMATO_LONG
