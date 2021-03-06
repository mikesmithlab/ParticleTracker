
def get_param_val(param):
    '''
    Simple function to determine if parameter is a list or something else
    Lists are 4 long and indicate an a parameter adjusted by the slider in TrackGui

    :param param: parameter to be tested
    :return: value from position zero of list or returns the parameter as is if not a list
    '''
    type_param = type(param)
    if type_param == type([]):
        return param[0]
    else:
        return param

def get_method_name(method):
    if '*' in method:
        method_name, call_num = method.split('*')
    else:
        method_name = method
        call_num = None
    return method_name, call_num

def get_method_key(method, call_num=None):
    if call_num is None:
        method_key = method
    else:
        method_key = method + '*' + call_num
    return method_key

