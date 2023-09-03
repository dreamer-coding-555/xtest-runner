#!/usr/bin/env python3
#
# Trilobite AppHub:
# author: Michael Gene Brockus (Dreamer)
# Gmail: <mail: michaelbrockus@gmail.com>
#
import tkinter as tk
from tkinter import scrolledtext
import subprocess
import os

class TestRunnerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.configure(bg="gray40")  # Set the background color of the app to gray40

        self.title("XTest Runner")
        self.geometry("600x400")
        self.resizable(False, False)  # Disable window resizing

        # Label at the top
        self.title_label = tk.Label(self, text="Trilobite XTest Runner - ", font=("Arial", 17, "bold"), bg="gray40", fg="blue")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")
        
        self.title_info = tk.Label(self, text="(The test runner GUI)", font=("Arial", 17, "bold"), bg="gray40", fg="dark blue")
        self.title_info.grid(row=0, column=1, columnspan=4, padx=10, pady=10, sticky="n")

        # Project Directory Input
        self.project_directory_label = tk.Label(self, text="Project Directory:", bg="gray40", fg="white", font=("Arial", 10, "bold"))
        self.project_directory_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.project_directory = tk.StringVar()
        self.project_directory_entry = tk.Entry(self, textvariable=self.project_directory, bg="white", width=80)
        self.project_directory_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky="ew")

        self.project_directory.set(os.getcwd())  # Auto-fill the project path with the current working directory

        # Output Text Area
        self.output_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=15, state=tk.DISABLED, bg="black", fg="light blue")
        self.output_text.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Button Frame
        self.button_frame = tk.Frame(self, bg="gray40")
        self.button_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        button_style = {'padx': 25, 'pady': 5, 'bg': 'gray', 'fg': 'white'}
        self.run_test_button = tk.Button(self.button_frame, text="Run XUnit Tests", command=self.run_tests, **button_style)
        self.run_test_button.grid(row=0, column=0, sticky="ew")

        self.run_benchmark_button = tk.Button(self.button_frame, text="Run Benchmarks", command=self.run_benchmarks, **button_style)
        self.run_benchmark_button.grid(row=0, column=1, sticky="ew")

        self.run_everything_button = tk.Button(self.button_frame, text="Run Everything", command=self.run_everything, **button_style)
        self.run_everything_button.grid(row=0, column=2, sticky="ew")

        self.clear_screen_button = tk.Button(self.button_frame, text="Clear Output Screen", command=self.clear_screen, **button_style)
        self.clear_screen_button.grid(row=0, column=3, sticky="ew")

    def write_to_output(self, text, color="light blue"):
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.insert(tk.END, text + "\n", color)
        self.output_text.configure(state=tk.DISABLED)
        self.output_text.see(tk.END)

    def clear_screen(self):
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.configure(state=tk.DISABLED)

    def run_tests(self, args=None):
        self.clear_screen()  # Clear the screen before running tests
        self.write_to_output("Running Tests...")
        self.run_command(['meson', 'test', '-C', f'{self.project_directory.get()}/builddir', '-v', '--test-args=--only-test'])
    
    def run_benchmarks(self, args=None):
        self.clear_screen()  # Clear the screen before running benchmarks
        self.write_to_output("Running Benchmarks...")
        self.run_command(['meson', 'test', '-C', f'{self.project_directory.get()}/builddir', '-v', '--test-args=--only-bench'])

    def run_everything(self):
        self.clear_screen()  # Clear the screen before running all
        self.write_to_output("Running Everything...")
        self.run_command(['meson', 'test', '-C', f'{self.project_directory.get()}/builddir', '-v', '--test-args=--run-both'])

    def run_command(self, command):
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True, cwd=self.project_directory.get())
            self.write_to_output(output)
        except subprocess.CalledProcessError as e:
            self.write_to_output(f"Error: {e.returncode}\n{e.output}", "red")

def greet():
    return "Hello, Python Developer"
# end of func
