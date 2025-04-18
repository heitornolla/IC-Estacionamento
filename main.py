import argparse

from src.estacionamento import Estacionamento

# Simulação de um cliente chegando
def simular_estacionamento(args):
    estacionamento = Estacionamento(total_vagas=args.total_vagas)
    print("\nSituação inicial do estacionamento:")
    estacionamento.exibir_vagas()

    print("\nBem-vindo ao estacionamento!")
    preferencia = input("Precisa de vaga preferencial? (sim/nao): ").strip().lower()
    preferencial = None
    if preferencia == "sim":
        tipo = input("Informe o tipo (idoso, deficiente, autismo, gestante): ").strip().lower()
        preferencial = tipo if tipo in ["idoso", "deficiente", "autismo", "gestante"] else None
    
    coberta = input("Prefere vaga coberta? (sim/nao/indiferente): ").strip().lower()
    if coberta == "sim":
        coberta = True
    elif coberta == "nao":
        coberta = False
    else:
        coberta = None
    
    vaga = estacionamento.encontrar_vaga(preferencial, coberta)
    if vaga:
        print(f"Vaga encontrada! {vaga}")
    else:
        print("Desculpe, não há vagas disponíveis com essas características.")

if __name__ == '__main__': 
  parser = argparse.ArgumentParser(description="Defina a quantidade de vagas na inicialização")
  parser.add_argument("--total_vagas", type=int)
  args = parser.parse_args()

  simular_estacionamento(args)