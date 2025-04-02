import tkinter as tk
from tkinter import messagebox

def calculate_fcfs():
    try:
        # Retrieve inputs from the GUI
        processes = process_input.get().split(",")
        arrival_times = list(map(int, arrival_input.get().split(",")))
        burst_times = list(map(int, burst_input.get().split(",")))

        if len(processes) != len(arrival_times) or len(processes) != len(burst_times):
            raise ValueError("The number of processes, arrival times, and burst times must be equal.")

        n = len(processes)
        completion_times = [0] * n
        waiting_times = [0] * n
        turnaround_times = [0] * n

        # Sort processes by arrival time
        processes_info = sorted(zip(processes, arrival_times, burst_times), key=lambda x: x[1])
        processes, arrival_times, burst_times = zip(*processes_info)

        # Calculate completion, turnaround, and waiting times
        current_time = 0
        for i in range(n):
            if current_time < arrival_times[i]:
                current_time = arrival_times[i]  # Wait for the process to arrive
            current_time += burst_times[i]
            completion_times[i] = current_time
            turnaround_times[i] = completion_times[i] - arrival_times[i]
            waiting_times[i] = turnaround_times[i] - burst_times[i]

        # Prepare and display the result in a table-like format
        result_text = "Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time\n"
        for i in range(n):
            result_text += f"{processes[i]}\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}\n"

        result_label.config(text=result_text, bg="#E8F8F5", fg="#34495E")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the GUI
root = tk.Tk()
root.title("FCFS Scheduling with Arrival Time")
root.configure(bg="#AED6F1")

# GUI Components
tk.Label(root, text="FCFS Scheduling Simulator", font=("Helvetica", 16, "bold"), bg="#AED6F1", fg="#2E86C1").grid(row=0, columnspan=2, pady=10)

tk.Label(root, text="Processes (comma-separated):", font=("Helvetica", 12), bg="#AED6F1").grid(row=1, column=0, sticky="e", padx=10, pady=5)
process_input = tk.Entry(root, font=("Helvetica", 12), width=30)
process_input.grid(row=1, column=1, pady=5)

tk.Label(root, text="Arrival Times (comma-separated):", font=("Helvetica", 12), bg="#AED6F1").grid(row=2, column=0, sticky="e", padx=10, pady=5)
arrival_input = tk.Entry(root, font=("Helvetica", 12), width=30)
arrival_input.grid(row=2, column=1, pady=5)

tk.Label(root, text="Burst Times (comma-separated):", font=("Helvetica", 12), bg="#AED6F1").grid(row=3, column=0, sticky="e", padx=10, pady=5)
burst_input = tk.Entry(root, font=("Helvetica", 12), width=30)
burst_input.grid(row=3, column=1, pady=5)

calculate_button = tk.Button(root, text="Calculate FCFS", font=("Helvetica", 12, "bold"), bg="#76D7C4", fg="white", command=calculate_fcfs)
calculate_button.grid(row=4, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Courier", 12), bg="#AED6F1", justify="left")
result_label.grid(row=5, columnspan=2, pady=10)

tk.Label(root, text="Designed by You!", font=("Helvetica", 10, "italic"), bg="#AED6F1", fg="#2E86C1").grid(row=6, columnspan=2, pady=10)

root.mainloop()
