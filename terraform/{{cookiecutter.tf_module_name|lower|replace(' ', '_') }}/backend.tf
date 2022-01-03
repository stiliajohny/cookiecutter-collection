terraform {
  required_providers {
      aws = {
          source = "hashicorp/aws"
          version = "{{cookiecutter.aws_provider_version}}"
      }
  }

  backend "s3" {
    acl              = "private"
    encrypt          = true
  }
}
