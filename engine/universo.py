from manim import *


class Sol(Circle):
    def __init__(self, raio=0.8):
        super().__init__(
            radius=raio,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        )


class Terra(Circle):
    def __init__(self, raio=0.35):
        super().__init__(
            radius=raio,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1,
        )


class Lua(Circle):
    def __init__(self, raio=0.12):
        super().__init__(
            radius=raio,
            color=LIGHT_GRAY,
            fill_color=LIGHT_GRAY,
            fill_opacity=1,
        )


class Estrela(Dot):
    def __init__(self):
        super().__init__(
            radius=0.02,
            color=WHITE,
        )