
# ============================================================
# PROJECT: CNN IMAGE CLASSIFICATION AND STREAMLIT APPLICATION
# Dataset: MNIST
# Streamlit App: Student Marks Calculator
# ============================================================

# STEP 1: IMPORT REQUIRED LIBRARIES

import os

# Reduce TensorFlow informational messages
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# Configure TensorFlow logging
tf.get_logger().setLevel("ERROR")


# ============================================================
# PART A: CNN IMAGE CLASSIFICATION
# ============================================================


# STEP 2: LOAD DATASET, PREPROCESS, BUILD AND TRAIN CNN MODEL

@st.cache_resource(show_spinner=False)
def train_cnn_model():

    # Load MNIST dataset
    (x_train, y_train), (x_test, y_test) = (
        tf.keras.datasets.mnist.load_data()
    )

    # Dataset information
    dataset_info = {
        "training_images": x_train.shape,
        "training_labels": y_train.shape,
        "testing_images": x_test.shape,
        "testing_labels": y_test.shape,
        "classes": len(np.unique(y_train))
    }

    # Normalize images
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    # Reshape images for CNN input
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)

    # Build CNN model
    model = tf.keras.Sequential([

        tf.keras.layers.Input(shape=(28, 28, 1)),

        # First convolution layer
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu"
        ),

        # First pooling layer
        tf.keras.layers.MaxPooling2D((2, 2)),

        # Second convolution layer
        tf.keras.layers.Conv2D(
            64, (3, 3), activation="relu"
        ),

        # Second pooling layer
        tf.keras.layers.MaxPooling2D((2, 2)),

        # Flatten layer
        tf.keras.layers.Flatten(),

        # Dense layer
        tf.keras.layers.Dense(64, activation="relu"),

        # Dropout layer
        tf.keras.layers.Dropout(0.5),

        # Output layer
        tf.keras.layers.Dense(10, activation="softmax")

    ])

    # Compile CNN model
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    # Train CNN model
    history = model.fit(
        x_train,
        y_train,
        epochs=5,
        batch_size=64,
        validation_split=0.2,
        verbose=0
    )

    # Evaluate model
    test_loss, test_accuracy = model.evaluate(
        x_test,
        y_test,
        verbose=0
    )

    # Predict test images
    predictions = model.predict(
        x_test,
        verbose=0
    )

    predicted_labels = np.argmax(
        predictions, axis=1
    )

    # Calculate correct and incorrect predictions
    correct = np.sum(predicted_labels == y_test)
    incorrect = np.sum(predicted_labels != y_test)

    # Capture model summary
    summary_lines = []
    model.summary(print_fn=lambda line: summary_lines.append(line))
    model_summary = "\n".join(summary_lines)

    return (
        model,
        history.history,
        dataset_info,
        test_loss,
        test_accuracy,
        correct,
        incorrect,
        x_train[0],
        y_train[0],
        x_test[:10],
        y_test[:10],
        predicted_labels[:10],
        model_summary
    )


# ============================================================
# PART B: STREAMLIT APPLICATION
# STUDENT MARKS CALCULATOR
# ============================================================


# STEP 3: STREAMLIT PAGE CONFIGURATION

st.set_page_config(
    page_title="CNN and Student Marks Calculator",
    page_icon="📚",
    layout="wide"
)


# Application heading
st.title("CNN Image Classification and Streamlit Application")



# ============================================================
# PART A: DISPLAY CNN RESULTS
# ============================================================

st.header("Part A : CNN Image Classification")

with st.spinner("Loading MNIST dataset and training CNN model..."):

    (
        model,
        history,
        dataset_info,
        test_loss,
        test_accuracy,
        correct,
        incorrect,
        sample_image,
        sample_label,
        test_images,
        actual_labels,
        predicted_labels,
        model_summary
    ) = train_cnn_model()


# Display dataset information

st.subheader("MNIST Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("Training Images", "60,000")
col2.metric("Testing Images", "10,000")
col3.metric("Number of Classes", "10")

st.write("Training Image Shape:", dataset_info["training_images"])
st.write("Testing Image Shape:", dataset_info["testing_images"])

# Display sample image

st.subheader("Sample MNIST Image")

st.image(
    sample_image.squeeze(),
    caption=f"Actual Handwritten Digit: {sample_label}",
    width=150
)


# Display CNN model summary

with st.expander("View CNN Model Summary"):

    st.code(model_summary, language="text")


# Display evaluation results

st.subheader("CNN Model Evaluation")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Test Accuracy",
    f"{test_accuracy * 100:.2f}%"
)

