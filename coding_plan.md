# Beginner Coding Crash Course

---

## Phase 0 — How Computers Think
*Goal: build a mental model before writing a single line of code.*

**Step 1.** Go to **[khanacademy.org](https://www.khanacademy.org)** and search for **"AP Computer Science Principles."** Inside that course, complete these two units only:
- "Computers and the Internet"
- "Algorithms"

These are videos and short exercises with no coding required. They explain *what a program actually is* and *how a computer follows instructions* — concepts that make everything else click faster.

**Step 2.** Go to **[cs50.harvard.edu/x](https://cs50.harvard.edu/x)** — that's the free, self-paced version of CS50's Introduction to Computer Science. Watch Lecture 0 and Lecture 1 only. The lectures are also on the **[CS50 YouTube channel](https://www.youtube.com/@cs50)** if you prefer watching there. Don't worry about doing any assignments — just watch. The instructor, David Malan, is one of the best in the world at explaining this stuff to beginners.

---

## Phase 1 — Write Your First Code
*Goal: learn the core building blocks of programming in a forgiving environment.*

**Step 1.** Go to **[khanacademy.org](https://www.khanacademy.org)** and search for **"Intro to JS: Drawing and Animation."** Start from the beginning and work through these units in order:
- "Drawing & Animation"
- "Programming Basics"

The canvas on the right updates live as you type, which makes it easy to see exactly what your code is doing. This is the best part of starting here.

**Step 2.** Stop when you finish the "Functions" unit. Don't go further into the JavaScript course — you've gotten what you need from it. The goal was to learn the *concepts*, not the language.

**Step 3.** By the end of this phase, you should be able to answer these questions in your own words:
- What is a variable?
- What does an `if` statement do?
- What is a loop and why would you use one?
- What is a function?

If those feel fuzzy, re-do the relevant unit before moving on.

---

## Phase 2 — Learn Python
*Goal: learn a clean, professional language used in real jobs, data science, and research.*

Python is the right language to go deep on. It has minimal punctuation clutter, reads almost like plain English, and is one of the most in-demand languages in the world.

**Step 1.** Go directly to the course page: **[MIT OCW 6.0001 — Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)**. Watch the lectures in order and take notes.

**Step 2.** After each lecture, open a Python environment and try to reproduce what was shown from scratch without looking. This is the most important habit to build.

> To run Python on your computer: download it from **[python.org](https://www.python.org)**. The installer includes **IDLE**, a simple built-in editor — open it from your Applications folder after installing. No account or extra setup needed.

**Step 3.** Do the problem sets. They're hard — that's the point. Sit with a problem for 20–30 minutes before looking anything up. That discomfort is where the learning actually happens.

**Step 4.** Alongside the MIT course, read the matching chapters of **Automate the Boring Stuff with Python**, free at **[automatetheboringstuff.com](https://automatetheboringstuff.com)**. It covers the same concepts but frames them around practical tasks like renaming files or reading spreadsheets, which helps when the MIT material feels abstract.

**Step 5.** By the end of this phase, you should be comfortable with:
- Variables and data types (strings, integers, lists, dictionaries)
- `if/else` statements and `for`/`while` loops
- Writing and calling your own functions
- Reading a Python error message and understanding what went wrong

---

## Phase 3 — Practice Problem-Solving
*Goal: make the concepts automatic by using them over and over in new situations.*

**Step 1.** Go to **[codingbat.com/python](https://codingbat.com/python)** and start with "Warmup-1," moving forward from there. These are small, focused problems — most take 5–15 minutes. Do one or two per day rather than cramming.

**Step 2.** When CodingBat starts feeling manageable, move to **[exercism.org](https://exercism.org)**. Create a free account, go to the Python track, and enable mentored mode. You'll submit solutions and get feedback from a real person on your style and approach — not just whether it works.

**Step 3.** Keep a running list of any problem type that stumps you more than once. Those are your weak spots, and they're worth drilling.

---

## Phase 4 — Build Something Real
*Goal: experience the full loop of having an idea, writing code to make it happen, and fixing it when it breaks.*

Pick **one** of these projects and finish it completely before moving on:

- **Quiz game** — the program asks multiple-choice questions, tracks the score, and prints a result at the end
- **Budget tracker** — the user can add income and expenses, and the program shows a running total
- **Personal automation** — a script that does something useful for your own life (rename a folder of files, pull data out of a spreadsheet, etc.)

Rules for this phase:
- Start with the simplest possible version that works, then add features one at a time
- When something breaks, read the error message first before googling
- The project doesn't have to be pretty — it has to be *finished*

---

## Phase 5 — Pick a Direction
*Goal: transition from "learning to code" to "coding to build something you care about."*

Take your time here. Look around, see what interests you, and follow that thread.

---

## What to Google When You're Stuck

This is a skill in itself. Knowing *how* to search is as important as knowing *what* to search.

**When you get an error message:**
Search the exact error text in quotes, plus the word `python`. Example:
> `"TypeError: can only concatenate str (not int) to str" python`

Don't paraphrase the error — copy it verbatim. Someone has almost certainly hit the exact same message.

**When you don't know how to do something:**
Use the pattern: `python how to [thing you want]`. Example:
> `python how to check if a number is even`
> `python how to loop through a list`

**When the docs feel too dense:**
Search the same topic with `"for beginners"` or `"simple example"` added. Example:
> `python dictionary simple example`

**When you want the authoritative answer:**
Go straight to **[docs.python.org/3](https://docs.python.org/3/)** — Python's official documentation. It's more readable than it looks. Use the search bar at the top.

**When a [Stack Overflow](https://stackoverflow.com) answer works but you don't understand why:**
Don't just copy it. Paste it into your file, then search for each piece of it you don't recognize. Understanding *why* it works is the rep.

**Terms worth knowing early (they'll come up constantly):**
- **[f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)** — a cleaner way to put variables inside text
- **[list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)** — a compact way to build lists
- **[try/except](https://docs.python.org/3/tutorial/errors.html)** — how to handle errors gracefully
- **[reading a stack trace](https://docs.python.org/3/library/traceback.html)** — how to interpret the error report Python gives you

**The golden rule:** if you've been stuck for more than 30 minutes and searches aren't helping, you're probably asking the wrong question. Step back and describe the problem out loud as if explaining it to someone else. Often that alone unsticks you — this is called [rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging), and it genuinely works.

---

## Three habits that matter more than any course

1. **Write code every day, even for 20 minutes.** Consistency beats marathon sessions.
2. **Type everything out by hand.** Copy-pasting code you don't understand yet is skipping the rep.
3. **Get comfortable being stuck.** Every professional developer spends most of their day debugging. It's not a sign you're doing it wrong.
