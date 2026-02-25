programa{
    funcao inicio(){
         inteiro n, contador, soma
        
        contador = 1
        soma = 0 

        escreva("digite um número: ")
        leia(n)

          enquanto ( contador <= n) {
           soma = soma + contador
           contador = contador + 1
          }

          escreva("A soma de 1 ate", N, "é:", soma)
    }
}