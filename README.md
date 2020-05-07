# <center> Transverse_Ising </center>
A python code for the computation of excited states of the Transverse Ising model through the use of a Qiskit circuit.

The structure of the code is as follows:
<ul>
  <li>In the file "E.py " the is the definition of the Heisenberg Hamiltonian and the momentum operator. 
</li>
  <li>The "matrix_plot.py" can by used to create 2d plots from the matrices in "E.py" as well a scatter plot of momenta vs Energy of the excited states.
</li>
  <li>The "circuit.py" has definitions of the circuits that can be used for the computations.
</li>
  <li>The "states.py" creates the "state_dict.py" file which contains the eigenvalues and eigenvectors of the Heisenberg Hamiltonian.
</li>
  <li>The "b_values.py" creates the "b_values_data.py" which contains the b arrays used for the computation of excited states.
</li>
  <li>The "optimizing.py" is the main file for optimization.
</li>
  <li>The "optimizing_functions.py" contains the definition of functions used for the computation of the ground and excited states.
</li>
  <li>The "custom_optimizers.py" contains a function for sequencial optimization.
</li>
  <li>The "main.py" is the central file through which the user may interact. 
</li>
  <li>The resulting plots and data are created in the /trial folder.
</li>
</ul>

# Dependencies
<ul>
  <li>Qiskit
</li>
  <li>scipy
</li>
  <li>sys
</li>
  <li>matplotlib
</li>
  <li>numpy
</li>
  <li>pathlib
</li>
</ul>

Please note that the code is currently under heavy customization.
The code is made to test arXiv:2002.06210v2 and arXiv:1805.08138v5
