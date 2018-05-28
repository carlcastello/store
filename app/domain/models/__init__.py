class Domain:
    
    def clean_key(self, key: str) -> str:
        return key[1:] if key[0] == '_' else key
    
    def convert_value(self, value: object) -> dict:
        return value.to_dict() if hasattr(value.__class__, 'to_dict') else value

    def to_dict(self, is_nested = True):
        """
            Converts domain instances into a dictionary
        """
        return {
            self.clean_key(key): self.convert_value(value) if is_nested else value
            for key, value in vars(self).items()
        }

    def __eq__(self, other: object) -> bool: 
        return self.__dict__ == other.__dict__