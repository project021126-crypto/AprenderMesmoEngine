from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


RAIZ_PROJETO = Path(__file__).resolve().parent.parent
PASTA_EPISODIOS = RAIZ_PROJETO / "episodios"
PASTA_RENDERS = RAIZ_PROJETO / "renders"


def localizar_episodio(categoria: str, episodio: str) -> Path:
    ficheiro = PASTA_EPISODIOS / categoria / f"{episodio}.py"

    if not ficheiro.exists():
        raise FileNotFoundError(
            f"Não encontrei o episódio:\n{ficheiro}"
        )

    return ficheiro


def renderizar(
    categoria: str,
    episodio: str,
    nome_cena: str,
    qualidade: str = "l",
) -> None:
    ficheiro = localizar_episodio(categoria, episodio)

    qualidades = {
        "l": "-ql",
        "m": "-qm",
        "h": "-qh",
        "k": "-qk",
    }

    opcao_qualidade = qualidades.get(qualidade)

    if opcao_qualidade is None:
        raise ValueError(
            "Qualidade inválida. Usa: l, m, h ou k."
        )

    PASTA_RENDERS.mkdir(parents=True, exist_ok=True)

    comando = [
        sys.executable,
        "-m",
        "manim",
        opcao_qualidade,
        "--disable_caching",
        "--media_dir",
        str(PASTA_RENDERS),
        str(ficheiro),
        nome_cena,
    ]

    print()
    print("🎬 Aprender Mesmo Studio")
    print(f"Categoria: {categoria}")
    print(f"Episódio: {episodio}")
    print(f"Cena: {nome_cena}")
    print(f"Qualidade: {qualidade}")
    print()

    resultado = subprocess.run(
        comando,
        cwd=RAIZ_PROJETO,
    )

    if resultado.returncode != 0:
        raise RuntimeError(
            "A renderização terminou com erro."
        )

    print()
    print("✅ Renderização concluída.")
    print(f"📁 Renders: {PASTA_RENDERS}")


def criar_argumentos() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Renderizador do Aprender Mesmo Studio."
    )

    parser.add_argument(
        "categoria",
        help="Exemplo: universo, matematica ou fisica",
    )

    parser.add_argument(
        "episodio",
        help="Exemplo: ep001_eclipse",
    )

    parser.add_argument(
        "cena",
        help="Exemplo: Episodio001Eclipse",
    )

    parser.add_argument(
        "-q",
        "--qualidade",
        default="l",
        choices=["l", "m", "h", "k"],
        help="l=baixa, m=média, h=alta, k=4K",
    )

    return parser


def main() -> None:
    parser = criar_argumentos()
    argumentos = parser.parse_args()

    renderizar(
        categoria=argumentos.categoria,
        episodio=argumentos.episodio,
        nome_cena=argumentos.cena,
        qualidade=argumentos.qualidade,
    )


if __name__ == "__main__":
    main()