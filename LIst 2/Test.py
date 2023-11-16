import psutil

def verificar_processos():
    processos = psutil.process_iter()

    for processo in processos:
        uso_cpu = processo.cpu_percent()

        if uso_cpu > 0.0:
            nome_do_processo = processo.name
            print(f"O processo {nome_do_processo} está usando {uso_cpu}% da CPU.")

    # Imprime as informações sobre o sistema de virtualização

    print("Informações sobre o sistema de virtualização:")
    print(psutil.virtual_memory())
    print(psutil.cpu_times())

if __name__ == "__main__":
    verificar_processos()