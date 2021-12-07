import pygame
from math import ceil
from time import time
from algs_description import descriptionsDict
import queue
import random

# Initialize pygame modules
pygame.init()

# Display settings
windowSize = (900, 600)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Sorting Algorithms Visualizer')

# Font
baseFont = pygame.font.SysFont('Arial', 24)
smallFont = pygame.font.SysFont('Arial', 18)
# Used Colors
grey = (100, 100, 100)
green = (125, 240, 125)
white = (250, 250, 250)
red = (255, 50, 50)
black = (0, 0, 0)
blue = (50, 50, 255)


class Box:
    def __init__(self, rect):
        self.isActive = False
        self.rect     = pygame.Rect(rect)
    
    def update(self):
        self.mousePos = pygame.mouse.get_pos()
        self.clicked  = pygame.mouse.get_pressed() != (0, 0, 0)
        self.isActive = True if self.rect.collidepoint(self.mousePos) else False


class InputBox(Box):
    def __init__(self, name, color, rect):
        super().__init__(rect)
        self.name  = name
        self.color = color
        
    def draw(self):
        label = baseFont.render(self.name, True, self.color)
        screen.blit(label, (self.rect.x + (self.rect.w - label.get_width()) / 2, self.rect.y - 32))
        pygame.draw.rect(screen, self.color, self.rect, 3)


class TextBox(InputBox):
    def __init__(self, name, color, rect, text='100'):
        super().__init__(name, color, rect)
        self.text = text
        self.draw() # establish the correct width for initial rendering
    
    def draw(self):
        super().draw()
        surface = baseFont.render(self.text, True, self.color)
        screen.blit(surface, (self.rect.x + 10, self.rect.y + 10))
        self.rect.w = max(surface.get_width() + 20, 50)

    def update(self, event):
        super().update()
        if self.isActive and event.type == pygame.KEYDOWN:
            if   event.key == pygame.K_BACKSPACE: self.text = self.text[:-1]
            elif event.unicode.isdigit()        : self.text += event.unicode
        

class SlideBox(InputBox):
    def __init__(self, name, color, rect):
        super().__init__(name, color, rect)
        self.start = self.rect.x + 6
        self.end   = self.rect.x + self.rect.w - 6
        self.value = self.start

    def draw(self):
        super().draw()
        pygame.draw.line(screen, self.color, (self.start, self.rect.y + 25), (self.end, self.rect.y + 25), 2)
        pygame.draw.line(screen, self.color, (self.value, self.rect.y + 5), (self.value, self.rect.y + 45), 12)

    def update(self, event):
        super().update()
        previousStart = self.start
        self.rect.x = sizeBox.rect.x + sizeBox.rect.w + 20
        self.start  = self.rect.x + 6
        self.end    = self.rect.x + self.rect.w - 6
        self.value += self.start - previousStart
        
        if self.isActive:
            if self.clicked:
                if self.start <= self.mousePos[0] <= self.end: self.value = self.mousePos[0]
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if   event.button == 4: self.value = min(self.value + 10, self.end)
                elif event.button == 5: self.value = max(self.value - 10, self.start)

class VerticalSliderBox(InputBox):
    def __init__(self, name, color, rect):
        super().__init__(name, color, rect)
        self.start = self.rect.y+6
        self.end   = self.rect.y+self.rect.h
        self.value = self.start
        self.isActive=True

    def draw(self):
        x=self.rect.x
        pygame.draw.line(screen, grey,  (x,  self.start-6),  (x,self.end), 25)
        pygame.draw.line(screen, white, (x+5,  self.value),  (x+5,self.value+20), 8)

    def update(self,event):
        super().update()
        previousStart = self.start
        self.start = self.rect.y+6
        self.end   = self.rect.y + self.rect.h
        self.value += self.start - previousStart
        if self.isActive:
            if self.clicked:
                if self.start <= self.mousePos[1] <= self.end: self.value = self.mousePos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if   event.button == 4: self.value = min(self.end  ,self.value + 10)
                elif event.button == 5: self.value = max(self.start,self.value - 10)

