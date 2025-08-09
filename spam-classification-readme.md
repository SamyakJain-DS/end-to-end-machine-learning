# ✉️ E-Mail/SMS Spam Classification — Development Highlights

## 🔗 Live App
Access the live deployed project at [https://samyak-jain-ml.streamlit.app/E-Mail_Spam_Detector](https://samyak-jain-ml.streamlit.app/E-Mail_Spam_Detector)

1. Parsing and Extracting E-Mail Files:

- Successfully handled raw `.eml` files, including those with complex multipart structures and HTML content.
- Built robust parsing utilities using Python’s email library and BeautifulSoup to extract clean message bodies from diverse e-mail formats.

2. Custom Preprocessing Classes for scikit-learn Pipelines:

- Developed `custom transformer classes` (e.g., CleanBody) to preprocess e-mail text, compatible with scikit-learn’s pipeline API.
- Overcame serialization and compatibility issues by ensuring all custom functions and classes were picklable and properly integrated.

3. Threshold Tuning for Optimal Performance:

- Achieved outstanding spam detection metrics by tuning the classification threshold:
- - Retained a `Precision Score` of `99%`, while
- - `Recall Score` boosted to `91%` (from a base of 76%)
This careful threshold adjustment allowed the model to balance false positives and false negatives, maximizing real-world utility.

### Summary:
The project tackled real-world challenges in `e-mail parsing`, `custom pipeline engineering`, and `advanced model tuning`, resulting in a spam classifier that is both accurate and practical for deployment.

