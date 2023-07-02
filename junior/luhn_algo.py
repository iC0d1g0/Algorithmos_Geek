def verificar_luhn(numero_tarjeta):
    # Convertir el número de tarjeta en una lista de dígitos
    digitos = [int(digito) for digito in str(numero_tarjeta)]
    # Pasos del algoritmo de Luhn
    digitos_duplicados = []
    for i, digito in enumerate(digitos[::-1]):
        if i % 2 == 1:
            digito_duplicado = digito * 2
            if digito_duplicado > 9:
                digito_duplicado -= 9
            digitos_duplicados.append(digito_duplicado)
        else:
            digitos_duplicados.append(digito) 
    suma_total = sum(digitos_duplicados)

    # Verificar validez según el algoritmo de Luhn
    if suma_total % 10 == 0:
        return True
    else:
        return False

# Ejemplo de uso
numero_tarjeta = 4213519029933862  # Número de tarjeta válido (ejemplo)
valido = verificar_luhn(numero_tarjeta)
if valido:
    print("El número de tarjeta es válido según el algoritmo de Luhn.")
else:
    print("El número de tarjeta no es válido según el algoritmo de Luhn.")
