# This installs flask using pip3

exec { 'flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
