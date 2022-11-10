pgbackup
========

CLI for backing up remote PostgrSQL databases locally or to AWS S3

Preparing for Development
-------------------------

1. Ensure ``pip``, and ``pipend`` are installed.
2. Clone the repository: ``<put repository here>``
3. Fetch development dependencies: ``make install``

Usage
-----

Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

::
	$ pgbackup postgres://user@example-domain.com:5432/db_one --driver s3 backups

Local Example w/ local path:
	
::
	$ pgbackup postgres://user@example-domain.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::
	$ make

If virtualenv is not active then use:

::
	$ pipenv run make
