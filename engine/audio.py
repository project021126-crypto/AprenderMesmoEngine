from __future__ import annotations

import asyncio
import hashlib
from pathlib import Path

import edge_tts
from mutagen.mp3 import MP3


VOZ_PADRAO = "pt-PT-RaquelNeural"
PASTA_NARRACOES = Path("narracoes")


def criar_nome_audio(texto: str, voz: str = VOZ_PADRAO) -> str:
    """
    Cria um nome único e previsível para cada narração.

    Se o mesmo texto e a mesma voz forem usados novamente,
    o motor reutiliza o áudio já existente.
    """

    identificador = hashlib.sha256(
        f"{voz}|{texto}".encode("utf-8")
    ).hexdigest()[:16]

    return f"narracao_{identificador}.mp3"


async def _gerar_audio_async(
    texto: str,
    caminho: Path,
    voz: str,
    velocidade: str,
    volume: str,
) -> None:
    """
    Gera o ficheiro MP3 através do Microsoft Edge TTS.
    """

    comunicador = edge_tts.Communicate(
        text=texto,
        voice=voz,
        rate=velocidade,
        volume=volume,
    )

    await comunicador.save(str(caminho))


def gerar_audio(
    texto: str,
    voz: str = VOZ_PADRAO,
    pasta: str | Path = PASTA_NARRACOES,
    velocidade: str = "+0%",
    volume: str = "+0%",
    forcar: bool = False,
) -> Path:
    """
    Gera uma narração em português europeu.

    Se o áudio já existir, será reutilizado, exceto quando
    `forcar=True`.

    Retorna o caminho completo do ficheiro MP3.
    """

    texto = texto.strip()

    if not texto:
        raise ValueError("O texto da narração não pode estar vazio.")

    pasta_destino = Path(pasta)
    pasta_destino.mkdir(parents=True, exist_ok=True)

    nome_ficheiro = criar_nome_audio(texto, voz)
    caminho_audio = pasta_destino / nome_ficheiro

    if caminho_audio.exists() and not forcar:
        return caminho_audio

    try:
        asyncio.run(
            _gerar_audio_async(
                texto=texto,
                caminho=caminho_audio,
                voz=voz,
                velocidade=velocidade,
                volume=volume,
            )
        )
    except RuntimeError:
        loop = asyncio.new_event_loop()

        try:
            loop.run_until_complete(
                _gerar_audio_async(
                    texto=texto,
                    caminho=caminho_audio,
                    voz=voz,
                    velocidade=velocidade,
                    volume=volume,
                )
            )
        finally:
            loop.close()

    if not caminho_audio.exists():
        raise FileNotFoundError(
            f"O áudio não foi criado: {caminho_audio}"
        )

    return caminho_audio


def obter_duracao_audio(caminho_audio: str | Path) -> float:
    """
    Retorna a duração do ficheiro MP3 em segundos.
    """

    caminho = Path(caminho_audio)

    if not caminho.exists():
        raise FileNotFoundError(
            f"O ficheiro de áudio não existe: {caminho}"
        )

    audio = MP3(str(caminho))
    return float(audio.info.length)