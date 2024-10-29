# Number Plate Detection

This project demonstrates a simple number plate detection system using OpenCV and Haar Cascade Classifier. The system captures video frames, processes them to detect number plates, and highlights the detected plates with bounding boxes.

## Requirements

- Python 3.10
- OpenCV
- NumPy

## Setup

1. Clone the repository.
2. Create a virtual environment:
    ```sh
    python -m venv myenv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```sh
        source myenv/bin/activate
        ```
4. Install the required packages:
    ```sh
    pip install opencv-python numpy
    ```

## Running the Project

1. Ensure you have the Haar Cascade XML file for number plate detection in the Resources directory.
2. Place the video file (`anpr.mp4`) in the Resources directory.
3. Run the script:
    ```sh
    python main.py
    ```

## Code Explanation

- The script initializes video capture from a file and sets the frame width, height, and brightness.
- It loads a Haar Cascade Classifier for number plate detection.
- The script reads frames from the video, converts them to grayscale, and detects number plates.
- If a detected number plate's area is larger than a minimum threshold, it draws a rectangle around the number plate and labels it.
