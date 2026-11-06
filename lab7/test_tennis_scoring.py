from hypothesis import given, strategies as st

from tennis_scoring import parse_score, game_lead, set_spread


# TEST 1: FUZZ PARSE_SCORE

@given(st.text() | st.none())
def test_parse_score_no_crash(s):
    result = parse_score(s)

    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and all(type(value) is int and value >= 0 for value in result)
    )


# TEST 2: FUZZ GAME_LEAD

@given(st.text() | st.none())
def test_game_lead_no_crash(s):
    result = game_lead(s)

    assert result is None or (
        type(result) is int and -3 <= result <= 3
    )


# TEST 3: FUZZ SET_SPREAD

@given(st.text() | st.none())
def test_set_spread_no_crash(s):
    result = set_spread(s)

    assert result is None or (
        type(result) is int and result >= 0
    )


# TEST 4: VALID PARSE_SCORE INPUTS

@given(
    a=st.integers(min_value=0, max_value=1000000),
    b=st.integers(min_value=0, max_value=1000000)
)
def test_parse_score_valid_inputs(a, b):
    assert parse_score(f"{a}-{b}") == (a, b)


# TEST 5: VALID GAME_LEAD INPUTS

@given(
    a=st.sampled_from(["0", "15", "30", "40"]),
    b=st.sampled_from(["0", "15", "30", "40"])
)
def test_game_lead_valid_inputs(a, b):
    values = {"0": 0, "15": 1, "30": 2, "40": 3}

    assert game_lead(f"{a}-{b}") == values[a] - values[b]


# TEST 6: VALID SET_SPREAD INPUTS

@given(
    scores=st.lists(
        st.integers(min_value=0, max_value=100000),
        min_size=1,
        max_size=30
    )
)
def test_set_spread_valid_inputs(scores):
    csv = ",".join(str(score) for score in scores)

    assert set_spread(csv) == max(scores) - min(scores)
