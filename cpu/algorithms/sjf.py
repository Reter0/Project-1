def sjf(processes):
    """
    TODO: Implement Shortest Job First (SJF) CPU scheduling algorithm
    
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
    
    # TODO:
    # Currently returning empty data - replace with your implementation
    
    gantt_chart = []
    waiting_times = {}
    turnaround_times = {}
    completion_times = {}
    
    # TODO: Step 1 - Sort processes by arrival time (and burst time for ties)
    
    # TODO: Step 2 - Initialize variables
    
    # TODO: Step 3 - Main scheduling loop
    
    # TODO: Step 4 - Return the results
    
    return gantt_chart, waiting_times, turnaround_times, completion_times