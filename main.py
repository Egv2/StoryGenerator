import tkinter as tk
from tkinter import scrolledtext
from random import choice

def read_lines(url):
    """Read the lines from the file."""
    lines = []
    with open(url, encoding="utf8") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

class Datasets:
    """The datasets."""
    PART_ONE = {"WOMAN": read_lines("./datasets/part_one/woman.txt"),
                "MAN": read_lines("./datasets/part_one/man.txt")}
    PART_TWO = {"WOMAN": read_lines("./datasets/part_two/woman.txt"),
                "MAN": read_lines("./datasets/part_two/man.txt")}
    PART_THREE = {"WOMAN": read_lines("./datasets/part_three/woman.txt"),
                  "MAN": read_lines("./datasets/part_three/man.txt")}
    PART_FOUR = {"WOMAN": read_lines("./datasets/part_four/woman.txt"),
                 "MAN": read_lines("./datasets/part_four/man.txt")}
    NAMES = {"WOMAN": read_lines("./datasets/names/woman.txt"),
             "MAN": read_lines("./datasets/names/man.txt")}

def generate_story(gender=None):
    """Generates a homework story."""
    first_gender = gender if gender else choice(["MAN", "WOMAN"])
    first_name = choice(Datasets.NAMES[first_gender])
    first_line = f"{choice(Datasets.PART_ONE[first_gender])} {first_name}, {choice(Datasets.PART_TWO[first_gender])}."
    second_line = f"{choice(Datasets.PART_THREE[first_gender])} {first_name}, {choice(Datasets.PART_FOUR[first_gender])}"
    return first_line + " " + second_line


def update_story_text(gender=None):
    story = generate_story(gender)
    story_text.delete(1.0, tk.END)
    story_text.insert(tk.INSERT, story)

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(story_text.get("1.0", tk.END).strip())


window = tk.Tk()
window.title("Homework Story Generator")
window.geometry("500x350")


generate_man_button = tk.Button(window, text="Generate Man Story", command=lambda: update_story_text("MAN"))
generate_man_button.pack()

generate_woman_button = tk.Button(window, text="Generate Woman Story", command=lambda: update_story_text("WOMAN"))
generate_woman_button.pack()

generate_random_button = tk.Button(window, text="Generate Random Story", command=lambda: update_story_text())
generate_random_button.pack()

story_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=15)
story_text.pack()

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

window.mainloop()
