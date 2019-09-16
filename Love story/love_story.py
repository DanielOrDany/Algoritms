from time import time
import unittest

def isSumInArray(array, expected_amount):
    temp_array = []

    if len(array) == 3:
        result_sum = 0

        for locale_sum in array:
            result_sum += locale_sum

        if result_sum == expected_amount:
            return True

    for el in array:
        if el < expected_amount and el != expected_amount - 1:
            temp_array.append(el)

    if len(temp_array) == 3:
        result_sum = 0

        for locale_sum in temp_array:
            result_sum += locale_sum

        if result_sum == expected_amount:
            return True

    else:
        w = len(temp_array)
        n = 2**w

        for i in range(0,n):
            subarray = []

            for j in range(0,w):
                if ( i & (1<<j)): 
                    subarray.append(temp_array[j])

            if len(subarray) == 3:
                result_sum = 0

                for locale_sum in subarray:
                    result_sum += locale_sum

                if result_sum == expected_amount:
                    #print(subarray)
                    return True
    return False

class MyTest(unittest.TestCase):

  def test_on_true(self):
      a = [8,9,5,4,2,2,4,5,2]
      p = 6
      self.assertEqual(isSumInArray(a, p), True)

  def test_on_false(self):
       a = [8,9,5,4,2,2,4,5,1]
       p = 6
       self.assertEqual(isSumInArray(a, p), False)

  def test_on_time(self):
      t0 = time()
      a = [8,9,5,4,2,2,4,5,2]
      p = 6
      print(isSumInArray(a, p))
      t1 = time()
      print ('function isSumInArray takes ', t1-t0)

if __name__ == '__main__':
    unittest.main()
