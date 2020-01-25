import pytest

from imdb.core.metrics import tnr


@pytest.mark.parametrize(
    "y_true, y_pred, expected",
    (
        ([0, 0, 0, 1, 1, 1], [1, 1, 0, 0, 1, 1], 1 / 3),
        ([0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1], 1),
        ([0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], 0),
        ([1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1], 0),
    ),
)
def test_tnr(y_true, y_pred, expected):
    assert tnr(y_true, y_pred) == expected


def test_tnr_raise_warning_for_all_positives_and_no_fp():
    y_true, y_pred = [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]
    msg = (
        "TNR = 1, but no true negatives actually found. That's because ground "
        "truth contains no negatives"
    )
    with pytest.warns(Warning, match=msg):
        x = tnr(y_true, y_pred)
    assert x == 1
