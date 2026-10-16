Project: ciphercracker, a classical-cipher cryptanalysis CLI.
Rules:
- Python 3.10+, standard library only in the package. matplotlib is allowed only inside eval/.
- Package name: ciphercracker. Layout: ciphers/, analysis/, scoring/, data/, cli.py.
- Dev environment is Windows PowerShell. Terminal output must work on Windows, and ANSI color must be switchable off.
- Type hints and docstrings on every public function. Docstrings explain WHY, not just what.
- Never claim a feature works unless there is a test for it.
- Do not implement scoring or confidence logic unless I explicitly ask. I write that myself.
- Small commits. After each task, summarize what changed and what I should test.
- Ask before adding any dependency or running pip.
- When creating files, use UTF-8 without a byte-order mark.