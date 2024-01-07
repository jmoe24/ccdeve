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