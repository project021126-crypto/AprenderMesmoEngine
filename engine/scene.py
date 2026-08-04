from manim import config
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from engine.core import Studio, StudioConfig
from engine.texto import TextoMixin
from engine.audio import AudioMixin


class CenaAprenderMesmo(AudioMixin, TextoMixin, VoiceoverScene):
    """
    Cena base de todos os vídeos do Aprender Mesmo.

    Liga:
    - configuração do Studio;
    - formato Short ou Long;
    - Manim;
    - narração em português;
    - ferramentas de texto e legendas.
    """

    studio_config = StudioConfig()

    def setup(self) -> None:
        super().setup()

        self.studio = Studio(config=self.studio_config)
        self.studio.preparar_pastas()

        config.pixel_width = self.studio.config.largura
        config.pixel_height = self.studio.config.altura
        config.frame_rate = self.studio.config.fps
        config.background_color = self.studio.config.cor_fundo

        self.set_speech_service(
            GTTSService(
                lang="pt",
                tld="pt",
            )
        )