# MonkeyType CLI Clone

Welcome to the **MonkeyType CLI Clone**, a command-line-based typing speed and accuracy tester! This project is a great way to sharpen your typing skills while having fun. Challenge yourself and see how fast and accurately you can type!

---

## Features 🚀

- **WPM Calculation:** Measures words per minute in real-time.
- **Accuracy Tracking:** Shows how accurate your typing is.
- **Random Text Selection:** A variety of sentences to keep it engaging.
- **Dynamic Feedback:** Highlights correct and incorrect characters as you type.
- **User-Friendly Interface:** Runs smoothly in the terminal with color-coded output.

---

## How It Works 🤔

1. Launch the program in your terminal.
2. A random sentence will appear for you to type.
3. Start typing! As you type:
   - Correct characters are highlighted in **green**.
   - Incorrect characters are highlighted in **red**.
4. Once you've completed the sentence, you'll see:
   - Your **WPM (Words Per Minute)** score.
   - Your **accuracy percentage**.
5. Press any key to try another round or `ESC` to exit.

---

## Installation 🛠️

### Prerequisites

- Python 3.8+

### Steps

1. Clone this repository:
   ```
   git clone https://github.com/your-username/typing-test-cli.git
   ```

2. Navigate to the project directory:
   ```
   cd typing-test-cli
   ```

3. Install required dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

4. Run the program:
   ```
   python main.py
   ```

---

## Modules Used 📚

- **curses**: For creating the interactive terminal interface with color-coded feedback.
- **random**: To randomly select sentences for the typing test.
- **time**: For calculating typing speed (WPM) and accuracy based on elapsed time.

---

## File Structure 📂

```
.
├── main.py               # Entry point of the application
├── typing_test.py        # Core logic for the typing test
├── typing_texts.txt      # Collection of sentences for the typing test
└── README.md             # Project documentation
```

---

## Contributing 🤝

Contributions are welcome! Here’s how you can contribute:

1. Fork the repository.
2. Create a new branch:
   ```
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```
   git push origin feature-name
   ```
5. Create a pull request.

---

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments 🙌

- Thanks to the **open-source community** for inspiration and support.
- Special shoutout to **you** for checking out this project!
