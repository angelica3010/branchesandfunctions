class Map(object):
    scenes = {
    'Bryant Park': Bryant_park(),
    'Central Park': Central_park(),
    'Met': Met(),
    "Egyptiangallery": Egyptiangallery(),
    "Winner": Winner(),
    "Gameover": Gameover()

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
