from CCparse import parser
from semantics import analyze

def compile(source_code):
    # Step 1: Parse the source code into an AST
    ast = parser.parse(source_code)
    print("Parsing completed successfully.")

    # Step 2: Perform semantic analysis
    semantic_analyzer = analyze(ast)
    if semantic_analyzer.get_errors():
        for error in semantic_analyzer.get_errors():
            print(error)
        return None
    print("Semantic analysis completed successfully.")

    # If interpreting, execute the semantically valid AST directly
    # execution_result = execute(semantic_analyzer)

    # return execution_result  # Uncomment if you are executing the AST

if __name__ == "__main__":
    # Get source code from a file
    file_path = "/Users/user/PycharmProjects/APL/venv/source_code.cc"
    try:
        with open(file_path, 'r') as source_file:
            source_code = source_file.read()
    except FileNotFoundError:
        print(f"Source file not found: {file_path}")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    else:
        # The result could be the execution result if interpreting
        result = compile(source_code)
        if result is not None:
            print("Compilation and semantic analysis successful.")
            # Process the result if needed, e.g., by printing the output of the execution
            #print(result)
