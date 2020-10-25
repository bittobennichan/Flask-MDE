Flask-MDE Changelog
=========================

FLask-MDE follows `Semantic Versioning 2.0.0 <https://semver.org/>`_

1.2.1
-----

* Replaced `HTMLString` with `markupsafe.Markup` for `MdeField`. `Github Issue # 7 - Button Bar Not Displaying <https://github.com/jmcmanus/pagedown-extra>`_.


1.2.0
-----

* Added support for `pagedown-extra <https://github.com/jmcmanus/pagedown-extra>`_.

1.1.2
-----

* Fixed `application factory usage issue. <https://github.com/bittobennichan/Flask-MDE/issues/2>`_

1.1.1
-----

* ``make-pretty`` was not pretty printing ``<pre>`` tags. Fixed.

1.1.0
-----

* ``make-pretty`` css class added to make the output HTML pretty.

1.0.0
-----

* This is the Public API.