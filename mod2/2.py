import sys


def get_mean_size(lines):
    if not lines:
        print("Directory is empty")
        return
    lines = [line.split() for line in lines]
    sizes = [int(line[4]) for line in lines]
    average_file_size = sum(sizes) / len(sizes)
    print(average_file_size)

def main():
    lines = sys.stdin.readlines()[1:]
    get_mean_size(lines)

if __name__ == "__main__":
    main()