import boto3

client = boto3.client("ssm")


def extract_value(params):
    status = "success"
    key = params["ssm_parameter"]
    try:
        details = client.get_parameter(Name=key, WithDecryption=True)
        try:
            value = details["Parameter"]["Value"]
        except:
            print("Unable to extract value for parameter " + key)
            status = "failure"
            value = "NotAvailable"
    except:
        print("parameter " + key + " not found")
        status = "failure"
        value = "NotFound"
    return status, value


def handler(event, context):
    result = extract_value(event["params"])
    return {
        "requestId": event["requestId"],
        "status": result[0],
        "fragment": result[1],
    }
