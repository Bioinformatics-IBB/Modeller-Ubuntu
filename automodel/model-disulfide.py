# Comparative modeling by the automodel class
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

# Redefine the special_patches routine to include the additional disulfides
# (this routine is empty by default):
class MyModel(automodel):
    def special_patches(self, aln):
        # A disulfide between residues 8 and 45:
        self.patch(residue_type='DISU', residues=(self.residues['8'],
                                                  self.residues['45']))

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = MyModel(env,
            alnfile  = 'alignment.ali',     # alignment filename
            knowns   = '5fd1',              # codes of the templates
            sequence = '1fdx')              # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 1                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling
