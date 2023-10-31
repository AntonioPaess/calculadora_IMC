

# É necessário saber o sexo para estimar o IMC corretamente
sexo = int(input("""[1] Masculino
[2] Feminino \n: """))

# Calculo do IMC 
peso = float(input("Qual seu peso atualem KG? "))
altura = float(input("Qual sua altura atual em metros? "))


# Fórmula do IMC
IMC = (peso / (altura ** 2))

# Formatando o IMC:
IMC_FORMAT = "{:.2f}".format(IMC)  # Para que o IMC tenha apenas duas casas decimais

# Resposta do seu IMC
print(f"Seu IMC é:",IMC_FORMAT , "\n")

# Caso você seja do sexo masculino, esse é a resposta do seu cálculo do IMC:
if sexo == 1:
    if IMC <= 18.5:
        print("""-------------------------
VOCÊ ESTÁ ABAIXO DO PESO.
-------------------------""", "\n")
    elif IMC >= 18.6 and IMC <= 24.9:
        print("""----------------------------
VOCÊ ESTÁ COM O PESO NORMAL.
----------------------------""", "\n")
    elif IMC >= 25 and IMC <= 29.9:
        print("""------------------------
VOCÊ ESTÁ COM SOBREPESO.
------------------------""", "\n")
    elif IMC >= 30 and IMC <= 34.9:
        print("""----------------------------------
VOCÊ ESTÁ COM OBESIDADE DE GRAU I.
----------------------------------""", "\n")
    elif IMC >= 35 and IMC <= 39.9:
        print("""-----------------------------------
VOCÊ ESTÁ COM OBESIDADE DE GRAU II.
-----------------------------------""", "\n")
    else:
        print("""------------------------------------
VOCÊ ESTÁ COM OBESIDADE DE GRAU III.
------------------------------------""", "\n")

# Caso você seja do sexo feminino, esse é a resposta do seu cálculo do IMC:
if sexo == 2:
    if IMC <= 19:
        print("""-------------------------
VOCÊ ESTÁ ABAIXO DO PESO.
-------------------------""", "\n")
    elif IMC >= 19 and IMC <= 23.9:
        print("""----------------------------
VOCÊ ESTÁ COM O PESO NORMAL.
----------------------------""", "\n")
    elif IMC >= 24 and IMC <= 28.9:
        print("""------------------------
VOCÊ ESTÁ COM SOBREPESO.
------------------------""", "\n")
    elif IMC >= 29 and IMC <= 33.9:
        print("""----------------------------------
VOCÊ ESTÁ COM OBESIDADE DE GRAU I.
----------------------------------""", "\n")
    elif IMC >= 34 and IMC <= 38.9:
        print("""-----------------------------------
VOCÊ ESTÁ COM OBESIDADE DE GRAU II.
-----------------------------------""", "\n")
    else:
        print("""------------------------------------
VOCÊ ESTÁ COM OBESIDADE DE GRAU III.
------------------------------------""", "\n")


print("""ATENÇÃO ESTE RESULTADO É APENAS BASEADO EM NÚMEROS, UMA CALCULADORA, NÃO É BASEADO EM TODO O CONTEXTO DA SUA VIDA, 
                        PARA MELHORES INFORMAÇÕES É NECESSÁRIO BUSCAR UM PROFISSIONAL NA ÁREA!""")