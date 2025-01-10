import os
import pickle
import mediapipe as mp
import cv2

# Mediapipe Initialization
print("Initializing Mediapipe Hands...")
try:
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=2,  # Detect up to 2 hands
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    print("Mediapipe Hands initialized successfully.")
except Exception as e:
    print(f"Error initializing Mediapipe Hands: {e}")
    exit(1)

# Data Directory
DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    print(f"Creating data directory at {DATA_DIR}...")
    os.makedirs(DATA_DIR)

# Initialize data structures
data = []
labels = []

# Process data
print("Processing images...")
for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)
    if not os.path.isdir(dir_path):
        continue

    print(f"Processing class '{dir_}'...")
    for img_path in os.listdir(dir_path):
        img_file_path = os.path.join(dir_path, img_path)
        data_aux = []
        x_ = []
        y_ = []

        # Read and validate image
        img = cv2.imread(img_file_path)
        if img is None:
            print(f"Error reading image: {img_file_path}. Skipping...")
            continue

        # Convert image to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process image with Mediapipe Hands
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Collect landmarks
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                # Normalize landmarks
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels.append(dir_)
        else:
            print(f"No hand landmarks detected in image: {img_file_path}. Skipping...")

# Save processed data
print("Saving processed data...")
try:
    with open('data.pickle', 'wb') as f:
        pickle.dump({'data': data, 'labels': labels}, f)
    print("Data saved successfully in 'data.pickle'.")
except Exception as e:
    print(f"Error saving data: {e}")
    exit(1)

print("Dataset creation complete.")