import json
class Actions:
    @staticmethod
    def load(file_obj):
        return json.load(file_obj)
    @staticmethod
    def loads(file_obj):
        return json.loads(file_obj)
actions = {
    'load': Actions.load,
    'loads': Actions.loads,
}