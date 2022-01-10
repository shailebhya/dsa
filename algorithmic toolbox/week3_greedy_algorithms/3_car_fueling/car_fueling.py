# python3
import sys


def compute_min_refills(distance, tank, stops):

    refuel = 0
    capacity = tank
    stopsD = []

    for i in range(len(stops)):
      if stops[i]<=distance:
            if i==0:
                stopsD.append(stops[i]-0)
            else:
                stopsD.append(stops[i]-stops[i-1])
    
    stopsD.append(distance-sum(stopsD))
    stopsD.append(0)
    # print(stopsD)
    # write your code here
    if distance<tank:
        return 0 

    for i in range(len(stops)+1):
        if distance==0:
            return refuel

        elif distance<=tank:
            return refuel

        elif tank-stopsD[i]==0:
            refuel=refuel+1
            tank=capacity
            distance=distance-stopsD[i]
        
        elif tank-stopsD[i]>0:
            # print("tank is{}",tank)
            tank=tank-stopsD[i]
            distance=distance-stopsD[i]
            if tank-stopsD[i+1]<0:
                refuel=refuel+1
                tank=capacity
        
        elif tank-stopsD[i]<0:
            return -1
                


    return refuel

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
