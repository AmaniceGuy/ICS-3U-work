def main():
    traffic_sign(5)
    
def traffic_sign(n):
    if n > 0 :
        print("No Parking")
        traffic_sign(n-1)

main()