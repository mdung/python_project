import ast
from jinja2 import Environment, FileSystemLoader

class DocumentationGenerator:
    def __init__(self, source_code_file, output_file):
        self.source_code_file = source_code_file
        self.output_file = output_file
        self.comments = []

    def parse_code(self):
        with open(self.source_code_file, 'r') as file:
            tree = ast.parse(file.read(), filename=self.source_code_file)

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):
                if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str):
                    docstring = node.body[0].value.s.strip()
                    self.comments.append({'name': node.name, 'docstring': docstring})

    def generate_documentation(self):
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('documentation_template.jinja2')

        with open(self.output_file, 'w') as file:
            file.write(template.render(comments=self.comments))

if __name__ == "__main__":
    source_file = "your_code.py"
    output_file = "documentation_output.md"

    generator = DocumentationGenerator(source_file, output_file)
    generator.parse_code()
    generator.generate_documentation()
