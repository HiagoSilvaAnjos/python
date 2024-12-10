def arrendondar_baixo (value):
    number = value
    decimal_value = value - int(value)

    if decimal_value <= 0.5: number = int(value) 
    
    return number
print(arrendondar_baixo(9.5))

def arrendondar_cima (value):
    number = value
    decimal_value = value - int(value)

    if decimal_value >= 0: number = int(value) + 1
    
    return number
print(arrendondar_cima(9.5))

def arrendondar_convencional (value):
    number = value
    decimal_value = value - int(value)

    if decimal_value >= 0.5:
        number = int(value) + 1
    else:
        number = int(value)
    
    return number
print(arrendondar_convencional(9.5))