

import input_to_dic
import leftovers_to_dic
import conditions_to_reuse

default_file_path = "C:/Users/User/Desktop/Python project/references/"

cu_filename = "castunit.txt"
leftovers_filename = "leftovers.csv"

rebar_in_model = input_to_dic.cu_rebar_dic(default_file_path + cu_filename)
rebar_leftovers = leftovers_to_dic.leftovers_dic(default_file_path + leftovers_filename)

rebars = conditions_to_reuse.rebars_to_use(rebar_in_model, rebar_leftovers)

print(rebars)

print("Reinforcement bars currently in leftovers stock, that can be used for selected element:")
for rebar_no, param in rebars.items():
    print("rebar no:", rebar_no, "length:", param[2])

