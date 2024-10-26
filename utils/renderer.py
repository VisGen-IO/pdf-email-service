from jinja2 import Environment, FileSystemLoader

def render_template(template_name, data):
    """
    Renders an HTML template with the given data.
    """
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    return template.render(data)
