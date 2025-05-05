# ShellSort Algorithm Implementation

## 📚 Project Description
Implementation of the ShellSort algorithm with three different gap sequences for the INF01124 - Classification and Data Search course at Universidade Federal do Rio Grande do Sul (UFRGS).

## 🧠 Key Features
- **Three gap sequences implemented**:
  - Shell's original (powers of 2)
  - Knuth's sequence (3x+1)
  - Ciura's empirically derived sequence
- **Detailed output** showing array state after each increment
- **Performance benchmarking** across different input sizes
- **Modular design** for easy extension

## 🛠 Technical Implementation
```python
class ShellSortAlgorithm:
    def __init__(self, array, sequence_func, sequence_name):
        self.array = array
        self.sequence_func = sequence_func
        self.sequence_name = sequence_name
    
    def sort(self):
        # Implements ShellSort with configurable gap sequence
        # Writes intermediate states to output file
        # Measures and records execution time
