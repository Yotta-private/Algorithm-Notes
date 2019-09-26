# rdkit.Chem.rdmolfiles.MolFragmentToSmiles
>rdkit.Chem.rdmolfiles.MolFragmentToSmiles((Mol)mol, (AtomPairsParameters)atomsToUse[, (AtomPairsParameters)bondsToUse=0[, (AtomPairsParameters)atomSymbols=0[, (AtomPairsParameters)bondSymbols=0[, (bool)isomericSmiles=True[, (bool)kekuleSmiles=False[, (int)rootedAtAtom=-1[, (bool)canonical=True[, (bool)allBondsExplicit=False[, (bool)allHsExplicit=False]]]]]]]]]) → str :¶
Returns the canonical SMILES string for a fragment of a molecule

## ARGUMENTS:
>>mol: the molecule

>>atomsToUse : a list of atoms to include in the fragment

>>bondsToUse : (optional) a list of bonds to include in the fragment

>>if not provided, all bonds between the atoms provided will be included.

>> atomSymbols : (optional) a list with the symbols to use for the atoms
in the SMILES. This should have be mol.GetNumAtoms() long.

>> bondSymbols : (optional) a list with the symbols to use for the bonds
in the SMILES. This should have be mol.GetNumBonds() long.

>> isomericSmiles: (optional) include information about stereochemistry in the SMILES. Defaults to true.
>> kekuleSmiles: (optional) use the Kekule form (no aromatic bonds) in the SMILES. Defaults to false.
>> rootedAtAtom: (optional) if non-negative, this forces the SMILES to start at a particular atom. Defaults to -1.
canonical: (optional) if false no attempt will be made to canonicalize the molecule. Defaults to true.
allBondsExplicit: (optional) if true, all bond orders will be explicitly indicated in the output SMILES. Defaults to false.
allHsExplicit: (optional) if true, all H counts will be explicitly indicated in the output SMILES. Defaults to false.
doRandom: (optional) if true, randomized the DFS transversal graph, so we can generate random smiles. Defaults to false.
