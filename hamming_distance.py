def hammingDistance(x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binary_x = format(x, '032b')
        binary_y = format(y, '032b')
        counter = 0
        print binary_y
        for i in range(0, len(binary_x)):
            if binary_x[i] != binary_y[i]:
                counter += 1
           
        return counter

if __name__ == "__main__":
    result = hammingDistance(1, 4)
    print result