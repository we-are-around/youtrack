docker::run { 'around-youtrack':
  image        => 'wearearound/youtrack',
  ports        => ['80:80'],
  hostname     => 'around-youtrack',
  name	       => 'around-youtrack',
}
