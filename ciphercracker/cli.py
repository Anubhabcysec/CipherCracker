"""Command-line interface entry point for ciphercracker."""

import argparse
import sys

from ciphercracker.ciphers.caesar import brute_force


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        prog="ciphercracker",
        description="Analyze and crack classical ciphers.",
    )
    parser.add_argument(
        "text", nargs="?",
        help="ciphertext (or pipe it in, or omit to be prompted)",
    )
    return parser.parse_args(argv)


def read_input(args) -> str:
    """Get ciphertext from the argument, piped stdin, or an interactive prompt."""
    if args.text is not None:
        return args.text
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    try:
        return input("Enter ciphertext: ").strip()
    except EOFError:
        return ""


def main(argv=None) -> int:
    args = parse_args(argv)
    text = read_input(args)
    if not text.strip():
        print("Error: no ciphertext provided.", file=sys.stderr)
        return 1
    for shift, plain in brute_force(text):
        print(f"Shift {shift:02d}: {plain}")
    return 0


if __name__ == "__main__":
    sys.exit(main())