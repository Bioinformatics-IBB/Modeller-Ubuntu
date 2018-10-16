from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

env.io.atom_files_directory = ['.', '../atom_files']

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # Two residue ranges (both will be refined simultaneously)
        return selection(self.residue_range('19:', '28:'),
                         self.residue_range('45:', '50:'))

a = MyLoop(env,
           alnfile  = 'alignment.ali',      # alignment filename
           knowns   = '5fd1',               # codes of the templates
           sequence = '1fdx',               # code of the target
           loop_assess_methods=assess.DOPE) # assess each loop with DOPE
a.starting_model= 1                 # index of the first model
a.ending_model  = 1                 # index of the last model

a.loop.starting_model = 1           # First loop model
a.loop.ending_model   = 2           # Last loop model

a.make()                            # do modeling and loop refinement
