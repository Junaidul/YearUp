# import pickle

# import cv2
# import mediapipe as mp
# import numpy as np

# model_dict = pickle.load(open('./model.p', 'rb'))
# model = model_dict['model']

# cap = cv2.VideoCapture(0)

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles

# hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# labels_dict = {0: 'A', 1: 'B', 2: 'L'}
# while True:

#     data_aux = []
#     x_ = []
#     y_ = []

#     ret, frame = cap.read()

#     H, W, _ = frame.shape

#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     results = hands.process(frame_rgb)
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(
#                 frame,  # image to draw
#                 hand_landmarks,  # model output
#                 mp_hands.HAND_CONNECTIONS,  # hand connections
#                 mp_drawing_styles.get_default_hand_landmarks_style(),
#                 mp_drawing_styles.get_default_hand_connections_style())

#         for hand_landmarks in results.multi_hand_landmarks:
#             for i in range(len(hand_landmarks.landmark)):
#                 x = hand_landmarks.landmark[i].x
#                 y = hand_landmarks.landmark[i].y

#                 x_.append(x)
#                 y_.append(y)

#             for i in range(len(hand_landmarks.landmark)):
#                 x = hand_landmarks.landmark[i].x
#                 y = hand_landmarks.landmark[i].y
#                 data_aux.append(x - min(x_))
#                 data_aux.append(y - min(y_))

#         x1 = int(min(x_) * W) - 10
#         y1 = int(min(y_) * H) - 10

#         x2 = int(max(x_) * W) - 10
#         y2 = int(max(y_) * H) - 10

#         prediction = model.predict([np.asarray(data_aux)])

#         predicted_character = labels_dict[int(prediction[0])]

#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
#         cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
#                     cv2.LINE_AA)

#     cv2.imshow('frame', frame)
#     cv2.waitKey(1)


# cap.release()
# cv2.destroyAllWindows()









import pickle
import cv2
import mediapipe as mp
import numpy as np

# Load model
print("Loading trained model...")
try:
    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Initialize Mediapipe Hands
print("Initializing Mediapipe Hands...")
try:
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    print("Mediapipe Hands initialized successfully.")
except Exception as e:
    print(f"Error initializing Mediapipe Hands: {e}")
    exit(1)

# Labels dictionary
labels_dict = {0: 'A', 1: 'B', 2: 'L'}

# Capture video
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit(1)

print("Starting webcam feed...")
while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from webcam.")
        break

    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

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

        # Check feature count consistency
        if len(data_aux) == 42:  # Single hand
            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = labels_dict[int(prediction[0])]
        elif len(data_aux) == 84:  # Two hands
            # Optionally handle two-hand scenarios or simplify to single-hand
            print("Two hands detected. Adjust model if necessary.")
            continue
        else:
            print(f"Unexpected feature count: {len(data_aux)}")
            continue

        # Display prediction
        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10
        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                    cv2.LINE_AA)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()