class ButtonBox(Box):
    def __init__(self, img_path, rect):
        super().__init__(rect)
        self.img = pygame.image.load(img_path)
    
    def draw(self):
        self.rect.x = algorithmBox.rect.x + algorithmBox.rect.w + 20
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def update(self):
       super().update()
       if self.isActive: self.isActive = True if self.clicked else False


class DropdownBox(InputBox):
    DEFAUTL_OPTION = 0

    def __init__(self, name, rect, font, color=grey):
        super().__init__(name, color, rect)
        self.isActive      = False
        self.font          = font
        self.options_color = white
        self.active_option = -1
        
    def add_options(self, options):
        self.options = options
        dropdown_width = ceil((len(self.options)-1) * self.rect.height / self.rect.y) * self.rect.width
        self.dropdown_rect = pygame.Rect((self.rect.x, 0, dropdown_width, self.rect.y))

    def get_active_option(self):
        return self.options[self.DEFAUTL_OPTION]

    def draw(self):
        super().draw()
        option_text = self.font.render(self.options[self.DEFAUTL_OPTION], 1, grey)
        screen.blit(option_text, option_text.get_rect(center=self.rect.center))

        if self.isActive:
            column = 0
            index = 0
            rect_start = self.rect.y - self.rect.height
            for i in range(self.DEFAUTL_OPTION+1, len(self.options)):
                rect = self.rect.copy()
                rect.y -= (index + 1) * self.rect.height
                if rect.y <= self.dropdown_rect.y:
                    column += 1
                    index = 0
                    rect.y = rect_start
                index += 1
                rect.x = self.rect.x + column * self.rect.width
                
                options_color = black if i - 1 == self.active_option else grey
                pygame.draw.rect(screen, self.options_color, rect, 0)
                pygame.draw.rect(screen, self.color, rect, 3) # draw border
                option_text = self.font.render(self.options[i][:12], 1, options_color)
                screen.blit(option_text, option_text.get_rect(center=rect.center))

    def update(self):
        self.rect.x = delayBox.rect.w + delayBox.rect.x + 20
        mouse_position = pygame.mouse.get_pos()
        column = 0
        index = 0
        rect_start = self.rect.y - self.rect.height
        for i in range(len(self.options)-1):
            rect = self.rect.copy()
            rect.y -= (index + 1) * self.rect.height
            if rect.y <= self.dropdown_rect.y:
                column += 1
                index = 0
                rect.y = rect_start
            index += 1
            rect.x = self.rect.x + column * self.rect.width

            if rect.collidepoint(mouse_position):
                self.active_option = i
        
        if pygame.mouse.get_pressed() != (0, 0, 0):
            if self.isActive and self.dropdown_rect.collidepoint(mouse_position):
                self.options[self.DEFAUTL_OPTION], self.options[self.active_option+1] =\
                     self.options[self.active_option+1], self.options[self.DEFAUTL_OPTION]
                self.active_option = -1
            self.isActive = self.rect.collidepoint(mouse_position)
        if not self.isActive:
            self.active_option = -1


class DescriptionBox(InputBox):
    
    desc_box = pygame.Rect((0, 0, 0, 0))
    def __init__(self, name, rect, font, color=grey):
        super().__init__(name, color, rect)
        self.isActive      = False
        self.font          = font
        self.options_color = white

    def draw(self):
        option_text = self.font.render(algorithmBox.get_active_option(), 1, grey)
        screen.blit(option_text, option_text.get_rect(center=(530, 525)))
        label = baseFont.render(self.name, True, self.color)
        screen.blit(label, (480, 500 - 32))
        pygame.draw.rect(screen, self.color, (460, 500, 140, 50), 3)

        if self.isActive:
            chunks = descriptionsDict[algorithmBox.get_active_option()].split('\n')
            n = len(chunks)
            self.desc_box = pygame.Rect((460, 500-n*30, 420, n*30))
            pygame.draw.rect(screen, white, self.desc_box, 0)
            pygame.draw.rect(screen, grey, self.desc_box, 3) # draw border
            chunk_dist=15
            for line in chunks:
                description_text = smallFont.render(line, 1, grey)
                screen.blit(description_text, description_text.get_rect(center=(670, 500-n*30 + chunk_dist)))
                chunk_dist = chunk_dist + 25

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        description_text = self.font.render(descriptionsDict[algorithmBox.get_active_option()], 1, grey)
        
        if pygame.mouse.get_pressed() != (0, 0, 0):
            desc_rect = pygame.Rect((460, 500, 140, 50))
            if desc_rect.collidepoint(mouse_position) and not self.isActive:
                self.isActive = True
            elif self.isActive and self.desc_box.collidepoint(mouse_position):
                self.isActive = True
            else:
                self.isActive = False

