#Draw a Scene - Suhaani Singh 
#This program illustrates a snowman on a sunny, snowy day standing next to a 
#snowball pile and a christmas tree 

size(400,400)
background(80,150,255)                               #changes background colour from default
                                                     #to blue to illustrate a sky

def snowy_ground():
    """this function creates a ground filled with snow by making it a very light gray"""
    fill(230)
    rect(0,320,400,80)
    
def snowman_body():
    """this function creates the two body parts of the snowman, the face and the body""" 
    fill(230)                                        #colour coordinates with the snowy ground 
    ellipse(100,210,70,70)                           #face, smaller circle
    ellipse(100,300,110,110)                         #body, bigger circle 
    
def snowman_eye(x,y):
    """this function with parameters creates two black circles for the snowman's eyes""" 
    fill(0)
    ellipse(x,y,5,5)
    
def snowman_smile():
    """this function creates the smile of the snowman by making a semicircle of dark red circles"""
    fill(130,10,20)
    ellipse(85,220,5,5)
    ellipse(90,225,5,5)
    ellipse(96,230,5,5)
    ellipse(115,220,5,5)
    ellipse(110,225,5,5)
    ellipse(104,230,5,5)
    
def snowman_arms():
    """this function creates the two arms of the snowman on either sides"""
    line(145,270,190,230)
    line(55,270,10,230)

def snowman_accesories():
    """this function creates the snowman's red hat and three black buttons"""
    fill(240,10,20)
    rect(75,120,50,60) 
    fill(130,10,20)
    ellipse(100,180,80,5)                            #the bottom, darker part of the hat              
    fill(0)
    ellipse(100,305,12,12)
    ellipse(100,285,12,12)
    ellipse(100,325,12,12)
    
def snow_falling(x,y):
    """this function with parameters and a for loop creates a snow fall in the 
    background in 4 columns"""
    for i in range(5):
        fill(230)                                    #colour coordinates with the snowman body
                                                     #and the snowy ground 
        ellipse(x,y,17,17)
        y=y+75

def draw_tree():
    """this function creates a tree in sections of three green triangles and a brown trunk"""
    fill(130,70,0)
    rect(305,290,30,60)
    fill(0,130,0)
    triangle(320,210,260,290,380,290)
    fill(0,130,0)
    triangle(320,170,260,250,380,250)
    fill(0,130,0)
    triangle(320,140,260,210,380,210)

def tree_lights():
    """this function creates the red, green, blue fairy lights which wraps around the tree"""
    line(290,175,365,190)
    fill(225,0,0)
    ellipse(304,182,7,7)
    fill(0,255,0)
    ellipse(323,186,7,7)
    fill(0,0,225)
    ellipse(345,190,7,7)
    line(285,220,370,240)
    fill(225,0,0)
    ellipse(304,230,7,7)
    fill(0,255,0)
    ellipse(323,234,7,7)
    fill(0,0,225)
    ellipse(345,238,7,7)
    line(280,265,370,280)
    fill(225,0,0)
    ellipse(304,273,7,7)
    fill(0,255,0)
    ellipse(323,276,7,7)
    fill(0,0,225)
    ellipse(345,280,7,7)
    
def snow_ball_pile():
    """this function creates a pile of 6 snowballs next to the snowman"""
    fill(230)                                        #colour coordinates with the snowman, the snowy
                                                     #ground and the snow fall 
    ellipse(190,340,15,15)
    ellipse(205,340,15,15)
    ellipse(220,340,15,15)
    ellipse(198,325,15,15)
    ellipse(213,325,15,15)
    ellipse(206,311,15,15)
    
def draw_sun():
    """this function creates a sun with 8 sun rays coming out from it"""
    stroke(255,255,0)
    fill(255,255,0)
    ellipse(340,60,60,60)
    line(340,92,340,110)
    line(360,85,375,98)
    line(370,60,390,60)
    line(350,45,380,25)
    line(340,40,340,10)
    line(320,45,305,25)
    line(310,60,290,60)
    line(320,85,305,98)
    

snowy_ground()
snowman_body()            
snowman_eye(90,205)  
snowman_eye(110,205)   
snowman_smile() 
snowman_arms()
snowman_accesories()
snow_falling(50,50)
snow_falling(150,50)
snow_falling(250,50)
snow_falling(350,125)
draw_tree()
tree_lights()
snow_ball_pile()
strokeWeight(2)                                      #to make the sun rays bolder and pop out 
draw_sun()
