def get_profitability_pct(volume, open_price, oPCR, net_profit) -> str:
    denominator = volume * float(open_price) * float(oPCR or 1)
    if denominator == 0:
        return "0.00"
    value = (float(net_profit) / denominator) * 100
    return f"{value:.2f}" if value > 0 else f"{value:.2f}"


def test_get_profitability_pct():
    res = get_profitability_pct(volume=10, open_price=100, oPCR=1, net_profit=50)
    assert res == "+5.00"