class GraphBox(InputBox):
    def __init__(self, name, color, rect):
        super().__init__(name, color, rect)
        self.isActive      = False

    def draw(self):
        #super().draw()
        label = baseFont.render(self.name, True, self.color)
        screen.blit(label, label.get_rect(center=(700, 525)))
        pygame.draw.rect(screen, self.color, (630, 500, 140, 50), 3)

    def update(self):
        #super().update()
        mouse_position = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() != (0, 0, 0) and self.rect.collidepoint(mouse_position):
            self.isActive = True
            
    def setFalse(self):
        self.isActive = False


# END OF MODULE #


# Global Variables
numBars = 0
delay   = 0
do_sorting = False
paused = False
timer_space_bar   = 0


# Input Boxes
sizeBox        = TextBox('Size', grey, (30, 500, 50, 50), '100')
delayBox       = SlideBox('Delay', grey, (105, 500, 112, 50))
algorithmBox   = DropdownBox('Algorithm', (242, 500, 140, 50), baseFont)
playButton     = ButtonBox('images/playButton.png', (390, 500, 50, 50))
stopButton     = ButtonBox('images/stopButton.png', (390, 500, 50, 50))
descBox        = DescriptionBox('Description', (460, 500, 140, 50), baseFont)
graphBox       = GraphBox('Graph', grey, (620, 500, 140, 50))


def updateWidgets(event):
    sizeBox.update(event)
    delayBox.update(event)
    algorithmBox.update()
    if do_sorting:
        stopButton.update()
    else:
        playButton.update()
    descBox.update()
    algorithmBox.update()
    graphBox.update()

def drawBars(array, redBar1, redBar2, blueBar1, blueBar2, greenRows = {}, **kwargs):
    '''Draw the bars and control their colors'''
    if numBars != 0:
        bar_width  = 900 / numBars
        ceil_width = ceil(bar_width)
    
    # Coordinate Added
    max_value = 0
    if len(array)!=0:
        max_value = max(array)
        for cord in range(5):
            y_cord = round(max_value/5) * (cord + 1)
            coordinate = baseFont.render(str(y_cord), True, grey)
            screen.blit(coordinate, (15, 450 - y_cord - 15))
            pygame.draw.line(screen, red, (0, 450 - y_cord), (10, 450 - y_cord))

    for num in range(numBars):
        if   num in (redBar1, redBar2)  : color = red
        elif num in (blueBar1, blueBar2): color = blue
        elif num in greenRows           : color = green        
        else                            : color = grey
        pygame.draw.rect(screen, color, (num * bar_width, 450 - array[num], ceil_width, array[num]))


def drawBottomMenu():
    '''Draw the menu below the bars'''
    sizeBox.draw()
    delayBox.draw()
    algorithmBox.draw()
    if do_sorting:
        stopButton.draw()
    else:
        playButton.draw()
    descBox.draw() 
    algorithmBox.draw()
    graphBox.draw()


def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


def draw_polygon_alpha(surface, color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)


