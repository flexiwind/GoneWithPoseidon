#encoding=utf-8
'''
Created on 2016 5月11

@author: tangfeng
'''

import random

from data import *
import copy

class DrawUi(object):
    
    def __init__(self, row, col):
        self.score = 0
        self.high_score = 0
        self.row = row
        self.col = col
    
    def show_help_string(self):
        print '(W)Up (S)Down (A)Left (D)Right'
        print '(R)Reset (Q)Exit'
            
    def draw_hor_line(self):
        print '%s' % '+----'*self.row + '+'
        
    def draw_hor_num(self, matrix):
        print 'SCORE:%d,     HIGH SCORE:%d' % (self.score, self.high_score)
        for item in range(self.col):
            self.draw_hor_line()
            print '|%s|' % '|'.join(['%4s' % col_num for col_num in matrix[item]])
        self.draw_hor_line()
        self.show_help_string()
    
    def change_score(self, new_score):
        self.score = new_score
    
    def change_high_score(self, new_high_score):
        self.high_score = new_high_score
        
class MatrixUtilFor2048(object):
    
    def __init__(self, matrix, score):
        self.matrix = matrix
        self.score = score
        
    def generate_num(self, base_num):
        #产生随机数，如果不为空一直产生
        index_list = [(col_index, row_index) 
                    for col_index in range(len(self.matrix)) 
                        for row_index in range(len(self.matrix[col_index])) 
                            if self.matrix[col_index][row_index] == ' '
                    ]
        c,r = random.choice(index_list)
        self.matrix[c][r] = base_num
        
    def merge_col(self, col):
        pair_flag = False
        length = len(col)
        new_col = []
        for i in range(length):
            if pair_flag and col[i] != ' ':
                self.score+=2*eval(col[i])
                new_col.append(str(2*eval(col[i])))
                pair_flag = False
            else:
                if i+1 < length and col[i] == col[i+1] and col[i] != ' ':
                    pair_flag = True
                else:
                    new_col.append(col[i])
        for i in range(length - len(new_col)):
            new_col.append(' ')
        return new_col
    
    def get_new_col(self, col):
        newcol = []
        for row in range(len(col)):
            if col[row] != ' ':
                newcol.append(col[row])
        for i in range(len(col) - len(newcol)):
            newcol.append(' ')
        return newcol
    
    def move_left(self):
        for col in range(len(self.matrix)):
            newcol = []   #保存有数据的格子
            #1提取
            newcol = self.get_new_col(self.matrix[col])
            #2 合并
            newcol = self.merge_col(newcol)
            newcol = self.get_new_col(newcol)
            #3 替换
            self.matrix[col] = newcol
            
    def move_is_possible(self):
        col_result = []
        for item in self.matrix:
            for i in range(len(item) - 1):
                if item[i] == ' ' and item[i+1] != ' ':
                    col_result.append(True)
                if item[i] != ' ' and item[i] == item[i+1]:
                    col_result.append(True)
                col_result.append(False)
        return any(col_result)
        
    def get_score(self):
        return self.score    
    
    def get_matrix(self):
        return self.matrix
    
class MainHandle(object):
    
    def __init__(self, col, row, *args):
        self.d1 = DrawUi(col, row)
        self.op = MatrixUtilFor2048(copy.deepcopy(ORG_DATA), self.d1.score)
        self.win = args[0]
        
    def init_2048(self):
        self.op.generate_num('2')
        self.op.generate_num('2')
        init_data = self.op.get_matrix()
        self.d1.draw_hor_num(init_data)
        
    def move_left(self):
        print 'left111'
    
    def move_right(self):
        print 'right2222'
        
    def move_up(self):
        print 'up 33333'
        
    def move_down(self):
        print 'down44444'
        
    def move_direction(self, status):
        move_dict = {
                     'Left':self.move_left,
                     'Right':self.move_right,
                     'Up':self.move_up,
                     'Down':self.move_down,
                     }
        return move_dict.get(status, lambda:'error')
        
        
      
if __name__ == "__main__":
    MH = MainHandle(4,4,2048)
    status = ''
    while(1):
        if not status:
            MH.init_2048()
        next_choice = raw_input()
        try:
            status = ACTIONS_DICT.get(ord(next_choice), ' ')
        except:
            status = ' '
            continue
        a = MH.move_direction(status)()
        if a:
            print a
#         if status == 'Left':
# #             if MH.op.move_is_possible():
# #                 MH.op.move_left()
# #                 MH.op.generate_num('2')
# #                 MH.d1.change_score(MH.op.get_score())
# #                 MH.d1.draw_hor_num(MH.op.get_matrix())
# #             else:
# #                 print 'GameOver'
# #                 if MH.d1.score > MH.d1.high_score:
# #                     MH.d1.change_high_score(MH.d1.score)
# #                 MH.d1.change_score(0)
# #                 MH.op.score = 0
# #                 MH.op.matrix = copy.deepcopy(ORG_DATA)
# #                 MH.init_2048()
# #                     #MH.d1.draw_hor_num(MH.op.get_matrix())
#         elif status == 'Down':
#             pass
#         elif status == 'Right':
#             pass
#         elif status == 'Up':
#             pass
#         elif status == 'Restart':
#             pass
#         elif status == 'Exit':
#             pass
        print status
            
 
    


