import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def draw_lines(img, lines, color=(0, 255, 0), thickness=3):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

def process_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    height, width = image.shape[:2]
    vertices = np.array([[(0, height), (width / 2, height / 2), (width, height)]], dtype=np.int32)
    masked_edges = region_of_interest(edges, vertices)

    rho = 2
    theta = np.pi / 180
    threshold = 50
    min_line_length = 100
    max_line_gap = 100
    lines_image = hough_lines(masked_edges, rho, theta, threshold, min_line_length, max_line_gap)

    result = cv2.addWeighted(image, 0.8, lines_image, 1, 0)
    return result

if __name__ == "__main__":
    # Open a video file or capture video from a camera (replace 'your_video.mp4' with the video file or camera index)
    cap = cv2.VideoCapture('your_video.mp4')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_image(frame)

        cv2.imshow('Lane Detection', processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
