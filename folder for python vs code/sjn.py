import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class Process:
    def __init__(self, pid, priority, burst_time, arrival_time):
        self.pid = pid
        self.priority = priority
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.start_time = -1
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def priority_scheduling(preemptive=True):
    global processes
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    current_time, completed = 0, 0
    n = len(processes)
    gantt_chart = []
    
    while completed < n:
        available_processes = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
        
        if available_processes:
            available_processes.sort(key=lambda x: x.priority)
            current_process = available_processes[0]
            
            if current_process.start_time == -1:
                current_process.start_time = current_time
                
            if preemptive:
                current_process.remaining_time -= 1
                gantt_chart.append((current_process.pid, current_time))
                if current_process.remaining_time == 0:
                    current_process.completion_time = current_time + 1
                    completed += 1
            else:
                for _ in range(current_process.burst_time):
                    gantt_chart.append((current_process.pid, current_time))
                    current_time += 1
                current_process.completion_time = current_time
                current_process.remaining_time = 0
                completed += 1
        else:
            gantt_chart.append(("Idle", current_time))
        
        current_time += 1
    
    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
    
    show_gantt_chart(gantt_chart)

def show_gantt_chart(gantt_chart):
    process_ids, start_times = zip(*gantt_chart)
    unique_ids = list(dict.fromkeys(process_ids))
    colors = plt.cm.Paired(np.linspace(0, 1, len(unique_ids)))
    color_map = {pid: colors[i] for i, pid in enumerate(unique_ids)}
    
    plt.figure(figsize=(10, 3))
    for pid, start in gantt_chart:
        plt.barh(y=0, width=1, left=start, height=0.4, color=color_map[pid], label=f'P{pid}' if pid != "Idle" else "Idle")
    
    plt.xlabel('Time')
    plt.yticks([])
    plt.title('Gantt Chart')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

def add_process():
    try:
        pid = len(processes) + 1
        priority = int(priority_entry.get())
        burst_time = int(burst_time_entry.get())
        arrival_time = int(arrival_time_entry.get())
        if priority < 0 or burst_time <= 0 or arrival_time < 0:
            raise ValueError
        processes.append(Process(pid, priority, burst_time, arrival_time))
        process_list.insert(tk.END, f'P{pid} - Priority: {priority}, Burst: {burst_time}, Arrival: {arrival_time}')
        messagebox.showinfo('Success', 'Process Added Successfully!')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter valid positive numbers!')

def schedule():
    if not processes:
        messagebox.showerror('Error', 'No processes to schedule!')
        return
    preemptive = preemptive_var.get()
    priority_scheduling(preemptive)

def reset():
    global processes
    processes = []
    process_list.delete(0, tk.END)
    messagebox.showinfo('Reset', 'All processes have been cleared!')

processes = []
root = tk.Tk()
root.title('Priority Scheduling Mini OS')

tk.Label(root, text='Priority:').grid(row=0, column=0)
priority_entry = tk.Entry(root)
priority_entry.grid(row=0, column=1)

tk.Label(root, text='Burst Time:').grid(row=1, column=0)
burst_time_entry = tk.Entry(root)
burst_time_entry.grid(row=1, column=1)

tk.Label(root, text='Arrival Time:').grid(row=2, column=0)
arrival_time_entry = tk.Entry(root)
arrival_time_entry.grid(row=2, column=1)

tk.Button(root, text='Add Process', command=add_process).grid(row=3, column=0, columnspan=2)

process_list = tk.Listbox(root, width=50)
process_list.grid(row=4, column=0, columnspan=2)

preemptive_var = tk.BooleanVar()
tk.Checkbutton(root, text='Preemptive', variable=preemptive_var).grid(row=5, column=0, columnspan=2)

tk.Button(root, text='Schedule', command=schedule).grid(row=6, column=0)
tk.Button(root, text='Reset', command=reset).grid(row=6, column=1)

root.mainloop()
