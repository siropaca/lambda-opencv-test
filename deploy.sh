#!/bin/bash

ZIP_FILENAME="function"
LAMBDA_FUNCNAME="image_test"

echo "Zipping..."
zip -rq $ZIP_FILENAME.zip ./lambda_function.py -x deploy.sh

echo "Uploading..."
aws lambda update-function-code  \
   --function-name $LAMBDA_FUNCNAME  \
   --zip-file fileb://$ZIP_FILENAME.zip

echo "Cleaning..."
rm ./$ZIP_FILENAME.zip

echo "Finished!"