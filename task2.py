import tkinter as tk
from tkinter import messagebox

tasks = []

def detect_time_section(text):
    text = text.lower()
    if "today" in text or "now" in text:
        return "Today"
    elif "tmrw" in text or "tomorrow" in text:
        return "Tomorrow"
    elif "next week" in text:
        return "Next Week"
    else:
        return "Later"

def add_task():
    title = task_entry.get()
    priority = priority_var.get()

    if title == "":
        messagebox.showwarning("Error", "Task cannot be empty")
        return

    section = detect_time_section(title)

    tasks.append({
        "title": title,
        "priority": priority,
        "section": section
    })

    task_entry.delete(0, tk.END)
    messagebox.showinfo("Added", f"Task added to {section}")

def show_all():
    output.delete(1.0, tk.END)
    output.insert(tk.END, "--- ALL TASKS ---\n")

    for t in tasks:
        output.insert(
            tk.END,
            f"[{t['section']}] ({t['priority'].upper()}) - {t['title']}\n"
        )

def focus_mode():
    output.delete(1.0, tk.END)
    output.insert(tk.END, "--- FOCUS MODE (Today + High Priority) ---\n")

    for t in tasks:
        if t["section"] == "Today" or t["priority"] == "high":
            output.insert(
                tk.END,
                f"[{t['section']}] ({t['priority'].upper()}) - {t['title']}\n"
            )

# -------- UI SETUP --------

root = tk.Tk()
root.title("To-Do Formatter")
root.geometry("420x450")

tk.Label(root, text="Task Description").pack(pady=5)
task_entry = tk.Entry(root, width=45)
task_entry.pack(pady=5)

tk.Label(root, text="Priority").pack()
priority_var = tk.StringVar(value="normal")
tk.OptionMenu(root, priority_var, "high", "normal").pack(pady=5)

tk.Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)
tk.Button(root, text="Show All Tasks", width=20, command=show_all).pack(pady=5)
tk.Button(root, text="Focus Mode", width=20, command=focus_mode).pack(pady=5)

output = tk.Text(root, height=10, width=50)
output.pack(pady=10)

root.mainloop()
