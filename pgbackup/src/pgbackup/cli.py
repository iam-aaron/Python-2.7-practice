import argparse

known_drivers = ['local', 's3']

class DriverAction(argparse.Action): #inheritance
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 'local' and 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination
        

def create_parser():
    parser = argparse.ArgumentParser(description="""
    Back up PostgreSQL databases locally or to AWS S3.
    """)
    parser.add_argument('url', help='URL of database to backup')
    parser.add_argument('--driver', help='How and where to store back up', nargs=2, metavar=("DRIVER", "DESTINATION"), action=DriverAction, required=True) 
    return parser

