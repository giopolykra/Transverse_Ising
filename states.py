import numpy as np
from numpy import array,linalg

from E import *
f = open('state_dict.py', 'w+')
f.write('from numpy import array\n')
# Returns the energies and the energy eigenstates shorted in two dictionaries

def state_vectors(N,J,h, PBC):
    H = HeisenbergHamiltonian(N,J,h,PBC)
    T = getT(N)
    HT = H+0.001*T
    U1, U2 = linalg.eig(HT)
    idx = U1.real.argsort()[::+1]
    U1 = U1[idx]
    U2 = U2[:,idx]
#     energies, en_vec = linalg.eig(H)
#     momenta, mom_vec = linalg.eig(T)
    energies = np.diag(np.dot(np.dot(U2.conj().T,H),U2)).real
    momenta = np.angle(np.diag(np.dot(np.dot(U2.conj().T,T),U2)))
    ind = energies.real.argsort()[::+1]
    energies = energies[ind]
    momenta = momenta[ind]
    # Identify -pi with pi
    ind2 = np.where(np.abs(momenta+np.pi) <1E-6)
    momenta[ind2] = -1.* momenta[ind2]
    momenta = momenta/np.pi
    vec = {}
    en = {}
    for k in range(len(U2)):
        state = []
        [state.append(U2[i][k]) for i in range(len(U2))]
        state = np.asarray(state)
        energy = np.dot(np.conjugate(state.T),np.dot(HT,state)).real
        # Adding a second index to mark the momenta of each state
        vec[('{}'.format(k),'{}'.format(int(momenta[k])))] = state
        en[('{}'.format(k),'{}'.format(int(momenta[k])))]  = energy
    return(en,vec)


for N in [2,3,4,5,6]:
    for i in [0.5,1,2,4,8,10,20]:
        h_name = str(i).replace('.','')
        J = [0,0,1]
        h = [i,0,0]
        for PBC in [True, False]:
            locals()['dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))] = {}
            locals()['dict_en_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))] = {}
            #print('dict_en_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC)))
            for x,y in zip(state_vectors(N,J,h,PBC = PBC)[0].items(),state_vectors(N,J,h,PBC =PBC)[1].items()):
                locals()['dict_en_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))].update({x[0]:x[1]})
                locals()['dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))].update({y[0]:y[1]})
            txt1  = 'dict_en_HT_N{}J{}h{}_{} = {}\n'.format(N,int(J[2]),h_name,str(PBC),eval('dict_en_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))))
            txt2  = 'dict_vec_HT_N{}J{}h{}_{} = {}\n'.format(N,int(J[2]),h_name,str(PBC),eval('dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))))
            f.write(txt1+txt2)
f.close()
