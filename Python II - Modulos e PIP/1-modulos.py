import calc #importando o modulo todo
from calc import div #em portugues: de calc importe apenas div

#importando o modulo todo, precisa chamar ele e depois a função.
print(calc.sum(10,2))
print(calc.sub(10,6))
print(calc.mult(10,6))
print(calc.div(10,2))

#apenas importando div
print(div(10,5))