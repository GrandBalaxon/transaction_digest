import pytest

from src.processing import filter_by_state
from tests.conftest import transactions


@pytest.mark.parametrize("transactions_list, state, expected", [
    (transactions, "CANCELED", [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]),

])
def test_filter_by_state(transactions_list, state, expected):
    assert filter_by_state(transactions_list, state) == expected