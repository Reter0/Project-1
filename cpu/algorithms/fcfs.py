# algorithms/fcfs.py

def fcfs(processes):
    """
    TODO: Implement First-Come, First-Served (FCFS) CPU scheduling algorithm
    
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
    
    # TODO: 
    # Currently returning empty data - replace with your implementation
    
    gantt_chart = []
    waiting_times = {}
    turnaround_times = {}
    completion_times = {}
    
    # TODO: Step 1 - Sort processes by arrival time
    
    # TODO: Step 2 - Initialize current_time
    
    # TODO: Step 3 - Process each job in FCFS order
    
    # TODO: Step 4 - Return the results
    
    return gantt_chart, waiting_times, turnaround_times, completion_times