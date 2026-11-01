# CNN Image Classification and Streamlit Application
#Demo :https://cnn-app-project-x6x6s2gekig22mnraz3sdt.streamlit.app/

## Project Overview

This project demonstrates two practical applications of Python:

1. **CNN Image Classification:** A Convolutional Neural Network (CNN) is developed and trained using the MNIST handwritten digit dataset to recognize digits from 0 to 9.
2. **Streamlit Application:** A Student Marks Calculator is developed using Streamlit to calculate total marks, percentage, average, grade, and pass/fail status.

The project combines deep learning concepts with interactive web application development.

## Project Objectives

- Understand the working of Convolutional Neural Networks.
- Perform image preprocessing and normalization.
- Build, train, and evaluate a CNN model.
- Predict handwritten digits using the MNIST dataset.
- Develop an interactive application using Streamlit.
- Automate student marks and grade calculations.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow | Deep learning framework |
| Keras | CNN model development |
| NumPy | Numerical operations |
| Matplotlib | Data visualization and graphs |
| Streamlit | Interactive web application |
| MNIST | Handwritten digit dataset |

## Project Structure

```text
CNN-Image-Classification-Streamlit/
│
├── PranathiR_CNN_Streamlit_Project.py
├── CNN_Image_Classification_Streamlit_Minor_Project_Report.pdf
└── README.md
```

## Part A: CNN Image Classification

### Dataset Description

The MNIST dataset is used for handwritten digit classification.

- Total Images: 70,000
- Training Images: 60,000
- Testing Images: 10,000
- Image Dimensions: 28 × 28 pixels
- Image Type: Grayscale
- Classes: 10 (Digits 0–9)

### Data Preprocessing

The following preprocessing operations are performed:

1. Load the MNIST dataset using TensorFlow Keras.
2. Convert image pixel values into floating-point numbers.
3. Normalize pixel values from 0–255 to 0–1.
4. Reshape images into the format (28, 28, 1).
5. Use the integer-encoded labels for classification.

### CNN Architecture

The CNN model consists of the following layers:

1. Input Layer
2. Convolutional Layer – 32 filters
3. MaxPooling Layer
4. Convolutional Layer – 64 filters
5. MaxPooling Layer
6. Flatten Layer
7. Dense Layer – 64 neurons
8. Dropout Layer – 0.5
9. Output Layer – 10 neurons with Softmax activation

### Model Training

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Evaluation Metric: Accuracy
- Epochs: 5
- Batch Size: 64
- Validation Split: 20%

### Model Evaluation

The trained model is evaluated using the MNIST test dataset.

| Metric | Result |
|---|---:|
| Test Accuracy | 98.81% |
| Test Loss | 0.0352 |
| Correct Predictions | 9,881 |
| Incorrect Predictions | 119 |
| Total Test Images | 10,000 |

## Part B: Streamlit Student Marks Calculator

### Application Description

The Student Marks Calculator is an interactive web application developed using Streamlit. It allows users to enter student details and marks in five subjects.

### User Inputs

- Student Name
- Python Marks
- Machine Learning Marks
- DBMS Marks
- Mathematics Marks
- Computer Networks Marks

### Application Features

- Simple and user-friendly interface.
- Student details and marks input.
- Input validation for student name.
- Marks restricted between 0 and 100.
- Automatic total marks calculation.
- Percentage and average calculation.
- Automatic grade assignment.
- Pass/Fail status checking.
- Organized result display.

### Grade Calculation

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| Below 60 | D |

**Passing Criteria:** A student must score at least 35 marks in every subject to pass.

## Installation and Setup

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### Step 3: Open the Project Folder

```bash
cd CNN-Image-Classification-Streamlit
```

### Step 4: Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Required Libraries

```bash
pip install tensorflow numpy matplotlib streamlit
```

## How to Run the Project

Open the project folder in VS Code or a terminal.

Run the following command:

