
import pytest
from tennis_scoring import game_score, set_winner, match_status


# GAME SCORE TESTS

def test_negative_a():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_negative_b():
    with pytest.raises(ValueError):
        game_score(0, -1)


def test_normal_score():
    assert game_score(1, 2) == "15-30"


def test_normal_score_other_side():
    assert game_score(2, 1) == "30-15"


def test_forty_thirty():
    assert game_score(3, 2) == "40-30"


def test_game_a_before_deuce():
    assert game_score(4, 2) == "game A"


def test_game_b_before_deuce():
    assert game_score(2, 4) == "game B"


def test_deuce():
    assert game_score(3, 3) == "deuce"


def test_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_advantage_b():
    assert game_score(3, 4) == "advantage B"


def test_game_a_after_deuce():
    assert game_score(5, 3) == "game A"


def test_game_b_after_deuce():
    assert game_score(3, 5) == "game B"


# SET WINNER TESTS

def test_set_a_wins_by_two():
    assert set_winner(6, 4) == "A"


def test_set_b_wins_by_two():
    assert set_winner(4, 6) == "B"


def test_set_a_not_enough_lead():
    assert set_winner(6, 5) is None


def test_set_b_not_enough_lead():
    assert set_winner(5, 6) is None


def test_set_a_tiebreak():
    assert set_winner(7, 6) == "A"


def test_set_b_tiebreak():
    assert set_winner(6, 7) == "B"


def test_set_equal_scores():
    assert set_winner(6, 6) is None


def test_set_both_seven():
    assert set_winner(7, 7) is None


# MATCH STATUS TESTS

def test_match_a_wins():
    assert match_status(2, 0, 3) == "A wins"


def test_match_b_wins():
    assert match_status(0, 2, 3) == "B wins"


def test_match_decider():
    assert match_status(1, 1, 3) == "decider"


def test_match_in_progress():
    assert match_status(0, 0, 3) == "in progress"


def test_match_in_progress_second_condition():
    assert match_status(1, 0, 3) == "in progress"


def test_match_decider_best_of_five():
    assert match_status(2, 2, 5) == "decider"
