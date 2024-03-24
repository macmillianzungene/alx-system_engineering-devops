#!/usr/bin/env bash
# This Puppet manifest configures the client SSH for password-less authentication

file { '/home/ubuntu/.ssh/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

file { '/home/ubuntu/.ssh/config':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

file_line { 'Declare identity file':
  path => '/home/ubuntu/.ssh/config',
  line => 'IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwd auth':
  path => '/home/ubuntu/.ssh/config',
  line => 'PasswordAuthentication no',
}

