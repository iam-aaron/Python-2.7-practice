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
	$ pgbackup --driver s3 pytest-db-backup postgres://demo-user:password@44.207.7.28:80/sample

Local Example w/ local path:
	
::
	$ pgbackup --driver local ./local-dump.sql postgres://demo-user:password@44.207.7.28:80/sample

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::
	$ make

If virtualenv is not active then use:

::
	$ pipenv run make
