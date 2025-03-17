class Vaga:
    def __init__(self, numero, preferencial=None, coberta=False):
        self.numero = numero
        self.preferencial = preferencial  # Ex: "idoso", "deficiente", None para normal
        self.coberta = coberta
        self.ocupada = False

    def __str__(self):
        tipo = "Normal" if not self.preferencial else f"Preferencial ({self.preferencial})"
        cobertura = "Coberta" if self.coberta else "Descoberta"
        return f"Vaga {self.numero}: {tipo}, {cobertura}, {'Ocupada' if self.ocupada else 'Livre'}"
