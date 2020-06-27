

def cu_rebar_dic(cu_text):
    rebar_start = rebar_finder(cu_text)[0]
    rebar_end = rebar_finder(cu_text)[1]
    cu_dic = text_to_dic(cu_text, rebar_start, rebar_end)
    return cu_dic


def rebar_finder(cu_text):
    with open(cu_text) as text:
        linecounter = 0
        for line in text:
            words = line.split()
            if words != []:
                linecounter += 1
                if words[0] == "Numbered":
                    rebarstart = linecounter + 1
                if "=" in words[0]:
                    rebarend = linecounter
    return (rebarstart, rebarend)


def text_to_dic(cu_text, rebar_start, rebar_end):
    with open(cu_text) as text:
        cu_rebar = dict()
        linecounter = 0
        for line in text:
            words = line.split()
            if words != []:
                linecounter += 1
                if linecounter >= rebar_start and linecounter < rebar_end:
                    cu_rebar[words[0]] = (
                        words[1], words[2], words[3], words[4], words[5])
    return(cu_rebar)


#print(cu_rebar_dic("castunit.txt"))