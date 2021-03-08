# ml_project1_ocr
First Machine Learning App OCR. Logistic Regression with OCR
First written application for Machine Learning OCR. App written to defeat Verification Codes on https://afrts.forest.gov.tw/OT01_1.aspx.
https://user-images.githubusercontent.com/10494709/110335968-bfa23e80-8067-11eb-8a7a-0baa216e7cb5.png

# 1 Get Data
Using Python to get data:
1. `ocr_1_collect.py` download random 6 digit verification data with their file names to local.
https://user-images.githubusercontent.com/10494709/110336140-e9f3fc00-8067-11eb-9c2d-88b3c347fde0.jpg
3. `ocr_2_image_process.py` because the image is always neat, split the image into 6 separate files at exact locations. Grayscale.
https://user-images.githubusercontent.com/10494709/110336121-e5c7de80-8067-11eb-8c51-c40fb9521f58.jpg
4. `ocr_3_output.py` assort split digit files into digit folders groups.
5. `ocr_4_matrix.py` check the grayscale color and change to 0-255 matrix.

# 2 Train data
train data with `train.m`


# 3 Validation data
validate data by grabbing new files with 1 and do `predict.m` to find out results. Since this is a simple system, the accuracy is likely to be 100%
