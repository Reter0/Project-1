def srtf(processes):
    """
    TODO: Implement Shortest Remaining Time First (SRTF) CPU scheduling algorithm
    
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
    
    # TODO:
    # Currently returning empty data - replace with your implementation
    
    gantt_chart = []
    waiting_times = {}
    turnaround_times = {}
    completion_times = {}
    
    # TODO: Step 1 - Initialize data structures
    
    # TODO: Step 2 - Main scheduling loop
    
    # TODO: Step 3 - Convert gantt_chart to tuples and return results
    
    return gantt_chart, waiting_times, turnaround_times, completion_times