# ParamVersion CloudFormation Macro

The `ParamVersion` macro provides a function-scoped `ParamVersion` property for CloudFormation resources. It allows you to extract a Tag specified in a stack so that it can be reused elsewhere.

## How to install and use the ParamVersion macro

### Deploying

1. Package the Macro CloudFormation template. The provided template uses [the AWS Serverless Application Model](https://aws.amazon.com/about-aws/whats-new/2016/11/introducing-the-aws-serverless-application-model/) so must be transformed before you can deploy it.

    ```shell
    aws cloudformation package --template-file param_version.yml --output-template-file param_version_compiled.yml --s3-bucket shareddev.stacks  
    ```

2. Deploy the packaged CloudFormation template to a CloudFormation stack:

    ```shell
    aws cloudformation deploy --stack-name ParamVersionMacro --template-file param_version_compiled.yml --tags mission=cloud --capabilities CAPABILITY_IAM
    ```

3. To test out the macro's capabilities, have a look at the provided example template: `example.yml`
