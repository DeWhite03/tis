import numpy as np

def naloga3(vhod: list, n: int) -> tuple[list, str]:
    """
    Izvedemo dekodiranje binarnega niza `vhod`, zakodiranega 
    z razsirjenim Hammingovim kodom dolzine `n` in poslanega 
    po zasumljenem kanalu.
    Nad `vhod` izracunamo vrednost `crc` po standardu CRC-8/CDMA2000.

    Parameters
    ----------
    vhod : list
        Sporocilo y, predstavljeno kot seznam bitov (stevil tipa int) 
    n : int
        Stevilo bitov v kodni zamenjavi
    
    Returns
    -------
    (izhod, crc) : tuple[list, str]
        izhod : list
            Odkodirano sporocilo y (seznam bitov - stevil tipa int)
        crc : str
            Vrednost CRC, izracunana nad `vhod`. Niz dveh znakov.
    """

    # m = m_h + 1 = log_2(n) + 1
    # k = n - m
    # matrika H (H(7,4))
    # G = [ I | B] <- k vrstic, n_H stolpcev
    # H = [ B^T | I ] <- m_H vrstic, n_H stolpcev
    # nrdimo matriko k gre po vrsti in binarno napise index stolpca v polja. pol pa stolpce prestavmo tko da je identiteta na desni strani ostali stolpci so pa va levi
    '''
    primer H    1 2 3 4 5 6 7
                0 0 0 1 1 1 1
            H = 0 1 1 0 0 1 1
                1 0 1 0 1 0 1

                3 5 6 7   4 2 1
                0 1 1 1 | 1 0 0
            H = 1 0 1 1 | 0 1 0
                1 1 0 1 | 0 0 1

    ce napaka potemm poiscemon napako tko da zracunamo sindrom
    s = y * H^T
    in potem poisces sindrom v matriki H ter na mestu sindroma flipas bit v sporocilu
    '''
    izhod = []
    crc = ''
    return (izhod, crc)