import re


class ToolExecution:

    def execute(self, command: str) -> str:
        cleaned = command.strip().lower()
        print(f"[ToolExecution] Executing: {command}")

        # Direct print tool simulation
        if "print" in cleaned and "pdf" in cleaned:
            match = re.search(
                r"([\w\-\./]+\.pdf)",
                command,
                re.IGNORECASE,
            )
            pdf_name = (
                match.group(1)
                if match
                else "document.pdf"
            )
            return f"Print Tool: Printed PDF file '{pdf_name}' successfully."

        return f"Tool Execution: Action '{command}' executed successfully (placeholder)."
