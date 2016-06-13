docker::run { 'around-youtrack':
  image        => 'wearearound/youtrack:backup-1',
  ports        => ['80:80'],
  hostname     => 'around-youtrack',
  name	       => 'around-youtrack',
}
