def calculate_scores(video_results_list, audio_results_list):
    """
    Calculates final scores based on the collected video and audio metrics across all questions.
    """
    total_questions = len(video_results_list)
    if total_questions == 0:
        return {"confidence": 0, "nervousness": 0, "communication": 0}

    # Base scores
    confidence = 100
    nervousness = 0
    communication = 100

    # Aggregate penalties
    for v_res, a_res in zip(video_results_list, audio_results_list):
        # Video penalties
        if not v_res["face_detected"]:
            confidence -= 10
            nervousness += 10
        else:
            if v_res["eye_contact"] == "poor":
                confidence -= 5
                communication -= 5
            
            if v_res["movement"] == "high":
                nervousness += 10
                confidence -= 5

        # Audio penalties
        if a_res["filler_words"] > 3:
            communication -= 5
            nervousness += 5
            
        if a_res["pauses"] > 2:
            communication -= 5
            confidence -= 5
            
        if not a_res.get("meaningful", True):
            communication -= 20
            confidence -= 10

    # Normalize scores between 0 and 100
    confidence = max(0, min(100, confidence))
    nervousness = max(0, min(100, nervousness))
    communication = max(0, min(100, communication))

    return {
        "confidence": confidence,
        "nervousness": nervousness,
        "communication": communication
    }
