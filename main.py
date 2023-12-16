from AStar import a_star_search
matrix=[["1R","1","1","5","5","4","2C","1","15","1B"],
        ["1","1","5","3","5","5","4","5","X","X"],
        ["5","1I","1","6","2","2","2","1","1","1T"],
        ["X","X","1","6","5","5","2","1","1","X"],
        ["X","X","1","X","X","50","2","1C","1","X"],
        ["1","1","1","2","2","2T","2","1","1","1"]
        ]
addresses_of_R = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'R' in cell]
print(a_star_search(matrix,start=addresses_of_R[0])[1])
