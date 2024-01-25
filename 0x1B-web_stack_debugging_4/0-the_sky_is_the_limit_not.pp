# Ran the puppet command using 
# sudo puppet apply --modulepath=/home/ubuntu/.puppet/etc/code/modules:/usr/
# share/puppet/modules then filename which is  0-the_sky_is_the_limit_not.pp
# This Puppet code addresses potential issues with the Nginx server
# by setting a higher limit on the number of file descriptors Nginx can use.

# Include the stdlib module for useful functions and definitions
include ::stdlib

# Manage the 'LIMIT' parameter in the '/etc/default/nginx' file
file_line { 'allow many requests':
  ensure  => present,                # Ensure the line is present in the file
  path    => '/etc/default/nginx',   # Path to the target file
  line    => 'LIMIT="-n 4096"',      # The line to be added or replaced
  replace => true                    # Replace the line if it already exists
}

# Execute a command to restart the Nginx service
exec { 'restart nginx':
  command  => '/usr/sbin/service nginx restart',  # Command to restart Nginx
  provider => shell                              # Use a shell to execute the command
}
