#ecoding=utf-8
def merge_common(ori_list):
    switch = False
    new_list = []
    length = len(ori_list)
    for i in range(length):
        if switch:
            new_list.append(ori_list[i]*2)
            switch = False
        else:
            if i+1 < length and ori_list[i] == ori_list[i+1]:
                switch = True
            else:
                new_list.append(ori_list[i])
    new_list.extend([0 for i in range(length - len(new_list))])
    return new_list
import time
t1 = time.time()    
ori_list = [0,4,4,4]
print merge_common(ori_list)
print time.time() - t1

# #�������        
# matrix = [
#           ['2','2','2','2'],
#           ['3','4','5','8'],
#           ['32','16','8','54'],
#           ['128','512','1024','2048']
#           ]   
# print [list(row) for row in zip(*matrix)] 
# print [row[::-1] for row in matrix] 

# def get_random(self):
#     #������������Ϊ��һֱ����
#     all_index = [(c,r) for c in range(self.col) for r in range(self.row) if not self.matrix[c][r]]
#     c,r = random.choice(all_index)
#     self.matrix[c][r] = '2'
# 
# def init_matrix(self):
#     self.matrix = [["" for i in range(self.row)] for c in range(self.col)]
#     #���β���������
#     self.get_random()
#     self.get_random()
#     
# def merge_col(self, col):
#         pair_flag = False
#         length = len(col)
#         new_col = []
#         for i in range(length):
#             if pair_flag and col[i]:
#                 self.score+=2*eval(col[i])
#                 new_col.append(str(2*eval(col[i])))
#                 pair_flag = False
#             else:
#                 if i+1 < length and col[i] == col[i+1]:
#                     pair_flag = True
#                 else:
#                     new_col.append(col[i])
#         for i in range(length - len(new_col)):
#             new_col.append('')
#         return new_col
#     
# def move_left(self):
#         for col in range(self.col):
#             newcol = []   #��������ݵĸ���
#             #1��ȡ
#             for row in range(self.row):
#                 if self.matrix[col][row]:
#                     newcol.append(self.matrix[col][row])
#             for i in range(self.row - len(newcol)):
#                 newcol.append('') 
#             #2 �ϲ�
#             newcol = self.merge_col(newcol)
#             #3 �滻
#             self.matrix[col] = newcol
#         self.get_random()
#         self.draw_hor_num(self.matrix)
#         
#ת�þ���
def transpose(matrix):
    return [list(row) for row in zip(*matrix)] 

#����
def invert(matrix):
    return [row[::-1]for row in matrix]