import os
import re
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
with open('pns_2024-3D.txt') as f_pns:
    for line in f_pns:
        if line.startswith('#'):
            continue
        model, mass = line.strip().split()

        # Check for unknown mass
        if re.sub('[0-9.]', '', mass) == '':
            mass = float(mass)
        else:
            mass = -1.

        pns_mass[model] = float(mass)

with h5py.File(f'lum_spec_{args.progenitor}_dat.h5', 'w') as outf:
    model = args.progenitor
    Mpns = pns_mass[model] if model in pns_mass else -1.
    outf.attrs['Mpns'] = Mpns

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

        print(len(times))

        # Write attributes and datasets to each flavor group.
        grp.attrs['time'] = times
        grp.create_dataset('egroup', data=egroup)
        grp.create_dataset('degroup', data=degroup)
        for j in range(12):
            grp.create_dataset(f'g{j}', data=g[j])

    outf.close()
