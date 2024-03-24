from collections import Counter
import math
def naloga1(besedilo: str, p: int) -> float:
    """ Izracun povprecne nedolocenosti na znak 

    Parameters
    ----------
    besedilo : str
        Vhodni niz
    p : int
        Stevilo poznanih predhodnih znakov: 0, 1, 2 ali 3.
        p = 0: H(X1)
            racunamo povprecno informacijo na znak abecede 
            brez poznanih predhodnih znakov
        p = 1: H(X2|X1)
            racunamo povprecno informacijo na znak abecede 
            pri enem poznanem predhodnemu znaku.
        p = 2: H(X3|X1,X2)
            racunamo povprecno informacijo na znak abecede 
            pri dveh poznanih predhodnih znakih.
        p = 3: H(X4|X1,X2,X3)
            racunamo povprecno informacijo na znak abecede 
            pri treh poznanih predhodnih znakih.

    Returns
    -------
    H : float 
        Povprecna informacija na znak abecede z upostevanjem 
        stevila poznanih predhodnih znakov 'p'. V bitih.
    """
    H = calc_H(parse(besedilo), p)
    return H

def calc_H(besedilo:str, p:int) -> float:
    Hprev = 0
    for i in range(p-1, p+1):
        sub = substrings(besedilo, i+1)
        f = Counter(sub)
        fsum = sum(f.values())
        p = { freq:(f[freq]/fsum) for freq in f }
        H = { prob:(-p[prob]*math.log2(p[prob])) for prob in p }
        Hprev = sum(H.values()) - Hprev
    return Hprev

def parse(txt: str) -> str:
    return "".join([znak.upper() for znak in txt if znak.isalpha()])

def substrings(besedilo: str, p:int) -> list[str]:
    return [besedilo[i:i+p] for i in range(len(besedilo)-p+1)]