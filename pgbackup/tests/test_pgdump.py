import pytest
import subprocess

from pgbackup import pgdump

url = "postgres://demo-user:password@44.207.7.28:80/db_one"

def test_dump_call_pg_dump(mocker): #fixture from mock package
    """
    Utilize pg_dump to interact with Database.
    """
    proc = mocker.Mock()
    mocker.patch('subprocess.Popen', return_value=proc)
    assert pgdump.dump(url) == proc
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed.
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)

def test_dump_file_name_without_timestamp():
    """
    pgdump._dump_file_name returns the name of the database
    """
    assert pgdump.dump_file_name(url) == "db_one.sql"

def test_dump_file_name_with_timestamp():
    """
    pgdump._dump_file_name returns the name of the database with timestamp appended to it.
    """
    timestamp = "2022-11-15T11:11"
    assert pgdump.dump_file_name(url, timestamp) == "db_one-2022-11-15T11:11.sql"