def drawInterface(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs):
    '''Draw all the interface'''
    screen.fill(white)
    drawBars(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs)
    
    if paused and (time()-timer_space_bar)<0.5:
        draw_rect_alpha(screen,(255, 255, 0, 127),[(850/2)+10, 150+10, 10, 50])
        draw_rect_alpha(screen,(255, 255, 0, 127),[(850/2)+40, 150+10, 10, 50])
        
    elif not paused and (time()-timer_space_bar)<0.5:
        x,y = (850/2),150
        draw_polygon_alpha(screen, (150, 255, 150, 127), ((x+10,y+10),(x+10,y+50+10),(x+50,y+25+10)))
        
    drawBottomMenu()
    pygame.display.update()
    
    
    

################################### graph algorithm


SIZE = 30
WHITE = (255,255,255)
BLACK = (0,0,0)
# YELLOW = (255,255,0)
YELLOW = (139,0,0)
BLUE = (0,0,255)

#screen = pygame.display.set_mode((900,600))
#pygame.display.set_caption("Graph Algorithm Visualizer")

left_background = pygame.image.load('./Graph/background.png')
node1 = pygame.image.load('./Graph/r_circle.png')
node2 = pygame.image.load('./Graph/b_circle.png')
node3 = pygame.image.load('./Graph/y_circle.png')
plus = pygame.image.load('./Graph/plus.png')
add = pygame.image.load('./Graph/add.png')
cross = pygame.image.load('./Graph/cross.png')
algo_button = pygame.image.load('./Graph/algo_button.png')

button_font = pygame.font.Font('./Graph/roboto.ttf', 20)
msg_font = pygame.font.Font('./Graph/roboto.ttf', 15)

add_node = button_font.render('Add Nodes', True, WHITE)
add_edge = button_font.render('Add Edges', True, WHITE)
dfs_button = button_font.render('DFS', True, WHITE) 
bfs_button = button_font.render('BFS', True, WHITE)
find_bridges_button = button_font.render('Find Bridges', True, WHITE)
clear_button = button_font.render('Clear Screen', True, WHITE)
sort_button = button_font.render('SORT', True, WHITE) 
init_button = button_font.render('Initialize', True, WHITE)
msg_box = msg_font.render('', True, BLUE);

node_button = plus
edge_button = add
nodes = []
# pos = []
edges = []
yellow_edges = []
blue_edges = []
color = [node2,node1,node3]
node_color = []
pos = (-1,-1)
pointA = -1
pointB = -1
point = -1
state = 'start'
msg = ''

def initialize():
    available_pos1 = [i for i in range(220, 760, 25)]
    available_pos2 = [i for i in range(0, 550, 25)]
    selected_pos = {}
    j = 1
    while j <= SIZE:
        pos1_idx = random.randint(0, len(available_pos1)-1)
        pos2_idx = random.randint(0, len(available_pos2)-1)

        if ((pos1_idx, pos2_idx) not in selected_pos):
            pos1 = available_pos1[pos1_idx]
            pos2 = available_pos2[pos2_idx]
            selected_pos[(pos1_idx, pos2_idx)] = 1
        else:
            continue

        j += 1
        nodes.append((pos1, pos2))
        node_color.append(color[0])

    max_edges = int(SIZE * (SIZE-1)/2)
    min_edges = SIZE-1
    edge_nos = random.randint(min_edges, max_edges)
    curr_edge = 0

    while curr_edge <= edge_nos:
        src_node = random.randint(0, len(nodes)-1)
        dst_node = random.randint(0, len(nodes)-1)
        if src_node != dst_node:
            edges.append((src_node, dst_node))
            edges.append((dst_node, src_node))
            curr_edge += 1
        else:
            continue
        
        


def dfs(s,vis,adj):
    vis[s] = 1
    node_color[s] = color[1]
    show_edges()
    show_nodes()
    pygame.display.update()
    pygame.time.delay(200)
    for i in range(len(adj[s])):
        if vis[adj[s][i]] != 1:
            yellow_edges.append((s,adj[s][i]))
            yellow_edges.append((adj[s][i],s))
            show_edges()
            show_nodes()
            pygame.display.update()
            pygame.time.delay(200)
            dfs(adj[s][i],vis,adj)

def start_dfs(point):
    if(len(nodes)==0 or len(edges)==0):
        return
    adj = [[] for i in range(len(nodes))]
    vis = [0 for i in range(len(nodes))]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
    dfs(point,vis,adj)

