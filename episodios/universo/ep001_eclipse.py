from engine.scene import CenaAprenderMesmo


class Episodio001Eclipse(CenaAprenderMesmo):

    def construct(self):
        self.studio.selecionar_episodio("001 - Eclipse")

        print(self.studio.resumo())

        pass