#coding:utf-8

def likelihood(sensor_valuesA, sensor_valuesB):
    """
    1. compare A and B
       A,and B must be same range list of integers.

    2. return likelihood.
       if A is completely equaly as B, then likelihood is 1.0(Max)
       if A is completely different as B, likelihood is 0.0(Min)
       In almost cases, likelihood is between 1.0 and 0.0
    """
    if(type(sensor_valuesA) is list and type(sensor_valuesB) is list and len(sensor_valuesA) == len(sensor_valuesB) ) :
        l = 1.0
        n = len(sensor_valuesA)
        for i in range(n):
            if sensor_valuesA[i] != sensor_valuesB[i]:
                l -= (1.0 / n)
        return l

    else:
        print("""
        Error in likelihood(function)
        these arguments are incorrect types
        """)
