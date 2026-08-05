from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from manim import (
    Animation,
    FadeIn,
    FadeOut,
    Scene,
)

from engine.audio import VOZ_PADRAO, gerar_audio
from engine.legendas import criar_legenda
from engine.sync import calcular_duracao_narracao


class CenaAprenderMesmo(Scene):
    """
    Cena base do Aprender Mesmo.

    Permite criar narração, legenda e animação sincronizadas
    através do método `self.narrar(...)`.
    """

    pasta_narracoes = Path("narracoes")
    voz_padrao = VOZ_PADRAO
    velocidade_voz = "+0%"
    volume_voz = "+0%"

    def narrar(
        self,
        texto: str,
        animacoes: Animation | Sequence[Animation] | None = None,
        *,
        mostrar_legenda: bool = True,
        pausa_final: float = 0.20,
        margem_animacao: float = 0.15,
    ) -> None:
        """
        Gera a narração e sincroniza automaticamente:

        - ficheiro MP3;
        - duração da animação;
        - legenda;
        - pequena pausa final.

        Exemplos:

        self.narrar(
            "A Lua passa entre o Sol e a Terra.",
            FadeIn(lua),
        )

        self.narrar(
            "Os três astros ficam alinhados.",
            [
                lua.animate.move_to(...),
                FadeIn(sombra),
            ],
        )
        """

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
            legenda = criar_legenda(texto)
            self.add(legenda)

        self.add_sound(str(caminho_audio))

        if animacoes is None:
            self.wait(tempos.audio)

        else:
            if isinstance(animacoes, Animation):
                lista_animacoes = [animacoes]
            else:
                lista_animacoes = list(animacoes)

            if not lista_animacoes:
                self.wait(tempos.audio)
            else:
                self.play(
                    *lista_animacoes,
                    run_time=tempos.animacao,
                )

                tempo_restante = (
                    tempos.audio - tempos.animacao
                )

                if tempo_restante > 0:
                    self.wait(tempo_restante)

        if legenda is not None:
            self.play(
                FadeOut(legenda),
                run_time=0.15,
            )

        if tempos.pausa_final > 0:
            self.wait(tempos.pausa_final)

    def mostrar_sem_narracao(
        self,
        objeto,
        duracao: float = 0.6,
    ) -> None:
        """
        Mostra rapidamente um objeto sem narração.
        """

        self.play(
            FadeIn(objeto),
            run_time=duracao,
        )