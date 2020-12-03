# Matt Morrow
# Class: COP4533
# Prof: Henry Cutler
# Student ID: 2412353
# Collaboration statement: I, Matthew Morrow, have completed this assignment on my own.

import timeit

class BubbleSortList:
    def __init__(self):
        self.intList = []

    #Create add function to append items to the list
    def add(self, listItem):
        self.intList.append(listItem)
    def BubbleSort(self, listItem):
        listLenth = len(self.intList)
        print("The list unsorted is: ", self.intList)

        count = 0
        for count in range(listLenth - 1):

            for pos in range(0, listLenth - count - 1):


                if self.intList[pos] > self.intList[pos+1]:
                    self.intList[pos], self.intList[pos+1] = self.intList[pos+1], self.intList[pos]
        #print("The list bubble sorted is: ", self.intList)


print("****Test File for Sort Algorithm Runtimes****")
count = 0
while count < 1:
    count = count +1
    print("\nBubbleSort Search Test # ", count)



    print(timeit.timeit('''class BubbleSortList:
    def __init__(self):
        self.intList = []

    #Create add function to append items to the list
    def add(self, listItem):
        self.intList.append(listItem)
    def BubbleSort(self, listItem):
        listLenth = len(self.intList)
        print("The list unsorted is: ", self.intList)

        count = 0
        for count in range(listLenth - 1):

            for pos in range(0, listLenth - count - 1):


                if self.intList[pos] > self.intList[pos+1]:
                    self.intList[pos], self.intList[pos+1] = self.intList[pos+1], self.intList[pos]
        print("The list bubble sorted is: ", self.intList)




run1 = BubbleSortList()

run1.add(6)
run1.add(1)
run1.add(3)
run1.add(7)
run1.add(9)
run1.add(2)


run1.BubbleSort(10)




 ''', number = 1))


#Create MergeStringList class to sort using merge sort
class MergeSortList:
    def __init__(self):
        self.list = []

    #Create add function to append items to the list
    def add(self, input):
        self.list.append(input)
    #Create a merge method that merges the two lists together
    def merge(self, leftPos, rightPos):
        #print("The list unsorted is: ", self.list)

        setList = []
        count = 0
        pos = 0
        holdPosition = 0

        while count < len(leftPos) and holdPosition < len(rightPos):
            if len(leftPos[count]) <= len(rightPos[holdPosition]):
                setList.append(leftPos[count])
                count = count + 1
            else:
                setList.append(rightPos[holdPosition])
                pos = pos + 1

        setList += leftPos[count:]
        setList += rightPos[pos:]
        return setList

    def sort(self, nlist):
        if len(nlist) > 1:
            midPoint = len(nlist) // 2
            lefthalf = nlist[:midPoint]
            righthalf = nlist[midPoint:]

            self.sort(lefthalf)
            self.sort(righthalf)
            count = 0
            pos = 0
            holdPosition = 0

            while count < len(lefthalf) and holdPosition < len(righthalf):
                if lefthalf[count] < righthalf[holdPosition]:
                    nlist[pos] = lefthalf[count]
                    count = count + 1
                else:
                    nlist[pos] = righthalf[holdPosition]
                    holdPosition = holdPosition + 1
                pos = pos + 1

            while count < len(lefthalf):
                nlist[pos] = lefthalf[count]
                count = count + 1
                pos = pos + 1

            while holdPosition < len(righthalf):
                nlist[pos] = righthalf[holdPosition]
                holdPosition = holdPosition + 1
                pos = pos + 1

        return nlist

run2 = MergeSortList()
run2.add(6)
run2.add(1)
run2.add(3)
run2.add(7)
run2.add(9)
run2.add(2)

run2.sort(run2.list)
#print("The list merge sorted: ", run2.list)




