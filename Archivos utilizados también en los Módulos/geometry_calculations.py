## Ejemplo de módulo: geometry_calculations.py

# File: geometry_calculations.py

import math # ESTE MÓDULO INCLUYE LA IMPORTACIÓN DE MATH

def calculate_area_circle(radius): # FUNCIÓN 1
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radius**2

def calculate_circumference_circle(radius): # FUNCIÓN 2 
    """Calcula la circunferencia de un círculo dado su radio."""
    return 2 * math.pi * radius

class Rectangle: # CLASE
    """Representa un rectángulo con ancho y alto."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self): # MÉTODO 1
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def calculate_perimeter(self): # MÉTODO 2
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.width + self.height)