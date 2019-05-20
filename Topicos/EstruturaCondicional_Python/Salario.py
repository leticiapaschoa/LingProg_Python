nome = input('Nome: ')
dindin = float(input('Salário: '))
print('Salário: {:.2f}'.format(dindin))
if dindin <= 280:
    print('O valor do aumento é: {:.2f}'.format(dindin * 0.2))
    dindin = 0.2 * dindin + dindin

    print('Salário reajustado: {:.2f}'.format(dindin))
    print('O reajuste é de 20%')


elif dindin <= 700:
    print('O valor do aumento é: {:.2f}'.format(dindin * 0.15))
    dindin = 0.15 * dindin + dindin
    print('Salário reajustado: {:.2f}'.format(dindin))
    print('O reajuste é de 15%')


elif dindin <= 1500:
    print('O valor do aumento é: {:.2f}'.format(dindin * 0.10))
    dindin = 0.10 * dindin + dindin
    print('Salário reajustado: {:.2f}'.format(dindin))
    print('O reajuste é de 10%')


else:
    print('O valor do aumento é: {:.2f}'.format(dindin * 0.05))
    dindin = 0.05 * dindin + dindin
    print('Salário reajustado: {:.2f}'.format(dindin))
    print('O reajuste é de 5%')
