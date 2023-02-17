terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.21.0"
    }
  }
}

provider "azurerm" {
  # Configuration options
    features {}

  subscription_id = "810cf854-b0a9-4ad1-a9ce-438024596053"
  client_id       = "7b54bd92-4561-45be-ab10-c0510ab0917b"
  client_secret   = "Nmr8Q~J9UiffjbdLKiFPh34QJ8vCXLY6q-kVqad2"
  tenant_id       = "c2e6ffd9-4eef-4fe6-af0b-a9a0846fb515"
}