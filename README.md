## Integrating Amazon API Gateway private endpoints with on-premises networks

Read the blog about this application:
[Integrating Amazon API Gateway private endpoints with on-premises networks](https://aws.amazon.com/blogs/compute/integrating-amazon-api-gateway-private-endpoints-with-on-premises-networks/)


### Requirements for deployment

* <a href="https://aws.amazon.com/cli/" target="_blank">AWS CLI</a>
* <a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html" target="_blank">AWS SAM CLI</a>
* AWS credentials that provide the necessary permissions to create the resources. This example uses admin credentials.
* Amazon VPN or AWS Direct Connect with routing rules that allow DNS traffic to pass through to the Amazon VPC.


### Deploying

In the terminal, use the SAM CLI guided deployment the first time you deploy

1. Navigate to the cloned repo directory. Alternatively, use the sam init command and paste the repo URL.
 
3.	Build the AWS SAM application:
```bash
sam build
```
4.	Deploy the AWS SAM application:
```bash
sam deploy –guided
```

## Cleanup
1. Open the <a href="https://console.aws.amazon.com/cloudformation/home" target="_blank">CloudFormation console</a>
1. Locate the stack using the name entered in SAM deployment.
1. Select the radio option next to it
1. Select **Delete**
1. Select **Delete stack** to confirm

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

