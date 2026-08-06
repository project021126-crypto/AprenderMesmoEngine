from __future__ import annotations

from engine.scene import CenaLong

from episodios.universo.eclipse.long.cenas.cena_01_intro import (
    executar_cena_01,
)


VERSAO = "EP001_ECLIPSE_LONG_MODULAR_V1"


class Episodio001EclipseLong(CenaLong):
    """
    Episódio Long modular sobre eclipses solares.

    Este ficheiro apenas organiza e executa as cenas.
    Os desenhos e animações ficam nos respetivos módulos.
    """

    def construct(self) -> None:
        print(f"✅ A renderizar {VERSAO}")

        executar_cena_01(self)