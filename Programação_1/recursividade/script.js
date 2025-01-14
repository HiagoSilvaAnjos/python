function fatorial(n) {
    if (n === 0) return 1; // Caso base
    return n * fatorial(n - 1); // Chamada recursiva
}

console.log(fatorial(5)); // Saída: 120
