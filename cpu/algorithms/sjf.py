# algorithms/sjf.py

def sjf(processes):
    """
    Implement Shortest Job First (SJF) CPU scheduling algorithm
    
    SJF is a non-preemptive scheduling algorithm where the process with 
    the smallest burst time is selected for execution next.
    When multiple processes are available, the one with shortest burst time runs first.
    
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
    processes = sorted(processes, key=lambda p: (p[1], p[2])) 
    
    # TODO 2
    current_time = 0
    gantt_chart = []
    waiting_times = {}
    turnaround_times = {}
    completion_times = {}
    ready_queue = []  
    index = 0 
    
    # TODO 3
    while index < len(processes) or ready_queue:
        while index < len(processes) and processes[index][1] <= current_time:
            ready_queue.append(processes[index])
            index += 1
        
        if not ready_queue:
            if index < len(processes):
                current_time = processes[index][1]
            continue
        ready_queue.sort(key=lambda p: p[2])
        pid, arrival_time, burst_time = ready_queue.pop(0)
        start_time = current_time
        end_time = current_time + burst_time
        gantt_chart.append((pid, start_time, end_time))
        completion_times[pid] = end_time
        turnaround_times[pid] = end_time - arrival_time
        waiting_times[pid] = turnaround_times[pid] - burst_time
        
        current_time = end_time
    
    # TODO 4
    return gantt_chart, waiting_times, turnaround_times, completion_times