N = 40

def sieb(N):
    numbers = list(range(2, N))
    primes = []
    
    while len(numbers) != 0:
        kleinstes_elem = numbers[0]
        primes.append(kleinstes_elem)
        for i in numbers:
            if i%kleinstes_elem == 0:
                numbers.remove(i)
    return primes
                

print(max(sieb(1000)))