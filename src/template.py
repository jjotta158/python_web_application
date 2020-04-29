class Template:
    def __init__(self,name):
        self.name = name
    
    def header(self, title, subtitle, color, bgColor):
        self.title = title
        self.subtitle = subtitle
        self.color = color
        self.bgColor = bgColor

        return f"<header style='bgColor:{self.bgColor}><h1 style='color:{self.color}'>{self.title}</h1><h3>{self.subtitle}</h3></header>"