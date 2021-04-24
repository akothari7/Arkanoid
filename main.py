import arcade
import random
import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Paddle:

    def __init__(self):

        self.width = SCREEN_WIDTH * 0.15
        self.height = 10
        self.pos_x = SCREEN_WIDTH // 2
        self.pos_y = SCREEN_HEIGHT * 0.1
        self.vel_x = 0
        self.color = [random.randint(0, 155), random.randint(0, 155), random.randint(0, 155)]
    def get_left(self):
        pos_left = self.pos_x - (self.width / 2)
        return pos_left

    def set_left(self, x):
        self.pos_x = x + (self.width / 2)

    def get_right(self):
        pos_right = self.pos_x + (self.width / 2)
        return pos_right

    def set_right(self, x):
        self.pos_x = x - (self.width / 2)

    def get_top(self):
        return self.pos_y + (self.height / 2)

    def get_bottom(self):
        return self.pos_y - (self.height / 2)

    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.color)

    def update(self):
        if self.get_left() + self.vel_x <= 0:
            self.set_left(0)
        elif self.get_right() + self.vel_x >= SCREEN_WIDTH:
            self.set_right(SCREEN_WIDTH)
        else:
            self.pos_x += self.vel_x



class Ball:

    def __init__(self):
        self.radius = 5
        self.pos_x = SCREEN_WIDTH // 2
        self.pos_y = SCREEN_HEIGHT * 0.1 + 11
        self.vel_x = 0
        self.vel_y = 0
        self.color = 0, 101, 114
        self.released = False

    def get_bottom(self):
        return self.pos_y - self.radius

    def get_top(self):
        return self.pos_y + self.radius

    def get_left(self):
        return self.pos_x - self.radius

    def get_right(self):
        return self.pos_x + self.radius

    def release(self):
        pass

    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.color)

    def update(self):
        self.pos_x = self.pos_x + self.vel_x
        self.pos_y = self.pos_y + self.vel_y

        if self.get_right() >= SCREEN_WIDTH:
            self.vel_x = self.vel_x - (self.vel_x * 2)

        if self.get_top() >= SCREEN_HEIGHT:
            self.vel_y = self.vel_y - (self.vel_y * 2)

        if self.get_left() <= 0:
            self.vel_x = self.vel_x + (self.vel_x * -2)


class Score:

    def __init__(self):

        self.pos_x = 5
        self.pos_y = SCREEN_HEIGHT - 15
        self.text_color = arcade.color.BLACK
        self.value = 0

    def draw(self):
        arcade.draw_text("Score: %s" % str(self.value), self.pos_x, self.pos_y, self.text_color)


