tkinter.py

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Set window title to LastName-ToDo
        self.title("Craig-ToDo")  # Change Craig to your last name
        self.geometry("300x400")

        # Menu bar with complementary colors
        menu_bar = tk.Menu(self, bg="#87CEEB", fg="black")  # Light Blue
        file_menu = tk.Menu(menu_bar, tearoff=0, bg="#FFA500", fg="black")  # Orange
        file_menu.add_command(label="Exit", command=self.quit_program)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

        # Canvas and scrollable frame
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.tasks_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="nw")

        # Task entry field
        self.task_create = tk.Entry(self.text_frame, width=30)
        self.task_create.pack(side=tk.LEFT, fill=tk.X)
        self.task_create.bind("<Return>", self.add_task)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Instruction label
        instructions = tk.Label(self, text="Right-click a task to delete it", font=("Arial", 10))
        instructions.pack(pady=5)

        # Load existing tasks if any
        for task in self.tasks:
            self.add_task_to_list(task)

        # Bind scrolling
        self.tasks_canvas.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)

    def add_task(self, event=None):
        task_text = self.task_create.get().strip()
        if len(task_text) > 0:
            self.add_task_to_list(task_text)
            self.task_create.delete(0, tk.END)

    def add_task_to_list(self, task_text):
        # Label for each task
        new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
        new_task.bind("<Button-3>", self.remove_task)  # Right-click to delete
        new_task.pack(side=tk.TOP, fill=tk.X)
        self.tasks.append(new_task)

    def remove_task(self, event):
        task = event.widget
        confirm = msg.askyesno("Really Delete?", f"Delete '{task.cget('text')}'?")
        if confirm:
            self.tasks.remove(task)
            task.destroy()

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def mouse_scroll(self, event):
        self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def quit_program(self):
        self.quit()


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
