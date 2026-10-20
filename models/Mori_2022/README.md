# Mori_2022 1-D CCSN Models with Axion-like Particles

Neutrino data for 1-D CCSN models in presence of axion-like particles.

Data are available in the paper [**Shock revival in core-collapse supernovae assisted by heavy axionlike particles**](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.105.063009) by  Mori, K. _et al._, PhysRevD.105.063009, 2022.

## Available Simulations

The following models are included in ASCII format (MPNS is the proto-neutron star mass when the shock wave reaches r = 400 km. NR means shock revival does not occur for those sets of ALP parameters.):

| Progenitor mass [Msun] | Axion mass [MeV] | Axion-photon coupling [1e-10/GeV]| MPNS [Msun] |
| ----- | ---------------- | ------------ | ------------- | ---------------- | ---------- |
| 20 | 0 | 0 | NR | 
| 20 | 50 | 4 | NR |
| 20 | 50 | 10 | NR |
| 20 | 50 | 20 | NR |
| 20 | 50 | 40 | 1.88 |
| 20 | 100 | 4 | NR |
| 20 | 100 | 10 | NR |
| 20 | 100 | 20 | 1.85 |
| 20 | 100 | 40 | 1.69 |
| 20 | 200 | 4 | NR |
| 20 | 200 | 10 | 1.83 |
| 20 | 200 | 20 | 1.71 |
| 20 | 200 | 40 | 1.63 |
| 20 | 400 | 4 | 1.90 |
| 20 | 400 | 10 | 1.82 |
| 20 | 400 | 20 | 1.78 |
| 20 | 400 | 40 | 1.79 |
 

## Data Format

The format of the data files is:

| Column(s) | Value(s) |
| --------- | -------- |
| 1         | Time [s] |
| 2         | Post-bounce time [s] |
| 3-5       | Number luminosity [/s] |
| 6-8       | Luminosity [erg/s] |
| 9-11      | Mean energy [MeV] |
| 12-15     | RMS energy [MeV] |

