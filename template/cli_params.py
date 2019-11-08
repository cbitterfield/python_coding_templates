"""CLI Get parameters"""
import argparse, os
__prog_name__ = ''
__version__ = ''
DEBUG = None
VERBOSE = None
DRYRUN = None
LOGLEVELS = None
LOGLEVEL = None
DEFAULT_LOGFILE = os.path.splitext(__prog_name__)[0] + '.log'
LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
TEXT_SEPERATOR = '\t'
OUTPUT_FILENAME = ''
LOG_PARAMS = False
AWS_PARAMS = False
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_SESSION_TOKEN = ''
AWS_DEFAULT_REGION = 'us-east-1'
AWS_REGION = ''
AWS_PROFILE = ''
AWS_REGIONS = [
 'us-east-2',
 'us-east-1',
 'us-west-1',
 'us-west-2']
AWS_REGION_CHOICES = AWS_REGIONS + ['all']

def cli_params(cli_args, **kwargs):
    """
    Get preset command line arguments
    """
    description = 'Example Program Description'
    epilog = 'Example Program Epilog'
    print(kwargs)
    try:
        description = kwargs['description'] if kwargs['description'] else 'Example Program Description'
        epilog = kwargs['epilog'] if kwargs['epilog'] else 'Example Program Epilog'
        if 'DEBUG' in kwargs.keys():
            DEBUG = kwargs['DEBUG']
    except:
        pass

    if DEBUG:
        print('CLI Params {0}'.format(cli_args))
    parser = argparse.ArgumentParser(None)
    parser.prog = __prog_name__
    parser.description = description
    parser.epilog = epilog
    parser.add_argument('--version', action='version', version=('%(prog)s ' + __version__))
    parser.add_argument('-d', '--debug', help='Turn on debugging',
      action='store_true',
      required=False,
      dest='debug',
      default=False)
    parser.add_argument('-v', '--verbose', help='Turn on verbose output',
      action='store_true',
      required=False,
      dest='verbose',
      default=False)
    parser.add_argument('-dr', '--dryrun', help='Turn on verbose output',
      action='store_true',
      required=False,
      dest='dryrun',
      default=False)
    parser.add_argument('-of', '--output-file', type=str, help='Filename for output defaults to csv format',
      action='store',
      required=False,
      dest='output_filename',
      default='output')
    parser.add_argument('-f', '--output-format', type=str, help='Format for output { txt, csv, xls ,con} con is console / std out only',
      action='store',
      required=False,
      dest='format',
      default='con')
    if LOG_PARAMS:
        parser.add_argument('-l', '--loglevel', help=('Set the loglevel ' + str(LOG_LEVELS) + '-- Choices are limited to these values. Use CRITICAL to supress most messages'),
          type=str,
          action='store',
          choices=LOG_LEVELS,
          required=False,
          dest='loglevel',
          default=LOGLEVEL)
        parser.add_argument('-lt', '--log-to', help='Send logging to console, file or syslog',
          type=str,
          action='store',
          choices=[
         'console', 'filename', 'syslog'],
          required=False,
          dest='loglocation',
          default='console')
        parser.add_argument('-lf', '--log-file', help='Filename for logging defaults to program_name.log',
          type=str,
          action='store',
          required=False,
          dest='logfile',
          default='YES')
    if AWS_PARAMS:
        parser.add_argument('-p', '--profile', type=str, help='AWS Profile to use',
          action='store',
          required=False,
          dest='aws_profile',
          default=None)
        parser.add_argument('-r', '--region', type=str, help='AWS region to use',
          action='store',
          required=False,
          choices=AWS_REGION_CHOICES,
          dest='aws_region',
          default='us-east-1')
        parser.add_argument('-key', '--access-key', type=str, help='AWS access key',
          action='store',
          required=False,
          dest='aws_access_key',
          default=None)
        parser.add_argument('-secret', '--secret-access-key', type=str, help='AWS access key',
          action='store',
          required=False,
          dest='secret_access_key',
          default=None)
        parser.add_argument('-token', '--aws-session-token', type=str, help='AWS access session token',
          action='store',
          required=False,
          dest='aws_token',
          default=None)
    parse_out = parser.parse_args(cli_args)
    if DEBUG:
        print('Parser variables {}'.format(parse_out))
    return parse_out


def dummy():
    """
    put extra parser arguements not needed here
    """
    pass