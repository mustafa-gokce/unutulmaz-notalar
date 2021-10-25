import pathlib
import boto3

session = boto3.session.Session()
client = session.client("s3",
                        region_name="fra1",
                        endpoint_url="https://fra1.digitaloceanspaces.com",
                        aws_access_key_id="",
                        aws_secret_access_key="")

folder = "/home/m/pdfs/"
contents = list(pathlib.Path(folder).iterdir())

for i, content in enumerate(contents):
    full_path = str(content.absolute())
    stem = content.stem
    suffix = content.suffix

    results = client.list_objects(Bucket="uncdn", Prefix=stem + suffix)
    uploaded = "Contents" in results

    if not uploaded:
        client.upload_file(full_path, "uncdn", stem + suffix)
        print("Uploaded:", full_path)
    else:
        print("Already uploaded:", full_path)
