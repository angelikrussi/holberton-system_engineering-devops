# instale puppet-lint.

package { 'puppet-lint':
    ensure   => '2.5.0',
    provider => 'gem',
    soure    =>
    source   => 'https://rubygems.org',
}
