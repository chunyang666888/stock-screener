from screener.dataset import Stock
from screener.filters import (
    pe_below, pb_below, market_cap_above, momentum_above, volume_above, ma_trend_is,
)

S = Stock("X", "测试", 100.0, 10.0, 1.0, 5000.0, 5.0, 100000.0, "up")


def test_pe_below():
    assert pe_below(15)(S) is True
    assert pe_below(5)(S) is False
    assert pe_below(15)(Stock("Y", "亏", 1.0, -3.0, 1.0, 1.0, 0.0, 1.0, "up")) is False


def test_pb_below():
    assert pb_below(2)(S) is True
    assert pb_below(0.5)(S) is False


def test_market_cap_above():
    assert market_cap_above(1000)(S) is True
    assert market_cap_above(9000)(S) is False


def test_momentum_above():
    assert momentum_above(3)(S) is True
    assert momentum_above(10)(S) is False


def test_volume_above():
    assert volume_above(50000)(S) is True
    assert volume_above(200000)(S) is False


def test_ma_trend_is():
    assert ma_trend_is("up")(S) is True
    assert ma_trend_is("down")(S) is False
