import math
from collections import Counter

class StatEngine:
    def __init__(self, data):
        if not data:                    # if nothing is given
            raise ValueError("Error: Data list cannot be empty!")

        self.data = []                  # this will hold only clean numbers
        
        for item in data:
            try:
                number = float(item)    # try to make it a number
                self.data.append(number)
            except:
                continue                # skip bad items like text or None

        if not self.data:
            raise TypeError("Error: No valid numbers found!")

    def getmean(self):
        # calculate average
        total = sum(self.data)          # add all numbers
        count = len(self.data)          # how many numbers
        return total / count            # average = total / count

    def getmedian(self):
        # find the middle salary
        sorted_data = sorted(self.data) # sort small to big
        n = len(sorted_data)
        
        if n % 2 == 1:                  # odd number of salaries
            return sorted_data[n // 2]  # take the middle one
        else:                           # even number
            middle1 = sorted_data[n//2 - 1]
            middle2 = sorted_data[n//2]
            return (middle1 + middle2) / 2   # average of two middle

    def get_mode(self):
        # find the most common number
        if not self.data:
            return "No data"
        
        freq = Counter(self.data)       # count how many times each number appears
        max_count = max(freq.values())
        
        if max_count == 1:
            return "No unique mode: all values are unique"
        
        modes = [val for val, count in freq.items() if count == max_count]
        return sorted(modes)

    def getvariance(self, is_sample=True):
        # calculate variance
        n = len(self.data)
        if n == 0:
            return 0.0
        
        mean = self.getmean()
        
        # how much each number is away from average
        sum_squared_diff = sum((x - mean) ** 2 for x in self.data)
        
        if is_sample and n > 1:
            return sum_squared_diff / (n - 1)   # sample variance
        else:
            return sum_squared_diff / n         # population variance

    def getstandarddeviation(self, is_sample=True):
        # standard deviation = square root of variance
        variance = self.getvariance(is_sample=is_sample)
        return math.sqrt(variance)

    def get_outliers(self, threshold=2):
        # find salaries that are very different (outliers)
        if len(self.data) < 2:
            return []
        
        mean = self.getmean()
        std = self.getstandarddeviation(is_sample=False)
        
        outliers = []
        for x in self.data:
            if abs(x - mean) > threshold * std:
                outliers.append(x)
        
        return outliers