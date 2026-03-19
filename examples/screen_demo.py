"""Value + momentum screen over the bundled sample dataset (offline)."""
from screener.dataset import SAMPLE_STOCKS
from screener.engine import Screener
from screener.filters import (
    pe_below, pb_below, market_cap_above, momentum_above, ma_trend_is,
)


def main():
    screener = Screener([
        pe_below(25),          # cheap-ish earnings
        pb_below(5),           # reasonable price/book
        market_cap_above(2000),  # liquid, established names
        momentum_above(3.0),   # confirm uptrend
        ma_trend_is("up"),
    ])

    survivors = screener.filter(SAMPLE_STOCKS)
    print(f"Passed screen: {len(survivors)} / {len(SAMPLE_STOCKS)} stocks\n")

    ranked = screener.rank(survivors, lambda s: s.momentum_20d)
    print(f"{'代码':<8}{'名称':<8}{'PE':>6}{'PB':>6}{'市值(亿)':>10}{'20d动量%':>10}")
    for s in ranked:
        print(f"{s.code:<8}{s.name:<8}{s.pe:>6.1f}{s.pb:>6.1f}{s.market_cap:>10.0f}{s.momentum_20d:>10.1f}")


if __name__ == "__main__":
    main()
