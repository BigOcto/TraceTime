from json_file_editor import update_json_file
from command_dispatcher import run_command_adb_push_file
from command_dispatcher import read_excel


def main():
    # update_json_file('')
    # update_json_file('Card')
    # run_command_adb_push_file('/Users/zhangyu/PycharmProjects/TraceTime/TaskTest.json', '/sdcard/TaskTest.json')
    read_excel("/Users/zhangyu/PycharmProjects/TraceTime/qiyi_launch_task_time.xlsx", "1517")

if __name__ == '__main__':
    main()
