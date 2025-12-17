# algorithms/srtf.py

def srtf(processes):
    """
    Implement Shortest Remaining Time First (SRTF) CPU scheduling algorithm
    
    SRTF is a preemptive version of SJF where the process with the smallest
    remaining burst time is selected for execution at every time unit.
    A running process can be preempted if a new process arrives with shorter remaining time.
    
    Args:
        processes: List of tuples where each tuple represents a process
                  Format: (process_id, arrival_time, burst_time)
    
    Returns:
        tuple: (gantt_chart, waiting_times, turnaround_times, completion_times)
        - gantt_chart: List of tuples (pid, start_time, end_time)
        - waiting_times: Dictionary {pid: waiting_time}
        - turnaround_times: Dictionary {pid: turnaround_time}
        - completion_times: Dictionary {pid: completion_time}
    """
    
    # TODO 1
    processes = sorted(processes, key=lambda p: p[1])  
    n = len(processes)
    remaining_times = {p[0]: p[2] for p in processes}  
    completion_times = {}
    waiting_times = {}
    turnaround_times = {}
    gantt_chart = []
    current_time = 0
    ready_queue = [] 
    index = 0 
    current_pid = None
    start_time = None
    
    # TODO 2
    while len(completion_times) < n:
        while index < n and processes[index][1] <= current_time:
            ready_queue.append(processes[index])
            index += 1
        if not ready_queue:
            if index < n:
                current_time = processes[index][1]
            continue
        ready_queue.sort(key=lambda p: remaining_times[p[0]])
        next_pid, _, _ = ready_queue[0]
        if current_pid != next_pid:
            if current_pid is not None:
                gantt_chart.append((current_pid, start_time, current_time))
            start_time = current_time
            current_pid = next_pid
        remaining_times[current_pid] -= 1
        current_time += 1
        if remaining_times[current_pid] == 0:
            gantt_chart.append((current_pid, start_time, current_time))
            completion_times[current_pid] = current_time
            pid_index = next(i for i, p in enumerate(processes) if p[0] == current_pid)
            arrival_time = processes[pid_index][1]
            burst_time = processes[pid_index][2]
            turnaround_times[current_pid] = current_time - arrival_time
            waiting_times[current_pid] = turnaround_times[current_pid] - burst_time
            ready_queue = [p for p in ready_queue if p[0] != current_pid]
            current_pid = None
    
    # TODO 4
    return gantt_chart, waiting_times, turnaround_times, completion_times