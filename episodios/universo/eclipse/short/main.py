from __future__ import annotations

from engine.scene import CenaLong

from episodios.universo.eclipse.long.cenas.cena_01_intro import (
    executar_cena_01,
)


class Episodio001EclipseLong(CenaLong):
    def construct(self) -> None:
        executar_cena_01(self)