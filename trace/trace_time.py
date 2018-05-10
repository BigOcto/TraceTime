#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import print_function
import sys
import optparse
from command_dispatcher import CommandDispatcher


class TraceTime:
    def __init__(self):
        self.dispatcher = CommandDispatcher()

    def run(self, options, args):
        self.dispatcher.get_command(options, args)


def get_parser():
    usage = 'Usage: %prog [options] [category1 [category2 ...]]'
    desc = 'Example: %prog -t 15 '
    parser = optparse.OptionParser(usage=usage, description=desc)

    parser.add_option('-t', '--time',
                      dest='trace_times',
                      type='int',
                      help='trace for N seconds',
                      default=1)
    parser.add_option('-p', '--version_pre',
                      dest='trace_version_pre',
                      help='excel first row name prefix',
                      default='0.0')
    parser.add_option('-d', '--device',
                      dest='device_name',
                      help='adb device name',
                      default='')
    parser.add_option('-m', '--mode',
                      dest='trace_mode',
                      help='trace time or trace video',
                      default='launch_time')

    # parser.add_argument('-f', '--cleanBuild', action='store_true', help='force to execute a clean build')
    # parser.add_argument('-w', '--wait', action='store_true', help='make application wait for debugger')
    # parser.add_argument('-a', '--all', action='store_true',
    #                     help="together with '-f', freeline will force to clean build all projects.")
    # parser.add_argument('-c', '--clean', action='store_true', help='clean cache directory and workspace')
    # parser.add_argument('-d', '--debug', action='store_true', help='show freeline debug output (NOT DEBUG APPLICATION)')
    # parser.add_argument('-i', '--init', action='store_true', help='init freeline project')
    # parser.parse_args()
    return parser


def main():
    if sys.version_info > (3, 0):
        print(sys.version_info)
        print('TraceTime only support Python 2.7 now. Please use the correct version of Python for TraceTime.')
        exit()
    # 命令解析
    parser = get_parser()
    options, args = parser.parse_args()
    trace_time = TraceTime()
    trace_time.run(options=options, args=args)


if __name__ == '__main__':
    main()
