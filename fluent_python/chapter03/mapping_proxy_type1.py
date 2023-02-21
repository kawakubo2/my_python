from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
# MappingProxyTypeはイミュータブルな辞書
try:
    d_proxy[2] = 'B'
except TypeError as e:
    print(e)

d[2] = 'B'

# dの変化が動的に反映される
print(d_proxy)