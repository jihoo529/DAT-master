import tkinter as tk
from tkinter import filedialog
from input_dat import DAT
from tkinter import messagebox
from process import Process

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DAT Editor")
        self.root.geometry('1200x600')
        # self.input_path = Noen
        self.setup_gui()
        self.first_check = True
        # Main frame
        
    
    def setup_gui(self):
        self.frame = tk.Frame(self.root, width=1000, height=600)
        self.frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Input file button
        input_file_btn = tk.Button(self.frame, text="Input file", command=self.open_file_dialog, width=10)
        input_file_btn.pack()

        # Checkboxes: Control Number checkbox and Field checkbox
        self.checkbox_frame = tk.Frame(self.frame)
        self.checkbox_frame.pack(fill=tk.X)
        
        self.control_number_var = tk.BooleanVar()
        self.field_var = tk.BooleanVar()

        self.control_number_checkbox = tk.Checkbutton(self.checkbox_frame, text="Control Number", variable=self.control_number_var, command=self.print_checkbox, state="disabled")
        self.row_range_frame = tk.Frame(self.checkbox_frame)
        self.field_checkbox = tk.Checkbutton(self.checkbox_frame, text="Field", variable=self.field_var, command=self.print_checkbox, state="disabled")

        self.control_number_checkbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.row_range_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.field_checkbox.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        self.additional_frame = tk.Frame(self.frame)
        self.additional_frame.pack(fill=tk.X)

        #add label
        self.label_frame = tk.Frame(self.checkbox_frame)
        self.control_number_label = tk.Label(self.label_frame, text="Additional Information")
        self.control_number_label.pack(side=tk.LEFT, padx=5)

        # Input text boxes frame for control number
        self.textbox_frame = tk.Frame(self.frame)
        self.textbox_frame.pack(fill=tk.BOTH)
        self.textbox_frame.grid_columnconfigure(0, weight=1)
        self.textbox_frame.grid_columnconfigure(1, weight=1)
        self.textbox_frame.grid_rowconfigure(0, weight=1)

        self.left_frame = tk.Frame(self.textbox_frame)
        self.right_frame = tk.Frame(self.textbox_frame)

        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        
        self.left_text = tk.Text(self.left_frame, state="normal", width=8, bg='lightgrey')
        self.left_text.tag_config("color", foreground="red")
        self.left_text.insert("1.0", "Please input DAT file to proceed", "color")
        self.left_text.config(state='disabled')
        self.left_text.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Row range
        self.max_rows = 0
        self.row_from_var = tk.StringVar()
        self.row_to_var = tk.StringVar()
        tk.Label(self.row_range_frame, text="Row # range:").pack(side=tk.LEFT, padx=(5, 2))
        self.entry1 = tk.Entry(self.row_range_frame, textvariable=self.row_from_var, width=6, state="disabled")
        self.entry1.pack(side=tk.LEFT)
        tk.Label(self.row_range_frame, text="~").pack(side=tk.LEFT, padx=2)
        self.entry2 = tk.Entry(self.row_range_frame, textvariable=self.row_to_var, width=6, state="disabled")
        self.entry2.pack(side=tk.LEFT)
        tk.Label(self.row_range_frame, text="Row data starts from #1 (excluding the header).\nBlank entries assume min/max row number.", fg='blue').pack(side=tk.LEFT, padx=(5,2))

        # Additional label for max rows
        self.label = tk.Label(self.additional_frame, text=f"Max # of rows: {self.max_rows}")
        self.label.pack(anchor='w', padx=300)

    
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(pady=10)

        self.process_btn = tk.Button(self.button_frame, text="Process to DAT", command=lambda: self.process_output('dat'), width=12, state='disabled')
        self.process_btn.pack(side=tk.LEFT, padx=5)

        self.process_csv_btn = tk.Button(self.button_frame, text="Process to CSV\n(tab delimeter)", command=lambda: self.process_output('csv'), width=12, state='disabled')
        self.process_csv_btn.pack(side=tk.LEFT, padx=5)


    
    def open_file_dialog(self):
        self.input_path = filedialog.askopenfilename(title="Select a file", filetypes=(("DAT files", "*.dat*"), ("All files", "*.*")))
        if self.input_path:
            print("Selected file:", self.input_path)
            self.reset_gui()
            self.read_file()
            

    def read_file(self):
        if self.input_path:
            self.control_number_checkbox.config(state=tk.ACTIVE)
            self.field_checkbox.config(state=tk.ACTIVE)
            self.left_text.config(state="normal")
            self.left_text.delete("1.0", 'end')
            self.left_text.tag_config("color", foreground="red")
            self.left_text.insert("1.0", "Check 'Control Number' to manually enter a control number.\nUncheck to specify a range of rows.\nIf unchecked and no range is specified, all fields and all rows will be processed.", "color")
            self.left_text.config(state='disabled')
            dat_reader = DAT(self.input_path)
            self.headers = dat_reader.read_headers()
            self.max_rows = dat_reader.count_lines()
            self.label.config(text=f'Max # of rows: {self.max_rows}')
            self.entry1.config(state="normal")
            self.entry2.config(state="normal")
            self.process_btn.config(state='normal')
            self.process_csv_btn.config(state='normal')
            print(f"Headers from the file: {self.headers}")
            self.populate_right_frame()
        else:
            print("No file selected yet.")
    
    def reset_gui(self):
        # Reset all interactive GUI elements to their default state
        self.control_number_checkbox.config(state="disabled")
        self.field_checkbox.config(state="disabled")
        self.left_text.config(state="normal")
        self.left_text.delete("1.0", 'end')
        self.left_text.insert("1.0", "Please input DAT file to proceed", "color")
        self.control_number_var.set(False)
        self.field_var.set(False)
        # self.left_text.config(state='disabled')
        # self.process_btn.config(state='disabled')
        self.first_check = True
        self.row_from = None
        self.row_to = None

        self.criteria = [False, False]
        self.scrollable_frame = None
        self.docIDs = ''
        self.headers = []
        self.checked_headers = []
        self.header_vars = {}
        # Add any other resets needed for entry fields or other components

    def print_checkbox(self):
        if self.control_number_var.get():
            self.criteria[0] = True
        else:
            self.criteria[0] = False
        if self.field_var.get():
            self.criteria[1] = True
        else:
            self.criteria[1] = False
        
        print(self.criteria)
        # self.checked_headers = []
        self.show_text_box()

    def disable_widgets_recursively(self, frame):
        """Recursively disable all widgets in the given frame."""
        for widget in frame.winfo_children():
            # Check if the widget itself contains other widgets (e.g., Frame, LabelFrame)
            if isinstance(widget, tk.Frame) or isinstance(widget, tk.LabelFrame):
                self.disable_widgets_recursively(widget)
            try:
                # Attempt to disable the widget
                widget.config(state='disabled')
            except tk.TclError:
                # Some widgets might not support the 'state' attribute
                print(f"Warning: {type(widget).__name__} does not support disabling.")

    def enable_widgets_recursively(self, frame):
        """Recursively disable all widgets in the given frame."""
        for widget in frame.winfo_children():
            # Check if the widget itself contains other widgets (e.g., Frame, LabelFrame)
            if isinstance(widget, tk.Frame) or isinstance(widget, tk.LabelFrame):
                self.enable_widgets_recursively(widget)
            try:
                # Attempt to disable the widget
                widget.config(state='normal')
            except tk.TclError:
                # Some widgets might not support the 'state' attribute
                print(f"Warning: {type(widget).__name__} does not support disabling.")

    def show_text_box(self):
        if self.left_text:
            self.left_text.config(state="disabled")
        if self.right_frame:
            self.disable_widgets_recursively(self.right_frame)
            self.disable_widgets_recursively(self.scrollable_frame)


        # Scenario handling based on criteria
        if self.criteria[0]==False:
            self.left_text.config(state="normal")
            self.left_text.config(bg='lightgrey')
            self.left_text.config(fg='grey')
            self.left_text.config(state="disabled")  # Disable again if needed
            self.entry1.config(state='normal')
            self.entry2.config(state='normal')
        if self.criteria[0]:
            # Show input text box on the left side of frame
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')
            self.entry1.config(state='disabled')
            self.entry2.config(state='disabled')
            self.left_text.config(state="normal")
            self.left_text.config(bg='white')
            self.left_text.config(fg='black')
            if self.first_check:
                self.left_text.delete("1.0", 'end')
                self.first_check = False
            # self.left_text.delete("1.0", 'end')
            
        if self.criteria[1]:
            self.enable_widgets_recursively(self.scrollable_frame)
            self.enable_widgets_recursively(self.right_frame)
        
        if not self.criteria[1]:
            self.select_all_headers()

    def check_row_range(self):
        if not self.row_from and not self.row_to:
            return True
        if (self.row_from and not self.row_to) or (not self.row_from and self.row_to):
            print("yes")
            return True
        try:
            # Attempt to convert both row_from and row_to to integers
            row_from_int = int(self.row_from)
            row_to_int = int(self.row_to)
            print("Conversion passed")
            
            # Check if row_to is greater than row_from
            if row_to_int >= row_from_int:
                print('Valid range')
                return True
            else:
                print('Invalid range: row_to must be greater than row_from')
        except (ValueError, TypeError):
            print('Conversion failed: inputs must be convertible to integers')
    
        return False
    
    def process_output(self, type):
        docIDs = ''
        
        self.row_from = self.row_from_var.get() if self.row_from_var.get() else None
        self.row_to = self.row_to_var.get() if self.row_to_var.get() else None
        row_correct = self.check_row_range()

        if row_correct == False:
            messagebox.showinfo("Error", "Range incorrect")
            return


        if self.criteria[0]:
            docIDs = self.left_text.get("1.0", tk.END).splitlines()
            print('docID', self.left_text.get("1.0", tk.END))
        output_path = filedialog.asksaveasfilename(
            title="Save as",  # Title of the save dialog window
            filetypes=((f"{type} files", f"*.{type}"), ("All files", "*.*")),  # File type filters
            defaultextension=f".{type}"  # Default file extension
        )
        process_parser = Process(type, self.input_path, self.headers, self.checked_headers, output_path, docIDs, self.row_from, self.row_to)
        process_parser.process()
        result = process_parser.write_file()
        if result:
            messagebox.showinfo("Success", f"{type} file written successfully\n({result-1} items)")
        else:
            messagebox.showinfo("Error", "Failed to write file")

        
    def populate_right_frame(self):
        # Create a Canvas and a Scrollbar within the right_frame
        self.right_frame.grid_rowconfigure(0, weight=0)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(1, weight=0)

        button_frame = tk.Frame(self.right_frame)
        button_frame.grid(row=0, column=0, sticky="ew", pady=5)
        select_all_btn = tk.Button(button_frame, text="Select All", command=self.select_all_headers)
        unselect_all_btn = tk.Button(button_frame, text="Uncheck All", command=self.uncheck_all_headers)
        
        unselect_all_btn.pack(side="right", padx=10, expand=True)
        select_all_btn.pack(side="right", padx=10, expand=True)

        canvas = tk.Canvas(self.right_frame, width=0)
        scrollbar = tk.Scrollbar(self.right_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)  # This Frame will hold your checkboxes

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Configure the canvas and scrollbar
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")  # Adjust the scroll region to encompass the inner frame
            )
        )

        canvas.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")
    
         # Bind mouse wheel to the canvas
        canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        canvas.bind_all("<Button-4>", lambda event: self.on_mousewheel(event, canvas, amount=1))
        canvas.bind_all("<Button-5>", lambda event: self.on_mousewheel(event, canvas, amount=-1))

        # Create a list of checkboxes for each header in the scrollable_frame
        for header in self.headers:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.scrollable_frame, text=header.strip('þ'), variable=var,
                                command=lambda h=header, v=var: self.update_checked_headers(h, v))
            chk.pack(anchor='w', padx=5, pady=2)
            self.header_vars[header] = var
        self.disable_widgets_recursively(self.right_frame)
        self.disable_widgets_recursively(self.scrollable_frame)
        self.select_all_headers()
            
    def on_mousewheel(self, event, canvas, amount=None):
        if event.num == 4 or event.delta > 0:  # Unix or Windows scroll up
            canvas.yview_scroll(-1 * (amount if amount else 1), "units")
        elif event.num == 5 or event.delta < 0:  # Unix or Windows scroll down
            canvas.yview_scroll(1 * (amount if amount else 1), "units")

    def select_all_headers(self):
        """Select all checkboxes."""
        for var in self.header_vars.values():
            var.set(True)
        self.update_checked_headers_list()

    def uncheck_all_headers(self):
        """Uncheck all checkboxes."""
        for var in self.header_vars.values():
            var.set(False)
        self.update_checked_headers_list()

    def update_checked_headers_list(self):
        """Update the list of checked headers based on the current state of checkboxes."""
        self.checked_headers.clear()
        for header, var in self.header_vars.items():
            if var.get():
                self.checked_headers.append(header)

    def update_checked_headers(self, header, var):
        """Update the list of checked headers based on checkbox state."""
        if var.get():
            if header not in self.checked_headers:
                self.checked_headers.append(header)
        else:
            if header in self.checked_headers:
                self.checked_headers.remove(header)

    def run(self):
        self.root.mainloop()
