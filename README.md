# ml_project1_ocr
First Machine Learning App OCR
First written application for Machine Learning OCR. App written to defeat Verification Codes on https://afrts.forest.gov.tw/OT01_1.aspx

== 1 Get Data
Using Python to get data:
1. `ocr_1_collect.py` download random 6 digit verification data with their file names to local.
2. `ocr_2_image_process.py` because the image is always neat, split the image into 6 separate files at exact locations. Grayscale.
3. `ocr_3_output.py` assort split digit files into digit folders groups.
4. `ocr_4_matrix.py` check the grayscale color and change to 0-255 matrix.

== 2 Train data
train data with `train.m`


== 3 Validation data
validate data by grabbing new files with 1 and do `predict.m` to find out results. Since this is a simple system, the accuracy is likely to be 100%
