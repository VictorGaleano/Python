# Programa de calculadora em Python
# Apenas para fixar mais o conceito
# Guararema - 07/06/2018 - VG - Versão 0.1

#import para limpar tela e pausar para mostrar o erro
import os


# difinição do menu
def menu():
	print("Welcome to PyCalculator")
	print("\nOpções: " +
		"\n1 - Adição" +
		"\n2 - Subtração" +
		"\n3 - Multiplicação" +
		"\n4 - Divisão" + 
		"\nOu Zero para cancelar")

	cOpcao = int(input("\nEscolha uma Operação: "+				# cOpcao - recebe a escolha do operador
		"(Entre 1 e 4): "))

	if cOpcao == 1:												# Se cOpcao igual a '1'
		Adicao()												# chama Adicao()
	elif cOpcao == 2:
		Subtracao()
	elif cOpcao == 3:
		Multiplicacao()
	elif cOpcao == 4:
		Divisao()
	elif cOpcao == 0:											# Se cOpcao igual a '0' cancela o programa
		pass													# fecha o programa
	else:
		print("Opção inválida!!!")								# Opção invalida
		PAUSA()													# Pausa a tela para que possa ver o erro
		LIMPAR_TELA()											# Limpa a tela
		menu()													# chama o menu novamente

# método Adição
def Adicao():
	print("\nADIÇÃO")
	a = float(input("Digite um número: "))						# converte o texto para float e atribui a variavel 'a'
	b = float(input("Digite mais um número: "))					# converte o texto para float e atribui a variavel 'b'

	a = a + b													# atribui a variavel 'a', a soma entre 'a' e 'b'
	print("\nA Soma dos números é: ", a)						# exibe o resultado

	#verifica se o usuário sai da calucadora ou faz outra operação
	if a != " ":
		print("\nDeseja fazer outra operação? ")
		aux = input("(S - Sim u N - Não): ")
		if aux == "S" or aux == "s":
			LIMPAR_TELA()
			menu()
		else:
			LIMPAR_TELA()
			print("PyCalculator closed!!!")
			pass

# método Subtração
def Subtracao():
	print("\nSUBTRAÇÃO")
	a = float(input("Digite um número: "))						# converte o texto para float e atribui a variavel 'a'
	b = float(input("Digite mais um número: "))					# converte o texto para float e atribui a variavel 'b'
 
	a = a - b													# atribui a variavel 'a', a subtração entre 'a' e 'b'
	print("\nA Subtração dos números é: ", a)

	#verifica se o usuário sai da calucadora ou faz outra operação
	if a != " ":
		print("\nDeseja fazer outra operação? ")
		aux = input("(S - Sim u N - Não): ")
		if aux == "S" or aux == "s":
			LIMPAR_TELA()
			menu()
		else:
			LIMPAR_TELA()
			print("PyCalculator closed!!!")
			pass

# método Multiplicação
def Multiplicacao():
	print("\nMULTIPLICAÇÃO")
	a = float(input("Digite um número: "))						# converte o texto para float e atribui a variavel 'a'
	b = float(input("Digite mais um número: "))					# converte o texto para float e atribui a variavel 'b'
 
	a = a * b													# atribui a variavel 'a', a multiplicação entre 'a' e 'b'
	print("\nA Multiplicação dos números é: ", a)

	#verifica se o usuário sai da calucadora ou faz outra operação
	if a != " ":
		print("\nDeseja fazer outra operação? ")
		aux = input("(S - Sim u N - Não): ")
		if aux == "S" or aux == "s":
			LIMPAR_TELA()
			menu()
		else:
			LIMPAR_TELA()
			print("PyCalculator closed!!!")
			pass

# método Divisão
def Divisao():
	print("\nDIVISÃO")
	a = float(input("Digite um número: "))						# converte o texto para float e atribui a variavel 'a'
	b = float(input("Digite mais um número: "))					# converte o texto para float e atribui a variavel 'b'
 
	a = a / b													# atribui a variavel 'a', a divisão entre 'a' e 'b'
	print("\nA Divisão dos números é: ", a)

	#verifica se o usuário sai da calucadora ou faz outra operação
	if a != " ":
		print("\nDeseja fazer outra operação? ")
		aux = input("(S - Sim u N - Não): ")
		if aux == "S" or aux == "s":
			LIMPAR_TELA()
			menu()
		else:
			LIMPAR_TELA()
			print("PyCalculator closed!!!")
			pass

# método para limpar a tela 
def LIMPAR_TELA():
	os.system('cls')											# Limpar_tela

# método para dar pausa no programa
def PAUSA():
	os.system('pause')											# Pause
# main
if __name__ == '__main__':
	menu()