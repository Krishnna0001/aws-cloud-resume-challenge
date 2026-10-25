import importlib.util
import json
import os
import unittest
from pathlib import Path
from unittest.mock import patch


LAMBDA_PATH = (
    Path(__file__).resolve().parent.parent
    / "backend"
    / "visitor-counter"
    / "lambda_function.py"
)


class TestVisitorCounterLambda(unittest.TestCase):

    def setUp(self):
        # Configure the environment variable expected by the Lambda.
        self.env_patcher = patch.dict(
            os.environ,
            {"TABLE_NAME": "ResumeVisitorCounter"}
        )
        self.env_patcher.start()
        self.addCleanup(self.env_patcher.stop)

        # Mock boto3 so no real AWS resources are accessed.
        self.aws_patcher = patch("boto3.resource")
        self.mock_resource = self.aws_patcher.start()
        self.addCleanup(self.aws_patcher.stop)

        self.mock_table = (
            self.mock_resource.return_value.Table.return_value
        )

        # Load the actual Lambda source code.
        spec = importlib.util.spec_from_file_location(
            "lambda_function_under_test",
            LAMBDA_PATH
        )

        self.lambda_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.lambda_module)

    def test_returns_successful_visitor_count(self):
        self.mock_table.update_item.return_value = {
            "Attributes": {"visitCount": 26}
        }

        response = self.lambda_module.lambda_handler({}, None)

        self.assertEqual(response["statusCode"], 200)

        body = json.loads(response["body"])

        self.assertEqual(
            body["message"],
            "Visitor count retrieved successfully"
        )
        self.assertEqual(body["visitorCount"], 26)

    def test_increments_counter_using_dynamodb(self):
        self.mock_table.update_item.return_value = {
            "Attributes": {"visitCount": 27}
        }

        self.lambda_module.lambda_handler({}, None)

        self.mock_table.update_item.assert_called_once_with(
            Key={"counterId": "resume"},
            UpdateExpression="ADD visitCount :increment",
            ExpressionAttributeValues={":increment": 1},
            ReturnValues="UPDATED_NEW"
        )

    def test_sets_response_headers(self):
        self.mock_table.update_item.return_value = {
            "Attributes": {"visitCount": 28}
        }

        response = self.lambda_module.lambda_handler({}, None)

        self.assertEqual(
            response["headers"]["Content-Type"],
            "application/json"
        )
        self.assertEqual(
            response["headers"]["Cache-Control"],
            "no-store"
        )
        self.assertIn(
            "Access-Control-Allow-Origin",
            response["headers"]
        )

    def test_propagates_dynamodb_error(self):
        self.mock_table.update_item.side_effect = RuntimeError(
            "Simulated DynamoDB failure"
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "Simulated DynamoDB failure"
        ):
            self.lambda_module.lambda_handler({}, None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
