# Project documentation

## Introduction

This project provides a RESTful API using Flask that allows users to interact with a LLaMA model for text generation. The API accepts user input and returns generated text based on the input. It is designed to be simple and extensible for future enhancements.

## Requirements

- Python 3.9 or higher
- Flask
- Transformers (Hugging Face)
- Flask-CORS (for cross-origin resource sharing)
- PyTorch (or TensorFlow, depending on your model implementation)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/llama-api.git
   cd llama-api
   ```

2. **Create a virtual environment :**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   Create a `requirements.txt` file with the following content:

   ```plaintext
   flask
   transformers
   flask-cors
   torch  # or tensorflow, depending on your model
   ```

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the LLaMA model** (if not using a pre-trained model from Hugging Face):

   Follow the instructions from the [Hugging Face model hub](https://huggingface.co/models) to download the model and tokenizer.

## Usage

### Running the Application

1. Ensure you have set the correct path for the LLaMA model in `app.py`:

   ```python
   model_name = "path/to/llama/model"  # Replace with actual model path or name
   ```

2. Start the Flask application:

   ```
   python app.py
   ```

   The application will run on `http://localhost:5000`.

### API Endpoints

#### POST `/generate`

- **Description**: Generates text based on the input provided by the user.
- **Request Body**:

  ```json
  {
    "text": "Your input text here"
  }
  ```

- **Response**:

  - **Success (200)**:

    ```json
    {
      "response": "Generated text based on the input."
    }
    ```

  - **Error (400)**:

    ```json
    {
      "error": "Missing 'text' field in the request"
    }
    ```

### Error Handling

The API includes basic error handling for missing fields in the request body. If the `text` field is not provided, a 400 error response will be returned.

## Testing the API

You can test the API using `curl` or tools like Postman.

### Example `curl` Command

```
curl -X POST -H "Content-Type: application/json" -d '{"text": "What is the weather today?"}' http://localhost:5000/generate
```

### Example Postman Request

1. Set the request type to POST.
2. Enter the URL: `http://localhost:5000/generate`.
3. In the body, select "raw" and set the type to JSON, then enter:

   ```json
   {
     "text": "What is the weather today?"
   }
   ```

4. Send the request and view the response.

## Docker Setup

To containerize the application, you can use Docker. This allows you to run the application in a consistent environment across different systems

Create a file named Dockerfile in the root of your Project

Building the Docker Image
Navigate to the directory where your Dockerfile is located.
Build the Docker image using the following command:

docker build -t image-name .

then run it on your local host using:

docker run -p 5000:5000 image-name