class VelText:

    def __init__(self, ball):
        self.ball = ball

        self.pos_x = 5
        self.pos_y = SCREEN_HEIGHT - 30
        self.text_color = arcade.color.BLACK

    def draw(self):
        arcade.draw_text("Current x Velocity: %s" % str(self.ball.vel_x), self.pos_x, self.pos_y, self.text_color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.PALE_TURQUOISE)

        # Create objects and load resources
        self.paddle = Paddle()
        self.ball = Ball()
        self.score = Score()
        self.vel_text = VelText(self.ball)
        self.bounce_sound = arcade.load_sound("resources/sounds/paddle_bounce.wav")

        self.print_instructions()

    def print_instructions(self):
        print("Hello. This is a game where you try to bounce the ball off the paddle as many times as you can.")
        time.sleep(3.5)
        print("A few things you need to know before you begin:")
        time.sleep(3.5)
        print('1. The closer to the center of the paddle you hit the ball, the slower it will go, and the easier it will be.')
        time.sleep(3.5)
        print("2. If the ball falls through the bottom of the screen, that round is over, but it will reset after a few seconds.")
        time.sleep(3.5)
        print("3. At the beginning of each round, you can launch the ball by pressing the space bar.")
        time.sleep(3.5)
        print("4. In the top left hand corner, there will be two counters. One will be counting your round score, and the other, your current x velocity.")
        time.sleep(3.5)
        input("Click onto the terminal and press enter to start the game.")


    def on_key_press(self, symbol, modifiers):
        """ Called every time a keyboard key is pressed """
        if symbol == arcade.key.LEFT:
            self.paddle.vel_x = -6
        elif symbol == arcade.key.RIGHT:
            self.paddle.vel_x = 6
        if symbol == arcade.key.SPACE:
            if not self.ball.released:
                self.ball.vel_y = 4
                self.ball.vel_x = 4
                self.ball.released = True



    def on_key_release(self, symbol, modifiers):
        """ Called when a pressed keyboard key is releasesd """
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.paddle.vel_x = 0

    def check_collision(self):
        """ Determine if the ball hit the paddle"""
        if self.paddle.get_bottom() < self.ball.get_bottom() <= self.paddle.get_top():
            if self.ball.get_left() + self.ball.radius >= self.paddle.get_left():
                if self.ball.get_right() - self.ball.radius <= self.paddle.get_right():
                    self.ball.vel_y = self.ball.vel_y + (self.ball.vel_y * -2)
                    if self.ball.vel_x > 0:
                        if self.paddle.get_left() < self.ball.pos_x < self.paddle.get_left() + (self.paddle.width / 10):
                            self.ball.vel_x = 7
                        elif self.paddle.get_left() + (self.paddle.width / 10) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 2):
                            self.ball.vel_x = 6
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 2) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 3):
                            self.ball.vel_x = 5
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 3) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 4):
                            self.ball.vel_x = 4
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 4) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 5):
                            self.ball.vel_x = 3
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 5) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 6):
                            self.ball.vel_x = 3
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 6) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 7):
                            self.ball.vel_x = 4
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 7) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 8):
                            self.ball.vel_x = 5
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 8) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 9):
                            self.ball.vel_x = 6
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 9) <= self.ball.pos_x < self.paddle.get_right():
                            self.ball.vel_x = 7
                    else:
                        if self.ball.pos_x <= self.paddle.get_left() + (self.paddle.width / 10):
                            self.ball.vel_x = -7
                        elif self.paddle.get_left() + (self.paddle.width / 10) < self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 2):
                            self.ball.vel_x = -6
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 2) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 3):
                            self.ball.vel_x = -5
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 3) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 4):
                            self.ball.vel_x = -4
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 4) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 5):
                            self.ball.vel_x = -3
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 5) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 6):
                            self.ball.vel_x = -3
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 6) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 7):
                            self.ball.vel_x = -4
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 7) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 8):
                            self.ball.vel_x = -5
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 8) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 9):
                            self.ball.vel_x = -6
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 9) <= self.ball.pos_x < self.paddle.get_right():
                            self.ball.vel_x = -7

                    # print(self.ball.vel_x)
                    # print(self.paddle.get_left(), self.ball.pos_x, self.paddle.get_right())

                    self.score.value += 1
                    self.bounce_sound.play()


    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.paddle.update()
        if self.ball.released is True:
            self.check_collision()
            self.ball.update()
        else:
            self.ball.pos_x = self.paddle.pos_x
        if self.ball.get_top() < 0:
            time.sleep(2)
            self.paddle.pos_x = SCREEN_WIDTH // 2
            self.paddle.pos_y = SCREEN_HEIGHT * 0.1
            self.paddle.vel_x = 0
            self.paddle.color = [random.randint(0, 155), random.randint(0, 155), random.randint(0, 155), ]
            self.ball.pos_x = SCREEN_WIDTH // 2
            self.ball.pos_y = SCREEN_HEIGHT * 0.1 + 11
            self.ball.vel_x = 0
            self.ball.vel_y = 0
            self.ball.released = False
            self.score.value = 0


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        # Draw the paddle
        self.paddle.draw()
        # Draw the ball
        self.ball.draw()
        self.score.draw()
        self.vel_text.draw()

def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Arkanoid")
    arcade.run()


if __name__ == '__main__':
    main()


