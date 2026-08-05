from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from engine.audio import obter_duracao_audio


@dataclass(frozen=True)
class DuracaoNarracao:
    """
    Guarda a duração real do áudio e os tempos usados
    para sincronizar animações e legendas.
    """

    audio: float
    animacao: float
    legenda: float
    pausa_final: float


def calcular_duracao_narracao(
    caminho_audio: str | Path,
    margem_animacao: float = 0.15,
    pausa_final: float = 0.20,
    duracao_minima: float = 0.8,
) -> DuracaoNarracao:
    """
    Calcula os tempos de sincronização a partir da duração
    real do ficheiro de áudio.

    - `audio`: duração exata do MP3;
    - `animacao`: tempo disponível para a animação;
    - `legenda`: tempo total em que a legenda fica visível;
    - `pausa_final`: pequena pausa depois da frase.
    """

    if margem_animacao < 0:
        raise ValueError(
            "A margem da animação não pode ser negativa."
        )

    if pausa_final < 0:
        raise ValueError(
            "A pausa final não pode ser negativa."
        )

    if duracao_minima <= 0:
        raise ValueError(
            "A duração mínima deve ser superior a zero."
        )

    duracao_audio = obter_duracao_audio(caminho_audio)

    duracao_legenda = max(
        duracao_audio,
        duracao_minima,
    )

    duracao_animacao = max(
        duracao_audio - margem_animacao,
        duracao_minima,
    )

    return DuracaoNarracao(
        audio=duracao_audio,
        animacao=duracao_animacao,
        legenda=duracao_legenda,
        pausa_final=pausa_final,
    )