import json

task_configure_info = {
    'ReactTask': "ReactTask",
    'PingbackTask': "PingbackTask",
    'Qimo': "Qimo",
    'RN': "RN",
    'Pay': "Pay",
    'mPlayerTask': "mPlayerTask",
    'PaoPao': "PaoPao",
    'PingbackManagerWrapper': "PingbackManagerWrapper",
    'CrashReporter': "CrashReporter"
}

TEST_JSON_FILE_PATH = '/Users/zhangyu/PycharmProjects/TraceTime/TaskTest.json'


def update_json_file(task_name):
    with open(TEST_JSON_FILE_PATH, 'r') as jsonFile:
        data = json.load(jsonFile)
    old_list = data['list_task']
    old_task_name = old_list[0]['name']
    print("Old task name : " + old_task_name)
    if task_name == "":
        print("Update new name : " + "null")
        old_list[0]['name'] = "null"
    else:
        print("Update new name : " + task_configure_info.get(task_name))
        old_list[0]['name'] = task_configure_info.get(task_name)

    with open(TEST_JSON_FILE_PATH, 'w+') as jsonFile:
        jsonFile.write(json.dumps(data))
        jsonFile.close()
