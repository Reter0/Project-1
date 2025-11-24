from collections import deque

def round_robin(processes, time_quantum):
    """
    TODO: Implement Round Robin CPU scheduling algorithm
    
    Round Robin is a preemptive scheduling algorithm where each process 
    gets a fixed time quantum for execution. If a process doesn't complete
    within its time quantum, it's preempted and moved to the back of the ready queue.
    
    Args:
        processes: List of tuples where each tuple represents a process
                  Format: (process_id, arrival_time, burst_time)
        time_quantum: Integer representing the fixed time slice for each process
    
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
    
    # TODO: Step 2 - Initialize data structures
    
    # TODO: Step 3 - Main scheduling loop
    
    # TODO: Step 4 - Return the results
    
    return gantt_chart, waiting_times, turnaround_times, completion_times