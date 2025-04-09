class ButtonColor:
    def __init__(self, background, front="#FFFFFF", factor=0.3):
        """
        Initializes the ButtonColor class with background and front colors.

        Args:
            background (str): Background color in hex format (e.g., '#7AEA10' or '7AEA10')
            front (str): Front color in hex format (default: '#FFFFFF')
            factor (float): Factor to lighten or darken the background color:
                            > 1.0 lightens the color (e.g., 1.5 = 50% lighter)
                            < 1.0 darkens the color (e.g., 0.7 = 30% darker)
                            = 1.0 keeps the color unchanged
        """
        self.background = background
        self.front = front
        self.darker = self.adjust_color_brightness(background, 1-factor)
        self.lighter = self.adjust_color_brightness(background, 1+factor)

        self.front_rgb = self.hex_to_rgb(front)
        self.background_rgb = self.hex_to_rgb(background)
        self.darker_rgb = self.hex_to_rgb(self.darker)
        self.lighter_rgb = self.hex_to_rgb(self.lighter)
    
    def hex_to_rgb(self, hex_color):
        """
        Converts a hex color string to an RGB list.
        
        Args:
            hex_color (str): A hex color string (e.g., '#7AEA10' or '7AEA10')
            
        Returns:
            list: A list containing the RGB values [R, G, B]
        """
        hex_color = hex_color.replace('#', '').strip()
        hex_color = hex_color.upper()

        if len(hex_color) != 6:
                raise ValueError("Invalid hex color format. Expected format: '#RRGGBB' or 'RRGGBB'")
        
        try:
            red = int(hex_color[:2], 16)
            green = int(hex_color[2:4], 16)
            blue = int(hex_color[4:], 16)
            
            return [red, green, blue]
        except ValueError:
            raise ValueError("Invalid hex color format. Use hexadecimal values (0-9, A-F)")

    def adjust_color_brightness(self,hex_color, factor):
        """
        Adjusts the brightness of a hex color.
        
        Args:
            hex_color (str): A hex color string (e.g., '#7AEA10' or '7AEA10')
            factor (float): Factor to lighten or darken:
                            > 1.0 lightens the color (e.g., 1.5 = 50% lighter)
                            < 1.0 darkens the color (e.g., 0.7 = 30% darker)
                            = 1.0 keeps the color unchanged
        
        Returns:
            str: The adjusted color as a hex string (with # prefix)
        """
        # Remove '#' if present
        if hex_color.startswith('#'):
            hex_color = hex_color[1:]
        
        # Convert hex to RGB
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        # Apply the factor and ensure values stay within 0-255 range
        r = max(0, min(255, int(r * factor)))
        g = max(0, min(255, int(g * factor)))
        b = max(0, min(255, int(b * factor)))
        
        # Convert back to hex
        return f"#{r:02x}{g:02x}{b:02x}"

# Pallete of colors for buttons
# The colors are based on the Material Design color palette
pallete = {
    'red': ButtonColor('#F44336'),
    'pink': ButtonColor('#E91E63'),
    'purple': ButtonColor('#9C27B0'),
    'deep_purple': ButtonColor('#673AB7'),
    'indigo': ButtonColor('#3F51B5'),
    'blue': ButtonColor('#2196F3'),
    'light_blue': ButtonColor('#03A9F4', factor=0.15),
    'cyan': ButtonColor('#00BCD4', '#000000', factor=0.1),
    'teal': ButtonColor('#009688', '#000000', factor=0.1),
    'green': ButtonColor('#4CAF50', '#000000', factor=0.1),
    'light_green': ButtonColor('#8BC34A', '#000000', factor=0.1),
    'lime': ButtonColor('#CDDC39', '#000000', factor=0.1),
    'yellow': ButtonColor('#FFEB3B', '#000000', factor=0.05),
    'amber': ButtonColor('#FFC107', '#000000', factor=0.2),
    'orange': ButtonColor('#FF9800', '#000000', factor=0.15),
    'deep_orange': ButtonColor('#FF5722'),
    'brown': ButtonColor('#795548', factor=0.2),
    'grey': ButtonColor('#9E9E9E', '#000000', factor=0.15),
    'blue_grey': ButtonColor('#607D8B', factor=0.1),
    'white': ButtonColor('#FFFFFF', '#000000'),
    'black': ButtonColor('#212121'),
    'default_light': ButtonColor('#AACCF4', '#000000', 0.1),
    'default_dark': ButtonColor('#23456D', '#FFFFFF'),
}