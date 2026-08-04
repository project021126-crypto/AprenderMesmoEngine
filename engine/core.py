from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class FormatoVideo(str, Enum):
    SHORT = "short"
    LONG = "long"


@dataclass(frozen=True)
class StudioConfig:
    nome: str = "Aprender Mesmo Studio"
    idioma: str = "pt-PT"
    formato: FormatoVideo = FormatoVideo.LONG
    fps: int = 30
    cor_fundo: str = "#030712"

    @property
    def largura(self) -> int:
        if self.formato == FormatoVideo.SHORT:
            return 1080

        return 1920

    @property
    def altura(self) -> int:
        if self.formato == FormatoVideo.SHORT:
            return 1920

        return 1080

    @property
    def proporcao(self) -> str:
        if self.formato == FormatoVideo.SHORT:
            return "9:16"

        return "16:9"


class Studio:
    """
    Núcleo central do Aprender Mesmo Studio.

    Responsável por:
    - configuração do formato do vídeo;
    - caminhos do projeto;
    - identificação do episódio;
    - preparação das pastas.
    """

    def __init__(
        self,
        raiz_projeto: Path | None = None,
        config: StudioConfig | None = None,
    ) -> None:
        self.raiz_projeto = (
            raiz_projeto
            if raiz_projeto is not None
            else Path(__file__).resolve().parent.parent
        )

        self.config = config or StudioConfig()

        self.pasta_engine = self.raiz_projeto / "engine"
        self.pasta_episodios = self.raiz_projeto / "episodios"
        self.pasta_assets = self.raiz_projeto / "assets"
        self.pasta_renders = self.raiz_projeto / "renders"
        self.pasta_narracoes = self.raiz_projeto / "narracoes"

        self.episodio_atual: str | None = None

    def preparar_pastas(self) -> None:
        pastas = [
            self.pasta_engine,
            self.pasta_episodios,
            self.pasta_assets,
            self.pasta_renders,
            self.pasta_narracoes,
        ]

        for pasta in pastas:
            pasta.mkdir(parents=True, exist_ok=True)

    def selecionar_episodio(self, nome: str) -> None:
        nome_limpo = nome.strip()

        if not nome_limpo:
            raise ValueError("O nome do episódio não pode estar vazio.")

        self.episodio_atual = nome_limpo

    def resumo(self) -> str:
        episodio = self.episodio_atual or "nenhum"

        return (
            f"{self.config.nome}\n"
            f"Idioma: {self.config.idioma}\n"
            f"Formato: {self.config.formato.value}\n"
            f"Proporção: {self.config.proporcao}\n"
            f"Resolução: {self.config.largura}×{self.config.altura}\n"
            f"FPS: {self.config.fps}\n"
            f"Episódio atual: {episodio}\n"
            f"Projeto: {self.raiz_projeto}"
        )