# algorithms/fcfs.py

def fcfs(processes):
    """
    Implement First-Come, First-Served (FCFS) CPU scheduling algorithm
    
    FCFS is a non-preemptive scheduling algorithm where processes are executed 
    in the order of their arrival time.
    
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
    
    # TODO 2
    current_time = 0
    gantt_chart = []
    waiting_times = {}
    turnaround_times = {}
    completion_times = {}
    
    # TODO 3
    for pid, arrival_time, burst_time in processes:
        if current_time < arrival_time:
            current_time = arrival_time
        
        start_time = current_time
        end_time = current_time + burst_time
        gantt_chart.append((pid, start_time, end_time))
        
        completion_times[pid] = end_time
        turnaround_times[pid] = end_time - arrival_time
        waiting_times[pid] = turnaround_times[pid] - burst_time
        
        current_time = end_time
    # TODO 4
    return gantt_chart, waiting_times, turnaround_times, completion_times