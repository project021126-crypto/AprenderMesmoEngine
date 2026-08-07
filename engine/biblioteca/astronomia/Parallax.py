from __future__ import annotations

from manim import AnimationGroup

from engine.biblioteca.astronomia.StarField import StarField


def animar_parallax(
    starfield: StarField,
    *,
    deslocamento=(0.55, -0.10, 0.0),
    zoom: float = 1.04,
    duracao: float = 3.0,
) -> AnimationGroup:
    """
    Cria movimento de parallax entre as três camadas do StarField.

    As estrelas próximas movem-se mais.
    As médias movem-se a uma velocidade intermédia.
    As distantes movem-se pouco.

    Isto cria sensação de profundidade e deslocação da câmara.
    """

    if duracao <= 0:
        raise ValueError(
            "duracao tem de ser positiva."
        )

    if zoom <= 0:
        raise ValueError(
            "zoom tem de ser positivo."
        )

    dx, dy, dz = deslocamento

    deslocamento_distantes = [
        dx * 0.20,
        dy * 0.20,
        dz,
    ]

    deslocamento_medias = [
        dx * 0.52,
        dy * 0.52,
        dz,
    ]

    deslocamento_proximas = [
        dx,
        dy,
        dz,
    ]

    return AnimationGroup(
        starfield.distantes.animate
        .shift(deslocamento_distantes)
        .scale(1 + (zoom - 1) * 0.30),

        starfield.medias.animate
        .shift(deslocamento_medias)
        .scale(1 + (zoom - 1) * 0.65),

        starfield.proximas.animate
        .shift(deslocamento_proximas)
        .scale(zoom),

        lag_ratio=0.0,
        run_time=duracao,
    )


def animar_aproximacao_espacial(
    starfield: StarField,
    *,
    intensidade: float = 1.0,
    duracao: float = 3.0,
) -> AnimationGroup:
    """
    Preset cinematográfico para simular uma aproximação lenta
    através do espaço.

    intensidade:
    - 0.5 = movimento subtil
    - 1.0 = movimento normal
    - 1.5+ = movimento mais dramático
    """

    if intensidade <= 0:
        raise ValueError(
            "intensidade tem de ser positiva."
        )

    deslocamento = (
        0.42 * intensidade,
        -0.08 * intensidade,
        0.0,
    )

    zoom = 1.0 + 0.035 * intensidade

    return animar_parallax(
        starfield,
        deslocamento=deslocamento,
        zoom=zoom,
        duracao=duracao,
    )


def animar_deriva_lateral(
    starfield: StarField,
    *,
    direcao: str = "direita",
    intensidade: float = 1.0,
    duracao: float = 3.0,
) -> AnimationGroup:
    """
    Movimento lateral cinematográfico.

    Útil para:
    - introduções;
    - transições;
    - planos espaciais;
    - movimentos suaves enquanto existe narração.
    """

    if intensidade <= 0:
        raise ValueError(
            "intensidade tem de ser positiva."
        )

    if direcao not in {
        "direita",
        "esquerda",
    }:
        raise ValueError(
            "direcao deve ser 'direita' ou 'esquerda'."
        )

    sinal = 1 if direcao == "direita" else -1

    deslocamento = (
        0.45 * intensidade * sinal,
        0.03 * intensidade,
        0.0,
    )

    return animar_parallax(
        starfield,
        deslocamento=deslocamento,
        zoom=1.015,
        duracao=duracao,
    )