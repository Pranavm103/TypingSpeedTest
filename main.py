import tkinter as tk
import random
import time

# Set up the GUI window
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x400")

# Define the sample text
sample_text = "The quick brown fox jumps over the lazy dog. " * 10

# Initialize the game state variables
current_word_index = 0
start_time = None
typing_speed = None

# Define the GUI elements
instructions_label = tk.Label(root, text="Type the words as fast as you can!")
instructions_label.pack(pady=10)

word_label = tk.Label(root, text="")
word_label.pack(pady=10)

entry_box = tk.Entry(root)
entry_box.pack()

feedback_label = tk.Label(root, text="")
feedback_label.pack(pady=10)

# Define the event handlers
def start_game():
    global current_word_index, start_time, typing_speed
    current_word_index = 0
    typing_speed = None
    start_time = time.time()
    update_word()

def update_word():
    global current_word_index
    word_list = sample_text.split()
    if current_word_index < len(word_list):
        word_label.config(text=word_list[current_word_index])
        current_word_index += 1
    else:
        end_game()

def check_word(event):
    global typing_speed
    typed_word = entry_box.get()
    word_list = sample_text.split()
    correct_word = word_list[current_word_index - 1]
    if typed_word == correct_word:
        entry_box.delete(0, tk.END)
        feedback_label.config(text="Correct!")
        if current_word_index == len(word_list):
            end_game()
        else:
            update_word()
    else:
        feedback_label.config(text="Incorrect.")
    if current_word_index == 1:
        typing_speed = None
    else:
        typing_speed = (current_word_index - 1) / (time.time() - start_time) * 60
        feedback_label.config(text=f"Typing speed: {typing_speed:.2f} wpm")
        if typing_speed > 100:
            feedback_label.config(fg="green")
        elif typing_speed > 40:
            feedback_label.config(fg="orange")
        else:
            feedback_label.config(fg="red")

def end_game():
    entry_box.delete(0, tk.END)
    word_label.config(text="Game Over!")
    feedback_label.config(text=f"Your typing speed was: {typing_speed:.2f} wpm")

# Bind the events to the event handlers
entry_box.bind("<Return>", check_word)

# Add a button to start the game
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

# Run the GUI
root.mainloop()
