# Copyright 2023 Google LLC
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# __main__.py
"""A placeholder for a malloy module main entry point."""

import sys

from malloy.utils.third_party_licenses import output_third_party_licenses

def main():
  """Malloy Python Runtime Library"""
  if len(sys.argv) == 1:
    print("Hello Python")
    return

  for arg in sys.argv:
    if arg == 'help' or arg == '-h' or arg == '--help':
      print("""
Usage: python -m malloy [options] [command]
            
Options:
  -h, --help        display this help message
            
Commands:
  third-party       output third party license information
  help [command]    display help for command
            """)
      return

    if arg == 'third_party' or arg == 'third-party':
      output_third_party_licenses()
      return

if __name__ == "__main__":
  main()
