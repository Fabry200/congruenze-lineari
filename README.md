# Congruenze Lineari con Algoritmo di Euclide e Semplificazione

Questa è una seconda versione di un algoritmo che risolve congruenze lineari, utilizzando l'algoritmo di Euclide per il calcolo del massimo comune divisore (MCD), la semplificazione delle congruenze, e il Teorema Cinese dei Resti.

Il programma supporta:
- Calcolo del MCD tra due numeri.
- Semplificazione di una congruenza lineare.
- Risoluzione di sistemi di congruenze tramite il Teorema Cinese dei Resti.
- Verifica di primalità con l'algoritmo di Miller-Rabin.

## Funzionalità

### 1. Calcolo del MCD (Massimo Comune Divisore)
La funzione `Mcd(a, b)` calcola il massimo comune divisore tra due numeri `a` e `b` utilizzando l'algoritmo di Euclide.

### 2. Semplificazione di una Congruenza
La funzione `semplificazione(sxparam, dxparam, modulo)` semplifica la congruenza del tipo `sxparam * x ≡ dxparam (mod modulo)`, riducendo i coefficienti se possibile.

### 3. Verifica di Soluzioni Congruenti
La funzione `evalsol(sxparam, dxparam, modulo)` verifica se esistono soluzioni congruenti alla congruenza `sxparam * x ≡ dxparam (mod modulo)` e, se il MCD è maggiore di 1, prova a semplificare la congruenza.

### 4. Risoluzione di Sistemi di Congruenze
La funzione `sistemi(sistema)` risolve un sistema di congruenze utilizzando il Teorema Cinese dei Resti.

### 5. Algoritmo di Miller-Rabin per la Primalità
La funzione `millerrabin(n)` implementa l'algoritmo probabilistico di Miller-Rabin per verificare se un numero `n` è probabilmente primo. È una versione migliorata che riduce i numeri tramite la decomposizione in potenze di 2. (Fermat)

## Uso

1. **Congruenze Lineari**:
    - Per risolvere una singola congruenza, usa la funzione `trovasol(sxparam, dxparam, modulo)`.
    - Per risolvere un sistema di congruenze, usa la funzione `sistemi(sistema)` dove `sistema` è una lista di congruenze nella forma `[a, b, m]` con `a * x ≡ b (mod m)`.

2. **Primalità**:
    - Usa la funzione `millerrabin(n)` per verificare se `n` è probabilmente primo.


### Esempio di Uso

```python
# Risoluzione di una singola congruenza
result = trovasol(6, 3, 9)
print(result)

# Risoluzione di un sistema di congruenze
sistema = [[1, 3, 4], [2, 1, 3], [1, 4, 5]]
sistemi(sistema)

# Verifica se 83207 è probabilmente primo
millerrabin(83207)
