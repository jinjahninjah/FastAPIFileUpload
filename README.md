# FastAPI File Upload Workshop

This is a simple FastAPI application that demonstrates how to handle file uploads using the synchronous and asynchronous approaches.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)

## Prerequisites

Before you begin, make sure you have the following installed:

- Python (>= 3.6)
- FastAPI
- Uvicorn (for running the application)
- aiofiles (for asynchronous file handling)



## Installation

Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/FastAPIFileUpload.git
cd FastAPIFileUpload
```
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

To run the FastAPI application, use the following command:
```bash
uvicorn app.api:api 
```
The application will start, and you can access it at http://localhost:8000.

**Endpoints**
1. **Get API Version**
   - **URL:** `/version`
   - **HTTP Method:** POST
   - **Description:** Returns the version of the API.
   - **Example Request:**
     ```bash
     curl -X POST http://localhost:8000/version
     ```
   - **Example Response:**
     ```json
     {"result": "0.0.1"}

2. **Upload a Single File**
   - **URL:** `/upload-file`
   - **HTTP Method:** POST
   - **Description:** Uploads a single file to a directory in the app using the synchronous approach.
   - **Example Request:**
     ```bash
     curl -X POST -F "file=@/path/to/your/file.txt" http://localhost:8000/upload-file
     ```

3. **Upload Multiple Files**
   - **URL:** `/upload-files`
   - **HTTP Method:** POST
   - **Description:** Uploads multiple files to a directory in the app using the synchronous approach.
   - **Example Request:**
     ```bash
     curl -X POST -F "files=@/path/to/your/file1.txt" -F "files=@/path/to/your/file2.txt" http://localhost:8000/upload-files
     ```

4. **Upload File Contents Only**
   - **URL:** `/upload-file-contents`
   - **HTTP Method:** POST
   - **Description:** Uploads the file's contents straight from the SpooledTemporaryFile or UploadFile without saving the file anywhere. This is useful when you need to work within memory constraints and supports asynchronous programming.
   - **Example Request:**
     ```bash
     curl -X POST -F "file=@/path/to/your/file.txt" http://localhost:8000/upload-file-contents
     ```
   - **Example Response:**
     ```json
     {"result": "Contents of the uploaded file"}
     ```