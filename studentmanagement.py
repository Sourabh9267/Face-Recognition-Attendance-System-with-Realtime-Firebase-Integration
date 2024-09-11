import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
import pandas as pd
import datetime
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitonattendance-default-rtdb.firebaseio.com/"
})

# Firebase reference
ref = db.reference('Students')


class StudentDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM GUI")
        self.root.geometry("900x600")

        # Create UI Elements
        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        # Heading
        heading = tk.Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM GUI", font=("Arial", 16))
        heading.pack(pady=10)

        # Data Table
        self.tree = ttk.Treeview(self.root, columns=(
        "name", "id", "branch", "attendance", "total_attendance", "last_attendance_time"), show='headings')
        self.tree.heading("name", text="NAME")
        self.tree.heading("id", text="ID")
        self.tree.heading("branch", text="BRANCH")
        self.tree.heading("attendance", text="ATTENDANCE")
        self.tree.heading("total_attendance", text="TOTAL_ATTENDANCE")
        self.tree.heading("last_attendance_time", text="LAST_ATTENDANCE")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Entry Fields
        self.fields_frame = tk.Frame(self.root)
        self.fields_frame.pack(pady=10)

        self.id_label = tk.Label(self.fields_frame, text="ID")
        self.id_label.grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(self.fields_frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.name_label = tk.Label(self.fields_frame, text="Name")
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.fields_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.branch_label = tk.Label(self.fields_frame, text="Branch")
        self.branch_label.grid(row=2, column=0, padx=5, pady=5)
        self.branch_entry = tk.Entry(self.fields_frame)
        self.branch_entry.grid(row=2, column=1, padx=5, pady=5)

        self.attendance_label = tk.Label(self.fields_frame, text="Attendance")
        self.attendance_label.grid(row=3, column=0, padx=5, pady=5)
        self.attendance_var = tk.StringVar()
        self.attendance_menu = tk.OptionMenu(self.fields_frame, self.attendance_var, "A", "P", "E")
        self.attendance_menu.grid(row=3, column=1, padx=5, pady=5)

        self.total_attendance_label = tk.Label(self.fields_frame, text="Total Attendance")
        self.total_attendance_label.grid(row=4, column=0, padx=5, pady=5)
        self.total_attendance_entry = tk.Entry(self.fields_frame)
        self.total_attendance_entry.grid(row=4, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.remove_button = tk.Button(self.root, text="Remove Student", command=self.remove_student)
        self.remove_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.update_button = tk.Button(self.root, text="Update Student", command=self.update_student)
        self.update_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.export_button = tk.Button(self.root, text="Export to Excel", command=self.export_to_excel)
        self.export_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.reset_button = tk.Button(self.root, text="Reset Fields", command=self.reset_fields)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Bind treeview selection event
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

    def fetch_data(self):
        try:
            data = ref.get()
            if not data:
                return pd.DataFrame(
                    columns=["name", "id", "branch", "attendance", "total_attendance", "last_attendance_time"])

            # Convert the data to DataFrame
            if isinstance(data, dict):
                df = pd.DataFrame.from_dict(data, orient='index')
                # Ensure columns are in the correct order
                required_columns = ["name", "id", "branch", "attendance", "total_attendance", "last_attendance_time"]
                df = df.reindex(columns=required_columns)
                df.columns = ["name", "id", "branch", "attendance", "total_attendance", "last_attendance_time"]
                return df
            else:
                raise ValueError("Data fetched from Firebase is not in expected format")
        except Exception as e:
            print(f"Error converting data to DataFrame: {e}")
            return pd.DataFrame(
                columns=["name", "id", "branch", "attendance", "total_attendance", "last_attendance_time"])

    def populate_table(self):
        self.df = self.fetch_data()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for index, row in self.df.iterrows():
            self.tree.insert("", tk.END, values=row.tolist())

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        item = self.tree.item(selected_item[0])
        values = item['values']

        # Populate fields with selected student data
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.branch_entry.delete(0, tk.END)
        self.attendance_var.set("")
        self.total_attendance_entry.delete(0, tk.END)

        self.id_entry.insert(0, values[1])
        self.name_entry.insert(0, values[0])
        self.branch_entry.insert(0, values[2])
        self.attendance_var.set(values[3])
        self.total_attendance_entry.insert(0, values[4])

    def add_student(self):
        student_id = self.id_entry.get()
        name = self.name_entry.get()
        branch = self.branch_entry.get()
        attendance = self.attendance_var.get()
        total_attendance = self.total_attendance_entry.get()

        if not student_id or not name or not branch:
            messagebox.showerror("Error", "ID, Name, and Branch are required")
            return

        last_attendance_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") if attendance in ["P",
                                                                                                       "E"] else "2024-01-01 00:00:00"

        student_data = {
            "name": name,
            "id": student_id,
            "branch": branch,
            "attendance": attendance,
            "total_attendance": int(total_attendance) if total_attendance else 0,
            "last_attendance_time": last_attendance_time
        }

        ref.child(student_id).set(student_data)
        self.populate_table()

    def remove_student(self):
        student_id = self.id_entry.get()
        if not student_id:
            messagebox.showerror("Error", "ID is required")
            return

        ref.child(student_id).delete()
        self.populate_table()

    def update_student(self):
        student_id = self.id_entry.get()
        name = self.name_entry.get()
        branch = self.branch_entry.get()
        attendance = self.attendance_var.get()
        total_attendance = self.total_attendance_entry.get()

        if not student_id:
            messagebox.showerror("Error", "ID is required")
            return

        current_data = ref.child(student_id).get() or {}

        updated_data = {
            "name": name if name else current_data.get("name"),
            "id": student_id,
            "branch": branch if branch else current_data.get("branch"),
            "attendance": attendance if attendance else current_data.get("attendance"),
            "total_attendance": int(total_attendance) if total_attendance else current_data.get("total_attendance", 0),
            "last_attendance_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") if attendance in ["P",
                                                                                                            "E"] else current_data.get(
                "last_attendance_time")
        }

        ref.child(student_id).set(updated_data)
        self.populate_table()

    def export_to_excel(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if not file_path:
            return

        self.df.to_excel(file_path, index=False)

    def reset_fields(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.branch_entry.delete(0, tk.END)
        self.attendance_var.set("")
        self.total_attendance_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentDatabaseApp(root)
    root.mainloop()
