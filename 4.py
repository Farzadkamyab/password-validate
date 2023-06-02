def create_argument_dictionary(*args):
    arg_dict = {}
    for i, arg in enumerate(args):
        arg_name = f"arg{i+1}"
        arg_dict[arg_name] = arg
    return arg_dict

res1 = create_argument_dictionary(1,2,3,4,5)
res2 = create_argument_dictionary("farzad", "nima", "amir")
print(res1)
print(res2)