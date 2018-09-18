from json_file_editor import update_json_file
from command_dispatcher import run_command_adb_push_file


def main():
    update_json_file('')
    update_json_file('Card')
    run_command_adb_push_file('/Users/zhangyu/PycharmProjects/TraceTime/TaskTest.json', '/sdcard/TaskTest.json')

if __name__ == '__main__':
    main()
