#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to parse Mac OS com.apple.loginitems.plist Alias value."""

import argparse
import logging
import sys

from dtformats import alias_data
from dtformats import output_writers


def Main():
  """The main program function.

  Returns:
    bool: True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      'Extracts information from Mac OS com.apple.loginitems.plist Alias '
      'values.'))

  argument_parser.add_argument(
      '-d', '--debug', dest='debug', action='store_true', default=False,
      help='enable debug output.')

  argument_parser.add_argument(
      'source', nargs='?', action='store', metavar='PATH', default=None, help=(
          'path of the Mac OS com.apple.loginitems.plist Alias or AliasData '
          'value data.'))

  options = argument_parser.parse_args()

  if not options.source:
    print('Source file missing.')
    print('')
    argument_parser.print_help()
    print('')
    return False

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  output_writer = output_writers.StdoutWriter()

  try:
    output_writer.Open()
  except IOError as exception:
    print(f'Unable to open output writer with error: {exception!s}')
    print('')
    return False

  alias = alias_data.MacOSLoginItemAliasData(
      debug=options.debug, output_writer=output_writer)
  alias.Open(options.source)

  output_writer.WriteText(
      'Mac OS com.apple.loginitems.plist Alias information:\n')

  # TODO: print more information.

  output_writer.WriteText('\n')

  alias.Close()

  output_writer.Close()

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)