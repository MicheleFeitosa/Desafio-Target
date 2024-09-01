/* 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; */

function pertenceFibonacci(numero) {
    let a = 0, b = 1;
    
    while (b < numero) {
        [a, b] = [b, a + b]; 
    }
    
    return b === numero || numero === 0 
        ? `${numero} pertence à sequência de Fibonacci.` 
        : `${numero} não pertence à sequência de Fibonacci.`;
}

let numero1 = 25; 
let numero2 = 3;
console.log(pertenceFibonacci(numero1));
console.log(pertenceFibonacci(numero2));