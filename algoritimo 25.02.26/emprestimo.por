programa{
  funcao inicio(){

		real valorCasa, salario, prestacao
		inteiro anos, meses

		escreva("--- Sistema de Aprovação de Empréstimo ---\n")

		escreva("Qual o valor da casa? R$ ")
		leia(valorCasa)

		escreva("Qual o salário do comprador? R$ ")
		leia(salario)

		escreva("Em quantos anos pretende pagar? ")
		leia(anos)

	
		meses = anos * 12
		prestacao = valorCasa / meses

		escreva("\n-----------------------------------------")
		escreva("\nPara pagar uma casa de R$ ", valorCasa, " em ", anos, " anos:")
		escreva("\nA prestação será de: R$ ", prestacao)
 
	
		se (prestacao <= salario * 0.30)
		{
			escreva("\nEMPRÉSTIMO APROVADO! Parabéns!\n")
		}
		senao
		{
			escreva("\nEMPRÉSTIMO NEGADO!.\n")
		}
		escreva("\n-----------------------------------------\n")


  }
}