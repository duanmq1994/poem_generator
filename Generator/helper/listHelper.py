def add(source_list, *args):
    try:
        if len(args) > 1:
            source_list.extend(args)
        else:
            source_list.append(args[0])
        return source_list
    except Exception as err:
        return err

def addFromDict(source_list, source_dict, *keys):
    try:
        for key in keys:
            source_list.append(source_dict[key])
        return source_list
    except Exception as err:
        return err