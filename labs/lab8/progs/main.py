from sys import path
path.append('../modules')

import module

zeroes = [i for i in range(5)]
ones = [j for j in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
module.prodl(ones)
module.prodl(ones)
module.prodl(ones)
module.prodl(ones)

print(module.__counter)
