from neet_code.classes.linked_list_node import list_to_linkedlist


def print_results(examples: list[dict], function: any, complexity: str):
    print("\nSolution")
    for example in examples:
        inputs, outputs = example["input"], example["output"]
        print(f"|  examples = {str(inputs)}  |  expected_results = {outputs}  |  result = {function(**inputs)}  |")
    print(complexity)


def print_linkedlist_results(examples: list[dict], function: any, complexity: str):
    print("\nSolution")
    for example in examples:
        inputs = {k: list_to_linkedlist(v) if isinstance(v, list) else v for k, v in example["input"].items()}
        outputs = example["output"]

        print(f"|  examples = {str(inputs)}  |  expected_results = {outputs}  "
              f"|  result = {function(**inputs)}  |")
    print(complexity)


