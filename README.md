# MDH Private Key Finder
This is a basic educational python program based on the Merkle-Diffie-Hellman key exchange. I initially wrote this in C++, but then realised C++ does not handle large numbers so well, so I translated it into Python. This is actually my first Python program.

## How it works
Computes the public key (X) by raising the generator to the power of the private key (x) and then performing modulo P (G<sup>x</sup> mod P). The program iterates over private keys starting from 0, until a matching public key (public_key = X) is found.

## Demonstration
### 1. Input G (generator)
<picture><img width="500" alt="A_1" src="https://user-images.githubusercontent.com/100732009/203668195-8881db8b-a791-4178-b1b3-0f152fda3f14.png"></picture>

### 2. Input P (modulo)
<picture><img width="500" alt="A_2" src="https://user-images.githubusercontent.com/100732009/203668451-8bbade49-7396-41d0-901a-017ba0c97492.png"></picture>

### 3. Input X (public key)
<picture><img width="500" alt="A_3" src="https://user-images.githubusercontent.com/100732009/203668458-a2b6d32d-dcd5-4c10-862b-b422d4218272.png"></picture>

### 4. All trial results are printed to the console
<picture><img width="500" alt="A_4" src="https://user-images.githubusercontent.com/100732009/203668463-8db9826c-4ebc-4031-993b-18eb211b27ad.png"></picture>

### 5. We see the corresponding private key of X
<picture><img width="500" alt="A_5" src="https://user-images.githubusercontent.com/100732009/203668472-d3a1f6eb-1e59-4973-b67c-7c98e7e1e37f.png"></picture>
