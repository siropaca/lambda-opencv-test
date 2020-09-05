#!/bin/bash

ZIP_FILENAME="function"
LAMBDA_FUNCNAME="image_test"

echo "Zipping..."
zip -rq $ZIP_FILENAME.zip * -x deploy.sh