def bfs(s,dis,adj):
    level = 0
    q = queue.Queue()
    q.put((level,s))
    global screen,nodes
    dis[s] = 0
    node_color[s] = color[1]
    show_edges()
    show_nodes()
    pygame.display.update()
    pygame.time.delay(200)
    
    while not q.empty():
        f = q.queue[0];
        if(f[0] == (level+1)%2):
            level = (level+1)%2
            continue
        q.get()
        u = f[1]
        for i in range(len(adj[u])):
            if dis[adj[u][i]] == 1e9:
                yellow_edges.append((u,adj[u][i]))
                yellow_edges.append((adj[u][i],u))
                node_color[adj[u][i]] = color[1]
                show_edges()
                show_nodes()
                pygame.display.update()
                pygame.time.delay(200)
                dis[adj[u][i]] = dis[u] + 1
                q.put(((level+1)%2,adj[u][i]))
    
def start_bfs(point):
    if(len(nodes)==0 or len(edges)==0):
        return
    adj = [[] for i in range(len(nodes))]
    dis = [1e9 for i in range(len(nodes))]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
    bfs(point,dis,adj)

def find_bridges(u,counter,dfs_num,dfs_low,par,adj):
    counter = counter + 1
    dfs_num[u] = counter
    dfs_low[u] = counter
    ch_count = 0
    
    node_color[u] = color[1]
    show_edges()
    show_nodes()
    pygame.display.update()
    pygame.time.delay(200)
    
    for i in range(len(adj[u])):
        v = adj[u][i]
        if par[u] == v:
            continue
        if dfs_num[v] == 0:
            
            yellow_edges.append((u,v))
            yellow_edges.append((v,u))
            show_edges()
            show_nodes()
            pygame.display.update()
            pygame.time.delay(200)
            
            ch_count = ch_count + 1
            par[v] = u
            find_bridges(v,counter,dfs_num,dfs_low,par,adj)
            dfs_low[u] = min(dfs_low[u],dfs_low[v])
            
            show = False
            if par[u]!=-1 and dfs_low[v]>=dfs_num[u]:
                show = True
                node_color[u] = color[2]
                
            if dfs_low[v]>dfs_num[u]:
                show = True
                blue_edges.append((u,v))
                blue_edges.append((v,u))
                
            if show:
                show_edges()
                show_nodes()
                pygame.display.update()
                pygame.time.delay(500)
        else:
            dfs_low[u] = min(dfs_low[u],dfs_num[v])
            
    if ch_count>1 and par[u]==-1:
        node_color[u] = color[2]
        show_edges()
        show_nodes()
        pygame.display.update()
        pygame.time.delay(200)

def start_finding_bridges():
    n = len(nodes)
    m = len(edges)
    if(n==0 or m==0):
        return
    adj = [[] for i in range(n)]
    for i in range(m):
        adj[edges[i][0]].append(edges[i][1])
    counter = 0
    dfs_num = [0 for i in range(n)]
    dfs_low = [0 for i in range(m)]
    par = [0 for i in range(n)]
    for i in range(n):
        if dfs_num[i] == 0:
            par[i] = -1
            find_bridges(i,counter,dfs_num,dfs_low,par,adj)
            counter = 0
    
def make_equal(listA, listB):
    for i in range(len(listA)):
        listA[i] =listB[i]

def isClicked(x1,y1,x2,y2,mos_x,mos_y):
    if mos_x>x1 and (mos_x<x2):
        x_inside = True
    else: x_inside = False
    if mos_y>y1 and (mos_y<y2):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        return True
    else:
        return False

def ishovering(x1,y1,x2,y2):
    mos_x, mos_y = pygame.mouse.get_pos()
    if mos_x>x1 and (mos_x<x2):
        x_inside = True
    else: x_inside = False
    if mos_y>y1 and (mos_y<y2):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        return True
    else:
        return False

