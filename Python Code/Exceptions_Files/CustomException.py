import json
import inspect

class Custom_Exception(Exception):
    def __init__(self, original_exception):
        # Capture module & function dynamically
        stack = inspect.trace()
        if len(stack) > 1:
            frame = stack[1]  # caller frame
        else:
            frame = stack[0]  # top-level call

        module_name = frame.frame.f_globals.get("__name__", "__main__")
        function_name = frame.function
        self.module_name = f"{module_name}.{function_name}"

        self.original_exception = original_exception
        self.message = f"Error occurred in '{self.module_name}': {type(original_exception).__name__}"
        super().__init__(self.message)

    def to_dict(self):
        return {
            "module": self.module_name,
            "error_type": type(self.original_exception).__name__,
            "message": str(self.original_exception)
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)
