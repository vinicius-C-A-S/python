import qt
import os
from interface.gui.widgets.FindPath import findPath

class Button(qt.QPushButton):
    def __init__(self,
        text = "",
        font_size = 9,
        height = 40,
        minimum_width = 50,
        text_padding = 0,
        text_color = "#c3ccdf",
        icon_path = "",
        icon_color = "#c3ccdf",
        icon_size = 20,
        bgc_color = "#44475a",
        bgc_hover = "#4f5368",
        bgc_pressed = "#282a36",
        text_align = 'center',
        name = '',
        is_active = False):
        super().__init__()
    
    # DEFAULT PARAMETERS 
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setMinimumWidth(minimum_width)
        self.setCursor(qt.Qt.PointingHandCursor)
        
    # CUSTOM PARAMETERS
        self.minimun_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.bgc_color = bgc_color
        self.bgc_hover = bgc_hover
        self.bgc_pressed = bgc_pressed
        self.is_active = is_active
        self.text_align = text_align
        self.icon_size = icon_size
        self.name = name
        self.font_size = font_size
        self.image_path = findPath(icon_name = icon_path)
          
        # Set style
        self.set_style(
            name = self.name,
            font_size = self.font_size,
            text_padding = self.text_padding,
            text_color = self.text_color,
            bgc_color = self.bgc_color,
            bgc_hover = self.bgc_hover,
            bgc_pressed = self.bgc_pressed,
            text_align = self.text_align,
            image = self.image_path,
            image_size = self.icon_size,
            is_active = self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            name = self.name,
            font_size = self.font_size,
            text_padding = self.text_padding,
            text_color = self.text_color,
            bgc_color = self.bgc_color,
            bgc_hover = self.bgc_hover,
            bgc_pressed = self.bgc_pressed,
            text_align = self.text_align,
            image = self.image_path,
            image_size = self.icon_size,
            is_active = is_active_menu
        )
    
    # SET STYLESHEET  
    def set_style(
        self,
        name = '',
        font_size = 9,
        text_padding = 55,
        text_color = "#c3ccdf",
        bgc_color = "#44475a",
        bgc_hover = "#4f5368",
        bgc_pressed = "#282a36",
        text_align = "center",
        image = '',
        image_size = 20,
        is_active = False
    ):
    
            
        style_dictionary = {
            "base" : f'''
                        QPushButton{{
                            border: none;
                            color: {text_color};
                            background-color: {bgc_color};
                            padding-left: {text_padding}px;
                            text-align: {text_align};
                            font: 700 {font_size}pt 'sans-serif';}}''',
            "image_style" : f'''
                            QPushButton {{
                                icon: url({image});
                                icon-size: {image_size}px;}}''',
        
            "hover_press" : f'''
                            QPushButton:hover {{
                                icon: url({image[:-4] + '_color.svg'});
                                icon-size: {image_size}px;}}
                            QPushButton:pressed {{
                                icon: url({image[:-4] + '_color.svg'});
                                icon-size: {image_size}px;}}''',
                                
            "style" :   f'''      
                            QPushButton:hover {{
                                background-color: {bgc_hover};
                                color: white;}}
                            QPushButton:pressed {{
                                background-color: {bgc_pressed};
                                color: white;}}''',              
 
            "active_style" : f'''
                            QPushButton {{
                                background-color: #0084d9;
                                border-top-left-radius: 5px;
                                border-bottom-left-radius: 5px;}}''',
        }
        if image != '':
            style = style_dictionary["base"]+style_dictionary["image_style"]+style_dictionary["style"]
            
            if name == 'Reload':
               style = style_dictionary["base"] + style_dictionary["image_style"] + style_dictionary["style"]+ style_dictionary["hover_press"]
        else: 
            style = style_dictionary["base"]+style_dictionary["style"]#no_image + style

        if not is_active:
            self.setStyleSheet(style)
        else:
            style+=style_dictionary["active_style"]
            self.setStyleSheet(style)