from __future__ import annotations
from collections import Counter
from typing import List, Tuple, Sequence, Optional


def normalize_name(name: str) -> str:
    # TODO
    raise NotImplementedError


def top_k_frequent(items: Sequence[str], k: int) -> List[Tuple[str, int]]:
    # TODO
    raise NotImplementedError


def merge_intervals(intervals: Sequence[Tuple[int, int]]) -> List[Tuple[int, int]]:
    # TODO
    raise NotImplementedError


def connected_components(grid: Sequence[Sequence[int]]) -> int:
    # TODO
    raise NotImplementedError


class RunningStats:
    def __init__(self) -> None:
        # TODO
        raise NotImplementedError

    def add(self, x: float) -> None:
        # TODO
        raise NotImplementedError

    @property
    def count(self) -> int:
        # TODO
        raise NotImplementedError

    @property
    def mean(self) -> float:
        # TODO
        raise NotImplementedError

    @property
    def min(self) -> float:
        # TODO
        raise NotImplementedError

    @property
    def max(self) -> float:
        # TODO
        raise NotImplementedError
