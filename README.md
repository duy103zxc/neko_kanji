## Kanji Reading Quiz Documentation

### Overview

This JavaScript code implements a Kanji Reading Quiz application. Users can select a Japanese Language Proficiency Test (JLPT) level (N5, N4, N1, etc.) and start a quiz to test their knowledge of Kanji readings. The quiz offers features such as time attack mode, hints, and displays quiz results at the end.

### Features

1. **Quiz Levels:** Supports multiple JLPT levels (N5, N4, N1), and you can easily extend it for additional levels.

2. **Quiz Data Fetching:** Quiz data is fetched from external JSON files based on the selected JLPT level. The data includes Kanji characters, readings, and meanings.

3. **Shuffle Function:** The quiz data is shuffled to present questions in random order, enhancing the variety of questions for users.

4. **Quiz Modes:**
    - **Regular Mode:** Allows users to answer a specified number of questions.
    - **Time Attack Mode:** Users can set a time limit to answer as many questions as possible within the given time.

5. **Feedback and Hints:**
    - Provides feedback on correctness after each answer attempt.
    - Supports hints for users who need assistance.

6. **Results Display:**
    - Displays results at the end of the quiz, including score, time spent, and incorrect attempts.
    - Offers encouragement messages based on the user's performance.

7. **Unanswered Questions Display:**
    - If applicable, shows a list of unanswered questions at the end of the quiz.

8. **Copy to Clipboard:**
    - Allows users to copy unanswered questions to the clipboard for further review.

9. **Modal Help:**
    - Provides a modal window with additional information about the quiz when the "Help" link is clicked.

### Usage

1. **Select Quiz Options:**
    - Choose a JLPT level from the dropdown.
    - Optionally enable hints and time attack mode.

2. **Start Quiz:**
    - Click the "Start Quiz" button to initiate the quiz.

3. **Answer Questions:**
    - Type your answer in the input field and hit Enter
    - Receive feedback on correctness and hints if enabled.

4. **Quiz End:**
    - View quiz results, including score, time spent, and incorrect attempts.
    - If applicable, see a list of unanswered questions.

5. **Copy Unanswered Questions:**
    - Click the "Copy to Clipboard" button to copy unanswered questions for review.

6. **Help:**
    - Click the "Help" link to open a modal window with additional information about the quiz.

### Dependencies

- **External JSON Files:** The quiz relies on external JSON files for quiz data. Ensure that the JSON files are correctly formatted.

### Notes

- **Extension:** The code can be extended to support additional JLPT levels or include more features based on specific requirements.

---

