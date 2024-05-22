import numpy as np

def DCT(x: int, N: int, n: int) -> float:
    return 2 * np.sum([x*np.cos((np.pi/N)*(k+.5)*n) for k in range(N)])

def naloga4(slika: np.array, velikostOkna: int) -> float:
    """
    Poenostavi sliko

    Parameters
    ----------
    slika : numpy array
        vhodna slika 
    velikostOkna : int
        velikost okna za DCT
    
    Returns
    -------
    PSNR : float
         Peak Signal to Noise Ratio
    """
    print(slika)
    P = np.zeros((len(slika), len(slika[0])), dtype=float)
    print(P)

    for ri, row in enumerate(slika):
        for ei, element in enumerate(row):
            P[ri][ei] = DCT(ei, velikostOkna, ei)
    
    print(P)
    Pt = P.transpose()
    print(Pt)
    P2 = np.zeros((len(slika), len(slika[0])), dtype=float)
    for ri, row in enumerate(Pt):
        for ei, element in enumerate(row):
            P2[ri][ei] = DCT(ei, velikostOkna, ei)

    print(P2)
    PSNR = float('nan')
    return PSNR