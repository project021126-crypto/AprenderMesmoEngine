from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parent.parent


FORMATOS = {
    "short": {
        "frame_width": 8.0,
        "frame_height": 14.222,
        "resolucoes": {
            "l": (540, 960, 15),
            "m": (720, 1280, 30),
            "h": (1080, 1920, 30),
            "k": (1080, 1920, 60),
        },
    },
    "long": {
        "frame_width": 14.222,
        "frame_height": 8.0,
        "resolucoes": {
            "l": (854, 480, 15),
            "m": (1280, 720, 30),
            "h": (1920, 1080, 30),
            "k": (3840, 2160, 60),
        },
    },
}


def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Renderizador do Aprender Mesmo Studio."
    )

    parser.add_argument("categoria")
    parser.add_argument("episodio")
    parser.add_argument("cena")

    parser.add_argument(
        "-q",
        "--qualidade",
        choices=["l", "m", "h", "k"],
        default="l",
    )

    return parser


def identificar_formato(episodio: str, cena: str) -> str:
    nome = f"{episodio} {cena}".lower()

    if "short" in nome:
        return "short"

    if "long" in nome:
        return "long"

    raise ValueError(
        "O formato não foi identificado. "
        "O ficheiro ou a classe deve terminar em Short ou Long."
    )


def criar_config_temporaria(
    formato: str,
    qualidade: str,
    pasta_renders: Path,
) -> Path:
    configuracao = FORMATOS[formato]
    pixel_width, pixel_height, frame_rate = (
        configuracao["resolucoes"][qualidade]
    )

    conteudo = f"""[CLI]
pixel_width = {pixel_width}
pixel_height = {pixel_height}
frame_width = {configuracao["frame_width"]}
frame_height = {configuracao["frame_height"]}
frame_rate = {frame_rate}
media_dir = {pasta_renders.as_posix()}
disable_caching = True
progress_bar = display
"""

    ficheiro = Path(tempfile.gettempdir()) / (
        f"aprender_mesmo_{formato}_{qualidade}.cfg"
    )
    ficheiro.write_text(conteudo, encoding="utf-8")
    return ficheiro


def renderizar(
    categoria: str,
    episodio: str,
    cena: str,
    qualidade: str,
) -> None:
    ficheiro_episodio = (
        PASTA_PROJETO
        / "episodios"
        / categoria
        / f"{episodio}.py"
    )

    if not ficheiro_episodio.exists():
        raise FileNotFoundError(
            f"Episódio não encontrado: {ficheiro_episodio}"
        )

    formato = identificar_formato(episodio, cena)
    pasta_renders = PASTA_PROJETO / "renders"

    ambiente = os.environ.copy()
    pythonpath_atual = ambiente.get("PYTHONPATH", "")
    caminhos_python = [str(PASTA_PROJETO)]

    if pythonpath_atual:
        caminhos_python.append(pythonpath_atual)

    ambiente["PYTHONPATH"] = os.pathsep.join(caminhos_python)

    config_temporaria = criar_config_temporaria(
        formato=formato,
        qualidade=qualidade,
        pasta_renders=pasta_renders,
    )

    comando = [
        sys.executable,
        "-m",
        "manim",
        "render",
        "--config_file",
        str(config_temporaria),
        str(ficheiro_episodio),
        cena,
    ]

    print()
    print("🎬 Aprender Mesmo Studio")
    print(f"Categoria: {categoria}")
    print(f"Episódio: {episodio}")
    print(f"Cena: {cena}")
    print(f"Formato: {formato}")
    print(f"Qualidade: {qualidade}")
    print()

    resultado = subprocess.run(
        comando,
        cwd=PASTA_PROJETO,
        env=ambiente,
    )

    if resultado.returncode != 0:
        raise RuntimeError(
            f"A renderização terminou com o código "
            f"{resultado.returncode}."
        )

    print()
    print("✅ Renderização concluída.")
    print(f"📁 Renders: {pasta_renders}")


def main() -> None:
    parser = criar_parser()
    argumentos = parser.parse_args()

    renderizar(
        categoria=argumentos.categoria,
        episodio=argumentos.episodio,
        cena=argumentos.cena,
        qualidade=argumentos.qualidade,
    )


if __name__ == "__main__":
    main()
