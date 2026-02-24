programa{
    funcao inicio()  {
      inteiro mes

      escreva("digite um numero de 1 a 12:")
      leia(mes)

      escolha(mes) {
        caso 1: caso 3: caso 5: caso 7: caso 8: caso 10: caso 12:
        escreva("esse mes tem 31 dias \n")
        pare

        caso 4: caso 6: caso 9: caso 11:
        escreva("esse mes tem 30 dias \n")
        pare

        caso 2:
        escreva("esse mes tem 29 ou 28 dias \n")

        caso contrario:
         escreva("Mês invalido! \n ") 
                
      }
    }
}