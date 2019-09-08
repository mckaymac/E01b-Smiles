#!/usr/bin/env python3

#imports libraries and assests
import utils, open_color, arcade

#checks the version of python
utils.check_version((3,7))

# sets the dimensions and title of the window containing the smiley face.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smiley Face Example"

#creates Faces class
class Faces(arcade.Window):
    """ Our custom Window Class"""

    #initializes function to follow mouse cursor
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)

        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

        arcade.set_background_color(open_color.white)

    def on_draw(self):
        """ Draw the face """
        arcade.start_render()
        face_x,face_y = (self.x,self.y)
        smile_x,smile_y = (face_x + 0,face_y - 10)
        eye1_x,eye1_y = (face_x - 30,face_y + 20) 
        eye2_x,eye2_y = (face_x + 30,face_y + 20)
        catch1_x,catch1_y = (face_x - 25,face_y + 25) 
        catch2_x,catch2_y = (face_x + 35,face_y + 25) 

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        self.x = x
        self.y = y



window = Faces()
arcade.run()