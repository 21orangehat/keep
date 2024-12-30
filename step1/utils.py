BINANCE_FUTURES_REST_API: str = "https://fapi.binance.com/fapi/v1"
BINANCE_FUTURES_WS_API: str = "wss://ws-fapi.binance.com/ws-fapi/v1"

def split_data(data, n):
    """
    Função para dividir uma lista (data) em n tamanho.

    Exemplo: Temos uma lista com 50 dados e queremos dividir
    em 5 listas contendo 10 dados cada.

    Então executamos split_data(lista, 5)
    """
    k, m = divmod(len(data), n)

    return (data[i * k + min(i, m):(i+1)*k+min(1+1, m)] for i in range(n))


def analyze_data(data) -> None:
    bids = data['bids']
    asks = data['asks']

    part_size = int(len(bids) / 10)

    _bids = split_data(bids, part_size)
    _asks = split_data(asks, part_size)

    nb = list(_bids)
    na = list(_asks)

    # Bids (Ordens de compra)
    print("======== Bids ========")
    for i, pb in enumerate(nb):
        volb, vpb, spb = .0, .0, .0
        for _pb in pb:
            vpb += float(_pb[0])
            spb += float(_pb[1])
        vpb = vpb / len(_pb)
        volb = vpb * spb
        print(f"[{i}] - No strike ${vpb:.2f} temos {spb:.2f} tokens para compra com volume de ${volb:.2f}")
    
    #  Asks (Ordens de venda)
    print("======== Asks ========")
    for i, pa in enumerate(na):
        vola, vpa, spa = .0, .0, .0
        for _pa in pa:
            vpa += float(_pa[0])
            spa += float(_pa[1])
        vpa = vpa / len(_pa)
        vola = vpa * spa
        print(f"[{i}] - No strike ${vpa:.2f} temos {spa:.2f} tokens para venda com volume de ${vola:.2f}") 