count = 0
while count < 1:
    count = count +1
    print("\nMergeSort Search Test # ", count)



    print(timeit.timeit('''#Create MergeSort class to sort using merge sort
class MergeSortList:
    def __init__(self):
        self.list = []

    #Create add function to append items to the list
    def add(self, input):
        self.list.append(input)
    #Create a merge method that merges the two lists together

    def merge(self, leftPos, rightPos):

        setList = []
        count = 0
        pos = 0
        holdPosition = 0

        while count < len(leftPos) and holdPosition < len(rightPos):
            if len(leftPos[count]) <= len(rightPos[holdPosition]):
                setList.append(leftPos[count])
                count = count + 1
            else:
                setList.append(rightPos[holdPosition])
                pos = pos + 1

        setList += leftPos[count:]
        setList += rightPos[pos:]
        return setList

    def sort(self, nlist):

        if len(nlist) > 1:
            midPoint = len(nlist) // 2
            lefthalf = nlist[:midPoint]
            righthalf = nlist[midPoint:]

            self.sort(lefthalf)
            self.sort(righthalf)
            count = 0
            pos = 0
            holdPosition = 0

            while count < len(lefthalf) and holdPosition < len(righthalf):
                if lefthalf[count] < righthalf[holdPosition]:
                    nlist[pos] = lefthalf[count]
                    count = count + 1
                else:
                    nlist[pos] = righthalf[holdPosition]
                    holdPosition = holdPosition + 1
                pos = pos + 1

            while count < len(lefthalf):
                nlist[pos] = lefthalf[count]
                count = count + 1
                pos = pos + 1

            while holdPosition < len(righthalf):
                nlist[pos] = righthalf[holdPosition]
                holdPosition = holdPosition + 1
                pos = pos + 1

        return nlist

run2 = MergeSortList()
run2.add(6)
run2.add(1)
run2.add(3)
run2.add(7)
run2.add(9)
run2.add(2)

run2.sort(run2.list)
print("The list merge sorted: ", run2.list)



 ''', number = 1))


#Create the class QuickSort to operate the quicksort algorithm
class QuickSortList:
    def __init__(self):
        self.list = []
    #Create add function to append items to the list
    def add(self, input):
        self.list.append(input)
    #Run the sorting algorithm
    def sort(self, listOfValues):
        #Create three lists to make the sorting comparison

        lessThan = []
        equalValues = []
        greaterThanValues = []
        count = 0

        if len(listOfValues) > 1:

            pivot = listOfValues[0]

            for count in listOfValues:
                if count < pivot:
                    lessThan.append(count)
                elif count == pivot:
                    equalValues.append(count)
                elif count > pivot:
                    greaterThanValues.append(count)

            return self.sort(lessThan) + equalValues + self.sort(greaterThanValues)

        else:
            return listOfValues

run3 = QuickSortList()
run3.add(6)
run3.add(1)
run3.add(3)
run3.add(7)
run3.add(9)
run3.add(2)


#print("The list quick sorted: ", run3.sort(run3.list))


count = 0
while count < 1:
    count = count +1
    print("\nQuickSort Search Test # ", count)



    print(timeit.timeit('''#Create the class QuickSort to operate the quicksort algorithm
class QuickSortList:
    def __init__(self):
        self.list = []
    #Create add function to append items to the list
    def add(self, input):
        self.list.append(input)
    #Run the sorting algorithm
    def sort(self, listOfValues):
        #Create three lists to make the sorting comparison

        lessThan = []
        equalValues = []
        greaterThanValues = []
        count = 0

        if len(listOfValues) > 1:

            pivot = listOfValues[0]

            for count in listOfValues:
                if count < pivot:
                    lessThan.append(count)
                elif count == pivot:
                    equalValues.append(count)
                elif count > pivot:
                    greaterThanValues.append(count)

            return self.sort(lessThan) + equalValues + self.sort(greaterThanValues)

        else:
            return listOfValues

run3 = QuickSortList()
run3.add(6)
run3.add(1)
run3.add(3)
run3.add(7)
run3.add(9)
run3.add(2)


print("The list quick sorted: ", run3.sort(run3.list))



 ''', number = 1))
