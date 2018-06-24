# GAN-MP-Hybrid-Heuristic

The souce code of "A GAN-MP Hybrid Heuristic Method for Non-convex Portfolio Optimization Problem" \
Authors: Yerin Kim, Daemook Kang, Mingoo Jeon, and Chungmok Lee @ Hankuk University of Foreign Studies \
Corresponding Email: chungmok@hufs.ac.kr


## File Description

### Data
Data was provided by Principal (https://www.principal.com/).

### Executive Files
	
- GAN_MP_Hybrid_Heurisic.ipynb 
- GAN_MP_Hybrid_Heurisic_Robust.ipynb 
- couenne_portfolio : a code for solving the MINLP with Couenne


### Functional Files
	
- generator.py : NN based portfolio generator
- discriminator.py : formulation based portfolio discriminator

- mathematical_formulation.py : formulation for (P2) 
- mathematical_formulation_robust.py : formulation for (RP)

- Bisectional_Search.py : update the constraint (27) to (P2)
- Bisectional_Search_Robust.py  : update the constraint (27) to (RP)


### Execution Environment

- Programming Language : Python 3.6
- Web Application for Python : Jupiter Notebook
- Optimization Solver : ILOG CPLEX 12.6 and Couenne(https://projects.coin-or.org/Couenne/) 
- Neural Network Library : Pytorch (http://pytorch.org/)
- Parallel Computing Library : IPyparallel (https://github.com/ipython/ipyparallel)
- Library : pandas, scipy, numpy, math, random





