# Reverse string by recursion

def reverse(s):
    if len(s) ==1:
        return s[0];
    return reverse(s[1:]) + s[0];


def main():
    s = "abcd";
    print(s);
    print(reverse(s));

main()
