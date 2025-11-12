import sys

def main():
    input = sys.stdin.readline
    s,t = input().strip().split()
    
    vs = -1
    vt = -1
    
    versions = ["Ocelot","Serval","Lynx"]
    for i,v in enumerate(versions):
        if s == v:
            vs = i
        if t == v:
            vt = i
    if vs >= vt:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()