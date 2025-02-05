terraform {
  required_providers {
    time = {
      source  = "hashicorp/time"
      version = "0.12.1"  # Make sure to use the version that match latest version
    }
  }
}

provider "aws" {
  region = var.region
}
