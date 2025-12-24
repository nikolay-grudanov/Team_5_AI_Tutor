---
source_image: page_420.png
page_number: 420
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.68
tokens: 7557
characters: 1742
timestamp: 2025-12-24T03:12:00.852816
finish_reason: stop
---

KeySchema:
    - AttributeName: id
      KeyType: HASH
AttributeDefinitions:
    - AttributeName: id
      AttributeType: S
ProvisionedThroughput:
    ReadCapacityUnits: 10
    WriteCapacityUnits: 5
UpdateReplacePolicy: Retain
DeletionPolicy: Retain
Metadata:
    aws:cdk:path: cdk-lambda-dynamodb-fargate/Table/Resource
CDKMetadata:
    Type: AWS::CDK::Metadata
    Properties:
        Modules: aws-cdk=1.6.1,
            @aws-cdk/aws-applicationautoscaling=1.6.1,
            @aws-cdk/aws-autoscaling-common=1.6.1,
            @aws-cdk/aws-cloudwatch=1.6.1,
            @aws-cdk/aws-dynamodb=1.6.1,
            @aws-cdk/aws-iam=1.6.1,
            @aws-cdk/core=1.6.1,
            @aws-cdk/cx-api=1.6.1,@aws-cdk/region-info=1.6.1,
            jsii-runtime=Python/3.7.4

Развертываем стек CDK с помощью команды cdk deploy:

$ cdk deploy
cdk-lambda-dynamodb-fargate: deploying...
cdk-lambda-dynamodb-fargate: creating CloudFormation changeset...
  0/3 | 11:12:25 AM | CREATE_IN_PROGRESS   | AWS::DynamoDB::Table |
  Table (TableCD117FA1)
  0/3 | 11:12:25 AM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata  |
  CDKMetadata
  0/3 | 11:12:25 AM | CREATE_IN_PROGRESS   | AWS::DynamoDB::Table |
  Table (TableCD117FA1) Resource creation Initiated
  0/3 | 11:12:27 AM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata  |
  CDKMetadata Resource creation Initiated
  1/3 | 11:12:27 AM | CREATE_COMPLETE     | AWS::CDK::Metadata  |
  CDKMetadata
  2/3 | 11:12:56 AM | CREATE_COMPLETE     | AWS::DynamoDB::Table |
  Table (TableCD117FA1)
  3/3 | 11:12:57 AM | CREATE_COMPLETE     | AWS::CloudFormation::Stack |
  cdk-lambda-dynamodb-fargate

Stack ARN:
arn:aws:cloudformation:us-east-2:200562098309:stack/
cdk-lambda-dynamodb/3236a8b0-cdad-11e9-934b-0a7dfa8cb208