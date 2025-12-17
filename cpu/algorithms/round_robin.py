# algorithms/round_robin.py

from collections import deque

def round_robin(processes, time_quantum):
    """
    Implement Round Robin CPU scheduling algorithm
    
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
    
    # TODO 1
    processes = sorted(processes, key=lambda p: p[1])
    
    # TODO 2
    n = len(processes)
    remaining_times = {p[0]: p[2] for p in processes}
    completion_times = {}
    waiting_times = {p[0]: 0 for p in processes}
    turnaround_times = {}
    gantt_chart = []
    ready_queue = deque()
    current_time = 0
    index = 0
    last_pid = None 
    
    # TODO 3
    while len(completion_times) < n:
        while index < n and processes[index][1] <= current_time:
            ready_queue.append(processes[index][0]) 
            index += 1
        if not ready_queue:
            current_time += 1
            continue
        pid = ready_queue.popleft()

        if last_pid != pid and last_pid is not None:
            gantt_chart[-1] = (gantt_chart[-1][0], gantt_chart[-1][1], current_time)

        if last_pid != pid:
            gantt_chart.append([pid, current_time, None])
        slice_time = min(time_quantum, remaining_times[pid])

        for _ in range(slice_time):
            current_time += 1
            remaining_times[pid] -= 1
            for other_pid in ready_queue:
                waiting_times[other_pid] += 1
        gantt_chart[-1][2] = current_time

        
        if remaining_times[pid] > 0:
            ready_queue.append(pid)
        else:
            completion_times[pid] = current_time
            arrival_time = next(p[1] for p in processes if p[0] == pid)
            burst_time = next(p[2] for p in processes if p[0] == pid)
            turnaround_times[pid] = completion_times[pid] - arrival_time
            waiting_times[pid] = turnaround_times[pid] - burst_time
        
        last_pid = pid
    
    # TODO 4
    gantt_chart = [(entry[0], entry[1], entry[2]) for entry in gantt_chart]
    return gantt_chart, waiting_times, turnaround_times, completion_times