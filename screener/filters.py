"""Reusable filter predicates. Each factory returns a callable ``Stock -> bool``."""
from __future__ import annotations

from typing import Callable

from .dataset import Stock

Predicate = Callable[[Stock], bool]


def pe_below(threshold: float) -> Predicate:
    """Keep profitable stocks with P/E at or below ``threshold``."""

    def pred(s: Stock) -> bool:
        return 0 < s.pe <= threshold

    return pred


def pb_below(threshold: float) -> Predicate:
    def pred(s: Stock) -> bool:
        return 0 < s.pb <= threshold

    return pred


def market_cap_above(threshold: float) -> Predicate:
    """Keep stocks with market cap >= ``threshold`` (亿元)."""

    def pred(s: Stock) -> bool:
        return s.market_cap >= threshold

    return pred


def momentum_above(threshold_pct: float) -> Predicate:
    """Keep stocks whose 20-day momentum beats ``threshold_pct`` %."""

    def pred(s: Stock) -> bool:
        return s.momentum_20d >= threshold_pct

    return pred


def volume_above(threshold: float) -> Predicate:
    def pred(s: Stock) -> bool:
        return s.avg_volume >= threshold

    return pred


def ma_trend_is(direction: str) -> Predicate:
    """Keep stocks whose MA trend equals ``direction`` ('up'/'down'/'flat')."""

    def pred(s: Stock) -> bool:
        return s.ma_trend == direction

    return pred
