def compute_public_key(G, x, P):
    return G**x % P


G = int(input('\nGive G (generator): '))
P = int(input('Give P (modulo): '))
X = int(input('Give X (public key) to compute x (private key): '))
x = 0

public_key = compute_public_key(G, x, P)
i = 1   # i is an index to keep track of the trials
while public_key != X:
    print('\nTrial', i, '\b:')
    print('x =', x)
    print('X =', public_key)
    x += 1
    public_key = compute_public_key(G, x, P)
    i += 1

print('\nTrial', i, '\b:')
print('x =', x)
print('X =', public_key)
print('\nFound a match after', i, 'trials!')
print('Private key of public key X =', public_key, 'is x =', x)
print()