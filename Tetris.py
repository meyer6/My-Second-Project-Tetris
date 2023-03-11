import pygame
import datetime
import time
import keyboard
import sys
import random
import math
pygame.init()
pygame.key.set_repeat(200,0)
class rightL(object):
    def __init__(self,colour,start,end,move_finished,block1,block2,block3,block4):
        self.colour=colour
        self.start=start
        self.end=end
        self.move_finished=move_finished
        self.block1=block1
        self.block2=block2
        self.block3=block3
        self.block4=block4
    def spawn_piece(self):
        Board[1][4]=self.colour
        Board[1][5]=self.colour
        Board[2][4]=self.colour
        Board[3][4]=self.colour
        self.block1=[1,4]
        self.block2=[1,5]
        self.block3=[2,4]
        self.block4=[3,4]
    def clear_piece (self):
        Board[self.block1[0]][self.block1[1]]=None
        Board[self.block2[0]][self.block2[1]]=None
        Board[self.block3[0]][self.block3[1]]=None
        Board[self.block4[0]][self.block4[1]]=None
        global holding_board
        holding_board=[[None,None,None,None,None,None],
               [None,None,None,None,None,None],
               [None,None,None,None,None,None],
               [None,None,None,None,None,None],
               [None,None,None,None,None,None]]
    def holding(self):
        holding_board[1][2]=self.colour
        holding_board[1][3]=self.colour
        holding_board[2][2]=self.colour
        holding_board[3][2]=self.colour
    def soft_drop_piece(self):#drops the piece by one after a second
        global moving
        current_time = datetime.datetime.now() 
        if self.move_finished==True:
            self.move_finished=False
            self.start=math.floor(time.time())
            if self.start==59:
                self.start=-1
        else:
            self.end=math.floor(time.time())
            if (self.end-self.start)>=1:
                self.move_finished=True
                Board[self.block1[0]][self.block1[1]]=None
                Board[self.block2[0]][self.block2[1]]=None
                Board[self.block3[0]][self.block3[1]]=None
                Board[self.block4[0]][self.block4[1]]=None
                print(self.block4)
                if self.block1[0]+1<22 and self.block2[0]+1<22 and self.block3[0]+1<22 and self.block4[0]+1<22:
                    if (Board[self.block1[0]+1][(self.block1[1])]==None and Board[self.block2[0]+1][self.block2[1]]==None and
                        Board[self.block3[0]+1][self.block3[1]]==None and Board[self.block4[0]+1][self.block4[1]]==None):
                        self.block1[0]=self.block1[0]+1
                        self.block2[0]=self.block2[0]+1
                        self.block3[0]=self.block3[0]+1
                        self.block4[0]=self.block4[0]+1
                    elif Board[self.block1[0]+1][(self.block1[1])]==None and (self.block1[0]+1==self.block2[0] and self.block1[1]==self.block2[1]) and (self.block1[0]+1==self.block3[0] and self.block1[1]==self.block3[1]) and (self.block1[0]+1==self.block4[0] and self.block1[1]==self.block4[1]):
                        moving=True
                    elif Board[self.block2[0]+1][(self.block2[1])]==None and (self.block2[0]+1==self.block1[0] and self.block2[1]==self.block1[1]) and (self.block2[0]+1==self.block3[0] and self.block2[1]==self.block3[1]) and (self.block2[0]+1==self.block4[0] and self.block2[1]==self.block4[1]):
                        moving=True
                    elif Board[self.block3[0]+1][(self.block3[1])]==None and (self.block3[0]+1==self.block2[0] and self.block3[1]==self.block2[1]) and (self.block3[0]+1==self.block1[0] and self.block3[1]==self.block1[1]) and (self.block3[0]+1==self.block4[0] and self.block3[1]==self.block4[1]):
                        moving=True
                    elif Board[self.block4[0]+1][(self.block4[1])]==None and (self.block4[0]+1==self.block2[0] and self.block4[1]==self.block2[1]) and (self.block4[0]+1==self.block3[0] and self.block4[1]==self.block3[1]) and (self.block4[0]+1==self.block1[0] and self.block4[1]==self.block1[1]):
                        moving=True
                    else:
                        moving=False
                else:
                    moving=False

                Board[self.block1[0]][self.block1[1]]=self.colour
                Board[self.block2[0]][self.block2[1]]=self.colour
                Board[self.block3[0]][self.block3[1]]=self.colour
                Board[self.block4[0]][self.block4[1]]=self.colour
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                Board[self.block1[0]][self.block1[1]]=None
                Board[self.block2[0]][self.block2[1]]=None
                Board[self.block3[0]][self.block3[1]]=None
                Board[self.block4[0]][self.block4[1]]=None
                if self.block1[1]-1>-1 and self.block2[1]-1>-1 and self.block3[1]-1>-1 and self.block4[1]-1>-1:
                    if (Board[self.block1[0]][(self.block1[1]-1)]==None and Board[self.block2[0]][self.block2[1]-1]==None and
                        Board[self.block3[0]][self.block3[1]-1]==None and Board[self.block4[0]][self.block4[1]-1]==None):
                        self.block1[1]=self.block1[1]-1
                        self.block2[1]=self.block2[1]-1
                        self.block3[1]=self.block3[1]-1
                        self.block4[1]=self.block4[1]-1
                Board[self.block1[0]][self.block1[1]]=self.colour
                Board[self.block2[0]][self.block2[1]]=self.colour
                Board[self.block3[0]][self.block3[1]]=self.colour
                Board[self.block4[0]][self.block4[1]]=self.colour
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                Board[self.block1[0]][self.block1[1]]=None
                Board[self.block2[0]][self.block2[1]]=None
                Board[self.block3[0]][self.block3[1]]=None
                Board[self.block4[0]][self.block4[1]]=None
                if self.block1[1]+1<10 and self.block2[1]+1<10 and self.block3[1]+1<10 and self.block4[1]+1<10:
                    if (Board[self.block1[0]][(self.block1[1]+1)]==None and Board[self.block2[0]][self.block2[1]+1]==None and
                        Board[self.block3[0]][self.block3[1]+1]==None and Board[self.block4[0]][self.block4[1]+1]==None):
                        self.block1[1]=self.block1[1]+1
                        self.block2[1]=self.block2[1]+1
                        self.block3[1]=self.block3[1]+1
                        self.block4[1]=self.block4[1]+1
                Board[self.block1[0]][self.block1[1]]=self.colour
                Board[self.block2[0]][self.block2[1]]=self.colour
                Board[self.block3[0]][self.block3[1]]=self.colour
                Board[self.block4[0]][self.block4[1]]=self.colour
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                Board[self.block1[0]][self.block1[1]]=None
                Board[self.block2[0]][self.block2[1]]=None
                Board[self.block3[0]][self.block3[1]]=None
                Board[self.block4[0]][self.block4[1]]=None
                if self.block1[0]+1<22 and self.block2[0]+1<22 and self.block3[0]+1<22 and self.block4[0]+1<22:
                    if (Board[self.block1[0]+1][(self.block1[1])]==None and Board[self.block2[0]+1][self.block2[1]]==None and
                        Board[self.block3[0]+1][self.block3[1]]==None and Board[self.block4[0]+1][self.block4[1]]==None):
                        self.block1[0]=self.block1[0]+1
                        self.block2[0]=self.block2[0]+1
                        self.block3[0]=self.block3[0]+1
                        self.block4[0]=self.block4[0]+1
                Board[self.block1[0]][self.block1[1]]=self.colour
                Board[self.block2[0]][self.block2[1]]=self.colour
                Board[self.block3[0]][self.block3[1]]=self.colour
                Board[self.block4[0]][self.block4[1]]=self.colour

            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                Board[self.block1[0]][self.block1[1]]=None
                Board[self.block2[0]][self.block2[1]]=None
                Board[self.block3[0]][self.block3[1]]=None
                Board[self.block4[0]][self.block4[1]]=None

                block1_matrix=[(self.block1[0]-self.block3[0]),(self.block1[1]-self.block3[1])]
                block1_matrix=[block1_matrix[0]*0+1*block1_matrix[1],-1*block1_matrix[0]+0*block1_matrix[1]]
                potential_block1=[self.block3[0]+block1_matrix[0],self.block3[1]+block1_matrix[1]]

                block2_matrix=[(self.block2[0]-self.block3[0]),(self.block2[1]-self.block3[1])]
                block2_matrix=[block2_matrix[0]*0+1*block2_matrix[1],-1*block2_matrix[0]+0*block2_matrix[1]]
                potential_block2=[self.block3[0]+block2_matrix[0],self.block3[1]+block2_matrix[1]]

                block4_matrix=[(self.block4[0]-self.block3[0]),(self.block4[1]-self.block3[1])]
                block4_matrix=[block4_matrix[0]*0+1*block4_matrix[1],-1*block4_matrix[0]+0*block4_matrix[1]]
                potential_block4=[self.block3[0]+block4_matrix[0],self.block3[1]+block4_matrix[1]]

                if (potential_block1[0]<22 and potential_block2[0]<22 and potential_block4[0]<22 ):
                   if (potential_block1[1]<10 and potential_block2[1]<10 and potential_block4[1]<10 and potential_block1[1]>-1):
                       if(potential_block2[1]>-1 and potential_block4[1]>-1):
                            if (Board[potential_block1[0]][(potential_block1[1])]==None and Board[potential_block2[0]][potential_block2[1]]==None
                                and Board[potential_block4[0]][potential_block4[1]]==None):                                                        
                                    self.block1=potential_block1
                                    self.block2=potential_block2
                                    self.block4=potential_block4
                Board[self.block1[0]][self.block1[1]]=self.colour
                Board[self.block2[0]][self.block2[1]]=self.colour
                Board[self.block3[0]][self.block3[1]]=self.colour
                Board[self.block4[0]][self.block4[1]]=self.colour
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for i in range(22):
                    Board[self.block1[0]][self.block1[1]]=None
                    Board[self.block2[0]][self.block2[1]]=None
                    Board[self.block3[0]][self.block3[1]]=None
                    Board[self.block4[0]][self.block4[1]]=None
                    if self.block1[0]+1<22 and self.block2[0]+1<22 and self.block3[0]+1<22 and self.block4[0]+1<22:
                        if (Board[self.block1[0]+1][(self.block1[1])]==None and Board[self.block2[0]+1][self.block2[1]]==None and
                            Board[self.block3[0]+1][self.block3[1]]==None and Board[self.block4[0]+1][self.block4[1]]==None):
                            self.block1[0]=self.block1[0]+1
                            self.block2[0]=self.block2[0]+1
                            self.block3[0]=self.block3[0]+1
                            self.block4[0]=self.block4[0]+1
                        elif Board[self.block1[0]+1][(self.block1[1])]==None and (self.block1[0]+1==self.block2[0] and self.block1[1]==self.block2[1]) and (self.block1[0]+1==self.block3[0] and self.block1[1]==self.block3[1]) and (self.block1[0]+1==self.block4[0] and self.block1[1]==self.block4[1]):
                            moving=True
                        elif Board[self.block2[0]+1][(self.block2[1])]==None and (self.block2[0]+1==self.block1[0] and self.block2[1]==self.block1[1]) and (self.block2[0]+1==self.block3[0] and self.block2[1]==self.block3[1]) and (self.block2[0]+1==self.block4[0] and self.block2[1]==self.block4[1]):
                            moving=True
                        elif Board[self.block3[0]+1][(self.block3[1])]==None and (self.block3[0]+1==self.block2[0] and self.block3[1]==self.block2[1]) and (self.block3[0]+1==self.block1[0] and self.block3[1]==self.block1[1]) and (self.block3[0]+1==self.block4[0] and self.block3[1]==self.block4[1]):
                            moving=True
                        elif Board[self.block4[0]+1][(self.block4[1])]==None and (self.block4[0]+1==self.block2[0] and self.block4[1]==self.block2[1]) and (self.block4[0]+1==self.block3[0] and self.block4[1]==self.block3[1]) and (self.block4[0]+1==self.block1[0] and self.block4[1]==self.block1[1]):
                            moving=True
                        else:
                            moving=False
                    else:
                        moving=False
                    Board[self.block1[0]][self.block1[1]]=self.colour
                    Board[self.block2[0]][self.block2[1]]=self.colour
                    Board[self.block3[0]][self.block3[1]]=self.colour
                    Board[self.block4[0]][self.block4[1]]=self.colour                    
