import pytest

from scp.utils import get_data_json, filter_data_by_state, sorted_data_by_date


def test_get_data_json():
    assert get_data_json("tests/test.json") == [{"state": "EXECUTED"}]


def test_get_data_json_error():
    with pytest.raises(FileNotFoundError):
        assert get_data_json("test1.json") == [{"state": "EXECUTED"}]


@pytest.mark.parametrize("data, state, result", ([[{'state': 'EXECUTED'}], 'EXECUTED', [{'state': 'EXECUTED'}]],
                                                 [[{'state': 'CANCELED'}], 'EXECUTED', []]))
def test_filter_data(data, state, result):
    assert list(filter_data_by_state(data, state)) == result


@pytest.mark.parametrize("data, state, result", ([[{"date": "2019-02-14T17:38:09.910336"},
                                                   {"date": "2018-05-05T01:38:56.538074"}],
                                                  'date',
                                                  [{"date": "2019-02-14T17:38:09.910336"},
                                                   {"date": "2018-05-05T01:38:56.538074"}]],

                                                 [[{"date": "2018-05-05T01:38:56.538074"},
                                                   {"date": "2019-02-14T17:38:09.910336"}],
                                                  'date',
                                                  [{"date": "2019-02-14T17:38:09.910336"},
                                                   {"date": "2018-05-05T01:38:56.538074"}]]))
def test_sorted_data(data, state, result):
    assert sorted_data_by_date(data, state) == result
