provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "bad_bucket" {
  bucket = "my-iac-insecure-bucket-123456"
  acl    = "public-read"  # ❌ This will trigger Checkov
}
