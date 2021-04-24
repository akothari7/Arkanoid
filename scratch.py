    def check_collision(self):
        """ Determine if the ball hit the paddle"""
        if self.paddle.get_bottom() < self.ball.get_bottom() <= self.paddle.get_top():
            if self.ball.get_left() >= self.paddle.get_left():
                if self.ball.get_right() <= self.paddle.get_right():
                    self.ball.vel_y = self.ball.vel_y + (self.ball.vel_y * -2)
                    if self.ball.vel_x > 0:
                        if self.paddle.get_left() < self.ball.pos_x < self.paddle.get_left() + (self.paddle.width / 10):
                            self.ball.vel_x = 6
                        elif self.paddle.get_left() + (self.paddle.width / 10) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 2):
                            self.ball.vel_x = 5
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 2) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 3):
                            self.ball.vel_x = 4
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 3) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 4):
                            self.ball.vel_x = 3
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 4) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 5):
                            self.ball.vel_x = 2
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 5) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 6):
                            self.ball.vel_x = 2
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 6) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 7):
                            self.ball.vel_x = 3
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 7) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 8):
                            self.ball.vel_x = 4
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 8) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 9):
                            self.ball.vel_x = 5
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 9) <= self.ball.pos_x < self.paddle.get_right():
                            self.ball.vel_x = 6
                    else:
                        if self.ball.pos_x < self.paddle.get_left() + (self.paddle.width / 10):
                            self.ball.vel_x = -6
                        elif self.paddle.get_left() + (self.paddle.width / 10) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 2):
                            self.ball.vel_x = -5
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 2) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 3):
                            self.ball.vel_x = -4
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 3) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 4):
                            self.ball.vel_x = -3
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 4) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 5):
                            self.ball.vel_x = -2
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 5) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 6):
                            self.ball.vel_x = -2
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 6) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 7):
                            self.ball.vel_x = -3
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 7) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 8):
                            self.ball.vel_x = -4
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 8) <= self.ball.pos_x < self.paddle.get_left() + ((self.paddle.width / 10) * 9):
                            self.ball.vel_x = -5
                        elif self.paddle.get_left() + ((self.paddle.width / 10) * 9) <= self.ball.pos_x < self.paddle.get_right():
                            self.ball.vel_x = -6
