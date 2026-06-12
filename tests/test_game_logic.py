from logic_utils import check_guess, update_score

# FIX: AI and I added regression tests around the hint and scoring changes so the
# baseline bugs stay visible if someone reintroduces them later.

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_win_score_depends_on_attempt_and_not_previous_penalties():
    assert update_score(current_score=-5, outcome="Win", attempt_number=2) == 80

def test_win_score_has_minimum_floor():
    assert update_score(current_score=-30, outcome="Win", attempt_number=12) == 10

def test_too_high_even_attempt_still_deducts_points():
    assert update_score(current_score=20, outcome="Too High", attempt_number=2) == 15
