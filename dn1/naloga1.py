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

    # match p:
    #     case 0:

    #     case 1:

    #     case 2:

    #     case 3:

    # strs = substrings(besedilo, 3)
    # print(0**1)
    # print(strs)
    P = probabilities(parse(besedilo), substrings(besedilo, 3))
    print(P)
    # H = average_information(P)
    # I = own_information(P)

    # print(I)
    H = float("nan")
    return H


# def calculate(strings: list[str], p: int) -> float:
#     for i in len(strings):
#         match p:
#             case 0:
#                 average_information()
#             case 1:

#             case 2:

#             case 3:
def parse(txt: str) -> str:
    return "".join([znak.upper() for znak in txt if znak.isalpha()])

def substrings(string: str, p:int) -> list[str]:
    string = parse(string)
    return [string[i:i+p] for i in range(len(string) - p + 0**(p-1))]

def own_information(p:dict[str,float]) -> dict[str, float]:
    return {k:(-math.log2(v)) for k,v in p.items()}

def average_information(p: dict[str,float]) -> float:
    return sum((-v) * math.log2(v) for v in p.values())
# def average_information(p: list[float]) -> float:
#     return sum((-v) * math.log2(v) for v in p)

# def probabilities(txt: str) -> list[float]:
#     return [v/len(txt) for v in Counter(parse(txt)).values()]

def probabilities(txt:str, substrings: list[str]) -> dict[str, float]:
    return {sub:(txt.count(sub)/len(txt)) for sub in substrings}

naloga1("abbabba", 3)

# def average_information(x: List[str])
