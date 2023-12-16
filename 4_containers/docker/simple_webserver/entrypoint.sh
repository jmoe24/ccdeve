#!/bin/bash
# Replace placeholder with the value of the environment variable in the HTML file
sed -i "s/{{NAME}}/$NAME/g" /usr/share/nginx/html/index.html

# Start NGINX in the foreground
nginx -g "daemon off;"
