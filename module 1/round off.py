def roundOff(n):
    if Avg > n:
        return 0
    else:
        return 1

def main():
    res=map(roundOff, data)
    print(list(res))
    
data=[0.00, 0.12, 0.24, 0.36, 0.48, 0.52, 0.65, 0.50, 0.11, 0.09]
Avg=sum(data)/len(data)
main()
