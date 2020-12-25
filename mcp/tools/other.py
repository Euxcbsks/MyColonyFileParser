__all__ = ["fill_dic"]


def fill_dic(from_dic, to_dic, *, except_key=None):
    if len(from_dic) != len(to_dic):  # Check if the two lengths are the same

        def in_dic(k, from_dic, to_dic):
            if k not in to_dic:
                to_dic[k] = from_dic[k]

        if except_key is not None:
            for k in from_dic:
                if k not in except_key:
                    in_dic(k, from_dic, to_dic)
        else:
            for k in from_dic:
                in_dic(k, from_dic, to_dic)

    return to_dic