col2.metric(
    "Test Loss",
    f"{test_loss:.4f}"
)

col3.metric(
    "Correct Predictions",
    f"{correct}"
)

col4.metric(
    "Incorrect Predictions",
    f"{incorrect}"
)


# ============================================================
# STEP 4: DISPLAY ACCURACY GRAPH
# ============================================================

st.subheader("Training and Validation Accuracy")

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(
    history["accuracy"],
    label="Training Accuracy"
)

ax.plot(
    history["val_accuracy"],
    label="Validation Accuracy"
)

ax.set_title("CNN Model Accuracy")
ax.set_xlabel("Epochs")
ax.set_ylabel("Accuracy")
ax.legend()
ax.grid(True)

st.pyplot(fig)
plt.close(fig)


# ============================================================
# STEP 5: DISPLAY LOSS GRAPH
# ============================================================

st.subheader("Training and Validation Loss")

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(
    history["loss"],
    label="Training Loss"
)

ax.plot(
    history["val_loss"],
    label="Validation Loss"
)

ax.set_title("CNN Model Loss")
ax.set_xlabel("Epochs")
ax.set_ylabel("Loss")
ax.legend()
ax.grid(True)

st.pyplot(fig)
plt.close(fig)


# ============================================================
# STEP 6: DISPLAY ACTUAL AND PREDICTED LABELS
# ============================================================

st.subheader("Actual vs Predicted Digits")

fig, axes = plt.subplots(2, 5, figsize=(12, 5))

for i, ax in enumerate(axes.flat):

    ax.imshow(
        test_images[i].squeeze(),
        cmap="gray"
    )

    actual = actual_labels[i]
    predicted = predicted_labels[i]

    ax.set_title(
        f"Actual: {actual}\nPredicted: {predicted}"
    )

    ax.axis("off")

plt.tight_layout()

st.pyplot(fig)
plt.close(fig)


# ============================================================
# PART B: STUDENT MARKS CALCULATOR
# ============================================================

st.divider()

st.header("Part B : Student Marks Calculator")

st.write(
    "Enter your name and marks in five subjects "
    "to calculate your academic performance."
)


# STEP 7: STUDENT INPUTS

with st.form("student_marks_form"):

    student_name = st.text_input(
        "Enter Student Name"
    )

    st.subheader("Enter Subject Marks")

    col1, col2 = st.columns(2)

    with col1:

        python_marks = st.number_input(
            "Python Marks",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

        ml_marks = st.number_input(
            "Machine Learning Marks",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

        dbms_marks = st.number_input(
            "DBMS Marks",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    with col2:

        maths_marks = st.number_input(
            "Mathematics Marks",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

        cn_marks = st.number_input(
            "Computer Networks Marks",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    submitted = st.form_submit_button(
        "Calculate Results",
        use_container_width=True
    )


# ============================================================
# STEP 8: CALCULATE STUDENT RESULTS
# ============================================================

if submitted:

    # Validate student name

    if not student_name.strip():

        st.error("Please enter student name.")

    else:

        # Store subject marks

        marks = [
            python_marks,
            ml_marks,
            dbms_marks,
            maths_marks,
            cn_marks
        ]

        # Calculate total marks

        total = sum(marks)

        # Calculate percentage

        percentage = (total / 500) * 100

        # Calculate average

        average = total / 5

        # Check pass or fail
        # Minimum passing marks: 35 in each subject

        if min(marks) >= 35:

            result = "PASS"

            # Calculate grade

            if percentage >= 90:
                grade = "A+"

            elif percentage >= 80:
                grade = "A"

            elif percentage >= 70:
                grade = "B"

            elif percentage >= 60:
                grade = "C"

            else:
                grade = "D"

        else:

            result = "FAIL"
            grade = "F"


        # ====================================================
        # STEP 9: DISPLAY RESULTS
        # ====================================================

        st.divider()

        st.subheader("Student Results")

        st.write("Student Name:", student_name)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Marks",
            f"{total}/500"
        )

        col2.metric(
            "Percentage",
            f"{percentage:.2f}%"
        )

        col3.metric(
            "Average",
            f"{average:.2f}"
        )

        st.write("Grade:", grade)

        if result == "PASS":

            st.success("Result: PASS")

        else:

            st.error("Result: FAIL")

        st.caption(
            "Passing requirement: At least 35 marks "
            "in every subject."
        )



