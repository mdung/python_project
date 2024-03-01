import pygame
import random
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# Constants
FIELD_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = FIELD_SIZE * CELL_SIZE
MOVE_INTERVAL = 500  # Time interval between robot moves in milliseconds
WEED_IMAGE_SIZE = (224, 224)  # Image size required by the MobileNetV2 model
MODEL_TRAINING_STEPS = 10  # Number of steps for training the model
WEED_DETECTION_THRESHOLD = 0.5  # Threshold for weed detection probability

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class RoboticSystem:
    def __init__(self):
        self.robot_position = (0, 0)
        self.weeds = {(random.randint(0, FIELD_SIZE-1), random.randint(0, FIELD_SIZE-1)) for _ in range(FIELD_SIZE)}
        self.data = np.zeros((FIELD_SIZE, FIELD_SIZE))  # Data collection matrix
        self.model = self.build_model()  # CNN model for weed detection
        self.next_move_time = pygame.time.get_ticks() + MOVE_INTERVAL

    def build_model(self):
        base_model = MobileNetV2(weights='imagenet', include_top=False)
        model = Sequential([
            GlobalAveragePooling2D(input_shape=(7, 7, 1280)),
            Dense(512, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer=Adam(lr=0.001), loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def move_robot(self):
        directions = ["up", "down", "left", "right"]
        direction = random.choice(directions)
        self.robot_position = self.get_new_position(direction)

    def get_new_position(self, direction):
        x, y = self.robot_position
        if direction == "up" and y > 0:
            return (x, y-1)
        elif direction == "down" and y < FIELD_SIZE - 1:
            return (x, y+1)
        elif direction == "left" and x > 0:
            return (x-1, y)
        elif direction == "right" and x < FIELD_SIZE - 1:
            return (x+1, y)
        return self.robot_position  # If movement is not possible, stay in the same position

    def collect_data(self):
        x, y = self.robot_position
        self.data[x][y] = 1 if (x, y) in self.weeds else 0  # Collect data on presence of weeds

    def detect_weeds(self, image_path):
        img = load_img(image_path, target_size=WEED_IMAGE_SIZE)
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        prediction = self.model.predict(img_array)[0][0]
        return prediction

    def remove_weeds(self):
        x, y = self.robot_position
        if (x, y) in self.weeds:
            self.weeds.remove((x, y))
            self.data[x][y] = 0  # Update data after removing weeds

    def train_model(self):
        X = np.argwhere(self.data == 1)
        y = np.ones(X.shape[0])
        X = np.concatenate((X, np.argwhere(self.data == 0)), axis=0)
        y = np.concatenate((y, np.zeros(X.shape[0] - y.shape[0])), axis=0)
        self.model.fit(X, y, epochs=MODEL_TRAINING_STEPS, verbose=0)

    def draw(self, screen):
        screen.fill(WHITE)
        for x in range(FIELD_SIZE):
            for y in range(FIELD_SIZE):
                color = GREEN if (x, y) not in self.weeds else RED
                pygame.draw.rect(screen, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, BLUE, (self.robot_position[0]*CELL_SIZE, self.robot_position[1]*CELL_SIZE,
                                        CELL_SIZE, CELL_SIZE))
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Robotic Weed Detection and Removal Simulation")
    clock = pygame.time.Clock()
    system = RoboticSystem()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()
        if current_time >= system.next_move_time:
            system.move_robot()
            system.collect_data()
            weed_detection_probability = system.detect_weeds("weed_image.jpg")
            if weed_detection_probability >= WEED_DETECTION_THRESHOLD:
                system.remove_weeds()
                system.train_model()  # Retrain the model with updated data
            system.next_move_time = current_time + MOVE_INTERVAL

        system.draw(screen)
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