class leftL(rightL):
    def spawn_piece(self):
        Board[1][4]=self.colour
        Board[1][5]=self.colour
        Board[2][5]=self.colour
        Board[3][5]=self.colour
        self.block1=[1,4]
        self.block2=[1,5]
        self.block3=[2,5]
        self.block4=[3,5]
    def holding(self):
        holding_board[1][2]=self.colour
        holding_board[1][3]=self.colour
        holding_board[2][3]=self.colour
        holding_board[3][3]=self.colour
class line(rightL):
    def spawn_piece(self):
        Board[0][4]=self.colour
        Board[1][4]=self.colour
        Board[2][4]=self.colour
        Board[3][4]=self.colour
        self.block1=[0,4]
        self.block2=[1,4]
        self.block3=[2,4]
        self.block4=[3,4]
    def holding(self):
        holding_board[2][1]=self.colour
        holding_board[2][2]=self.colour
        holding_board[2][3]=self.colour
        holding_board[2][4]=self.colour
class square(rightL):
    def spawn_piece(self):
        Board[2][4]=self.colour
        Board[2][5]=self.colour
        Board[3][4]=self.colour
        Board[3][5]=self.colour
        self.block1=[2,4]
        self.block2=[2,5]
        self.block3=[3,4]
        self.block4=[3,5]
    def holding(self):
        holding_board[1][2]=self.colour
        holding_board[1][3]=self.colour
        holding_board[2][2]=self.colour
        holding_board[2][3]=self.colour
