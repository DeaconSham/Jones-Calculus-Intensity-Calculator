import sympy as sp
from sympy import * 
init_printing(use_unicode=True)
# Initialize project polarization states as [[x,y]] 1*2 matricies
L1 = Matrix([[1,0]])
R1 = Matrix([[0,1]])
H1 = Matrix([[sp.sqrt(2)/2, sp.sqrt(2)/2]])
V1 = Matrix([[sp.sqrt(2)/2, -(sp.sqrt(2)/2)]])
D1 = Matrix([[sp.sqrt(2)/2, I*(sp.sqrt(2)/2)]])
A1 = Matrix([[sp.sqrt(2)/2, -I*(sp.sqrt(2)/2)]])
# Initialize prepare polarization states as [x,y] 2*1 matricies
L2 = Matrix([1,0])
R2 = Matrix([0,1])
H2 = Matrix([sp.sqrt(2)/2, sp.sqrt(2)/2])
V2 = Matrix([sp.sqrt(2)/2, -(sp.sqrt(2)/2)])
D2 = Matrix([sp.sqrt(2)/2, I*(sp.sqrt(2)/2)])
A2 = Matrix([sp.sqrt(2)/2, -I*(sp.sqrt(2)/2)])
# Initialize Jones matrix
phi1, phi2, r = symbols('phi1 phi2 r')
T11 = E**(-I*(phi2-phi1))
T12 = 0
T13 = 0
T14 = E**(I*(phi2-phi1))
T1 = Matrix([[T11, T12], [T13, T14]])
T21 = 0
T22 = E**(-I*(phi1+phi2))
T23 = E**(I*(phi1+phi2))
T24 = 0
T2 = Matrix([[T21, T22], [T23, T24]])
J = (((1+E**(I*r))/2)*T1)+(((1-E**(I*r))/2)*T2)
# Jones matrix operation
project = Matrix()
prepare = Matrix()
askproject = input("What polarization state are you projecting? (L, R, H, V, D, A):\n")
if askproject == 'L':
    project = L1
elif askproject == 'R':
    project = R1
elif askproject == 'H':
    project = H1
elif askproject == 'V':
    project = V1
elif askproject == 'D':
    project = D1
elif askproject == 'A':
    project = A1
askprepare = input("What polarization state are you preparing? (L, R, H, V, D, A):\n")
if askprepare == 'L':
    prepare = L2
elif askprepare == 'R':
    prepare = R2
elif askprepare == 'H':
    prepare = H2
elif askprepare == 'V':
    prepare = V2
elif askprepare == 'D':
    prepare = D2 
elif askprepare == 'A':
    prepare = A2
operation = (Abs(project*J*prepare))**2
print("The following operation is proportional to the final intensity:")
pprint(operation)