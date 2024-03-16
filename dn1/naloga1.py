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

    

    H = average_information(probabilities(besedilo))
    return H

def parse(txt: str) -> str:
    return "".join([znak for znak in txt if znak.isalpha()]).upper()

def average_information(p: Dict[str,float]) -> float:
    return sum()
# def average_information(p: list[float]) -> float:
#     return sum((-v) * math.log2(v) for v in p)

# def probabilities(txt: str) -> list[float]:
#     return [v/len(txt) for v in Counter(parse(txt)).values()]

def probabilities(txt: str) -> Dict[str, float]:
    return {key:value for key,value in Counter(parse(txt)).values()}

naloga1("oaeuaaoeaaooehtns", 0)

# def average_information(x: List[str])
