def priority_non_preemptive(processes, priorities):
    """
    TODO: Implement Priority Non-Preemptive CPU scheduling algorithm
    
    Priority Non-Preemptive is a scheduling algorithm where processes are executed 
    based on their priority (higher priority first) without preemption.
    When multiple processes are available, the one with highest priority is selected.
    
    Args:
        processes: List of tuples where each tuple represents a process
                  Format: (process_id, arrival_time, burst_time)
        priorities: Dictionary mapping process_id to priority value
                   Format: {pid: priority}
                   Note: Higher value = Higher priority
    
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
    
    # TODO: Step 2 - Initialize current_time and remaining processes list
    
    # TODO: Step 3 - Process scheduling loop
    
    # TODO: Step 4 - Return the results
    
    return gantt_chart, waiting_times, turnaround_times, completion_times
