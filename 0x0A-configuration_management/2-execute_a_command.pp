# Using Puppet to kill a process

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
