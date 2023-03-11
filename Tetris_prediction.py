global Death
Death=False
abc=True
import pygame
import datetime
import time
import keyboard
import sys
import random
import math
while abc==True:
    Death=False
    pygame.init()
    pygame.key.set_repeat(150,0)
    class rightL(object):
        def __init__(self,colour,colour2,start,end,move_finished,block1,block2,block3,block4):
            self.colour=colour
            self.colour2=colour2
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
        def next_piece_spawn(self):
            global next_piece
            next_piece=[[None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None]]
            next_piece[1][2]=self.colour
            next_piece[1][3]=self.colour
            next_piece[2][2]=self.colour
            next_piece[3][2]=self.colour            
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
        def prediction_function(self):
            a=0
            Board[self.block1[0]][self.block1[1]]=None
            Board[self.block2[0]][self.block2[1]]=None
            Board[self.block3[0]][self.block3[1]]=None
            Board[self.block4[0]][self.block4[1]]=None
            Break=False
            for i in range(22):
                if self.block1[0]+i<22 and self.block2[0]+i<22 and self.block3[0]+i<22 and self.block4[0]+i<22 and Break==False:
                    if (Board[self.block1[0]+i][(self.block1[1])]==None and Board[self.block2[0]+i][self.block2[1]]==None and
                        Board[self.block3[0]+i][self.block3[1]]==None and Board[self.block4[0]+i][self.block4[1]]==None):
                        a=i
                    else:
                        Break=True
                        
            for y in range(22):
                for x in range(10):
                    prediction[y][x]=None
            prediction[self.block1[0]+a][self.block1[1]]=self.colour2
            prediction[self.block2[0]+a][self.block2[1]]=self.colour2
            prediction[self.block3[0]+a][self.block3[1]]=self.colour2
            prediction[self.block4[0]+a][self.block4[1]]=self.colour2
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
        def next_piece_spawn(self):
            global next_piece
            next_piece=[[None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None]]
            next_piece[1][2]=self.colour
            next_piece[1][3]=self.colour
            next_piece[2][3]=self.colour
            next_piece[3][3]=self.colour
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
        def next_piece_spawn(self):
            global next_piece
            next_piece=[[None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None]]
            next_piece[2][1]=self.colour
            next_piece[2][2]=self.colour
            next_piece[2][3]=self.colour
            next_piece[2][4]=self.colour
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
        def next_piece_spawn(self):
            global next_piece
            next_piece=[[None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None]]
            next_piece[1][2]=self.colour
            next_piece[1][3]=self.colour
            next_piece[2][2]=self.colour
            next_piece[2][3]=self.colour
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
        def next_piece_spawn(self):
            global next_piece
            next_piece=[[None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None]]
            next_piece[1][2]=self.colour
            next_piece[2][3]=self.colour
            next_piece[2][2]=self.colour
            next_piece[3][3]=self.colour
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
        def next_piece_spawn(self):
            global next_piece
            next_piece=[[None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None]]
            next_piece[1][3]=self.colour
            next_piece[2][3]=self.colour
            next_piece[2][2]=self.colour
            next_piece[3][2]=self.colour
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
        def next_piece_spawn(self):
            global next_piece
            next_piece=[[None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None],
                   [None,None,None,None,None,None]]
            next_piece[1][2]=self.colour
            next_piece[2][3]=self.colour
            next_piece[2][2]=self.colour
            next_piece[3][2]=self.colour
            
    def Game_State_Display(block_size):#displays the coloured blocks based on the configuration of the 2d array Board
        for y in range(22):#displays the grid
            for x in range(10):
                rect = pygame.Rect((x*(block_size+1)), (y*(block_size+1))+1, block_size, block_size)
                pygame.draw.rect(window, colour, rect)
        rect = pygame.Rect((360,1, 349, 647))
        pygame.draw.rect(window, (195,195,195), rect)
        
        rect = pygame.Rect((410,235, 217, 181))
        pygame.draw.rect(window, (0,0,0), rect)

        rect = pygame.Rect((410,130, 217, 73))
        pygame.draw.rect(window, (0,0,0), rect)

        rect = pygame.Rect((410,445, 217, 181))
        pygame.draw.rect(window, (0,0,0), rect)

        rect = pygame.Rect((410,25, 217, 73))
        pygame.draw.rect(window, (0,0,0), rect)
        
        for y in range(2):
            for x in range(6):
                rect = pygame.Rect((x*(block_size+1))+411, (y*(block_size+1))+131, block_size, block_size)
                pygame.draw.rect(window, (255,255,255), rect)
        for y in range(2):
            for x in range(6):
                rect = pygame.Rect((x*(block_size+1))+411, (y*(block_size+1))+26, block_size, block_size)
                pygame.draw.rect(window, (255,255,255), rect)

        pygame.font.init()
        myfont = pygame.font.Font(r'C:\Users\meyer\Desktop\Coding\Python\Tetris\PressStart2P-Regular.ttf',35)
        textsurface = myfont.render(str(score),True, (0, 0, 0))
        textRect = textsurface.get_rect()
        textRect.center = (521, 167)
        window.blit(textsurface,textRect)
        
        myfont = pygame.font.Font(r'C:\Users\meyer\Desktop\Coding\Python\Tetris\PressStart2P-Regular.ttf',15)
        textsurface = myfont.render("HIGH SCORE" ,True, (0, 0, 0))
        textRect = textsurface.get_rect()
        textRect.center = (521, 45)
        window.blit(textsurface,textRect)
        f = open('High_Score.txt','r')
        High_Score = (f.read())
        f.close()
        textsurface = myfont.render(High_Score ,True, (0, 0, 0))
        textRect = textsurface.get_rect()
        textRect.center = (521, 80)
        window.blit(textsurface,textRect)
        for y in range(5):
            for x in range(6):
                rect = pygame.Rect((x*(block_size+1))+411, (y*(block_size+1))+446, block_size, block_size)
                pygame.draw.rect(window, (255,255,255), rect)
        for y in range(5):
            for x in range (6):
                if next_piece[y][x]!=None:
                    rect = pygame.Rect((x*(block_size+1))+411, (y*(block_size+1))+446, block_size, block_size)
                    pygame.draw.rect(window, (next_piece[y][x]), rect)
        for y in range(5):
            for x in range(6):
                rect = pygame.Rect((x*(block_size+1))+411, (y*(block_size+1))+236, block_size, block_size)
                pygame.draw.rect(window, (255,255,255), rect)
        for y in range(5):
            for x in range (6):
                if holding_board[y][x]!=None:
                    rect = pygame.Rect((x*(block_size+1))+411, (y*(block_size+1))+236, block_size, block_size)
                    pygame.draw.rect(window, (holding_board[y][x]), rect)
        for y in range(4,22):
            for x in range (10):
                if prediction[y][x]!=None:
                    rect = pygame.Rect((x*(block_size+1)), ((y-4)*(block_size+1))+1, block_size, block_size)
                    pygame.draw.rect(window, (prediction[y][x]), rect)
        for y in range(4,22):
            for x in range (10):
                if Board[y][x]!=None:
                    rect = pygame.Rect((x*(block_size+1)), ((y-4)*(block_size+1))+1, block_size, block_size)
                    pygame.draw.rect(window, (Board[y][x]), rect)

        pygame.display.update()     
    def clear_line():
        global score
        global Death
        for y in range(4):
            for x in range(10):
                Board[y][x]==None                
        Delete=True
        a=0
        for y in range(22):
            for x in range(10):
                if Board[y][x]==None:
                    Delete=False
            if Delete==True:
                Board.pop(y)
                Board.insert(0,[None,None,None,None,None,None,None,None,None,None])
                a=a+1
            Delete=True
        if a==1:
            score=score+120
        if a==2:
            score=score+300
        if a==3:
            score=score+900
        if a==4:
            score=score+3600
        else:
            score=score+25
        f = open('High_Score.txt','r')
        High_Score = int(f.read())
        if High_Score<score:
            f = open('High_Score.txt','w')
            f.truncate()
            f.write(str(score))
        f.close()
        for i in range(10):
            if Board[3][i]!=None:
                Death=True
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
    global next_piece
    next_piece=[[None,None,None,None,None,None],
                  [None,None,None,None,None,None],
                  [None,None,None,None,None,None],
                  [None,None,None,None,None,None],
                  [None,None,None,None,None,None]]
    RightL=rightL(darkBlue,(138, 178, 224),0,0,True,[],[],[],[])
    LeftL=leftL(orange,(253, 211, 187),0,0,True,[],[],[],[])
    Line=line(lightBlue, (193, 227, 254),0,0,True,[],[],[],[])
    Square=square(yellow, (253, 246, 220),0,0,True,[],[],[],[])
    Pyramid=pyramid(purple, (207, 182, 229),0,0,True,[],[],[],[])
    RightS=rightS(green,(201, 222, 206),0,0,True,[],[],[],[])
    LeftS=leftS(red,(252, 204, 204),0,0,True,[],[],[],[])

    Pieces_joined=[RightL,LeftL,Line,Square,Pyramid,RightS,LeftS]
    run=True
    global moving
    moving=False
    holding=False
    held_piece_class=0
    occur_once=0
    current_time = datetime.datetime.now()
    tart=0
    holding_change=False
    global prediction
    prediction=[[None,None,None,None,None,None,None,None,None,None],#redundant
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
    Current_piece=random.choice(Pieces_joined)
    Next_piece=random.choice(Pieces_joined)
    Next_piece.next_piece_spawn()
    global score
    score=0
    while Death==False:
        pygame.time.wait(15)
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
            if holding_change==True:
                clear_line()
                Current_piece=Next_piece
                Next_piece=random.choice(Pieces_joined)
                Next_piece.next_piece_spawn()
            if holding_change==False:
                holding_change=True
            Current_piece.spawn_piece()
            moving=True
        else:
            if holding==True:
                held_piece_class.holding()          
            Current_piece.soft_drop_piece()
            Current_piece.move()
            Current_piece.prediction_function()
        Game_State_Display(block_size)
