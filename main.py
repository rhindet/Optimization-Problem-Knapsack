import time
maxNumber = 0
profitTotal = 0
weightTotal = 0
capacity2 = 0
a = 0
profitToCarry = []
weightToCarry = []


def getFileVariables(file_path):
    start_time = time.time()
    output_file = "file_path"  # Nombre del archivo de salida
    with open(file_path, 'r') as file:
        lines = file.readlines()

        numItems, capacity = map(int, lines[0].split())
        profit = []
        weight = []
        pw = []

        for line in lines[1:]:
            p, w = map(float, line.split())
            profit.append(p)
            weight.append(w)
            pw.append(p/w)

        calculateProblem(profit, weight, pw, numItems, capacity, output_file)
        printFinalResult(output_file)
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print("Execution time:", elapsed_time, "seconds")


def calculateProblem(profit ,weight,pw,numItems,capacity, output_file):

        global maxWeight
        global capacity2
        global maxNumber
        global profitTotal
        global weightTotal
        global profitToCarry
        global weightToCarry
        global a



        if(numItems > 0 ) :
            for i in range(numItems):
                if maxNumber < pw[i]:
                    if(weight[i] < capacity ):
                        maxNumber = pw[i]
                        a = i
            if(weight[a] > capacity ):
                print('Capacity Exceeded')
            else :
                capacity = capacity - weight[a]
                capacity2 = capacity
                profitTotal = profitTotal + profit[a]
                weightTotal = weightTotal + weight[a]
                weightToCarry.append(weight[a])
                profitToCarry.append(profit[a])

                printLap(profit, weight, pw, a, capacity, output_file)

                del pw[a]
                del weight[a]
                del profit[a]

                maxNumber = 0
                a = 0
                calculateProblem(profit, weight, pw, numItems - 1,capacity, output_file)


def printLap(profit, weight, pw, a, capacity, output_file):
    temporalListW = weight[a]
    temporalListP = profit[a]

    with open(output_file, 'a') as file:
        file.write('--------LAP-----------\n')
        file.write(f'Profit: {profit}\n')
        file.write(f'Weight: {weight}\n')
        file.write(f'P/W: {pw}\n')
        file.write('Item selected:\n')
        file.write(f'Profit Item: [{temporalListP}]\n')
        file.write(f'Weight Item: [{temporalListW}]\n')
        file.write(f'capacity: = {capacity}\n')
        file.write(f'profitTotal: {profitTotal}\n')
        file.write(f'weightTotal: {weightTotal}\n')
        file.write('------------------------\n')

def printFinalResult(output_file):
    with open(output_file, 'a') as file:
        file.write('--------Final Result-----------\n')
        file.write(f'profitTotal: {profitTotal}\n')
        file.write(f'weightTotal: {weightTotal}\n')
        file.write(f'finalCapacity: {capacity2}\n')
        file.write('Items to carry with:\n')
        file.write(f'Profit: {profitToCarry}\n')
        file.write(f'Weight: {weightToCarry}\n')

#file_path = "test"
#file_path = "f1_l-d_kp_10_269"
#file_path = "f2_l-d_kp_20_878"
#file_path = "f3_l-d_kp_4_20"
#file_path = "f4_l-d_kp_4_11"
#file_path = "f5_l-d_kp_15_375"
#file_path = "f6_l-d_kp_10_60"
#file_path = "f7_l-d_kp_7_50"
#file_path = "f8_l-d_kp_23_10000"
#file_path = "f9_l-d_kp_5_80"
file_path = "f10_l-d_kp_20_879"
getFileVariables(file_path)
