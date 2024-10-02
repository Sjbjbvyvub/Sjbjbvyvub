#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import threading
import time
from queue import Queue

# Queue for managing requests
q = Queue()

# Function to send a GET request to the website
def stress_test():
    while not q.empty():
        try:
            q.get()
            response = requests.get(url)
            print(f"Request completed with status code: {response.status_code}")
            q.task_done()
            time.sleep(delay_between_requests)  # Delay between requests
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            q.task_done()

# Main logic
if __name__ == '__main__':
    # User inputs for configuration
    url = input("Enter the website URL (e.g., http://example.com): ")
    num_threads = int(input("Enter the number of threads: "))
    num_requests = int(input("Enter the number of requests: "))
    delay_between_requests = float(input("Enter the delay between requests (in seconds): "))

    print(f"Starting stress test on {url} with {num_threads} threads, {num_requests} requests, and {delay_between_requests} seconds delay.")

    # Fill the queue with the number of requests
    for _ in range(num_requests):
        q.put(_)

    # Start stress testing with multiple threads
    for _ in range(num_threads):
        t = threading.Thread(target=stress_test)
        t.start()

    q.join()
    print("Stress test completed.")