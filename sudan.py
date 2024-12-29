import re

def remove_whitespaces_and_comments(code):
    # Remove single-line comments
    code = re.sub(r'//.*', '', code)
    # Remove multi-line comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # Remove all whitespaces (space, tab, newline)
    code = re.sub(r'\s+', '', code)
    return code

# Input code as a string
code = """
int main(){
//this is comment
int a=10;/* this is a 
multiline comment*/
return 0;
}
"""

# code = input("send the damn code: ")

# print("Enter your code (press Enter twice to finish):")
# lines = []
# while True:
#     line = input()
#     if line == "":  # Stop on empty line
#         break
#     lines.append(line)

# # Join the lines to create a single string
# code = "\n".join(lines)

# print("\nInput Code:")
# print(code)



# Clean the code
cleaned_code = remove_whitespaces_and_comments(code)

print("Original Code:\n", code)
print("\nCleaned Code:\n", cleaned_code)
