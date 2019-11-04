import unittest

def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) / 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

def myFunction(array, index, number):
    workArray = array[:index + 1]
    l = len(workArray)

    if l >= 3:
        for first_index in range(l - 2): # 5 too
            last_index = l - 1

            while last_index > first_index + 1:
                needed_number = number - (array[first_index] + array[last_index]) #3: 6 - (0 + 4)
                found_number = binarySearch(workArray, first_index, last_index, needed_number)

                if found_number > 0:
                    return True
                last_index -= 1 #f -> s

        return False
    else:
        return False

def isSumInArray(array, expected_amount):
    array.sort()
    i = binarySearch(array, 0, len(array) - 1, expected_amount)
    if i < 0:
        for x in range(expected_amount, 0, -1):
            j = binarySearch(array, 0, len(array) - 1, x)
            if j > 0:
                #print j
                result = myFunction(array, j, expected_amount)
                return result

    else:
        #print i
        result = myFunction(array, i, expected_amount)
        return result

class MyTest(unittest.TestCase):

  def test_on_true(self):
      a = [1,5,1,4,1,2]
      p = 3
      self.assertEqual(isSumInArray(a, p), True)

  def test_on_false(self):
       a = [8,9,5,4,2,2,4,5,1]
       p = 6
       self.assertEqual(isSumInArray(a, p), False)


if __name__ == '__main__':
    unittest.main()
