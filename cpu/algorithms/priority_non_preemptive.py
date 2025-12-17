# algorithms/priority_non_preemptive.py

def priority_non_preemptive(processes, priorities):
    """
    Implement Priority Non-preemptive CPU scheduling algorithm
    
    Priority Non-preemptive is a scheduling algorithm where processes are executed 
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
    
    # TODO 1
    processes = sorted(processes, key=lambda p: p[1])
    
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
        ready_queue.sort(key=lambda p: (-priorities[p[0]], p[1]))
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