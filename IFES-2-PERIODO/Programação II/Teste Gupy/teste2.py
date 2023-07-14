def main():
    print('''2) Usando a seguinte lista de temperatutas [23.6, 37.9, 25.1, 19.0, 29.8],
    escreva código que identifique e retorne.a) Menor temperaturab) Maior temperaturac) 
    Temperatura média''')

    T = [23.6, 37.9, 25.1, 19.0, 29.8]

    # FUNÇÔES PRONTAS

    # Menor temperatura
    menor = min(T)

    # Maior temperatura
    maior = max(T)

    # Temperatura média
    media = sum(T) / len(T)

    print(f'''
    Maior temperatura: {maior:.2f}°C
    Menor temperatura: {menor:.2f}°C
    Média: {media:.2f}°C''')

    # MANUAL
    # Menor temperatura
    menor_t = T[0]
    for temperatura in T:
        if temperatura < menor_t:
            menor_t = temperatura

    # Maior temperatura
    maior_t = T[0]
    for temperatura in T:
        if temperatura > maior_t:
            maior_t = temperatura

    # Temperatura média
    soma_t = 0
    for temperatura in T:
        soma_t += temperatura
    t_media = soma_t / len(T)

    
    print(f'''
    Maior temperatura: {maior_t:.2f}°C
    Menor temperatura: {menor_t:.2f}°C
    Média: {t_media:.2f}°C''')

    

if __name__ == '__main__':
    main()