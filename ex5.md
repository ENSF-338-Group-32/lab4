# ex5.md

## Question 1: Measurement Noise and Timeit Strategies

When timing a program, several issues can introduce noise and lead to incorrect measurements:
- **Background Processes**: Other applications running on the system can affect performance.
- **CPU Throttling**: Processors dynamically adjust speeds based on load and thermal conditions.
- **Garbage Collection**: In languages like Python, garbage collection can introduce delays.
- **JIT Compilation**: Some interpreters optimize code over time, leading to variations.

### Timeit Approaches:
1. **Using `timeit.timeit()` with `number`**
   - Runs the function multiple times in succession and returns the total time.
   - Reduces random variations by averaging multiple runs.
   - Useful when measuring a function that executes quickly (e.g., less than 1ms).

2. **Using `timeit.repeat()` with `repeat` and `number`**
   - Runs the function multiple times in separate iterations.
   - Helps capture variations in execution time across different runs.
   - Useful when the function is affected by system-wide performance fluctuations.

### When to Use Each:
- **Use `timeit.timeit()`** when the goal is to get a single average execution time for a short operation.
- **Use `timeit.repeat()`** when execution time varies significantly due to external factors, allowing a better sense of distribution.

## Question 2: Appropriate Statistics for Timeit Results

Three commonly used aggregate statistics are:
- **Average (mean)**: Sum of all times divided by the number of measurements.
- **Minimum**: The smallest recorded time.
- **Maximum**: The largest recorded time.

### Best Statistic for `timeit.timeit()`
- **Minimum (min)**: Since `timeit.timeit()` executes the function multiple times in a single run, the smallest recorded time best represents the true execution time, as it minimizes the impact of noise.

### Best Statistic for `timeit.repeat()`
- **Average (mean) and minimum (min)**:
  - The **average** helps understand the general performance.
  - The **minimum** is useful for estimating the best possible execution time under ideal conditions.
  - The maximum is usually ignored unless analyzing worst-case outliers.

Thus, using both min and mean from `timeit.repeat()` gives a better overall picture of performance trends.

