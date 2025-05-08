from datetime import date, datetime


class Serializer:
    def serialize_to_dict(self):
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(value, (datetime, date)):
                result[column.name] = value.isoformat() if value else None
            else:
                result[column.name] = value
        return result
