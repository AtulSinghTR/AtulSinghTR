class Matrix:
    def __init__(self, matrix_string):
        self.list_row = []
        for row in matrix_string.split("\n"):
            str_row=[]
            for val in row.split():
                str_row.append(int(val))
            self.list_row.append(str_row)
      
    
    def row(self, index):
        return self.list_row[index-1]

    def column(self, index):
        list_col=[]
        for row in self.list_row:
            list_col.append(row[index-1])
        return list_col