def generate_feedback(scores):
    """
    Generates positive, improvement, and negative feedback points, along with a final verdict.
    """
    conf = scores["confidence"]
    nerv = scores["nervousness"]
    comm = scores["communication"]

    positive = []
    improvement = []
    negative = []

    # Confidence rules
    if conf >= 80:
        positive.append("You appeared confident and composed.")
    elif conf >= 50:
        improvement.append("Try to project more confidence during answers.")
    else:
        negative.append("Low confidence detected; try to maintain focus.")

    # Nervousness rules
    if nerv <= 20:
        positive.append("You showed very little nervousness.")
    elif nerv <= 50:
        improvement.append("You seemed slightly nervous. Try to reduce sudden movements.")
    else:
        negative.append("High nervousness detected. Work on staying still and calm.")

    # Communication rules
    if comm >= 80:
        positive.append("Good communication clarity and fluency.")
    elif comm >= 50:
        improvement.append("Try reducing pauses and filler words.")
    else:
        negative.append("Too many pauses and filler words observed.")

    # Final Verdict Calculation based on Average Score
    avg_score = (conf + (100 - nerv) + comm) / 3
    
    if avg_score >= 80:
        verdict = "Ready for Interview"
        verdict_class = "verdict-Ready"
    elif avg_score >= 50:
        verdict = "Needs Improvement"
        verdict_class = "verdict-Improve"
    else:
        verdict = "Not Ready"
        verdict_class = "verdict-NotReady"

    return {
        "positive": positive,
        "improvement": improvement,
        "negative": negative,
        "verdict": verdict,
        "verdict_class": verdict_class,
        "overall_score": int(avg_score)
    }
