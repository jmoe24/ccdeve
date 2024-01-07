# Use official NGINIX image
FROM nginx:latest

# Set an environment variable with default value 'Josh'
ENV NAME Josh

# Create a directory within the container
WORKDIR /usr/share/nginx/html

# Remove the default NGINX static content
# Not necessary but reduces disk size for testing
RUN rm -rf ./*
# Note: If I didn't set the working directory above, I would perform this action
# with the following RUN command
#RUN rm -rf /usr/share/nginx/html/*

# Copy the custom index.html to NGINX default HTML directory
COPY index.html /usr/share/nginx/html/index.html

# Copy the entrypoint script into the container
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Note: Hhaven't been able to get logs sent to a mapped volume
# Check if the log directory exists before attempting to create it
#RUN [ -d /var/log/nginx ] || mkdir -p /var/log/nginx

# Create a symbolic link to the log directory
#RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log

# Expose port 80 for NGINX
EXPOSE 80

# Create a volume for logs (logs will be stored on the host machine)
#VOLUME ["/var/log/nginx"]

# Set the entrypoint to execute the shell script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Start NGINX in the foreground when the container starts
# Note: I don't need to use this command since I put the commands in the entrypoint file
#CMD ["nginx", "-g", "daemon off;"]
