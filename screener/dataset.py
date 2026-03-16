"""Stock snapshot model and a sample A-share dataset (offline demo data)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Stock:
    """A point-in-time snapshot of one listed stock."""

    code: str
    name: str
    price: float
    pe: float            # trailing P/E (<=0 means loss-making)
    pb: float            # price / book
    market_cap: float    # in 亿元 (100M CNY)
    momentum_20d: float  # % total return over the last 20 trading days
    avg_volume: float    # average daily turnover (手)
    ma_trend: str        # "up" | "down" | "flat"


# Sample dataset — illustrative only, not investment advice.
SAMPLE_STOCKS: List[Stock] = [
    Stock("600519", "贵州茅台", 1700.0, 32.1, 9.8, 21400, 6.2, 35000, "up"),
    Stock("000858", "五粮液", 145.0, 18.4, 4.2, 5600, 3.1, 120000, "up"),
    Stock("601318", "中国平安", 48.0, 8.6, 0.9, 8700, -2.4, 400000, "flat"),
    Stock("600036", "招商银行", 36.5, 6.2, 0.8, 9200, 1.8, 380000, "up"),
    Stock("300750", "宁德时代", 185.0, 22.7, 4.6, 8100, 9.5, 220000, "up"),
    Stock("002594", "比亚迪", 245.0, 21.3, 3.9, 7100, 7.8, 180000, "up"),
    Stock("600276", "恒瑞医药", 52.0, 41.5, 6.1, 3300, -5.1, 150000, "down"),
    Stock("000333", "美的集团", 68.0, 12.9, 2.6, 4700, 4.0, 160000, "up"),
    Stock("601012", "隆基绿能", 18.2, 11.2, 1.4, 1380, -12.3, 500000, "down"),
    Stock("688981", "中芯国际", 55.0, 95.0, 3.2, 4300, 5.6, 260000, "up"),
    Stock("000001", "平安银行", 11.2, 4.8, 0.5, 2170, 0.9, 700000, "flat"),
    Stock("300059", "东方财富", 14.5, 16.7, 2.1, 2280, 11.2, 900000, "up"),
]
