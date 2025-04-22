class Room:

    def __init__(self, id_room, room_name):
        self._id_room = id_room
        self._room_name = room_name

    @property
    def id_room(self):
        return self._id_room

    @id_room.setter
    def id_room(self, id_room):
        self._id_room = id_room

    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        self._room_name = room_name
