

```bash
aws lambda delete-function --function-name devops-lambda-cli

zip function.zip lambda_function.py 

 aws lambda create-function --function-name devops-lambda-cli --runtime python3.12 --role arn:aws:iam::183663605587:role/lambda_execution_role --handler lambda_function.lambda_handler --zip-file fileb://function.zip

aws lambda invoke --function-name devops-lambda-cli output.json
```