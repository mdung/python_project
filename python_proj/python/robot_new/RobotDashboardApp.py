import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QHBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt, QTimer
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.status = "Idle"
        self.position = [0, 0]
        self.battery_level = 100

    def update_status(self):
        # Simulate changing robot status
        status_options = ["Idle", "Moving", "Charging"]
        self.status = random.choice(status_options)

        # Simulate changing position
        self.position = [random.uniform(-10, 10), random.uniform(-10, 10)]

        # Simulate battery consumption
        if self.status == "Moving":
            self.battery_level -= random.uniform(0.1, 1)
        elif self.status == "Charging":
            self.battery_level += random.uniform(0.5, 2)

        # Ensure battery level is within the valid range
        self.battery_level = max(0, min(100, self.battery_level))

class RobotDashboardApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

        # Create and initialize three robots
        self.robots = [Robot("Robot 1"), Robot("Robot 2"), Robot("Robot 3")]

        # Set up a timer to update robot data every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_robots_data)
        self.timer.start(1000)

    def init_ui(self):
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('Robot Dashboard')

        # Create layouts
        main_layout = QVBoxLayout()
        robots_layout = QHBoxLayout()

        # Create robot widgets
        for robot in self.robots:
            robot_widget = self.create_robot_widget(robot)
            robots_layout.addWidget(robot_widget)

        # Add robots layout to the main layout
        main_layout.addLayout(robots_layout)

        # Set the main layout for the application window
        self.setLayout(main_layout)

    def create_robot_widget(self, robot):
        # Create a frame for the robot
        robot_frame = QFrame()
        robot_frame.setFrameShape(QFrame.Panel)
        robot_frame.setFrameShadow(QFrame.Sunken)

        # Create labels and progress bars for robot information
        robot_name_label = QLabel(robot.name)
        robot_status_label = QLabel(f"Status: {robot.status}")
        robot_position_label = QLabel(f"Position: ({robot.position[0]:.2f}, {robot.position[1]:.2f})")
        robot_battery_label = QLabel(f"Battery: {robot.battery_level:.1f}%")
        battery_progress = QProgressBar()
        battery_progress.setValue(robot.battery_level)

        # Create a button to manually trigger robot movement
        move_button = QPushButton("Move")
        move_button.clicked.connect(lambda: self.move_robot(robot))

        # Create a layout for the robot widget
        robot_layout = QVBoxLayout()
        robot_layout.addWidget(robot_name_label)
        robot_layout.addWidget(robot_status_label)
        robot_layout.addWidget(robot_position_label)
        robot_layout.addWidget(robot_battery_label)
        robot_layout.addWidget(battery_progress)
        robot_layout.addWidget(move_button)

        # Set the layout for the robot frame
        robot_frame.setLayout(robot_layout)

        return robot_frame

    def move_robot(self, robot):
        # Simulate moving the robot manually
        robot.status = "Moving"
        robot.position = [random.uniform(-10, 10), random.uniform(-10, 10)]
        robot.battery_level -= random.uniform(0.1, 1)

    def update_robots_data(self):
        # Update data for each robot
        for robot in self.robots:
            robot.update_status()

            # Find the corresponding widget for the robot
            for i in range(self.layout().count()):
                robot_widget = self.layout().itemAt(i).itemAt(0).widget()
                if robot_widget and robot_widget.layout().itemAt(0).text() == robot.name:
                    # Update information in the widget
                    robot_widget.layout().itemAt(1).setText(f"Status: {robot.status}")
                    robot_widget.layout().itemAt(2).setText(f"Position: ({robot.position[0]:.2f}, {robot.position[1]:.2f})")
                    robot_widget.layout().itemAt(3).setText(f"Battery: {robot.battery_level:.1f}%")
                    robot_widget.layout().itemAt(4).setValue(robot.battery_level)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard_app = RobotDashboardApp()
    dashboard_app.show()
    sys.exit(app.exec_())
