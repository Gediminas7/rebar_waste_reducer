# method which takes two dictionaries of rebars in model and rebars of leftovers. It returns dictionarie of elements that could be used form the leftovers

def rebars_to_use(model_rebar, leftover_rebar):
    rebars_to_use = dict()
    for params in model_rebar.values():
        for no, par in leftover_rebar.items():
            if params[4] == par[2]:
                rebars_to_use[no] = par

    return rebars_to_use