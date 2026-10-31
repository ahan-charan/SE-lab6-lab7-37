
import pytest
from tennis_scoring import game_score, set_winner, match_status


# GAME SCORE TESTS

def test_game_start():
    assert game_score(0, 0) == "0-0"


def test_normal_points():
    assert game_score(1, 2) == "15-30"


def test_game_score_40_30():
    assert game_score(3, 2) == "40-30"


def test_game_won_by_a():
    assert game_score(4, 2) == "game A"


def test_game_won_by_b():
    assert game_score(2, 4) == "game B"


def test_deuce():
    assert game_score(3, 3) == "deuce"


def test_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_advantage_b():
    assert game_score(3, 4) == "advantage B"


def test_game_won_after_deuce_a():
    assert game_score(5, 3) == "game A"


def test_game_won_after_deuce_b():
    assert game_score(3, 5) == "game B"


def test_negative_points():
    with pytest.raises(ValueError):
        game_score(-1, 0)


# SET WINNER TESTS

def test_set_undecided():
    assert set_winner(3, 2) is None


def test_set_won_by_a():
    assert set_winner(6, 4) == "A"


def test_set_won_by_b():
    assert set_winner(4, 6) == "B"


def test_set_tiebreak_a():
    assert set_winner(7, 6) == "A"


def test_set_tiebreak_b():
    assert set_winner(6, 7) == "B"


# MATCH STATUS TESTS

def test_match_a_wins():
    assert match_status(2, 0, 3) == "A wins"


def test_match_b_wins():
    assert match_status(0, 2, 3) == "B wins"


def test_match_decider():
    assert match_status(1, 1, 3) == "decider"


def test_match_in_progress():
    assert match_status(1, 0, 3) == "in progress"
