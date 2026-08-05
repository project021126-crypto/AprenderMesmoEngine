from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TipoFormato(str, Enum):
    SHORT = "short"
    LONG = "long"


@dataclass(frozen=True)
class ConfiguracaoFormato:
    tipo: TipoFormato
    pixel_width: int
    pixel_height: int
    frame_width: float
    frame_height: float
    tamanho_legenda: int
    margem_legenda: float


FORMATO_SHORT = ConfiguracaoFormato(
    tipo=TipoFormato.SHORT,
    pixel_width=1080,
    pixel_height=1920,
    frame_width=8.0,
    frame_height=14.222,
    tamanho_legenda=34,
    margem_legenda=0.32,
)


FORMATO_LONG = ConfiguracaoFormato(
    tipo=TipoFormato.LONG,
    pixel_width=1920,
    pixel_height=1080,
    frame_width=14.222,
    frame_height=8.0,
    tamanho_legenda=34,
    margem_legenda=0.28,
)