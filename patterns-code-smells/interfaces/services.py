class Entity:
    def __init__(self, connection, entity) -> None:
        self.entity = entity
        self.session = connection.get_session()

    def get_entity(self):
        raise NotImplementedError("Only allowed on child classes.")