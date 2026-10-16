from ciphercracker.ciphers.caesar import brute_force, shift_text


def test_known_answer():
    assert shift_text("Kpkkf pz OLYL!", -7) == "Diddy is HERE!"


def test_round_trip():
    assert shift_text(shift_text("Hello, World!", 5), -5) == "Hello, World!"


def test_negative_and_large_shifts():
    assert shift_text("abc", -1) == "zab"
    assert shift_text("abc", 26) == "abc"
    assert shift_text("abc", 29) == "def"


def test_empty_and_no_letters():
    assert shift_text("", 3) == ""
    assert shift_text("123 !?", 3) == "123 !?"


def test_non_ascii_untouched():
    assert shift_text("Caf\u00e9 123!", 3) == "Fdi\u00e9 123!"


def test_brute_force_returns_26_and_contains_answer():
    results = brute_force("Kpkkf pz OLYL!")
    assert len(results) == 26
    assert (7, "Diddy is HERE!") in results