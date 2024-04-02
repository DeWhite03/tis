def naloga2(vhod: list, nacin: int) -> tuple[list, float]:
    """
    Izvedemo kodiranje ali dekodiranje z algoritmom LZW.
    Zacetni slovar vsebuje vse 8-bitne vrednosti (0-255). 
    Najvecja dolzina slovarja je 4096.

    Parameters
    ----------
    vhod : list
        Seznam vhodnih znakov: bodisi znaki abecede
        (ko kodiramo) bodisi kodne zamenjave 
        (ko dekodiramo).
    nacin : int 
        Stevilo, ki doloca nacin delovanja: 
            0: kodiramo ali
            1: dekodiramo.

    Returns
    -------
    (izhod, R) : tuple[list, float]
        izhod : list
            Ce je nacin = 0: "izhod" je kodiran "vhod"
            Ce je nacin = 1: "izhod" je dekodiran "vhod"
        R : float
            Kompresijsko razmerje
    """

    match nacin:
        case 0:
            return encode(vhod)
        case 1:
            return decode(vhod)
    # code_dict = {chr(i):i for i in range(256)}
    # code_dict = {i:chr(i) for i in range(256)}
    # print(code_dict)
    # print(code_dict)
    # print(1 in code_dict)
    # print(1000 in code_dict)
    # print(encode(code_dict, vhod))
    # print(decode(vhod))
    izhod = []
    R = float('nan')
    return (izhod, R)

def encode(input_: list) -> tuple[list, float]:
    code_dict = {chr(i):i for i in range(256)}
    output = [];
    N = ""
    for c in input_:
        if(N+c in code_dict):
            N = N+c
        else:
            output.append(code_dict[N])
            if(len(code_dict) < 4096):
                code_dict[N+c] = len(code_dict)
            N = c;
    output.append(code_dict[N])
    return (output, (len(input_)*8)/(len(output) * 12))

def decode(input_: list) -> tuple[list, float]:
    code_dict = {i:chr(i) for i in range(256)}
    N = code_dict[input_[0]]
    output = [N]
    K = N
    for i in range(1, len(input_)):
        k = input_[i]
        if(k in code_dict):
            # output.append(code_dict[k]);
            N = code_dict[k]
        else:
            N = K+K[0]
        output.extend(list(map(lambda i:i, N)))
        code_dict[len(code_dict)] = K+N[0]
        K=N
    
    return (output, (len(output)*8)/(len(input_) * 12))
        
# print(naloga2([66, 82, 256, 82, 259, 82], 1))