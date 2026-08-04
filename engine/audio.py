from collections.abc import Iterable

from manim import Animation, FadeIn, FadeOut


class AudioMixin:
    """
    Ferramentas de narração sincronizada.

    Cada frase:
    - gera a voz;
    - mostra a legenda;
    - executa as animações durante o áudio;
    - remove a legenda no fim.
    """

    def narrar(
        self,
        texto: str,
        animacoes: Iterable[Animation] | None = None,
        tamanho_legenda: int = 30,
        pausa_final: float = 0.1,
    ) -> None:
        texto_limpo = texto.strip()

        if not texto_limpo:
            raise ValueError("O texto da narração não pode estar vazio.")

        legenda = self.criar_legenda(
            texto=texto_limpo,
            tamanho=tamanho_legenda,
        )

        self.play(
            FadeIn(legenda),
            run_time=0.2,
        )

        with self.voiceover(text=texto_limpo) as voz:
            if animacoes:
                self.play(
                    *animacoes,
                    run_time=voz.duration,
                )
            else:
                self.wait(voz.duration)

        self.play(
            FadeOut(legenda),
            run_time=0.2,
        )

        if pausa_final > 0:
            self.wait(pausa_final)