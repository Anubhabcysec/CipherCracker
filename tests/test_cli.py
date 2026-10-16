import subprocess
import sys


def run(*args, stdin=None):
    return subprocess.run(
        [sys.executable, "-m", "ciphercracker", *args],
        input=stdin, capture_output=True, text=True,
    )


def test_positional_argument():
    r = run("Kpkkf pz OLYL!")
    assert r.returncode == 0
    assert len(r.stdout.strip().splitlines()) == 26
    assert "Diddy is HERE!" in r.stdout


def test_stdin():
    r = run(stdin="Kpkkf pz OLYL!")
    assert r.returncode == 0
    assert "Diddy is HERE!" in r.stdout


def test_empty_input_errors():
    r = run(stdin="")
    assert r.returncode == 1
    assert "no ciphertext" in r.stderr