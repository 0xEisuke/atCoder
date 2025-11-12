import sys
input = sys.stdin.readline

def main():
    S = input().strip()
    
    s_rev = "".join(list(reversed(S)))
    # print(s_rev)
    
    lst = ["dream","dreamer","erase","eraser"]
    rev_lst = []
    for x in lst:
        rev_lst.append("".join(list(reversed(x))))
    
    while len(s_rev)>0:
        if s_rev[0:5] in rev_lst:
            s_rev = s_rev[5:]
        elif s_rev[0:6] in rev_lst:
            s_rev = s_rev[6:]
        elif s_rev[0:7] in rev_lst:
            s_rev = s_rev[7:]
        else:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()