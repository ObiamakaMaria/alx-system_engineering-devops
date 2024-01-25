# Ran the puppet command using 
# sudo puppet apply --modulepath=/home/ubuntu/.puppet/etc/code/modules:/usr/
# share/puppet/modules then filename which is  0-the_sky_is_the_limit_not.pp
# This Puppet code addresses potential issues with the Nginx server
# by setting a higher limit for file descriptors.

exec { 'Change ULIMIT':
  command  => 'echo "ULIMIT=\"-n 25000\"" > /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}