class rightS(rightL):
    def spawn_piece(self):
        Board[1][4]=self.colour
        Board[2][5]=self.colour
        Board[2][4]=self.colour
        Board[3][5]=self.colour
        self.block1=[1,4]
        self.block2=[2,5]
        self.block3=[2,4]
        self.block4=[3,5]
    def holding(self):
        holding_board[1][2]=self.colour
        holding_board[2][3]=self.colour
        holding_board[2][2]=self.colour
        holding_board[3][3]=self.colour
class leftS(rightL):
    def spawn_piece(self):
        Board[1][5]=self.colour
        Board[2][5]=self.colour
        Board[2][4]=self.colour
        Board[3][4]=self.colour
        self.block1=[1,5]
        self.block2=[2,5]
        self.block3=[2,4]
        self.block4=[3,4]
    def holding(self):
        holding_board[1][3]=self.colour
        holding_board[2][3]=self.colour
        holding_board[2][2]=self.colour
        holding_board[3][2]=self.colour
class pyramid(rightL):
    def spawn_piece(self):
        Board[1][4]=self.colour
        Board[3][4]=self.colour
        Board[2][4]=self.colour
        Board[2][5]=self.colour
        self.block1=[1,4]
        self.block2=[3,4]
        self.block3=[2,4]
        self.block4=[2,5]
    def holding(self):
        holding_board[1][2]=self.colour
        holding_board[2][3]=self.colour
        holding_board[2][2]=self.colour
        holding_board[3][2]=self.colour
        
