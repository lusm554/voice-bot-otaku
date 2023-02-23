class MissingEnvironmentVariable(Exception):
    """Describes error of missing environment variable.""" 
    ...

class UnableCastLiteral(Exception):
    """Describes a type conversion error that is not possible."""
    ...