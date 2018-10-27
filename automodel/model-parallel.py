# Comparative modeling by the automodel class, using multiple processors
from modeller import *
from modeller.automodel import *    # Load the automodel class
from modeller.parallel import *

# Use 2 CPUs in a parallel job on this machine
j = job()
j.append(local_slave())
j.append(local_slave())

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = automodel(env,
              alnfile  = 'alignment.ali',     # alignment filename
              knowns   = '5fd1',              # codes of the templates
              sequence = '1fdx')              # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 5                 # index of the last model
                                    # (determines how many models to calculate)
a.use_parallel_job(j)               # Use the job for model building
a.make()                            # do the actual comparative modeling
