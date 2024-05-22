import numpy as np

def generate_H(n: int, m: int):
    H_t = [np.array([*np.binary_repr(i,m)], dtype=np.int8) for i in range(1,n+1) if np.sum(np.array([*np.binary_repr(i, m)]), dtype=np.int8) > 1]
    H = np.transpose(H_t)
    H = np.concatenate((H, np.eye(m, dtype=np.int8)), axis=1)
    return H

def calculate_crc(vhod: list) -> str:
    crc = np.array([1, 1, 1, 1, 1, 1, 1, 1])
    polinome = np.array([1, 0, 0, 1, 1, 0, 1, 1])
    for i, b in enumerate(vhod):
        r = (crc[0]+b) % 2
        crc = np.append(crc, r)
        crc = crc[1:9]
        if r == 1:
            crc = np.bitwise_xor(crc, polinome)
            crc[7] = r

    crc = ''.join(str(c) for c in crc.tolist())
    return hex(int(crc, 2))[2:]

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

    m = int(np.log2(n))
    n_H = n - 1
    k = n_H - m
    H = generate_H(n_H, m)


    y = np.reshape(vhod, (len(vhod)//n, n))
    s = y[:,:-1] @ np.transpose(H) % 2
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
    izhod = y[:,:k].reshape(-1)

    crc = calculate_crc(vhod)

    return (izhod, crc)