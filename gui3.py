import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Radar Data Processor (RDP) GUI")
root.geometry("600x400")
root.configure(bg='#f0f0f0')

# Function to update the output
def update_output():
    algorithm = algorithm_var.get()
    filter_type = filter_var.get()
    track_initiation = track_initiation_var.get()
    plot_type = plot_var.get()
    
    output_text = f"Selected Algorithm: {algorithm}\n"
    output_text += f"Selected Filter: {filter_type}\n"
    output_text += f"Selected Track Initiation: {track_initiation}\n"
    output_text += f"Selected Plot Type: {plot_type}"
    
    output_box.config(state=tk.NORMAL)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, output_text)
    output_box.config(state=tk.DISABLED)

# Left Frame (Selection Area)
left_frame = tk.Frame(root, bg='#e6e6e6', padx=20, pady=20)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Right Frame (Output Area)
right_frame = tk.Frame(root, bg='#ffffff', padx=20, pady=20)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Algorithm selection
algorithm_label = tk.Label(left_frame, text="Select Algorithm:", bg='#e6e6e6', font=('Arial', 12))
algorithm_label.pack(anchor='w')
algorithm_var = tk.StringVar(value="JPDA")
algorithm_menu = ttk.Combobox(left_frame, textvariable=algorithm_var, values=["JPDA", "MUNKRES"], state="readonly")
algorithm_menu.pack(fill=tk.X, pady=5)

# Filter selection
filter_label = tk.Label(left_frame, text="Select Filter:", bg='#e6e6e6', font=('Arial', 12))
filter_label.pack(anchor='w')
filter_var = tk.StringVar(value="CV")
filter_menu = ttk.Combobox(left_frame, textvariable=filter_var, values=["CV", "CT", "CA", "IMM"], state="readonly")
filter_menu.pack(fill=tk.X, pady=5)

# Track initiation selection
track_initiation_label = tk.Label(left_frame, text="Select Track Initiation:", bg='#e6e6e6', font=('Arial', 12))
track_initiation_label.pack(anchor='w')
track_initiation_var = tk.StringVar(value="2 Step")
track_initiation_menu = ttk.Combobox(left_frame, textvariable=track_initiation_var, values=["2 Step", "3 Step", "4 Step"], state="readonly")
track_initiation_menu.pack(fill=tk.X, pady=5)

# Plot type selection
plot_label = tk.Label(left_frame, text="Select Plot Type:", bg='#e6e6e6', font=('Arial', 12))
plot_label.pack(anchor='w')
plot_var = tk.StringVar(value="PPI")
plot_menu = ttk.Combobox(left_frame, textvariable=plot_var, values=["PPI", "C-Scope", "V-Scope", "Time vs Range", "Time vs Azimuth", "Time vs Elevation", "Range vs Height"], state="readonly")
plot_menu.pack(fill=tk.X, pady=5)

# Submit Button
submit_button = tk.Button(left_frame, text="Submit", bg='#4CAF50', fg='white', font=('Arial', 12), command=update_output)
submit_button.pack(pady=20)

# Output Box on the Right Side
output_label = tk.Label(right_frame, text="Output:", bg='#ffffff', font=('Arial', 12))
output_label.pack(anchor='w')

output_box = tk.Text(right_frame, height=15, width=40, state=tk.DISABLED, bg='#f5f5f5', font=('Arial', 10))
output_box.pack(fill=tk.BOTH, expand=True)

# Start the GUI event loop
root.mainloop()
