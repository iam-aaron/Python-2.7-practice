import argparse
import time

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
    parser.add_argument('--driver', 
        '-d', 
        help='How and where to store back up', 
        nargs=2, 
        metavar=("DRIVER", "DESTINATION"), 
        action=DriverAction, 
        required=True
    ) 
    return parser

def main():
    import boto3
    from pgbackup import storage, pgdump

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print("Backing database to %s in S3 as %s" % (args.destination, file_name))
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        outfile = open(args.destination, 'w')
        print("Backing database up locally to %s" % outfile.name )
        storage.local(dump.stdout, outfile)
