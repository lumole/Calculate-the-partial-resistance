import numpy as np
import tkinter as tk
from tkinter import ttk
 
def get_standard_resistors(series):
    base_values = {
        'E24': np.array([1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]),
        'E48': np.array([1.00, 1.05, 1.10, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54, 1.62, 1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.90, 6.19, 6.49, 6.81, 7.15, 7.50, 7.87, 8.25, 8.66, 9.09, 9.53]),
        'E96': np.array([1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54, 1.58, 1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.00, 2.05, 2.10, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.80, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24, 3.32, 3.40, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49, 5.62, 5.76, 5.90, 6.04, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32, 7.50, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76]),
        'E192': np.array([1.00, 1.01, 1.02, 1.03, 1.05, 1.06, 1.07, 1.08, 1.10, 1.11, 1.12, 1.13, 1.15, 1.16, 1.18, 1.19, 1.21, 1.22, 1.24, 1.25, 1.27, 1.29, 1.30, 1.32, 1.33, 1.35, 1.37, 1.38, 1.40, 1.42, 1.43, 1.45, 1.47, 1.49, 1.50, 1.52, 1.54, 1.56, 1.58, 1.60, 1.62, 1.64, 1.65, 1.67, 1.69, 1.71, 1.74, 1.76, 1.78, 1.80, 1.82, 1.84, 1.86, 1.88, 1.91, 1.93, 1.95, 1.97, 2.00, 2.02, 2.04, 2.06, 2.09, 2.11, 2.13, 2.16, 2.18, 2.21, 2.23, 2.25, 2.28, 2.30, 2.32, 2.35, 2.37, 2.40, 2.43, 2.45, 2.48, 2.50, 2.53, 2.55, 2.58, 2.61, 2.63, 2.66, 2.69, 2.71, 2.74, 2.77, 2.80, 2.82, 2.85, 2.88, 2.91, 2.94, 2.97, 3.00, 3.02, 3.05, 3.08, 3.11, 3.14, 3.17, 3.20, 3.23, 3.26, 3.29, 3.32, 3.35, 3.38, 3.41, 3.44, 3.48, 3.51, 3.54, 3.57, 3.60, 3.64, 3.67, 3.70, 3.73, 3.76, 3.80, 3.83, 3.86, 3.90, 3.93, 3.96, 4.00, 4.03, 4.06, 4.10, 4.13, 4.17, 4.20, 4.23, 4.27, 4.30, 4.34, 4.37, 4.41, 4.44, 4.48, 4.52, 4.55, 4.59, 4.62, 4.66, 4.70, 4.73, 4.77, 4.81, 4.84, 4.88, 4.92, 4.96, 5.00, 5.03, 5.07, 5.11, 5.15, 5.19, 5.23, 5.27, 5.30, 5.34, 5.38, 5.42, 5.46, 5.50, 5.54, 5.58, 5.62, 5.66, 5.70, 5.74, 5.78, 5.82, 5.86, 5.90, 5.94, 5.98, 6.02, 6.06, 6.10, 6.14, 6.19, 6.23, 6.27, 6.31, 6.35, 6.40, 6.44, 6.48, 6.52, 6.56, 6.61, 6.65, 6.69, 6.74, 6.78, 6.82, 6.87, 6.91, 6.95, 7.00, 7.04, 7.08, 7.13, 7.17, 7.22, 7.26, 7.30, 7.35, 7.39, 7.44, 7.48, 7.53, 7.57, 7.62, 7.66, 7.71, 7.75, 7.80, 7.84, 7.89, 7.94, 7.98, 8.03, 8.07, 8.12, 8.17, 8.21, 8.26, 8.31, 8.35, 8.40, 8.45, 8.49, 8.54, 8.59, 8.64, 8.68, 8.73, 8.78, 8.83, 8.88, 8.92, 8.97, 9.02, 9.07, 9.12, 9.17, 9.22, 9.27, 9.31, 9.36, 9.41, 9.46, 9.51, 9.56, 9.61, 9.66, 9.71, 9.76, 9.81, 9.86, 9.91, 9.96])
    }
    
    multipliers = np.array([10**i for i in range(0, 7)])
    values = np.outer(base_values[series], multipliers).flatten()
    tolerance = {
        'E24': 0.05,
        'E48': 0.02,
        'E96': 0.01,
        'E192': 0.005
    }
    
    return values, tolerance[series]
 
