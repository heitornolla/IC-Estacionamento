import random
from lib.vaga import Vaga

class Estacionamento:
    def __init__(self, total_vagas=20):
        self.vagas = []
        tipos_preferenciais = ["idoso", "deficiente", "autismo", "gestante"]

        for i in range(1, total_vagas + 1):
            preferencial = random.choice([None] + tipos_preferenciais) if i % 4 == 0 else None
            coberta = random.choice([True, False])
            self.vagas.append(Vaga(i, preferencial, coberta))

    def encontrar_vaga(self, preferencial=None, coberta=None):
        for vaga in self.vagas:
            if not vaga.ocupada:
                if preferencial:
                    if vaga.preferencial == preferencial and (coberta is None or vaga.coberta == coberta):
                        vaga.ocupada = True
                        return vaga
                elif vaga.preferencial is None and (coberta is None or vaga.coberta == coberta):
                    vaga.ocupada = True
                    return vaga
        return None

    def exibir_vagas(self):
        for vaga in self.vagas:
            print(vaga)
