import re

def analyze_audio_behavior(text, duration):
    """
    Analyzes actual transcribed text to evaluate speech fluency, filler words, and pauses.
    """
    text = text.lower()
    
    # Check for empty speech
    if not text.strip():
        return {
            "transcribed_text": "No speech detected.",
            "filler_words": 0,
            "pauses": int(duration / 3), # Assume high pauses if no speech
            "fluency_score": 0,
            "meaningful": False
        }
        
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    
    # Common filler words
    fillers = ['um', 'uh', 'like', 'you know', 'basically', 'actually', 'literally']
    
    filler_count = 0
    for filler in fillers:
        if len(filler.split()) == 1:
            filler_count += text.split().count(filler)
        else:
            filler_count += text.count(filler)
            
    # Estimate pauses based on word count per second (avg normal speech is ~2.5 words/sec)
    expected_words = duration * 2.5
    pauses = 0
    if word_count < (expected_words * 0.5):
        # Very slow speech, indicates long pauses
        pauses = int((expected_words - word_count) / 2.5 / 2) # Rough estimation of heavy pauses
        
    # Meaningfulness check (simple heuristic: more than 10 words is considered meaningful enough for baseline)
    meaningful = word_count > 10
    
    # Calculate fluency out of 100
    base_fluency = 100
    fluency_score = base_fluency - (filler_count * 5) - (pauses * 5)
    
    # Penalty for not speaking much
    if not meaningful:
        fluency_score -= 30
        
    fluency_score = max(0, min(100, int(fluency_score)))
    
    return {
        "transcribed_text": text,
        "filler_words": filler_count,
        "pauses": pauses,
        "fluency_score": fluency_score,
        "meaningful": meaningful
    }
