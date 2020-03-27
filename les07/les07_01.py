class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        result = []
        minrows = min(len(self.matrix), len(other.matrix))
        maxrows = max(len(self.matrix), len(other.matrix))

        if len(other.matrix) < maxrows:
            for i in range(minrows, maxrows):
                row = [0 for j in range(len(other.matrix[0]))]
                other.matrix.append(row)
        else:
            for i in range(minrows, maxrows):
                row = [0 for j in range(len(self.matrix[0]))]
                self.matrix.append(row)

        for i in range(maxrows):
            mincols = min(len(self.matrix[0]), len(other.matrix[0]))
            sum = [self.matrix[i][j] + other.matrix[i][j] for j in range(mincols)] + self.matrix[i][mincols:] + other.matrix[i][mincols:]
            result.append(sum)

        result = Matrix(result)
        return '\n'.join(' '.join(map(str, row)) for row in result.matrix)




m1 = Matrix([[31, 22], [37, 43], [51, 86]])
m2 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

# print(m1.__str__())
print(m2 + m1)