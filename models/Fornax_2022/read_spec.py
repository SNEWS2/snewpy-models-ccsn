# coding: utf-8
import numpy as np
import argparse

class Spectrum:
    """Storage for spectrum data from the Fornax 2022 models."""

    def __init__(self, t, E, F):
        """Construct a spectrum object.

        Parameters
        ----------
        t : float
            Time stamp of simulation, post-core bounce.
        E : list
            Array of energy values.
        F : list
            Array of flux values.
        """
        self.t = t
        self.E = E
        self.F = F

        Emax = 100 * np.ceil(np.max(E)/100)
        nbin = len(E) + 1
        self.dE = np.diff(np.logspace(0, np.log10(Emax), nbin))
    
    def __str__(self):
        s = f'{t:12g} s\n'
        for _E, _dE, _F in zip(self.E, self.dE, self.F):
            s += f'{_E:12.6f}{_dE:12.6f}{_F:12g}\n'
        return s

def read_spec(filename):
    """Generate spectrum records from flat ASCII files.

    Parameters
    ----------
    filename : string
        Relative path to spectrum file from the Fornax 2022 simulations.

    Returns
    -------
    (t,E,F) : tuple generator
        Generator with a record of t, energy, and flux.
    """
    with open(filename, 'r') as f:
        t, E, F = None, [], []
        
        for line in f:
            if line.startswith('#Time'):
                if t is not None and E and F:
                    yield(t, E, F)
                    E, F = [], []
                t = float(line.strip().split()[-1])
            else:
                tokens = line.strip().split()
                if len(tokens) == 2:
                    E.append(float(tokens[0]))
                    F.append(float(tokens[1]))

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Fornax spectrum reader')
    p.add_argument('filename')
    args = p.parse_args()

    for (t, E, F) in read_spec(args.filename):
        sp = Spectrum(t,E,F)
        print(sp)
