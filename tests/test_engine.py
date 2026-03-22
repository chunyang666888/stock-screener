from screener.dataset import SAMPLE_STOCKS
from screener.engine import Screener, any_of
from screener.filters import pe_below, momentum_above, ma_trend_is, market_cap_above


def test_filter_applies_all_predicates():
    scr = Screener([pe_below(25), momentum_above(5.0), ma_trend_is("up")])
    results = scr.filter(SAMPLE_STOCKS)
    assert results  # non-empty
    for s in results:
        assert 0 < s.pe <= 25
        assert s.momentum_20d >= 5.0
        assert s.ma_trend == "up"


def test_rank_by_momentum():
    scr = Screener([market_cap_above(2000), ma_trend_is("up")])
    survivors = scr.filter(SAMPLE_STOCKS)
    ranked = scr.rank(survivors, lambda s: s.momentum_20d)
    assert ranked[0].momentum_20d >= ranked[-1].momentum_20d


def test_any_of_is_logical_or():
    pred = any_of([momentum_above(10.0), pe_below(6.0)])
    hits = [s for s in SAMPLE_STOCKS if pred(s)]
    assert any(s.momentum_20d >= 10.0 or 0 < s.pe <= 6.0 for s in hits)
