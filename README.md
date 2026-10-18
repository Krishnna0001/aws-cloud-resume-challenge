# AWS Cloud Resume Challenge

A personal resume website hosted on AWS with a serverless visitor counter powered by AWS Lambda and Amazon DynamoDB.

## Project Overview

This project demonstrates static website hosting, secure content delivery, serverless computing, and cloud database integration using AWS services.

## Live Website

https://d21qij5d5kmyfh.cloudfront.net

## Architecture

### Resume Website
Browser -> Amazon CloudFront -> Amazon S3

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

## Future Improvements

- Automate deployments using GitHub Actions.
- Add automated backend tests.
- Improve monitoring and error handling.
- Explore infrastructure as code.

