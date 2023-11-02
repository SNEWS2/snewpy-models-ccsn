# Mori_2023 Axionlike CCSN 2D Models

Neutrino data for 2D models with axion-like particles.

Data are available in the paper [**Multi-messenger signals of heavy axionlike particles in core-collapse supernovae: two-dimensional simulations**](https://arxiv.org/abs/2304.11360) by K.  Mori, T. Takiwaki, K. Kotake and S. Horiuchi, Phys. Rev. D 108:063027, 2023.

## Available Simulations

The following models are included in ASCII format:

| Model | Axion mass [MeV] | Coupling g10 | tpb,2000 [ms] | Ediag [1e51 erg] | MPNS [Msun] |
| ----- | ---------------- | ------------ | ------------- | ---------------- | ---------- |
| Standard | − | 0 | 390 | 0.40 | 1.78 |
| (100, 2) | 100 | 2 | 385 | 0.37 | 1.77 |
| (100, 4) | 100 | 4 | 362 | 0.34 | 1.76 |
| (100, 10) | 100 | 10 | 395 | 0.36 | 1.77 |
| (100, 12) | 100 | 12 | 357 | 0.43 | 1.77 |
| (100, 14) | 100 | 14 | 360 | 0.44 | 1.77 |
| (100, 16) | 100 | 16 | 367 | 0.51 | 1.77 |
| (100, 20) | 100 | 20 | 330 | 1.10 | 1.74 |
| (200, 2) | 200 | 2 | 374 | 0.45 | 1.77 |
| (200, 4) | 200 | 4 | 376 | 0.45 | 1.76 |
| (200, 6) | 200 | 6 | 333 | 0.54 | 1.75 |
| (200, 8) | 200 | 8 | 323 | 0.94 | 1.74 |
| (200, 10) | 200 | 10 | 319 | 1.61 | 1.73 |
| (200, 20) | 200 | 20 | 248 | 3.87 | 1.62 |

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
