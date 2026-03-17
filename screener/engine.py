"""The screener: combine predicates (AND/OR) and rank survivors."""
from __future__ import annotations

from typing import Callable, Iterable, List, Sequence

from .dataset import Stock
from .filters import Predicate

Scorer = Callable[[Stock], float]


class Screener:
    """Compose filters and rank stocks by a custom score."""

    def __init__(self, predicates: Sequence[Predicate] | None = None) -> None:
        self.predicates: List[Predicate] = list(predicates or [])

    def add(self, pred: Predicate) -> "Screener":
        self.predicates.append(pred)
        return self

    def filter(self, stocks: Iterable[Stock]) -> List[Stock]:
        """Return stocks passing ALL registered predicates (logical AND)."""
        return [s for s in stocks if all(p(s) for p in self.predicates)]

    def rank(self, stocks: Iterable[Stock], scorer: Scorer, reverse: bool = True) -> List[Stock]:
        """Return stocks sorted by ``scorer`` (highest first by default)."""
        return sorted(stocks, key=scorer, reverse=reverse)


def any_of(predicates: Sequence[Predicate]) -> Predicate:
    """Logical OR over predicates."""
    preds = list(predicates)

    def pred(s: Stock) -> bool:
        return any(p(s) for p in preds)

    return pred
