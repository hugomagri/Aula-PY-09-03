from sys import flags

#ex1
# veloCarro = int(input("Velocidade carro = "))
#
# if veloCarro>80:
#     valorMulta = (veloCarro-80)*5
#     print(f"Voce foi multado no valor de: R${valorMulta}")
# else:
#     print("Vc n foi multado")

    #ex2
#
# v1 = float(input("Número 1 = "))
# v2 = float(input("Número 2 = "))
# v3 = float(input("Número 3 = "))
#
# maior = v1
#
# if v2>=v1 and v2>=v3:
#     maior =v2
#
# if v3>=v1 and v3>=v2:
#     maior=v3
#
#
# menor = v1
#
# if v2<=v1 and v2<=v3:
#     menor =v2
#
# if v3<=v1 and v3<=v2:
#     menor=v3
#
# print(f"maior é {maior}")
# print(f"menor é {menor}")

#ex3
distancia = float(input("Qunato vc quer andar? "))
if distancia<=200:
        valorCorrida = distancia*0.50

else:
    valorCorrida = distancia*0.45

print(valorCorrida)

#ex4

sal = float(input("salario = R$"))

if sal> 1250:
    aumento = sal * 0.1
else:
    aumento = sal *0.15
print(f"o aumento foi de R${aumento:.2f}")









