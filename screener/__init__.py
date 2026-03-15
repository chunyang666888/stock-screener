"""stock-screener — a composable factor screener for equity selection.

Define predicates (valuation, momentum, size, trend), combine them with AND/OR,
and rank survivors by a custom score. Ships with a sample A-share dataset so it
runs offline out of the box.
"""

from .dataset import Stock, SAMPLE_STOCKS
from .filters import (
    pe_below,
    pb_below,
    market_cap_above,
    momentum_above,
    volume_above,
    ma_trend_is,
)
from .engine import Screener

__all__ = [
    "Stock",
    "SAMPLE_STOCKS",
    "pe_below",
    "pb_below",
    "market_cap_above",
    "momentum_above",
    "volume_above",
    "ma_trend_is",
    "Screener",
]
