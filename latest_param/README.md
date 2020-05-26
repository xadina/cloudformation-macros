# LatestParam CloudFormation Macro

The `LatestParam` macro provides a function-scoped `LatestParam` property for CloudFormation resources. It allows you to resolve the latest version of the requested SSM parameter. This macro will decrypt encrypted parameters.

## How to install and use the LatestParam macro

### Deploying

1. Package the Macro CloudFormation template. The provided template uses [the AWS Serverless Application Model](https://aws.amazon.com/about-aws/whats-new/2016/11/introducing-the-aws-serverless-application-model/) so it must be transformed before you can deploy it.

    ```shell
    aws cloudformation package --template-file latest_param.yml --output-template-file latest_param_compiled.yml --s3-bucket dev.stacks  
    ```

2. Deploy the packaged CloudFormation template to a CloudFormation stack:

    ```shell
    aws cloudformation deploy --stack-name LatestParamMacro --template-file latest_param_compiled.yml --capabilities CAPABILITY_IAM
    ```

3. To test out the macro's capabilities, have a look at the provided example template: `example.yml`
