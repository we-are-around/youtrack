docker::run { 'around-youtrack':
  image        => 'zoer/youtrack',
  ports        => ['80:80'],
  hostname     => 'around-youtrack',
  name	       => 'around-youtrack',
}
