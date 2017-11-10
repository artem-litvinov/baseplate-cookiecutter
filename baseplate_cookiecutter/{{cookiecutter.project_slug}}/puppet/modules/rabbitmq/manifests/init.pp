class rabbitmq {
  file { '/etc/apt/sources.list.d/rabbitmq.sources.list':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => 'deb http://www.rabbitmq.com/debian/ testing main',
  }

  file { '/tmp/rabbitmq_repo_key':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
    source => 'puppet:///modules/rabbitmq/repo_key',
  }

  exec { 'add rabbitmq repo key':
    command => 'apt-key add /tmp/rabbitmq_repo_key',
    unless  => 'apt-key list | grep 6026DFCA',
    before  => Exec['update apt cache'],
    notify  => Exec['update apt cache'],
    require => [
      File['/etc/apt/sources.list.d/rabbitmq.sources.list'],
      File['/tmp/rabbitmq_repo_key'],
    ],
  }

  package { 'rabbitmq-server':
    ensure  => installed,
  }

  service { 'rabbitmq':
    ensure  => running,
    require => Package['rabbitmq-server'],
  }
}
