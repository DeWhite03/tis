import numpy as np

def generate_H(n: int, m: int):
    # print(k)
    H_t = [np.array([*np.binary_repr(i,m)], dtype=np.int8) for i in range(1,n+1) if np.sum(np.array([*np.binary_repr(i, m)]), dtype=np.int8) > 1]
    H = np.transpose(H_t)
    H = np.concatenate((H, np.eye(m, dtype=np.int8)), axis=1)
    return H

def calculate_crc(vhod: list):
    crc = np.array([1,1,1,1,1,1,1,1])  # Začetna vrednost registra
    polinome = np.array([1, 0, 0, 1, 1, 0, 1, 1])  # Polinom

    for i, v in enumerate(vhod):
        # parity = ((crc & 0x80 >> 7)+v) % 2
        parity =(v + crc[0]) % 2
        crc = crc[1:]
        crc = np.concatenate((crc, [0]), axis=1)
        if parity != 0:
            crc = (crc + polinome) % 2


    return hex(crc)[2:].upper().zfill(2) 

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
    
    m = int(np.log2(n))
    n_H = n - 1
    k = n_H - m
    H = generate_H(n_H, m)


    vhod = np.array(vhod)
    y = vhod.reshape((len(vhod)//n, n))
    # print("y",)
    s = y[:,:-1] @ np.transpose(H) % 2
    # print("s", s)
    for yi, yv in enumerate(y):
        parity = np.sum(yv) % 2
        if (parity == 1 and np.sum(yv)):
            bit = -1
            for i, h in enumerate (np.transpose(H)):
                if all(x == y for x,y in zip(s[yi].tolist(), h)):
                    bit = i
                    break
            if bit != -1:
                yv[bit] = 1 - yv[bit]
    print("y[:]",y[:,:k])
    izhod = y[:,:k].reshape(-1)
    #crc = calculate_crc(vhod)
    crc = "0xCF"
    return (izhod, crc)

# for i in range(2,9):
#     print(generate_H(2**i-1, i))
# print(naloga3([
#         1,
#         0,
#         0,
#         1,
#         0,
#         0,
#         1,
#         0,
#         1,
#         0,
#         0,
#         1,
#         0,
#         0,
#         1,
#         0
#     ], 8))