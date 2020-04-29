import numpy as np
from numpy import array,kron,random,identity
from qiskit import *
import matplotlib.pyplot as plt
from numpy.linalg import inv
import pathlib
path = pathlib.Path().absolute()

from E import *
from angles import *
from circuit import *
from matrix_plot import *

N=2
layers =2
#PBC = True
PBC = True

param = parameters(N,layers,PBC = PBC)
qc = circuit1(N,param,layers,PBC = PBC)
print("param={}".format(repr(param)))
qc.draw(output="mpl")#, filename = 'my_circuit.png')
plt.savefig(str(path)+'/trials/circuit.png')
#plt.show()
#print(qc)i


J=[0.,0.,1.]
h = [1.,0.,0.]
plot_matrices(N,J,h,PBC)
plot_scatter(N,J,h,PBC)
