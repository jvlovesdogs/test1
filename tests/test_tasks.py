import pytest

from src.tasks import (
    normalize_name,
    top_k_frequent,
    merge_intervals,
    connected_components,
    RunningStats,
)


def test_normalize_name():
    assert normalize_name("  Ada   Lovelace ") == "ada lovelace"
    assert normalize_name("") == ""
    assert normalize_name("A") == "a"


def test_top_k_frequent_basic():
    items = ["a", "b", "a", "c", "b", "a"]
    assert top_k_frequent(items, 2) == [("a", 3), ("b", 2)]


def test_top_k_frequent_ties():
    items = ["b", "a", "b", "a"]
    assert top_k_frequent(items, 2) == [("a", 2), ("b", 2)]


def test_top_k_frequent_k_edge():
    assert top_k_frequent(["x"], 0) == []
    assert top_k_frequent([], 3) == []


def test_merge_intervals_empty():
    assert merge_intervals([]) == []


def test_merge_intervals_touching_and_overlapping():
    assert merge_intervals([(1, 3), (3, 4)]) == [(1, 4)]
    assert merge_intervals([(5, 7), (1, 2), (2, 4)]) == [(1, 4), (5, 7)]


def test_connected_components_basic():
    grid = [
        [1, 0, 1],
        [1, 0, 0],
        [0, 1, 1],
    ]
    assert connected_components(grid) == 3


def test_connected_components_empty():
    assert connected_components([]) == 0
    assert connected_components([[]]) == 0


def test_connected_components_non_rectangular():
    with pytest.raises(ValueError):
        connected_components([[1, 0], [1]])


def test_running_stats_basic():
    rs = RunningStats()
    rs.add(1)
    rs.add(3)
    rs.add(2)
    assert rs.count == 3
    assert rs.mean == pytest.approx(2.0)
    assert rs.min == 1
    assert rs.max == 3


def test_running_stats_empty_raises():
    rs = RunningStats()
    with pytest.raises(ValueError):
        _ = rs.mean
    with pytest.raises(ValueError):
        _ = rs.min
    with pytest.raises(ValueError):
        _ = rs.max
