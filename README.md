# InterviewSense AI – Real-Time Interview Performance Analyzer

InterviewSense AI is a Streamlit application designed to simulate a real-world interview scenario. It uses AI to analyze your behavior and speech metrics to provide a final score and targeted feedback on your interview readiness.

## Features

- **Text-to-Speech Questions**: The system speaks the questions aloud automatically.
- **Webcam Integration**: Uses your device's camera to analyze visual cues (eye contact, movement).
- **Simulated Speech Analytics**: Tracks pauses, filler words, and fluency.
- **Scoring Dashboard**: A comprehensive final verdict based on your confidence, nervousness, and communication skills.
- **Detailed Feedback**: Provides positive reinforcement and highlights areas for improvement.

## How to Run the Project

### 1. Prerequisites
Ensure you have Python installed on your system (Python 3.8 or above is recommended).

### 2. Install the Required Dependencies
Open your terminal or command prompt, navigate to the project folder, and run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

*Note: Depending on your system configuration, you may need to use `pip3` instead of `pip`.*

### 3. Run the Streamlit Application
Start the application by running:

```bash
streamlit run app.py
```

### 4. Setup Requirements
- **Camera Permissions**: When you start the interview, your browser will prompt you for camera access. Click **"Allow"** to ensure the video analysis can process your frames.
- **Audio Output**: Make sure your device's volume is turned up to hear the questions being spoken by the system.

Enjoy your mock interview practice!
