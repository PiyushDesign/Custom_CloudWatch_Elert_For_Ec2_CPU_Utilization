import multiprocessing
import time

def cpu_stress():
    # This function performs an infinite loop to stress the CPU
    while True:
        pass  # Infinite loop to simulate CPU load

if __name__ == "__main__":
    # Number of CPU cores to stress
    num_cores = multiprocessing.cpu_count()

    print(f"Starting CPU stress on {num_cores} cores...")

    # Create one process per CPU core
    processes = []
    for i in range(num_cores):
        p = multiprocessing.Process(target=cpu_stress)
        processes.append(p)
        p.start()

    # Let the stress run for a certain amount of time
    time_to_run = 300  # Run for 5 minutes (300 seconds)
    time.sleep(time_to_run)

    # Stop all processes after the specified time
    for p in processes:
        p.terminate()

    print("CPU stress test completed.")
