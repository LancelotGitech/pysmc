"""
Run SMC on the simple model.

Author:
    Ilias Bilionis

Date:
    9/28/2013

"""


import simple_model as model
import pymc
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import pysmc
import mpi4py.MPI as mpi
#import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Construct the SMC sampler
    smc_sampler = pysmc.SMC(model, num_particles=4000,
                            num_mcmc=10, verbose=1,
                            mpi=mpi, gamma_is_an_exponent=True)
    # Initialize SMC at gamma = 0.01
    smc_sampler.initialize(0.01)
    # Move the particles to gamma = 1.0
    smc_sampler.move_to(1.)
    # Get a particle approximation
    p = smc_sampler.get_particle_approximation()
    print p.use_mpi
    m = p.mean
    v = p.variance
    if mpi.COMM_WORLD.Get_rank() == 0:
        print m
        print v
    # Plot a histogram
#    pysmc.hist(plt, p, 'mixture', bins=100)
#    plt.show()