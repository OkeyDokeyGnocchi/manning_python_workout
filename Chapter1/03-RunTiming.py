# Run Timing
# Create a function run_timing
#  - Should loop until user enters blank space
#  - Should display the average time over given number of runs

def run_timing():
    # Set run_count to 0 and total_time to 0 on init
    run_count = 0
    total_time = 0

    # Loop until blank input to break
    while True:
        run_time = input("Enter 10km run time: ")
        if run_time == "":
            break
        else:
            try:
                total_time += int(run_time)
                run_count += 1
            except:
                print("Please only enter integers or use a blank line to exit.")
    
    run_average = total_time / run_count

    print(f"Average of {run_average:.2f}, over {run_count} runs")


if __name__ == "__main__":
    run_timing()