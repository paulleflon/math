# Math algorithms

## How to use
First of all, clone this repository:
```
git clone https://github.com/paulleflon/math.git
```
*or, using GitHub CLI:*
```bash
gh repo clone paulleflon/math
```

Execute the scripts using **`Python`**, by entering the values either as command line arguments or following the instructions.

Inputs for each script are detailed below:

### Extended Euclidean Algorithm
Performs the Extended Euclidean (a.k.a Extended GCD) algorithm for the given numbers
```bash
python3 extended_euclidean.py <a> <b>
```
#### Arguments
- `a`: non-null positive integer
- `b`: non-null positive integer

### Modulo Inverse
Computes the inverse of a number in the given ring.
```bash
python3 modulo_inverse.py <number> <modulo>
```
#### Arguments
 - `number`: the number to find the inverse of, a non-null positive integer, lower than `modulo`
 - `modulo`: the modulo to find the inverse to, a non-null positive integer

### Modulo Powers
Computes the power of a number in the given ring.
```bash
python3 modulo_powers.py <base> <exponent> <modulo>
```
#### Arguments
- `base`: a non-null positive integer lower than `modulo`
- `exponent`: the exponent of the power to compute, non-null positive integer
- `modulo`: the modulo to compute the power in, a non-null positive integer

### Modulo Linear Equations
Solves a linear equation (`ax = b`) in a ring

```bash
python3 modulo_equations.py <a> <b> <modulo>
```
#### Arguments
- `a`: a non-null positive integer
- `b`: a non-null positive integer
- `modulo`:a non-null positive integer
