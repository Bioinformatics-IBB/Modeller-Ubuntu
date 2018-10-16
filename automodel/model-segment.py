# Comparative modeling by the automodel class
#
# Demonstrates how to refine only a part of the model.
#
# You may want to use the more exhaustive "loop" modeling routines instead.
#
from modeller import *
from modeller.automodel import *    # Load the automodel class

log.verbose()

# Override the 'select_atoms' routine in the 'automodel' class:
# (To build an all-hydrogen model, derive from allhmodel rather than automodel
# here.)
class MyModel(automodel):
    def select_atoms(self):
        # Select residues 1 and 2 (PDB numbering)
        return selection(self.residue_range('1:', '2:'))

        # The same thing from chain A (required for multi-chain models):
        # return selection(self.residue_range('1:A', '2:A'))

        # Residues 4, 6, 10:
        # return selection(self.residues['4'], self.residues['6'],
        #                  self.residues['10'])

        # All residues except 1-5:
        # return selection(self) - selection(self.residue_range('1', '5'))


env = environ()
# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']
# selected atoms do not feel the neighborhood
env.edat.nonbonded_sel_atoms = 2

# Be sure to use 'MyModel' rather than 'automodel' here!
a = MyModel(env,
            alnfile  = 'alignment.ali',     # alignment filename
            knowns   = '5fd1',              # codes of the templates
            sequence = '1fdx')              # code of the target

a.starting_model= 3                # index of the first model
a.ending_model  = 3                # index of the last model
                                   # (determines how many models to calculate)
a.make()                           # do comparative modeling
