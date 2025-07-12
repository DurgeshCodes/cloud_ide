import re


def clean_terminal_output(output_bytes):
    raw = output_bytes.decode(errors="ignore")
    # Strip ANSI escape sequences
    clean = re.sub(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])", "", raw)
    # Remove zsh prompt patterns like %{[red]%}
    clean = re.sub(r"%\{.*?%\}", "", clean)
    return clean
