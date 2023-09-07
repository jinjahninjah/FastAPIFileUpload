import io
import os
import shutil

from fastapi import FastAPI, File, UploadFile

from app.utilities import extract_text

api = FastAPI(
    docs_url="/",
    version="0.0.1"
)


@api.post("/version")
def version_endpoint():
    """Returns the version of the API"""
    return {"result": api.version}


@api.post("/upload-file")
def upload_file_endpoint(file: UploadFile = File(...)):
    """Uploads a file to a directory in the app using the
    synchronous approach"""
    dir_fp = os.path.relpath("source_data")
    if not os.path.exists("source_data"):
        os.mkdir(dir_fp)
    fp = os.path.join(dir_fp, file.filename)
    with open(fp, "wb") as f:
        shutil.copyfileobj(file.file, f)


@api.post("/upload-files")
def upload_files_endpoint(files: list[UploadFile] = File(...)):
    """Uploads multiple files to a directory in the app using the
    synchronous approach"""
    dir_fp = os.path.relpath("source_data")
    if not os.path.exists("source_data"):
        os.mkdir(dir_fp)
    for file in files:
        fp = os.path.join(dir_fp, file.filename)
        with open(fp, "wb") as f:
            shutil.copyfileobj(file.file, f)


@api.post("/upload-file-contents")
async def upload_contents_endpoint(file: UploadFile):
    """Uploads the file's contents straight from the
     SpooledTemporaryFile (where the memory magic happens)
     without saving the file anywhere. This is useful
     when you need to work within memory constraints. We are also
     taking advantage of asynchronous programming, which means
     we can handle multiple requests at the same time"""
    contents = io.BytesIO(await file.read())
    text = extract_text(contents)
    return {"result": text}
