import os
import h5py
import numpy as np
from argparse import ArgumentParser
from tqdm import tqdm

p = ArgumentParser(description='Validate HDF5 outputs from Fornax data')
p.add_argument('filenames', nargs='+', help='HDF5 file name(s)')
args = p.parse_args()

for filename in tqdm(args.filenames):
    with h5py.File(filename, 'r') as hf:

        # Check for the PNS mass attribute.
        assert('Mpns' in hf.attrs)

        for flavor in '012':
            nutype = f'nu{flavor}'

            # Check that nuX group is present.
            assert(nutype in hf)

            # Check for attributes in times.
            assert('time' in hf[nutype].attrs)
            n = len(hf[nutype].attrs['time'])

            # Check for egroup and degroup data.
            assert('egroup' in hf[nutype])
            assert(n == len(hf[nutype]['egroup']))

            assert('degroup' in hf[nutype])
            assert(n == len(hf[nutype]['degroup']))

            # Check flux data in 12 bins.
            for i in range(12):
                fluxbin = f'g{i}'
                assert(fluxbin in hf[nutype])
                assert(n == len(hf[nutype][fluxbin]))