def getNode(mos_x,mos_y):
    for i in range(len(nodes)):
        x1 = nodes[i][0]
        y1 = nodes[i][1]
        if isClicked(x1, y1, x1 + node2.get_width(), y1 + node2.get_height(), mos_x, mos_y):
            return i
    return -1

def show_nodes():
    if(len(nodes)==0): return
    for i in range(len(nodes)):
        screen.blit(node_color[i],nodes[i])

def show_edges():
    if(len(edges)==0): return
    for i in range(len(edges)):
            pygame.draw.line(screen,BLACK,(nodes[edges[i][0]][0]+16,nodes[edges[i][0]][1]+16),(nodes[edges[i][1]][0]+16,nodes[edges[i][1]][1]+16),1)
    for i in range(len(yellow_edges)):
            pygame.draw.line(screen,YELLOW,(nodes[yellow_edges[i][0]][0]+16,nodes[yellow_edges[i][0]][1]+16),(nodes[yellow_edges[i][1]][0]+16,nodes[yellow_edges[i][1]][1]+16),1)
    for i in range(len(blue_edges)):
            pygame.draw.line(screen,BLUE,(nodes[blue_edges[i][0]][0]+16,nodes[blue_edges[i][0]][1]+16),(nodes[blue_edges[i][1]][0]+16,nodes[blue_edges[i][1]][1]+16),2)

def show_buttons():
    global state
    if(state == 'start'):
        screen.blit(algo_button,(7,550))
        screen.blit(clear_button,(7+algo_button.get_width()/2-53,550+algo_button.get_height()/2-13))
        screen.blit(algo_button,(7,498))
        screen.blit(dfs_button,(7+algo_button.get_width()/2-20,498+algo_button.get_height()/2-13))
        screen.blit(algo_button,(7,446))
        screen.blit(bfs_button,(7+algo_button.get_width()/2-20,446+algo_button.get_height()/2-13))
        screen.blit(algo_button,(7,394))
        screen.blit(find_bridges_button,(7+algo_button.get_width()/2-50,394+algo_button.get_height()/2-13))
        screen.blit(algo_button,(7,342))
        screen.blit(sort_button,(7+algo_button.get_width()/2-25,342+algo_button.get_height()/2-13))
        screen.blit(algo_button,(7,290))
        screen.blit(init_button,(7+algo_button.get_width()/2-40,290+algo_button.get_height()/2-13))
        
def show_msg():
    msg_box = msg_font.render(msg, True, BLUE);
    screen.blit(msg_box,(215,570))
    

