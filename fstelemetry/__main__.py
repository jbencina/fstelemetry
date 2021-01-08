from .telemetry import Telemetry
from datetime import datetime
import argparse
import yaml

def get_keys(path):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    keys = data['keys']
    print(f'Logging {len(keys)} keys from Flight Simulator: '
                 '','.join(keys)')
    return keys

def main():
    logname = datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'
    parser = argparse.ArgumentParser()

    parser.add_argument('--config', default='config.yaml',
                        help='Relative path to the config file')
    parser.add_argument('--log', default=logname,
                        help='Relative path for the output log file')
    parser.add_argument('--interval', default=1.0,
                        help='Polling interval in seconds')

    args = parser.parse_args()


    keys = get_keys(args.config)

    t = Telemetry(keys=keys)
    t.listen(path=args.log, interval=args.interval)

if __name__ == '__main__':
    main()