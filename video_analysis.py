import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

def analyze_frame(image):
    """
    Analyzes a single numpy array frame (RGB) to detect face and approximate metrics.
    """
    results = face_detection.process(image)
    
    face_detected = False
    eye_contact = "poor"
    movement = "high"
    
    if results.detections:
        face_detected = True
        
        # Approximate eye contact based on face centralization
        bboxC = results.detections[0].location_data.relative_bounding_box
        if 0.2 < bboxC.xmin < 0.8 and 0.2 < bboxC.ymin < 0.8:
            eye_contact = "good"
            movement = "low"
        else:
            eye_contact = "poor"
            movement = "high"

    return {
        "face_detected": face_detected,
        "eye_contact": eye_contact,
        "movement": movement
    }

def aggregate_video_analysis(frames):
    """
    Takes a list of RGB numpy arrays, analyzes each, and returns aggregated metrics.
    """
    if not frames:
        return {"face_detected": False, "eye_contact": "poor", "movement": "high"}

    face_count = 0
    good_eye_contact = 0
    high_movement_count = 0

    for frame in frames:
        res = analyze_frame(frame)
        if res["face_detected"]:
            face_count += 1
            if res["eye_contact"] == "good":
                good_eye_contact += 1
            if res["movement"] == "high":
                high_movement_count += 1

    total = len(frames)
    
    # Aggregation rules
    face_detected = (face_count / total) > 0.5  # true if face detected in >50% of frames
    eye_contact = "good" if (good_eye_contact / max(1, face_count)) > 0.6 else "poor"
    movement = "high" if (high_movement_count / max(1, face_count)) > 0.4 else "low"

    return {
        "face_detected": face_detected,
        "eye_contact": eye_contact,
        "movement": movement
    }
