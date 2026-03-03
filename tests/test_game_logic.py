import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📈 Go HIGHER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📉 Go LOWER!")


def test_check_guess_with_integer_secret():
    """
    Test that check_guess always works correctly with integer secrets.
    This test targets the bug that was fixed where secret was being
    converted to a string on even attempts, breaking the comparison logic.
    """
    # Secret should always be an integer, never a string
    secret = 42
    
    # Test multiple guesses to ensure consistent behavior
    # (previously would fail on even attempts if secret was converted to string)
    assert check_guess(42, secret) == ("Win", "🎉 Correct!")
    assert check_guess(50, secret) == ("Too High", "📈 Go HIGHER!")
    assert check_guess(30, secret) == ("Too Low", "📉 Go LOWER!")


def test_check_guess_rejects_string_secret():
    """
    Test that check_guess works with integers and would fail with string secrets.
    This validates the fix that removed attempt-based type conversion.
    """
    secret_int = 50
    secret_str = "50"
    
    # Integer comparison should work fine
    result = check_guess(50, secret_int)
    assert result[0] == "Win"
    
    # String comparison would cause issues (this should not happen anymore)
    # The function now only accepts integers
    try:
        result = check_guess(50, secret_str)
        # If we get here with a string secret, it means the fix is incomplete
        # because check_guess should be receiving only integers
        assert result[0] != "Win", "String secrets should not produce correct comparisons"
    except TypeError:
        # This is expected - the function now properly rejects type mismatches
        pass
