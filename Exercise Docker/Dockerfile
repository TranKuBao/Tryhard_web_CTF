FROM ubuntu:22.04

# Define environment variables using key=value format
ENV user=chall
ENV chall_port=2222

# Update and install required packages
RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

# Add user and set up necessary files
RUN adduser --disabled-password --gecos "" $user

# Add flag and executable file to the home directory
ADD ./deploy/flag /home/$user/flag
ADD ./deploy/$user /home/$user/$user

# Adjust ownership and permissions
RUN chown -R root:$user /home/$user && \
    chmod 755 /home/$user/$user && \
    chmod 440 /home/$user/flag

# Set working directory, user, and expose port
WORKDIR /home/$user
USER $user
EXPOSE $chall_port

# Use JSON format for CMD to improve signal handling
CMD ["socat", "-T", "30", "TCP-LISTEN:2222,reuseaddr,fork", "EXEC:/home/chall/chall"]
