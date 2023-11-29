# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create a basic HTML file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => present,
  content => '<html><head><title>Hello World Page</title></head><body><p>Hello World!</p></body></html>',
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {\n  listen 80;\n  server_name localhost;\n\n  location / {\n    root /var/www/html;\n    index index.html;\n  }\n\n  location /redirect_me {\n    return 301 http://newdomain.com;\n  }\n}\n",
}

# Create a symbolic link to enable the Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
