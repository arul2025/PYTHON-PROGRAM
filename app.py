import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# --- 1️⃣ Define standard goals by age ---
AGE_GOALS = {
    "Children (4–8)": 1200,
    "Teens (9–13)": 1700,
    "Adults (14–64)": 2200,
    "Seniors (65+)": 1800
}

# --- App state variables ---
total_intake = 0
goal = 0

# --- 2️⃣ Main functions ---

def set_goal():
    """Set daily goal based on age group selection."""
    global goal, total_intake
    age = age_var.get()
    goal = AGE_GOALS[age]
    total_intake = 0
    update_display()

def log_water(amount):
    """Add water intake and update progress."""
    global total_intake
    if goal == 0:
        messagebox.showinfo("Info", "Select your age group first!")
        return
    total_intake += amount
    update_display()

def reset_day():
    """Reset daily data."""
    global total_intake
    if messagebox.askyesno("Reset", "Start a new day?"):
        total_intake = 0
        update_display()

def update_display():
    """Update progress bar, text, and messages."""
    if goal == 0:
        progress_label.config(text="Select age to begin.")
        return
    progress = min((total_intake / goal) * 100, 100)
    progress_bar["value"] = progress
    progress_label.config(text=f"You’ve reached {progress:.1f}% of your goal ({total_intake} ml / {goal} ml)")
    
    # Motivational messages
    if progress < 50:
        message.set("Let's keep going 💧")
    elif progress < 75:
        message.set("Great job! Keep sipping 🫗")
    elif progress < 100:
        message.set("Almost there! 💪")
    else:
        message.set("🎉 Goal achieved! Stay hydrated!")

# --- 3️⃣ Tkinter UI setup ---

root = tk.Tk()
root.title("WaterBuddy 💧")
root.geometry("400x400")
root.configure(bg="#E6F7FF")

# Age selection
tk.Label(root, text="Select your age group:", bg="#E6F7FF", font=("Arial", 12)).pack(pady=10)
age_var = tk.StringVar(value="Adults (14–64)")
tk.OptionMenu(root, age_var, *AGE_GOALS.keys()).pack()
tk.Button(root, text="Set Goal", command=set_goal, bg="#68C0E8", fg="white").pack(pady=5)

# Progress
progress_label = tk.Label(root, text="Select age to begin.", bg="#E6F7FF", font=("Arial", 10))
progress_label.pack(pady=10)

progress_bar = tk.ttk.Progressbar(root, length=300, mode="determinate")
progress_bar.pack(pady=5)

# Log buttons
tk.Button(root, text="+250 ml", command=lambda: log_water(250), bg="#4DB6AC", fg="white").pack(pady=5)
tk.Button(root, text="+500 ml", command=lambda: log_water(500), bg="#4DB6AC", fg="white").pack(pady=5)

# Motivational message
message = tk.StringVar()
tk.Label(root, textvariable=message, bg="#E6F7FF", font=("Arial", 11, "italic")).pack(pady=10)

# Reset button
tk.Button(root, text="Reset (New Day)", command=reset_day, bg="#FF8A65", fg="white").pack(pady=10)

root.mainloop()
