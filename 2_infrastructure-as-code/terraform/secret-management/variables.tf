# user variable

# exploring using hashicorp vault to store these creds
variable "vault" {
  description = "HC Vault"
  address = var.vault_url
  token = var.vault_token
}

variable "user" {
  description = "Login information"
  type        = map
  default     = {
    username = "admin"
    password = "1234QWer!"
    url      = "https://192.168.86.240"
  }
}



