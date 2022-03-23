import math

n = 0x65446ab139efe9744c78a271ad04d94ce541a299f9d4dcb658f66f49414fb913d8ac6c90dacc1ad43135454c3c5ac76c56d71d2816dac23db5c8caa773ae2397bd5909a1f2823c230f44ac684c437f16e4ca75d50b75d2f7e5549c034aa8a723c9eaa904572a8c5c6c1ed7093a0695522a5c41575c4dbf1158ca940c02b223f50ae86e6782819278d989200a2cd2be4b7b303dffd07209752ee5a3060c6d910a108444c7a769d003bf8976617b4459fdc15a2a73fc661564267f55be6a0d0d2ec4c06a4951df5a096b079d9e300f7ad72fa6c73a630f9a38e472563434c10225bde7d08c651bdd23fd471077d44c6aab4e01323ed78641983b29633ad104f3fd# The number you want to factorize

primes = []

def polynomial(x, n):
    return (x ** 2 - 1) % n

def algorithm(n):
    d = 1
    x = 2
    y = 2
    while d == 1:
        x = int(polynomial(x, n))
        y = int(polynomial(polynomial(y, n), n))
        d = math.gcd(int(abs(x - y)), n)
        print(x, y, d)

    if d == n:
        return "Done"
    else:
        return d

if algorithm(n) == "Done":
    primes.append(n)
else:
    first = int(algorithm(n))
    primes.append(first)
    check = n

    while check / first != 1:
        m = int(check / first)
        next = algorithm(m)
        if next == "Done":
            primes.append(int(n / math.prod(primes)))
            break
        else:
            primes.append(next)
            check =  check / next

print(primes)
