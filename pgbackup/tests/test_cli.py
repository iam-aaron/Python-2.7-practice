import pytest
from pgbackup import cli

url = "postgres://demo-user:password@3.86.162.195:80/sample"

@pytest.fixture()
def parser(): #fixture
    return cli.create_parser()

def test_parser_without_driver(parser): #inject the fixture
    """
    Without specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args(url)

def test_parser_with_driver(parser): #inject the fixture
    """
    The parser will exit if it receives a driver without a destination.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'local'])

def test_parser_with_driver_and_destination(parser): #inject the fixture
    """
    The parser will not exit if it receives a driver and a destination
    """
    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.driver == 'local'
    assert args.destination == '/some/path'

def test_parser_with_unknown_driver(parser): #inject the fixture
    """
    The parser will exit if the driver name is unknown.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])

def test_parser_with_known_drivers(parser): #inject the fixture
    """
    The parser will not exit if the driver name is known.
    """
    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])