def Game_State_Display(block_size):#displays the coloured blocks based on the configuration of the 2d array Board
    for y in range(22):#displays the grid
        for x in range(10):
            rect = pygame.Rect((x*(block_size+1)), (y*(block_size+1))+1, block_size, block_size)
            pygame.draw.rect(window, colour, rect)
    rect = pygame.Rect((360,0, 351, 649))
    pygame.draw.rect(window, (195,195,195), rect)
    rect = pygame.Rect((410,50, 217, 181))
    pygame.draw.rect(window, (0,0,0), rect)
    for y in range(5):
        for x in range(6):
            rect = pygame.Rect((x*(block_size+1))+411, (y*(block_size+1))+51, block_size, block_size)
            pygame.draw.rect(window, (255,255,255), rect)
    for y in range(5):
        for x in range (6):
            if holding_board[y][x]!=None:
                rect = pygame.Rect((x*(block_size+1))+411, (y*(block_size+1))+51, block_size, block_size)
                pygame.draw.rect(window, (holding_board[y][x]), rect)
    for y in range(4,22):
        for x in range (10):
            if Board[y][x]!=None:
                rect = pygame.Rect((x*(block_size+1)), ((y-4)*(block_size+1))+1, block_size, block_size)
                pygame.draw.rect(window, (Board[y][x]), rect)
    pygame.display.update()     
