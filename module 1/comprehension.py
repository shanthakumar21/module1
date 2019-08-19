def main():
    n=int(input("Enter a number :"))
    res=[x for x in range(0,n) if x**2 < n]
    print(res)
main()
