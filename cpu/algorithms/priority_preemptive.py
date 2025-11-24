def priority_preemptive(processes, priorities):
    """
    TODO: Implement Priority Preemptive CPU scheduling algorithm
    
    Priority Preemptive is a scheduling algorithm where processes are executed 
    based on their priority (higher priority first) with preemption.
    At every time unit, the highest priority available process is selected.
    A running process can be preempted if a higher priority process arrives.
    
    Args:
        processes: List of tuples where each tuple represents a process
                  Format: (process_id, arrival_time, burst_time)
        priorities: Dictionary mapping process_id to priority value
                   Format: {pid: priority}
                   Note: Higher numeric value = Higher priority
    
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
    
    # TODO: Step 1 - Initialize data structures
    
    # TODO: Step 2 - Main scheduling loop
    
    # TODO: Step 3 - Return the results
    
    return gantt_chart, waiting_times, turnaround_times, completion_times