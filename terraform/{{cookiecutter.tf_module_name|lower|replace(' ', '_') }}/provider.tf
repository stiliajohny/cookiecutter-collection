provider "aws" {
  version = "~> 1.0"
  region  = "{{cookiecutter.aws_provider_region|lower}}"
}