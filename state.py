class State:
    def __init__(self, on, bri, hue, sat):
        self.on = on
        self.bri = bri
        self.hue = hue
        self.sat = sat

    def to_json(self):
        return """{
"on": %s,
"bri": %s,
"hue": %s,
"sat": %s
}""" % (self.on, self.bri, self.hue, self.sat)
