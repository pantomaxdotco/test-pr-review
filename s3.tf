resource "aws_s3_bucket_policy" "s3_policy" {
  bucket = "${my_s3_bucket.mybucket.id}"
  policy = jsonencode({
    Id      = "s3_policy"
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        AWS = "*"
      }
      Action = [
        "s3:PutObject"
      ]
      Resource = "${my_s3_bucket.mybucket.arn}/*"
      }
    ]
  })
}
