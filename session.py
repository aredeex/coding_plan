#!/usr/bin/env python3
"""
Show one session at a time from your coding plan.

Usage:
  python session.py        — resume where you left off
  python session.py 15     — jump to a specific session
"""
import os
import re
import sys
import urllib.request

PLAN_URL = "https://raw.githubusercontent.com/aredeex/coding_plan/main/.coding_plan.md"
SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".current_session")


def fetch_plan():
    try:
        with urllib.request.urlopen(PLAN_URL) as r:
            return r.read().decode("utf-8")
    except Exception:
        local = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".coding_plan.md")
        if os.path.exists(local):
            print("(offline — using local copy)\n")
            return open(local).read()
        raise SystemExit("Couldn't fetch the plan and no local copy found.")


def parse_sessions(content):
    sessions = {}
    current_num = None
    current_lines = []

    for line in content.splitlines():
        m = re.match(r"\*\*Session (\d+)", line)
        if m:
            if current_num is not None:
                sessions[current_num] = "\n".join(current_lines).rstrip()
            current_num = int(m.group(1))
            current_lines = [line]
        elif current_num is not None:
            if line.startswith("---") or re.match(r"^#{1,3} ", line):
                sessions[current_num] = "\n".join(current_lines).rstrip()
                current_num = None
                current_lines = []
            else:
                current_lines.append(line)

    if current_num is not None:
        sessions[current_num] = "\n".join(current_lines).rstrip()

    return sessions


def render(text):
    # Links: keep label, put URL in parens after
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", text)
    # Strip bold/italic markers
    text = text.replace("**", "")
    text = re.sub(r"\*([^*\n]+)\*", r"\1", text)
    # Blockquotes: indent slightly
    text = re.sub(r"^> ?", "  ", text, flags=re.MULTILINE)
    # Inline code: strip backticks, keep content
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text


def load_saved():
    try:
        return int(open(SAVE_FILE).read().strip())
    except Exception:
        return None


def save(n):
    with open(SAVE_FILE, "w") as f:
        f.write(str(n))


def main():
    sessions = parse_sessions(fetch_plan())
    total = max(sessions)

    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            raise SystemExit("Usage: python session.py [session number]")
    else:
        saved = load_saved()
        if saved:
            ans = input(f"Last session: {saved}. Press Enter to continue, or type a number: ").strip()
            n = int(ans) if ans else saved
        else:
            ans = input(f"Which session would you like to start with? (1-{total}): ").strip()
            n = int(ans)

    if n not in sessions:
        raise SystemExit(f"Session {n} not found. Valid range: 1-{total}.")

    save(n)

    width = 64
    print()
    print("=" * width)
    print()
    print(render(sessions[n]))
    print()
    print(f"  Session {n} of {total}")
    print()
    print("=" * width)
    print()


if __name__ == "__main__":
    main()
