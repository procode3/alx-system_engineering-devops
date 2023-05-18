# Updating configs for NGINX to allow more traffic

exec { 'ngix-conf':
  command => 'sed -i "s/15/5012/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Nginx Restart
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
