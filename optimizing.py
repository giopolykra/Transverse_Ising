import sys
import numpy as np
from numpy import array
from qiskit import *
from scipy.optimize import basinhopping
from scipy.optimize import minimize
from scipy.optimize import fmin_l_bfgs_b
from qiskit.aqua.components.optimizers import COBYLA, NELDER_MEAD, SLSQP, SPSA, ADAM, CG, L_BFGS_B,TNC
from E import *
from angles import *
from circuit import *
from state_dict import *
from custom_optimizers import *
from optimizing_functions import *

import pathlib
path = pathlib.Path().absolute()



def main_opt(layers,Iter,N,K,J,h,PBC):
    file = open(str(path)+'/trials/results_2.py','w+')
    file.write('from numpy import array\n')
    if N==2 and K>4:
        sys.stdout.write("There are only 4 eigenstates for N=2. Please provide K<5")
        sys.stdout.flush()
    for layers in [3,2,1]:#
        error_calls = []
        momenta_calls = []
        opt_energy =[]
        opt_param =[]
        # the bounds
        xmin = -np.ones(4*layers)*np.pi*2
        xmax = np.ones(4*layers)*np.pi*2
        # rewrite the bounds in the way required by PSO
        bounds = [(low, high) for low, high in zip(xmin, xmax)]

        for h_value in [1]:
            h_name = str(h_value).replace('.','')
            class Glo:
                h = [h_value,0,0]
            x0 = parameters(N,layers,PBC = PBC)
            global p
            locals()['Seq_en_N{}J1h{}_l{}_iter{}_{}'.format(N,h_name,layers,Iter,str(PBC))] = []
            locals()['Seq_errors_N{}J1h{}_l{}_iter{}_{}'.format(N,h_name,layers,Iter,str(PBC))] = []
            locals()['Seq_momenta_N{}J1h{}_l{}_iter{}_{}'.format(N,h_name,layers,Iter,str(PBC))] = []
            for p in range(K):
                if p!=0:
                    sys.stdout.write('k{}\x09layers{}\n'.format(p,layers))
                    sys.stdout.flush()
                    #sys.stdout.write('opt_param ->{}\n'.format(opt_param))
                    ret = minimize(extra_term,x0,args=(layers,N,J,Glo.h,PBC,p,opt_param),method='COBYLA',jac=None, bounds=None, tol=None, callback=None,options={'maxiter': 10})
                    ret = [array(ret.x),ret.fun]
                    sys.stdout.write('end ret\x09->{}\n'.format(ret[1]))
                    sys.stdout.flush()
                    res_sequencial = sequencial_minimizer(extra_term,ret[0],Iter,layers,N,J,h,PBC,p,opt_param)
                    sys.stdout.write('end res_seq \x09-> {}\n'.format(res_sequencial[1]))
                    sys.stdout.flush()
                    opt_param.append(res_sequencial[0])
                    opt_energy.append(res_sequencial[1])
                    error_callbacks(res_sequencial[0],layers,N,J,h,PBC,p,error_calls)
                    momenta_callbacks(res_sequencial[0],N,J,h,PBC,p,momenta_calls)
                    sys.stdout.write('param \x09-> {}\n'.format(opt_param))
                    sys.stdout.flush()
                else:
                    sys.stdout.write('k{}\x09layers{}\n'.format(p,layers))
                    sys.stdout.flush()
                    ret = minimize(base_term,x0,args=(layers,N,J,Glo.h,PBC,p,opt_param),method='COBYLA',jac=None, bounds=None, tol=None, callback=None,options={'maxiter': 10})
                    ret = [array(ret.x),ret.fun]
                    sys.stdout.write('end ret\x09->{}\n'.format(ret[1]))
                    sys.stdout.flush()
                    res_sequencial = sequencial_minimizer(base_term,ret[0],Iter,layers,N,J,h,PBC,p,opt_param)
                    sys.stdout.write('end res_seq \x09-> {}\n'.format(res_sequencial[1]))
                    sys.stdout.flush()
                    opt_param.append(res_sequencial[0])
                    #sys.stdout.write('opt_param ->{}\n'.format(opt_param))
                    opt_energy.append(res_sequencial[1])
                    error_callbacks(res_sequencial[0],layers,N,J,h,PBC,p,error_calls)
                    momenta_callbacks(res_sequencial[0],N,J,h,PBC,p,momenta_calls)
                if p==K-1:
                    txt1 = "Seq_en_N{}J1h{}_l{}_iter{}_{} = np.array({})\n".format(N,h_name,layers,Iter,str(PBC),opt_energy)
                    txt2 = "Seq_errors_N{}J1h{}_l{}_iter{}_{} = np.array({})\n".format(N,h_name,layers,Iter,str(PBC),error_calls)
                    txt3 = "Seq_momenta_N{}J1h{}_l{}_iter{}_{} = np.array({})\n".format(N,h_name,layers,Iter,str(PBC),momenta_calls)
                    file.write(txt1+txt2+txt3)
            txt4 = "Seq_param_N{}J1h{}_l{}_iter{}_{} = {} ".format(N,h_name,layers,Iter,str(PBC),opt_param)
            file.write(txt4)
    file.close()

#N = 2
#K = 4
#Iter = 10
#layers = 2
#J = [0,0,1]
#h = [1,0,0]
#PBC = True
#main_opt(layers,Iter,N,K,J,h,PBC)
