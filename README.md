# AWS Cloud Resume Challenge

A personal resume website hosted on AWS with a serverless visitor counter and automated CI/CD deployment using GitHub Actions and OpenID Connect (OIDC).

## Project Overview

This project demonstrates static website hosting, secure content delivery, serverless computing, and cloud database integration using AWS services.

## Live Website

https://d21qij5d5kmyfh.cloudfront.net

## Architecture

### Resume Website
Browser -> Amazon CloudFront (HTTPS) -> CloudFront OAC -> Private Amazon S3 Bucket

### Visitor Counter
Browser -> Amazon API Gateway -> AWS Lambda -> Amazon DynamoDB

## AWS Services Used

- Amazon S3: Stores website files.
- Amazon CloudFront: Delivers the website over HTTPS.
- CloudFront Origin Access Control: Secures access to the S3 origin.
- Amazon API Gateway: Exposes the visitor-counter endpoint.
- AWS Lambda: Processes visitor-counter requests.
- Amazon DynamoDB: Stores the visitor count.
- Amazon CloudWatch: Collects Lambda execution logs.
- AWS IAM: Controls access to AWS resources.
- GitHub Actions: Automates frontend deployment.
- OpenID Connect (OIDC): Allows GitHub Actions to assume an AWS IAM role using temporary credentials.

## Technologies

- Python
- HTML5
- CSS3
- JavaScript
- AWS CLI
- JSON
- Git

## Features

- Personal resume website.
- HTTPS delivery through CloudFront.
- Private S3 origin with Origin Access Control.
- Serverless visitor-counter API.
- DynamoDB-backed visitor counter.
- API CORS restricted to the website origin.
- AWS infrastructure configured using CLI commands and JSON files.
- Automated frontend deployment to S3 using GitHub Actions.
- CloudFront cache invalidation after deployment.

## Project Structure

    cloud-resume-challenge/
    ├── backend/
    │   └── visitor-counter/
    │       ├── lambda_function.py
    │       ├── trust-policy.json
    │       └── dynamodb-lambda-policy.json
    ├── frontend/
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    ├── bucket-policy.json
    ├── cloudfront-distribution.json
    ├── cors-config.json
    ├── .gitignore
    └── README.md

## Visitor Counter Workflow

1. The website requests the visitor-count API.
2. API Gateway forwards the request to Lambda.
3. Lambda increments the counter in DynamoDB.
4. Lambda returns the updated count.
5. The frontend displays the count.

The counter measures successful API invocations, not unique visitors. Refreshing the website or making another API request can increase the count.

## Security

- S3 Block Public Access is enabled.
- CloudFront accesses S3 using Origin Access Control.
- Lambda has narrowly scoped DynamoDB permissions.
- API CORS allows the deployed CloudFront website origin.
- AWS credentials and generated deployment artifacts should not be committed to Git.

## Deployment Region

AWS Asia Pacific (Mumbai): `ap-south-1`

## Key Learnings

- Static website hosting with Amazon S3.
- HTTPS content delivery with CloudFront.
- Secure S3 access using Origin Access Control.
- Serverless APIs using API Gateway and Lambda.
- DynamoDB integration.
- IAM permissions and least privilege.
- AWS CLI resource management.
- Frontend JavaScript integration with a serverless backend.

## Automated Deployment

1. A change is pushed to the configured GitHub branch.
2. GitHub Actions starts the deployment workflow when its configured triggers match.
3. GitHub authenticates to AWS using OIDC.
4. The workflow assumes the configured IAM role and obtains temporary credentials.
5. Frontend files are synchronized to Amazon S3.
6. A CloudFront invalidation refreshes cached website content.

## Future Improvements

- Add automated backend tests.
- Improve monitoring and error handling.
- Explore infrastructure as code.


## Automated Testing

The project includes Python unit tests for the Lambda visitor-counter function. Tests cover successful responses, DynamoDB updates, response headers, and error handling. DynamoDB interactions are mocked during testing.

Run the tests locally:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p "test_*.py" -v
```

## CI/CD Deployment

GitHub Actions runs the Lambda unit tests before deployment. After successful tests on an eligible push to `main`, GitHub Actions authenticates to AWS using OIDC, synchronizes frontend files to S3, and invalidates the CloudFront cache. Pull requests run tests without deploying.

## Repository

Source code: https://github.com/Krishnna0001/aws-cloud-resume-challenge
