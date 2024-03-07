import sys

def decrypt(s):
    i = 0
    s_list = list(s)
    while i < len(s_list):
        if s_list[i] == '.':
            if s_list[i:i+2] == ['.','.']:
                if i > 0:
                    del s_list[i-1]
                    i -= 1
                del s_list[i:i+2]
                # i -= 1
            else:
                del s_list[i]
        else:
            i += 1
            
    return ''.join(s_list)

def main():
    input_str = sys.stdin.read()
    print(decrypt(input_str))

if __name__ == "__main__":
    main()