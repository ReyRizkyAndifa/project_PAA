import random
import time
import matplotlib.pyplot as plt


def generate_array(n, max_value = 271, seed=42):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]


def is_unique(arr):
    return len(arr) == len(set(arr))


def measure_time(arr):
    start_time = time.perf_counter()
    _ = is_unique(arr)
    end_time = time.perf_counter()
    return end_time - start_time


n_values = [100, 150, 200, 250, 300, 350, 400, 500]
last_3_digits = 79  
max_value = 250 - last_3_digits


worst_case_times = []
average_case_times = []


for n in n_values:
    
    worst_case_array = [1] * n
    worst_time = measure_time(worst_case_array)
    worst_case_times.append(worst_time)

    
    average_times = []
    for _ in range(10):  
        avg_case_array = generate_array(n, max_value)
        avg_time = measure_time(avg_case_array)
        average_times.append(avg_time)
    average_case_times.append(sum(average_times) / len(average_times))


with open("worst_avg.txt", "w") as file:
    file.write("n\tWorst Case (s)\tAverage Case (s)\n")
    for i, n in enumerate(n_values):
        file.write(f"{n}\t{worst_case_times[i]:.6f}\t{average_case_times[i]:.6f}\n")


plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_case_times, label="Worst Case", marker="o")
plt.plot(n_values, average_case_times, label="Average Case", marker="o")
plt.title("Time Complexity for Array Uniqueness Check")
plt.xlabel("Array Size (n)")
plt.ylabel("Time (s)")
plt.legend()
plt.grid()
plt.savefig("complexity_plot.jpg")
plt.show()

