class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
                #判断新的点是否合理
        #chess_list，记录Q所在位置
        #形式 [[row,col],[row,col],[row,col]]
        def is_valid(chess_list,nr,nc,n):
            if len(chess_list)==0:
                return True                
            for i in range(len(chess_list)):
                #同行、同列
                if chess_list[i][0]==nr or chess_list[i][1]==nc:
                    return False
                #斜
                if abs(nr-chess_list[i][0]) == abs(nc-chess_list[i][1]):
                    return False
            return True
        
        #递归获取结果
        def get_solution(chess_list, new_row, n):
            solution_list = []
            if new_row >= n-1:
                #最后一行
                for col in range(n):
                    if is_valid(chess_list, new_row, col, n):
                        chess_list.append([new_row, col])
                        #一旦到达最后一行，就只可能有一个正确结果
                        new_chess_list = chess_list.copy()
                        solution_list.append(new_chess_list)
                        chess_list.pop()
                return solution_list
            else:
            #其他列
                for col in range(n):
                    if is_valid(chess_list, new_row, col, n):
                        chess_list.append([new_row,col])
                        temp_solution_list=get_solution(chess_list, new_row+1, n)
                        for i in range(len(temp_solution_list)):
                            solution_list.append(temp_solution_list[i])
                        chess_list.pop()
            return solution_list
        
        chess_list = []
        solution_list_str = []
        solution_list = get_solution(chess_list,0,n)
        return len(solution_list)
