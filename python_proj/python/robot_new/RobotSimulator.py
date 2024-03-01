import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsRectItem
from PyQt5.QtCore import Qt, QTimer
import pygame
from pygame.locals import QUIT

class RobotSimulator(QMainWindow):
    def __init__(self):
        super(RobotSimulator, self).__init__()

        self.setWindowTitle("Robot Simulator")
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)

        self.robot = QGraphicsRectItem(0, 0, 50, 50)
        self.scene.addItem(self.robot)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_simulation)
        self.timer.start(16)  # 60 FPS

        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    def update_simulation(self):
        self.handle_input()

        # Update robot position or perform physics simulation here
        # For simplicity, let's just move the robot in a circle
        self.robot.setPos(self.robot.x() + 1, self.robot.y() + 1)

        self.render()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def render(self):
        self.scene.update()
        self.clock.tick(60)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    simulator = RobotSimulator()
    simulator.show()
    sys.exit(app.exec_())
