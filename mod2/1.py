import os
def main():
    filename = "processes.txt"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(BASE_DIR, filename)
    print(filepath)

    def get_summary_rss(filepath):
        with open(filepath) as file:
            text = file.readlines()[1:]
            sizes = [int(line.split()[4]) for line in text]
            sum_size = sum(sizes) # in Byte
            return convert_Bytes(sum_size)

    def convert_Bytes(n): # 1kiB = 1.000B
        PREFIXES = ["B","KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]
        digits_number = len(str(n))
        prefix_num = (digits_number - 1) // 3
        prefix = PREFIXES[prefix_num]
        converted_n = n // (1000**prefix_num)
        return f"{converted_n} {prefix}"

    print(get_summary_rss(filepath))

if __name__ == "__main__":
    main()