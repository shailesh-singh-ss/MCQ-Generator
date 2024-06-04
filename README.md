# MCQ Question Generator with AI

This project leverages generative AI to create multiple-choice questions (MCQs) with a review mechanism. The system utilizes `LangChain`, `Python`, `Streamlit`, and the `Cohere` LLM (Language Model) to generate questions based on the content of uploaded PDF or TXT files.

## Features

- Upload a PDF or TXT file containing the content.
- Specify the topic and number of questions to generate.
- Select the difficulty level for the questions.
- Generate MCQs using a generative AI model.
- Review and edit the generated questions.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Streamlit
- Cohere API Key (for using Cohere's LLM)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/mcq-question-generator.git
    cd mcq-question-generator
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the Cohere API key:
    - Sign up on [Cohere](https://cohere.ai) and get your API key.
    - Create a file named `.env` in the root directory and add your API key:
        ```env
        COHERE_API_KEY=your_cohere_api_key
        ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload a PDF or TXT file, enter the topic name, specify the number of questions, and choose the difficulty level.

4. Click on "Generate Questions" to create the MCQs.

5. Review the generated questions and make any necessary edits.

## Project Structure

- `app.py`: Main Streamlit application file.
- `mcq_generator.py`: Contains the logic for generating MCQs using the Cohere LLM.
- `requirements.txt`: List of Python packages required for the project.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please contact us at your-ss.forcoding.com.

---