```bash
streamlit run PranathiR_CNN_Streamlit_Project.py
```

After execution, Streamlit will provide a local URL. Open that URL in your web browser to access the application.

**Note:** The MNIST dataset is downloaded through TensorFlow Keras when the dataset-loading code is executed. An internet connection may be required for the initial download.

## Expected Results

### CNN Image Classification

The CNN model predicts handwritten digits from 0 to 9 and displays the actual and predicted labels. It also displays training and validation accuracy, loss graphs, and test performance.

### Student Marks Calculator

The application accepts student details and subject marks and displays the calculated academic results.

**Example Output:**

| Details | Result |
|---|---:|
| Total Marks | 419/500 |
| Percentage | 83.80% |
| Average | 83.80 |
| Grade | A |
| Result | PASS |

## Challenges Faced

- Understanding CNN architecture and its layers.
- Preparing image data for model training.
- Monitoring model accuracy and loss.
- Designing an interactive Streamlit interface.
- Implementing grade calculations and input validation.

## Future Improvements

- Improve the CNN model using advanced architectures.
- Allow users to upload handwritten digit images for prediction.
- Extend classification to datasets such as CIFAR-10.
- Integrate a database to store student records.
- Add performance charts and PDF result downloads.

## Learning Outcomes

This project provides practical experience in:

- Python programming and data preprocessing.
- Deep learning and CNN architecture.
- Model training, testing, and evaluation.
- Image classification and prediction.
- Streamlit application development.
- Input validation and automated calculations.

## Conclusion

The project successfully demonstrates handwritten digit classification using a CNN model and the development of a Student Marks Calculator using Streamlit.

The CNN model achieved a test accuracy of 98.81% on the MNIST dataset. The Streamlit application successfully calculates and displays student academic results.

Overall, this project helped develop practical knowledge of deep learning, image processing, Python programming, and interactive web application development.

## References

1. TensorFlow: https://www.tensorflow.org/
2. Keras: https://keras.io/
3. Streamlit: https://docs.streamlit.io/
4. MNIST Dataset: https://keras.io/api/datasets/mnist/
## Project Overview

This project demonstrates two practical applications of Python:

1. **CNN Image Classification:** A Convolutional Neural Network (CNN) is developed and trained using the MNIST handwritten digit dataset to recognize digits from 0 to 9.
2. **Streamlit Application:** A Student Marks Calculator is developed using Streamlit to calculate total marks, percentage, average, grade, and pass/fail status.

The project combines deep learning concepts with interactive web application development.

## Project Objectives

- Understand the working of Convolutional Neural Networks.
- Perform image preprocessing and normalization.
- Build, train, and evaluate a CNN model.
- Predict handwritten digits using the MNIST dataset.
- Develop an interactive application using Streamlit.
- Automate student marks and grade calculations.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow | Deep learning framework |
| Keras | CNN model development |
| NumPy | Numerical operations |
| Matplotlib | Data visualization and graphs |
| Streamlit | Interactive web application |
| MNIST | Handwritten digit dataset |

## Project Structure

```text
CNN-Image-Classification-Streamlit/
│
├── PranathiR_CNN_Streamlit_Project.py
├── CNN_Image_Classification_Streamlit_Minor_Project_Report.pdf
└── README.md
```

## Part A: CNN Image Classification

### Dataset Description

The MNIST dataset is used for handwritten digit classification.

- Total Images: 70,000
- Training Images: 60,000
- Testing Images: 10,000
- Image Dimensions: 28 × 28 pixels
- Image Type: Grayscale
- Classes: 10 (Digits 0–9)

### Data Preprocessing

The following preprocessing operations are performed:

1. Load the MNIST dataset using TensorFlow Keras.
2. Convert image pixel values into floating-point numbers.
3. Normalize pixel values from 0–255 to 0–1.
4. Reshape images into the format (28, 28, 1).
5. Use the integer-encoded labels for classification.

### CNN Architecture

The CNN model consists of the following layers:

