from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parent.parent


def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Renderizador do Aprender Mesmo Studio."
    )

    parser.add_argument(
        "categoria",
        help="Categoria do episódio, por exemplo: universo",
    )

    parser.add_argument(
        "episodio",
        help="Nome do ficheiro sem .py, por exemplo: ep001_eclipse",
    )

    parser.add_argument(
        "cena",
        help="Nome da classe Manim, por exemplo: Episodio001Eclipse",
    )

    parser.add_argument(
        "-q",
        "--qualidade",
        choices=["l", "m", "h", "k"],
        default="l",
        help="Qualidade: l, m, h ou k",
    )

    return parser


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

    pasta_renders = PASTA_PROJETO / "renders"

    ambiente = os.environ.copy()

    pythonpath_atual = ambiente.get("PYTHONPATH", "")

    caminhos_python = [str(PASTA_PROJETO)]

    if pythonpath_atual:
        caminhos_python.append(pythonpath_atual)

    ambiente["PYTHONPATH"] = os.pathsep.join(caminhos_python)

    comando = [
        sys.executable,
        "-m",
        "manim",
        f"-q{qualidade}",
        "--disable_caching",
        "--media_dir",
        str(pasta_renders),
        str(ficheiro_episodio),
        cena,
    ]

    print()
    print("🎬 Aprender Mesmo Studio")
    print(f"Categoria: {categoria}")
    print(f"Episódio: {episodio}")
    print(f"Cena: {cena}")
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