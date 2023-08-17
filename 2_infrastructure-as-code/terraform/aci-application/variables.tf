# user variable
variable "user" {
  description = "Login information"
  type        = map
  default     = {
    username = "admin"
    password = "1234QWer!"
    url      = "https://192.168.86.240"
  }
}

variable "tenant" {
    type    = string
    default = "terraform_tenant"
}

variable "vrf" {
    type    = string
    default = "prod_vrf"
}

variable "bd" {
    type    = string
    default = "prod_bd"
}

variable "subnet" {
    type    = string
    default = "10.10.101.1/24"
}