import os
import time

class ShellSortAlgorithm:
    def __init__(self, array, sequence_func, sequence_name):
        self.array = array
        self.sequence_func = sequence_func
        self.sequence_name = sequence_name

    def sort(self):
        n = len(self.array)
        sequence = self.sequence_func(n)

        start_time = time.perf_counter()

        with open("saida1.txt", "a") as output_file:
            output_file.write(f"{self.sequence_name}\n")
            output_file.write(f"{self.array}\n")

            for i, gap in enumerate(sequence, start=1):
                output_file.write(f"INCR={gap}\n")
                for j in range(gap, n):
                    temp = self.array[j]
                    k = j
                    while k >= gap and self.array[k - gap] > temp:
                        self.array[k] = self.array[k - gap]
                        k -= gap
                    self.array[k] = temp
                    output_file.write(f"{self.array}\n")

        end_time = time.perf_counter()

        execution_time = (end_time - start_time) * 1000

        hardware_info = "AMD Ryzen 5 3600X, 3.8GHz (4.4GHz Max Turbo)"

        with open("saida2.txt", "a") as output_file:
            output_file.write(
                f"{self.sequence_name},{n},{execution_time:.6f},{hardware_info}\n"
            )

def power_of_two_sequence(n):
    sequence = []
    gap = 1
    while gap < n:
        sequence.append(gap)
        gap = 2 * gap + 1
    sequence.reverse()
    return sequence

def knuth_sequence(n):
    sequence = []
    gap = 1
    while gap < n:
        sequence.append(gap)
        gap = 3 * gap + 1
    sequence.reverse()
    return sequence

def ciura_sequence(n):
    sequence = [1]
    while sequence[-1] < n:
        next_gap = 1.25 * sequence[-1] + 1
        sequence.append(int(next_gap))
    sequence.pop()
    sequence.reverse()
    return sequence

def process_files(directory):
    with open(directory, 'r') as input_file:
        lines = input_file.readlines()
        data_input = [int(e) for e in lines[1].split()]
        num_elements = data_input[0]
        elements = data_input[1:]

        copied_array = elements.copy()
        ShellSortAlgorithm(copied_array, power_of_two_sequence, "SEQ=SHELL").sort()

        copied_array = elements.copy()
        ShellSortAlgorithm(copied_array, knuth_sequence, "SEQ=KNUTH").sort()

        copied_array = elements.copy()
        ShellSortAlgorithm(copied_array, ciura_sequence, "SEQ=CIURA").sort()

def main():
    directory_path = "entradas"

    files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]

    for file_name in files:
        file_directory = os.path.join(directory_path, file_name)
        process_files(file_directory)

if __name__ == "__main__":
    with open("saida1.txt", "w") as output_file:
        output_file.write("")

    with open("saida2.txt", "w") as output_file:
        output_file.write("")

    main()
