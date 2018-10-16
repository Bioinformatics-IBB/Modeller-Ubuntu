# Comparative modeling by the automodel class

from modeller import *

from modeller.automodel import *    # Load the automodel class

env = environ()  # create a new MODELLER environment to build this model in
log.verbose()    # request verbose output

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = loopmodel(env,
              alnfile  = 'alignment.ali',      # alignment filename
              knowns   = '5fd1',               # codes of the templates
              sequence = '1fdx',               # code of the target
              assess_methods = assess.GA341)   # assess with GA341 score
a.starting_model= 1                 # index of the first model
a.ending_model  = 2                 # index of the last model
                                    # (determines how many models to calculate)

# Import all of the library restraints
import modeller.library_restraints as lib

# Use these restraints (rather than the CHARMM libraries) for both standard
# modeling and loop refinement
a.use_library_restraints(lib)
a.loop.use_library_restraints(lib)

a.loop.starting_model = 1
a.loop.ending_model   = 2
a.loop.md_level = refine.fast
a.loop.assess_methods = assess.DOPE

a.make()                            # do the actual comparative modeling
