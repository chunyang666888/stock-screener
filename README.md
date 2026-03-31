# stock-screener
![tests](https://github.com/chunyang666888/stock-screener/actions/workflows/ci.yml/badge.svg)


> A **composable factor screener** for equity selection — valuation, momentum, size and trend filters you combine with AND/OR, then rank survivors by a custom score. Ships with a sample A-share dataset so it runs offline immediately.

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](#running-tests)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)

## Why this repo exists

Stock selection is the bridge between "I have indicators" and "I have a book". Recruiters want to see you think in **factors and predicates**, not one-off `if` statements. This library models screening as composable, testable functions — the same pattern used in production alpha pipelines.

## Features

- Predicate factories: `pe_below`, `pb_below`, `market_cap_above`, `momentum_above`, `volume_above`, `ma_trend_is`.
- `Screener` combines predicates with logical **AND**, plus `any_of(...)` for **OR**.
- `rank(...)` sorts survivors by any scorer (e.g. momentum, or a blended factor).
- `SAMPLE_STOCKS`: 12 illustrative A-share snapshots — no network needed.
- Standard-library only.

## Installation

```bash
pip install -r requirements.txt
# or
pip install -e .
```

## Quick start

```python
from screener.dataset import SAMPLE_STOCKS
from screener.engine import Screener
from screener.filters import pe_below, momentum_above, ma_trend_is

screener = Screener([pe_below(25), momentum_above(3.0), ma_trend_is("up")])
survivors = screener.filter(SAMPLE_STOCKS)
ranked = screener.rank(survivors, lambda s: s.momentum_20d)
```

Run the bundled demo:

```bash
python examples/screen_demo.py
```

## Architecture

```
Factors (predicates) ──▶ Screener.filter (AND) ──▶ Survivors ──▶ rank(scorer)
                         Screener + any_of (OR) ──▶
```

| Module | Responsibility |
|--------|----------------|
| `dataset.py`   | `Stock` model + `SAMPLE_STOCKS` |
| `filters.py`   | Predicate factories |
| `engine.py`    | `Screener` (AND/OR) + `rank` |

## Extending

Add a factor in one line — it's just `Stock -> bool`:

```python
def low_debt_ratio(threshold):
    return lambda s: s.debt_ratio <= threshold
```

## Running tests

```bash
pytest -q
```

## Project structure

```
stock-screener/
├── screener/
│   ├── __init__.py
│   ├── dataset.py
│   ├── filters.py
│   └── engine.py
├── examples/
│   └── screen_demo.py
├── tests/
│   ├── test_filters.py
│   └── test_engine.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## License

MIT — free for personal and commercial use.
