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
    besedilo = parse(besedilo)
    print(besedilo)
    match p:
        case 0:
            f0 = Counter(besedilo)
            p0 = { freq:(f0[freq]/len(besedilo)) for freq in f0 }
            H0 = { prob:-p0[prob]*math.log2(p0[prob]) for prob in p0 }
            print(sum(H0.values()))
            return H0
        case 1:
            # sub = zip(besedilo, besedilo[1:])
            H0 = naloga1(besedilo, 0)
            sub = [ "".join(s) for s in zip(besedilo, besedilo[1:]) ]
            f1 = {s:sub.count(s) for s in tuple(sub)}
            fsum = sum(f1.values())
            p1 = { freq:(f1[freq]/fsum) for freq in f1 }
            H1 = { prob:(-p1[prob]*math.log2(p1[prob]) - H0[prob[:1]]) for prob in p1 }
            print(sum(H1.values()))
            return H1
        case 2:

            # test = zip(besedilo, besedilo[1:], besedilo[2:]);
            # print(tuple(test))
            H1 = naloga1(besedilo, 1)
            sub = [ "".join(s) for s in zip(besedilo, besedilo[1:], besedilo[2:]) ]
            f2 = {s:sub.count(s) for s in tuple(sub)}
            fsum = sum(f2.values())
            p2 = { freq:(f2[freq]/fsum) for freq in f2 }
            H2 = { prob:(-p2[prob]*math.log2(p2[prob]) - H1[prob[:2]]) for prob in p2 }
            print(sum(H2.values()))
            return H2
        case 3:
            # test = zip(besedilo, besedilo[1:],besedilo[2:],besedilo[3:]);
            # print(tuple(test))
            H2 = naloga1(besedilo, 2)
            sub = [ "".join(s) for s in zip(besedilo, besedilo[1:],besedilo[2:],besedilo[3:]) ]
            f3 = {s:sub.count(s) for s in tuple(sub)}
            fsum = sum(f3.values())
            p3 = { freq:(f3[freq]/fsum) for freq in f3 }
            H3 = { prob:(-p3[prob]*math.log2(p3[prob]) - H2[prob[:3]]) for prob in p3 }
            print(sum(H3.values()))

    # strs = substrings(besedilo, 3)
    # print(0**1)
    # print(strs)
    # P = probabilities(parse(besedilo), substrings(besedilo, 3))
    # print(P)
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

# naloga1("abbabba", 0)
# naloga1("abbabba", 1)
# naloga1("abbabba", 2)
naloga1("AbB,a.bC", 1)

# def average_information(x: List[str])