def calculate_resistor_values(Vref, Vout, series, error_tolerance=0.01):
    standard_resistors, resistor_tolerance = get_standard_resistors(series)
    results = []
 
    for R1 in standard_resistors:
        for R2 in standard_resistors:
            R1_min = R1 * (1 - resistor_tolerance)
            R1_max = R1 * (1 + resistor_tolerance)
            R2_min = R2 * (1 - resistor_tolerance)
            R2_max = R2 * (1 + resistor_tolerance)
 
            Vout_nominal = Vref * (1 + (R2 / R1))
            Vout_min = Vref * (1 + (R2_min / R1_max))
            Vout_max = Vref * (1 + (R2_max / R1_min))
 
            nominal_error = abs(Vout_nominal - Vout) / Vout
            min_error = abs(Vout_min - Vout) / Vout
            max_error = abs(Vout_max - Vout) / Vout
 
            if nominal_error < error_tolerance:
                results.append((R1, R2, nominal_error, min_error, max_error))
 
    results.sort(key=lambda x: x[2])
    
    # Filter out results with the same ratios but different magnitudes
    filtered_results = []
    seen_ratios = set()
    for result in results:
        R1, R2, nominal_error, min_error, max_error = result
        ratio = R2 / R1
        if ratio not in seen_ratios:
            seen_ratios.add(ratio)
            filtered_results.append(result)
 
    return filtered_results
 
def calculate_and_display():
    try:
        Vref = float(entry_vref.get())
        Vout = float(entry_vout.get())
        error_tolerance = float(entry_error_tolerance.get()) / 100
        series = series_var.get()
 
        results = calculate_resistor_values(Vref, Vout, series, error_tolerance)
 
        for row in tree.get_children():
            tree.delete(row)
        
        for result in results:
            R1, R2, nominal_error, min_error, max_error = result
            tree.insert("", "end", values=(f"{R1:.2f}K", f"{R2:.2f}K", f"{nominal_error*100:.2f}%", f"{min_error*100:.2f}%", f"{max_error*100:.2f}%"))
    except ValueError:
        for row in tree.get_children():
            tree.delete(row)
        tree.insert("", "end", values=("Invalid input", "", "", "", ""))
 
# GUI Setup
root = tk.Tk()
root.title("Voltage Divider Calculator")
 
# Configure grid layout to be resizable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
 
# Input Frame
input_frame = ttk.LabelFrame(root, text="Input Parameters")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
 
input_frame.grid_rowconfigure(4, weight=1)
input_frame.grid_columnconfigure(1, weight=1)
 
ttk.Label(input_frame, text="Vref (V):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_vref = ttk.Entry(input_frame)
entry_vref.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
 
ttk.Label(input_frame, text="Vout (V):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_vout = ttk.Entry(input_frame)
entry_vout.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
 
ttk.Label(input_frame, text="Output Error Tolerance (%):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_error_tolerance = ttk.Entry(input_frame)
entry_error_tolerance.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
 
ttk.Label(input_frame, text="Resistor Series:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
series_var = tk.StringVar()
series_combobox = ttk.Combobox(input_frame, textvariable=series_var)
series_combobox['values'] = ('E24', 'E48', 'E96', 'E192')
series_combobox.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
series_combobox.current(2)  # Default to E96
 
calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)
 
# Result Frame
result_frame = ttk.LabelFrame(root, text="Results")
result_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
 
result_frame.grid_rowconfigure(0, weight=1)
result_frame.grid_columnconfigure(0, weight=1)
 
columns = ("R1", "R2", "Nominal Error", "Min Error", "Max Error")
tree = ttk.Treeview(result_frame, columns=columns, show="headings")
tree.heading("R1", text="R1 (KΩ)")
tree.heading("R2", text="R2 (KΩ)")
tree.heading("Nominal Error", text="Nominal Error (%)")
tree.heading("Min Error", text="Min Error (%)")
tree.heading("Max Error", text="Max Error (%)")
tree.grid(row=0, column=0, sticky="nsew")
 
# Add a scrollbar
scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')
 
# Run the GUI event loop
root.mainloop()