"""Caesar cipher primitives."""

from __future__ import annotations


def shift_text(text: str, k: int) -> str:
    """Shift ASCII letters by k, preserving case.

    Only A-Z and a-z are shifted. Digits, punctuation and non-ASCII
    characters pass through untouched, so str.isalpha() is deliberately
    not used: it would treat accented letters as shiftable and corrupt them.
    """
    k %= 26
    out = []
    for ch in text:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + k) % 26 + 97))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + k) % 26 + 65))
        else:
            out.append(ch)
    return "".join(out)


def brute_force(ciphertext: str) -> list[tuple[int, str]]:
    """Return (shift, plaintext) for all 26 shifts.

    A shift of s means the text was encrypted by moving letters forward
    s places, so we decrypt by moving back s places.
    """
    return [(s, shift_text(ciphertext, -s)) for s in range(26)]