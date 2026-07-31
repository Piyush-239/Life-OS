import re
import sympy


class Calculator:

    def calculate(self, expression: str) -> str:
        # Clean up expression: e.g. remove spaces, handle trailing question marks
        cleaned = expression.strip()
        if cleaned.endswith("?"):
            cleaned = cleaned[:-1].strip()

        # Try to find a math expression pattern in the string (numbers, operators, common math functions)
        match = re.search(
            r"([\d\+\-\*\/\(\)\s\.\^]|sqrt|pow|sin|cos|tan|log)+",
            cleaned,
            re.IGNORECASE,
        )
        if match:
            expr_str = match.group(0).strip()
        else:
            expr_str = cleaned

        try:
            # sympify parses the expression safely
            expr = sympy.sympify(expr_str)
            result = expr.evalf()

            # Convert to python float/int if possible
            val = float(result)
            if val.is_integer():
                return str(int(val))
            return str(val)
        except Exception:
            # Fallback to evaluating the whole cleaned text
            try:
                expr = sympy.sympify(cleaned)
                result = expr.evalf()
                val = float(result)
                if val.is_integer():
                    return str(int(val))
                return str(val)
            except Exception as e:
                return f"Calculator error: could not evaluate expression. Details: {str(e)}"
