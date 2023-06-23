import os

# Print the value of an environment variable
def print_variable_value(variable_name):
    value = os.getenv(variable_name)
    print(f"{variable_name}: {value}")

# List of environment variables to print
variables_to_print = [
    "BUILD_NUMBER",
    "BUILD_SOURCEVERSION",
    "BUILD_SOURCEBRANCH",
    "BUILD_REPOSITORY_NAME",
    "BUILD_DEFINITIONNAME"
]

# Print the values of the environment variables
for variable in variables_to_print:
    print_variable_value(variable)
