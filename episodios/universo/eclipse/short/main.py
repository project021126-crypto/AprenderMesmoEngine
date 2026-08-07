from __future__ import annotations

from engine.scene import CenaLong

from episodios.universo.eclipse.long.cenas.cena_01_intro import (
    executar_cena_01,
)

from episodios.universo.eclipse.long.cenas.cena_02_segredo_400 import (
    executar_cena_02,
)


VERSAO = "EP001_ECLIPSE_LONG_MODULAR_V2"


class Episodio001EclipseLong(CenaLong):
    """
    Episódio Long modular sobre eclipses solares.
    """

    def construct(self) -> None:

        print(
            f"✅ A renderizar {VERSAO}"
        )

        executar_cena_01(self)

        executar_cena_02(self)