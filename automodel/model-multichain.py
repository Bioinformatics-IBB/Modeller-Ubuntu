# Comparative modeling by the automodel class
#
# Demonstrates how to build multi-chain models
#
from modeller import *
from modeller.automodel import *    # Load the automodel class

log.verbose()

class MyModel(automodel):
    def special_patches(self, aln):
        # Rename both chains and renumber the residues in each
        self.rename_segments(segment_ids=['X', 'Y'],
                             renumber_residues=[1, 1])
        # Another way to label individual chains:
        self.chains[0].name = 'X'
        self.chains[1].name = 'Y'

    def special_restraints(self, aln):
        rsr = self.restraints
        at = self.atoms
#       Restrain the specified CB-CB distance to 8 angstroms (st. dev.=0.1)
#       Use a harmonic potential and X-Y distance group.
#       Note that because special_patches is called before special_restraints,
#       we must use the relabeled chain IDs and residue numbers here.
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CB:40:Y'],
                                                         at['CB:71:Y']),
                               mean=8.0, stdev=0.1))

env = environ()
# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Be sure to use 'MyModel' rather than 'automodel' here!
a = MyModel(env,
            alnfile  = 'twochain.ali' ,     # alignment filename
            knowns   = '2abx',              # codes of the templates
            sequence = '1hc9')              # code of the target

a.starting_model= 2                # index of the first model
a.ending_model  = 2                # index of the last model
                                   # (determines how many models to calculate)
a.make()                           # do comparative modeling
