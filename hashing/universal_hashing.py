"""
- We have to introduce randomness by choosing a hash function randomly
from a set of hash functions H (universal family).

- We need some assumtion about H to be universal hash family.

- Probability that {h(k) = h(k')} <= 1/m

- THEOREM:
For n arbitrary distinct keys
For random h € H (universal)
The expected random keys in the slot

- Number of keys colliding with Ki:
let Iinj = {1 if h(ki) = h(kj)}, 0 else

Bad universal hash function:
H = {h: {0, 1, ..., n-1}} -> {0, 1, ... m-1} -> takes to much time and space
Dot-product has family:
- assume m (table size) is prime
- assume u = m^r
- view a key k in base m
whenever  k = <k0a, k1a, k2a..., kr-1>
- for key a = <a0r, a1r, a2r..., ar-1>
define ha(k) = (a * k) mod m
"""