def run_graph():
    global state, node_button, edge_button
    running = True
    initialize()
    while running:
        screen.fill(WHITE)
        screen.blit(left_background,(0,0))
        
        if(state == 'start' or state == 'add_node' or state == 'exit'):
            screen.blit(node_button,(5,5))
            
        if(state == 'start' or state == 'add_edge1' or state == 'add_edge2'):
            screen.blit(edge_button,(5,42))
            
        show_buttons()
        show_msg()
        
        if state == 'start':
            node_button = plus
            edge_button = add
            if(ishovering(5,5,5+node_button.get_width(),5+node_button.get_height())):
                screen.blit(add_node,(60,12))
            if(ishovering(5,42,5+edge_button.get_width(),42+edge_button.get_height())):
                screen.blit(add_edge,(60,48))
                
        if state == 'dfs':
            temp_node = [color[0] for i in range(len(node_color))]
            make_equal(temp_node,node_color)
            start_dfs(point)
            make_equal(node_color,temp_node)
            yellow_edges.clear()
            state = 'start'  
            point = -1
            
        if state == 'bfs':
            temp_node = [color[0] for i in range(len(node_color))]
            make_equal(temp_node,node_color)
            start_bfs(point)
            make_equal(node_color,temp_node)
            yellow_edges.clear()
            state = 'start'  
            point = -1
        
        if state == 'find_bridges':
            temp_node = [color[0] for i in range(len(node_color))]
            make_equal(temp_node,node_color)
            start_finding_bridges()
            state = 'exit'
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break;
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0]!=-1 & pos[1]!=-1):
                    if state == 'start':
                        if(isClicked(7,498,7+algo_button.get_width(),498+algo_button.get_height(),pos[0],pos[1])):
                            if len(nodes) != 0:
                                state = 'choose start point for dfs'
                                msg = 'Choose source for the Depth First Search.'
                            else: state = 'start'
                        elif(isClicked(5,5,5+node_button.get_width(),5+node_button.get_height(),pos[0],pos[1])):
                            state = 'add_node'
                            msg = 'Click on the screen to add a node there.'
                            node_button = cross
                            edge_button = cross
                        elif(isClicked(5,42,5+edge_button.get_width(),42+edge_button.get_height(),pos[0],pos[1])):
                            msg = 'Choose initial vertex of the edge.'
                            state = 'add_edge1'
                            node_button = cross
                            edge_button = cross
                        elif(isClicked(7,446,7+algo_button.get_width(),446+algo_button.get_height(),pos[0],pos[1])):
                            if len(nodes) != 0:
                                state = 'choose start point for bfs'
                                msg = 'Choose source for the Breadth First Search.'
                            else: state = 'start'
                        elif(isClicked(7,394,7+algo_button.get_width(),394+algo_button.get_height(),pos[0],pos[1])):
                            if len(nodes) != 0:
                                node_button = cross
                                state = 'find_bridges'
                                msg = 'Articution Points: Yellow nodes    Bridges: Blue edges'
                            else: state = 'start'
                        elif(isClicked(7,550,7+algo_button.get_width(),550+algo_button.get_height(),pos[0],pos[1])):
                            nodes.clear()
                            node_color.clear()
                            edges.clear()
                        elif(isClicked(7,342,7+algo_button.get_width(),342+algo_button.get_height(),pos[0],pos[1])):
                            running = False
                            nodes.clear()
                            node_color.clear()
                            edges.clear()
                            break
                        elif(isClicked(7,290,7+algo_button.get_width(),290+algo_button.get_height(),pos[0],pos[1])):
                            nodes.clear()
                            node_color.clear()
                            edges.clear()
                            initialize()
                    elif state == 'add_node':
                        if pos[0]>200 and pos[1]<550:
                            nodes.append((pos[0]-16,pos[1]-16))
                            node_color.append(color[0])
                        if(isClicked(5,5,5+node_button.get_width(),5+node_button.get_height(),pos[0],pos[1])):
                            state = 'start'
                            msg = ''
                    elif state == 'add_edge1':
                        pointA = getNode(pos[0],pos[1])
                        if(pointA != -1):
                            state = 'add_edge2'
                            msg = 'Choose terminal vertex of the edge.'
                        if(isClicked(5,42,5+edge_button.get_width(),42+edge_button.get_height(),pos[0],pos[1])):
                            state = 'start'
                            msg = ''
                    elif state == 'add_edge2':
                        pointB = getNode(pos[0],pos[1])
                        if pointB != -1 and pointB != pointA:
                            edges.append((pointA,pointB))
                            edges.append((pointB,pointA))
                            state = 'add_edge1'
                            msg = 'Choose initial vertex of the edge.'
                            pointA = -1
                            pointB = -1
                        if(isClicked(5,42,5+edge_button.get_width(),42+edge_button.get_height(),pos[0],pos[1])):
                            state = 'start'
                            msg = ''
                    elif state == 'choose start point for dfs':
                        point  = getNode(pos[0],pos[1])
                        if point != -1:
                            state = 'dfs'
                            msg = ''
                    elif state == 'choose start point for bfs':
                        point  = getNode(pos[0],pos[1])
                        if point != -1:
                            state = 'bfs'
                            msg = ''
                    elif state == 'exit':
                        if(isClicked(5,5,5+node_button.get_width(),5+node_button.get_height(),pos[0],pos[1])):
                            make_equal(node_color,temp_node)
                            yellow_edges.clear()
                            blue_edges.clear()
                            state = 'start'
                            msg = ''
                pos = (-1,-1)
                
        show_edges()
        show_nodes()
        pygame.display.update()
        #clock.tick(60)
        
    # pygame.quit()

