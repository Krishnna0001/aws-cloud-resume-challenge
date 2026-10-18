import json
import os
import boto3

dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={"counterId": "resume"},
            UpdateExpression="ADD visitCount :increment",
            ExpressionAttributeValues={":increment": 1},
            ReturnValues="UPDATED_NEW"
        )

        count = int(response["Attributes"]["visitCount"])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Cache-Control": "no-store"
            },
            "body": json.dumps({
                "message": "Visitor count retrieved successfully",
                "visitorCount": count
            })
        }

    except Exception:
        print("Error updating the visitor counter")
        raise
