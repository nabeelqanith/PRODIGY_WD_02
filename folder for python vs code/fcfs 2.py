import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def fcfs_scheduling():
    global processes
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    gantt_chart = []
    
    for p in processes:
        if current_time < p.arrival_time:
            current_time = p.arrival_time
        p.completion_time = current_time + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        gantt_chart.append((p.pid, current_time, current_time + p.burst_time))
        current_time += p.burst_time
    
    show_gantt_chart(gantt_chart)

def show_gantt_chart(gantt_chart):
    if not gantt_chart:
        messagebox.showerror("Error", "No processes to schedule!")
        return
    
    fig, ax = plt.subplots(figsize=(8, 4))
    for pid, start, end in gantt_chart:
        ax.barh(pid, end - start, left=start, height=0.5, color='skyblue', edgecolor='black')
        ax.text((start + end) / 2, pid, f'P{pid}', ha='center', va='center', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('Time')
    ax.set_ylabel('Processes')
    ax.set_title('Gantt Chart')
    ax.set_yticks([p[0] for p in gantt_chart])
    ax.set_xticks(range(0, max(p[2] for p in gantt_chart) + 1))
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def add_process():
    try:
        pid = len(processes) + 1
        burst_time = int(burst_time_entry.get())
        arrival_time = int(arrival_time_entry.get())
        processes.append(Process(pid, burst_time, arrival_time))
        process_list.insert(tk.END, f'P{pid} - Burst: {burst_time}, Arrival: {arrival_time}')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter valid numbers!')

def schedule():
    fcfs_scheduling()

def reset():
    global processes
    processes = []
    process_list.delete(0, tk.END)

# GUI Setup
processes = []
root = tk.Tk()
root.title('FCFS Scheduling Mini OS')
root.geometry('400x350')

# Labels and Entries
tk.Label(root, text='Burst Time:').grid(row=0, column=0)
burst_time_entry = tk.Entry(root)
burst_time_entry.grid(row=0, column=1)

tk.Label(root, text='Arrival Time:').grid(row=1, column=0)
arrival_time_entry = tk.Entry(root)
arrival_time_entry.grid(row=1, column=1)

# Buttons
tk.Button(root, text='Add Process', command=add_process).grid(row=2, column=0, columnspan=2, pady=5)

process_list = tk.Listbox(root, width=50)
process_list.grid(row=3, column=0, columnspan=2, pady=5)

tk.Button(root, text='Schedule', command=schedule).grid(row=4, column=0, pady=5)
tk.Button(root, text='Reset', command=reset).grid(row=4, column=1, pady=5)

root.mainloop()

