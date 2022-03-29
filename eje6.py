sexo = "m"
edad = 59
cotizaciones = 800
aniosServ = 26

if aniosServ >= 25 and cotizaciones >= 750:
    if (sexo == "m" and edad >= 60) or (sexo == "f" and edad >= 60):
        print("Usteded aplica para ser jubilado")
    else:
        print("Usteded no aplica para ser jubilado")
else:
    print("Usteded no aplica para ser jubilado")