1. Input Layer
2. Convolutional Layer – 32 filters
3. MaxPooling Layer
4. Convolutional Layer – 64 filters
5. MaxPooling Layer
6. Flatten Layer
7. Dense Layer – 64 neurons
8. Dropout Layer – 0.5
9. Output Layer – 10 neurons with Softmax activation

### Model Training

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Evaluation Metric: Accuracy
- Epochs: 5
- Batch Size: 64
- Validation Split: 20%

### Model Evaluation

The trained model is evaluated using the MNIST test dataset.

| Metric | Result |
|---|---:|
| Test Accuracy | 98.81% |
| Test Loss | 0.0352 |
| Correct Predictions | 9,881 |
| Incorrect Predictions | 119 |
| Total Test Images | 10,000 |

## Part B: Streamlit Student Marks Calculator

### Application Description

The Student Marks Calculator is an interactive web application developed using Streamlit. It allows users to enter student details and marks in five subjects.

### User Inputs

- Student Name
- Python Marks
- Machine Learning Marks
- DBMS Marks
- Mathematics Marks
- Computer Networks Marks

### Application Features

- Simple and user-friendly interface.
- Student details and marks input.
- Input validation for student name.
- Marks restricted between 0 and 100.
- Automatic total marks calculation.
- Percentage and average calculation.
- Automatic grade assignment.
- Pass/Fail status checking.
- Organized result display.

### Grade Calculation

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| Below 60 | D |

**Passing Criteria:** A student must score at least 35 marks in every subject to pass.

## Installation and Setup

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### Step 3: Open the Project Folder

```bash
cd CNN-Image-Classification-Streamlit
```

### Step 4: Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Required Libraries

```bash
pip install tensorflow numpy matplotlib streamlit
```

## How to Run the Project

Open the project folder in VS Code or a terminal.

Run the following command:

```bash
streamlit run PranathiR_CNN_Streamlit_Project.py
```

After execution, Streamlit will provide a local URL. Open that URL in your web browser to access the application.

**Note:** The MNIST dataset is downloaded through TensorFlow Keras when the dataset-loading code is executed. An internet connection may be required for the initial download.

## Expected Results

### CNN Image Classification

The CNN model predicts handwritten digits from 0 to 9 and displays the actual and predicted labels. It also displays training and validation accuracy, loss graphs, and test performance.

### Student Marks Calculator

The application accepts student details and subject marks and displays the calculated academic results.

**Example Output:**

| Details | Result |
|---|---:|
| Total Marks | 419/500 |
| Percentage | 83.80% |
| Average | 83.80 |
| Grade | A |
| Result | PASS |

## Challenges Faced

- Understanding CNN architecture and its layers.
- Preparing image data for model training.
- Monitoring model accuracy and loss.
- Designing an interactive Streamlit interface.
- Implementing grade calculations and input validation.

## Future Improvements

- Improve the CNN model using advanced architectures.
- Allow users to upload handwritten digit images for prediction.
- Extend classification to datasets such as CIFAR-10.
- Integrate a database to store student records.
- Add performance charts and PDF result downloads.

## Learning Outcomes

This project provides practical experience in:

- Python programming and data preprocessing.
- Deep learning and CNN architecture.
- Model training, testing, and evaluation.
- Image classification and prediction.
- Streamlit application development.
- Input validation and automated calculations.

## Conclusion

The project successfully demonstrates handwritten digit classification using a CNN model and the development of a Student Marks Calculator using Streamlit.

The CNN model achieved a test accuracy of 98.81% on the MNIST dataset. The Streamlit application successfully calculates and displays student academic results.

Overall, this project helped develop practical knowledge of deep learning, image processing, Python programming, and interactive web application development.

## References

1. TensorFlow: https://www.tensorflow.org/
2. Keras: https://keras.io/
3. Streamlit: https://docs.streamlit.io/
4. MNIST Dataset: https://keras.io/api/datasets/mnist/
