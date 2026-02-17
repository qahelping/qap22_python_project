import html
import re

import allure

"""CSS styles and formatters for Allure HTML attachments."""

COMMON_FIXTURE_CSS = """
<style>
    .common-container {
        font-family: 'Courier New', monospace;
        font-size: 13px;
        line-height: 1.8;
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    .common-item {
        margin: 8px 0;
        padding: 2px 0;
    }
    .common-key {
        color: #881391;
        font-weight: bold;
    }
    .common-value {
        color: #1a1a1a;
    }
    .object-container {
        display: inline-block;
        vertical-align: top;
    }
    .object-name {
        color: #000080;
        font-weight: bold;
    }
    .params-container {
        margin-left: 28px;
        margin-top: 4px;
        margin-bottom: 4px;
        padding-left: 4px;
        border-left: 2px solid #e0e0e0;
    }
    .param-line {
        margin: 3px 0;
        padding-left: 4px;
    }
    .param-name {
        color: #0066cc;
        font-weight: 500;
    }
    .param-value {
        color: #1a1a1a;
    }
    .param-value-string {
        color: #008000;
    }
    .param-value-number {
        color: #ff6600;
    }
    .param-value-list {
        color: #666;
        font-style: italic;
    }
    .common-empty {
        font-family: 'Courier New', monospace;
        color: #666;
    }
</style>
"""


class CommonFormatter:
    """Formatter for Common fixture data to HTML."""

    @staticmethod
    def _parse_object_string(obj_str):
        """Parse object string into class name and parameters."""
        normalized = re.sub(r"\s+", " ", obj_str.strip())
        match = re.match(r"^(\w+)\((.*)\)$", normalized)
        if not match:
            return None, []

        class_name, params_str = match.groups()
        if not params_str.strip():
            return class_name, []

        params = []
        current_param = ""
        paren_depth = 0
        bracket_depth = 0
        in_quotes = False
        quote_char = None

        for i, char in enumerate(params_str):
            if char in ("'", '"'):
                if not in_quotes:
                    in_quotes = True
                    quote_char = char
                elif char == quote_char:
                    if i + 1 < len(params_str) and params_str[i + 1] == quote_char:
                        current_param += char + char
                    else:
                        in_quotes = False
                        quote_char = None
                current_param += char
            elif not in_quotes:
                if char == "(":
                    paren_depth += 1
                elif char == ")":
                    paren_depth -= 1
                elif char == "[":
                    bracket_depth += 1
                elif char == "]":
                    bracket_depth -= 1
                elif char == "," and paren_depth == 0 and bracket_depth == 0:
                    if current_param.strip():
                        params.append(current_param.strip())
                    current_param = ""
                    continue
                current_param += char
            else:
                current_param += char

        if current_param.strip():
            params.append(current_param.strip())

        return class_name, params

    @staticmethod
    def _format_param_value(param_value):
        """Format parameter value with syntax highlighting."""
        param_value = param_value.strip()

        if param_value.startswith("[") and param_value.endswith("]"):
            return f'<span class="param-value-list">{html.escape(param_value)}</span>'

        if (param_value.startswith("'") and param_value.endswith("'")) or (
            param_value.startswith('"') and param_value.endswith('"')
        ):
            return f'<span class="param-value-string">{html.escape(param_value)}</span>'

        if param_value in ("True", "False", "None"):
            return f'<span class="param-value-number">{html.escape(param_value)}</span>'

        try:
            float(param_value)
            return f'<span class="param-value-number">{html.escape(param_value)}</span>'
        except ValueError:
            pass

        return f'<span class="param-value">{html.escape(param_value)}</span>'

    @staticmethod
    def _format_param(param):
        """Format a single parameter with name and value highlighting."""
        if "=" not in param:
            return html.escape(param)

        param_name, param_value = param.split("=", 1)
        formatted_name = f'<span class="param-name">{html.escape(param_name.strip())}</span>='
        formatted_value = CommonFormatter._format_param_value(param_value)
        return f"{formatted_name}{formatted_value}"

    @staticmethod
    def _format_object_string_html(obj_str):
        """Format object string representation as HTML with proper formatting."""
        class_name, params = CommonFormatter._parse_object_string(obj_str)
        if class_name is None:
            return html.escape(obj_str)

        if not params:
            return f'<span class="object-name">{html.escape(class_name)}</span>()'

        formatted_params = [
            f'<div class="param-line">{CommonFormatter._format_param(param)}{"," if i < len(params) - 1 else ""}</div>'
            for i, param in enumerate(params)
        ]
        return (
            f'<div class="object-container">'
            f'<span class="object-name">{html.escape(class_name)}</span>('
            f'<div class="params-container">{"".join(formatted_params)}</div>'
            f")</div>"
        )

    @staticmethod
    def _is_object_string(value_str):
        """Check if string looks like an object representation: ClassName(...)"""
        if not isinstance(value_str, str):
            return False
        normalized = re.sub(r"\s+", " ", value_str.strip())
        return bool(re.match(r"^\w+\(.*\)$", normalized))

    @staticmethod
    def _format_value(value):
        """Format a single value to HTML."""
        value_str = str(value)
        if CommonFormatter._is_object_string(value_str):
            return CommonFormatter._format_object_string_html(value_str)
        return html.escape(value_str) if hasattr(value, "__dict__") else f'"{html.escape(value_str)}"'

    @staticmethod
    def to_html(common_dict):
        """Convert Common object dictionary to HTML representation."""
        if not common_dict:
            return f'{COMMON_FIXTURE_CSS}<div class="common-empty">Common()</div>'

        html_parts = ['<div class="common-container">']
        for key, value in sorted(common_dict.items()):
            value_html = CommonFormatter._format_value(value)
            html_parts.append(
                f'<div class="common-item">'
                f'<span class="common-key">"{html.escape(str(key))}"</span>: '
                f'<span class="common-value">{value_html}</span>'
                f"</div>"
            )

        html_parts.append("</div>")
        return COMMON_FIXTURE_CSS + "".join(html_parts)


def attache_screenshot_and_url(request):
    try:
        page = request.getfixturevalue("page")
        allure.attach(page.screenshot(full_page=True), "Final screenshot", allure.attachment_type.PNG)
        allure.attach(page.url, "URL", allure.attachment_type.URI_LIST)
    except Exception:
        return None
