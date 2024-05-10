import numpy as np

def generate_H(n: int, m: int, k: int):
    # print(k)
    H_t = [np.array([*np.binary_repr(i,k)], dtype=np.int8) for i in range(1,n) if np.sum(np.array([*np.binary_repr(i, k)]), dtype=np.int8) > 1]
    H = np.transpose(H_t)
    H = np.concatenate((H, np.eye(k, dtype=np.int8)), axis=1)
    print(H_t)
    print(H)
    return H



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
    
    m = int(np.log2(n) + 1)
    n_H = n -1
    k = n_H - m
    H = generate_H(n, m, k)
    print(H)
    s = vhod[:n_H] @ np.transpose(H) % 2
    bit = -1
    print(np.transpose(H))
    for i, h in enumerate (np.transpose(H)):
        print(s)
        print(i , h)
        if all(x == y for x,y in zip(s, h)):
            bit = i
            break
    
    print(bit)
    vhod[bit] = 1 - vhod[bit]
    # s = s % 2

    # s = [i % 2 for i in s]
    # print(vhod[:7])
    # print(s)
    izhod = vhod[:m]
    # print(H)
    crc = 0
    return (izhod, crc)

print(naloga3([
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0
    ], 8))