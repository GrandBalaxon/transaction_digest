import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import transactions_stateless


@pytest.mark.parametrize("state, expected", [
    ("CANCELED", [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]),
    ("EXECUTED" ,[
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ])
])
def test_filter_by_state(transactions, state, expected):
    assert filter_by_state(transactions, state) == expected


def test_filter_by_state_empty():
    assert filter_by_state([]) == []


def test_filter_by_state_key_error(transactions_stateless):
    with pytest.raises(KeyError):
        assert filter_by_state(transactions_stateless)


def test_filter_by_state_none():
    with pytest.raises(TypeError):
        assert filter_by_state(None)


@pytest.mark.parametrize("descending, expected", [
    (True, [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"}
    ]),
    (False, [
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"}
    ])
])
def test_sort_by_date(transactions_stateless, descending, expected):
    assert sort_by_date(transactions_stateless, descending) == expected


def test_sort_by_date_with_repeats(transactions_stateless):
    transactions_repeated = transactions_stateless + transactions_stateless
    assert sort_by_date(transactions_repeated) == [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"}
    ]