def clear_line():
    for y in range(4):
        for x in range(10):
            Board[y][x]==None                
    Delete=True
    for y in range(22):
        for x in range(10):
            if Board[y][x]==None:
                Delete=False
        if Delete==True:
            Board.pop(y)
            Board.insert(0,[None,None,None,None,None,None,None,None,None,None])
        Delete=True
window=pygame.display.set_mode((672,649))
pygame.display.set_caption("Tetris")
height=630
width=357
block_size=35
colour=(255,255,255)

purple=(155,1,185)
lightBlue=(0,208,226)
green=(0,232,49)
darkBlue=(4,100,200)
red=(213,10,0)
orange=(244,168,0)
yellow=(255,239,38)
global Board
Board=[[None,None,None,None,None,None,None,None,None,None],#redundant
       [None,None,None,None,None,None,None,None,None,None],#
       [None,None,None,None,None,None,None,None,None,None],#
       [None,None,None,None,None,None,None,None,None,None],#
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None],
       [None,None,None,None,None,None,None,None,None,None]]
global holding_board
holding_board=[[None,None,None,None,None,None],
              [None,None,None,None,None,None],
              [None,None,None,None,None,None],
              [None,None,None,None,None,None],
              [None,None,None,None,None,None]]
RightL=rightL(darkBlue,0,0,True,[],[],[],[])
LeftL=leftL(orange,0,0,True,[],[],[],[])
Line=line(lightBlue,0,0,True,[],[],[],[])
Square=square(yellow,0,0,True,[],[],[],[])
Pyramid=pyramid(purple,0,0,True,[],[],[],[])
RightS=rightS(green,0,0,True,[],[],[],[])
LeftS=leftS(red,0,0,True,[],[],[],[])

Pieces_joined=[RightL,LeftL,Line,Square,Pyramid,RightS,LeftS]
run=True
global moving
moving=False
holding=False
held_piece_class=0
occur_once=0
current_time = datetime.datetime.now()
start=0
holding_change=True
while run:
    end=math.floor(time.time())    
    if keyboard.is_pressed('c') and moving==True and holding==False:
        Current_piece.clear_piece()
        holding=True
        held_piece_class=Current_piece
        moving=False
        start=math.floor(time.time())
    elif keyboard.is_pressed('c') and moving==True and holding==True and end-start>1:
        start=math.floor(time.time())
        Current_piece.clear_piece()
        a=held_piece_class
        held_piece_class=Current_piece
        Current_piece=a
        moving=False
        holding_change=False
    if moving==False:
        clear_line()
        if holding_change==True:
            Current_piece=random.choice(Pieces_joined)
        if holding_change==False:
            holding_change=True
        Current_piece.spawn_piece()
        moving=True
    else:
        if holding==True:
            held_piece_class.holding()
        Current_piece.soft_drop_piece()
        Current_piece.move()
    Game_State_Display(block_size)
