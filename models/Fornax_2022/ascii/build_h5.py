import os
import h5py
import numpy as np
from read_spec import read_spec, Spectrum
from argparse import ArgumentParser
from tqdm import tqdm

p = ArgumentParser(description='Generate HDF5 outputs from Fornax data')
p.add_argument('progenitor', help='progenitor folder name')
args = p.parse_args()

# Read in list of PNS baryon masses.
pns_mass = {}
with open('pns_2022-2D.txt') as f_pns:
    for line in f_pns:
        if line.startswith('#'):
            continue
        tokens = line.strip().split()
        pns_mass[tokens[0]] = float(tokens[1])

with h5py.File(f'lum_spec_{args.progenitor}_dat.h5', 'w') as outf:
    mass = args.progenitor[:-3] if 'bh' in args.progenitor else args.progenitor
    outf.attrs['Mpns'] = pns_mass[mass]

    # Loop over flavor.
    for flavor in tqdm('012'):
        nufile = os.path.join(args.progenitor, f'nuspec.{flavor}.xg')
        nutype = f'nu{flavor}'

        grp = outf.create_group(nutype)

        # Storage for times, fluxes, energy bins, and energy bin widths.
        times = []
        g  = [ [] for _ in range(12) ]
        egroup  = []
        degroup = []

        for (t, E, F) in read_spec(nufile):
            spec = Spectrum(t, E, F)
            times.append(spec.t.to_value('s'))
            egroup.append(list(spec.E.to_value('MeV')))
            degroup.append(list(spec.dE.to_value('MeV')))

            for j, fl in enumerate(spec.F):
                g[j].append(fl.to_value('1e50 erg/(MeV s)'))

        # Write attributes and datasets to each flavor group.
        grp.attrs['time'] = times
        grp.create_dataset('egroup', data=egroup)
        grp.create_dataset('degroup', data=degroup)
        for j in range(12):
            grp.create_dataset(f'g{j}', data=g[j])

    outf.close()
