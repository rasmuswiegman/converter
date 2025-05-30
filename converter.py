#!/usr/bin/env python3
"""
Converter CLI - Time and Weight Conversion Tool
A cross-platform command-line utility for converting time and weight units.
"""

import sys
import argparse
import os
import shutil
import platform
from pathlib import Path


class Converter:
    """Main converter class handling time and weight conversions."""
    
    # Time conversion factors (to seconds)
    TIME_UNITS = {
        'seconds': 1,
        'sec': 1,
        's': 1,
        'minutes': 60,
        'min': 60,
        'm': 60,
        'hours': 3600,
        'hr': 3600,
        'h': 3600,
        'days': 86400,
        'd': 86400
    }
    
    # Weight conversion factors (to grams)
    WEIGHT_UNITS = {
        'grams': 1,
        'gram': 1,
        'g': 1,
        'kilograms': 1000,
        'kilogram': 1000,
        'kg': 1000,
        'pounds': 453.592,
        'pound': 453.592,
        'lb': 453.592,
        'lbs': 453.592,
        'ounces': 28.3495,
        'ounce': 28.3495,
        'oz': 28.3495
    }
    
    # Length conversion factors (to meters)
    LENGTH_UNITS = {
        'millimeters': 0.001,
        'millimeter': 0.001,
        'mm': 0.001,
        'centimeters': 0.01,
        'centimeter': 0.01,
        'cm': 0.01,
        'meters': 1,
        'meter': 1,
        'm': 1,
        'kilometers': 1000,
        'kilometer': 1000,
        'km': 1000,
        'inches': 0.0254,
        'inch': 0.0254,
        'in': 0.0254,
        'feet': 0.3048,
        'foot': 0.3048,
        'ft': 0.3048,
        'yards': 0.9144,
        'yard': 0.9144,
        'yd': 0.9144,
        'miles': 1609.34,
        'mile': 1609.34,
        'mi': 1609.34
    }
    
    # Baking/Volume conversion factors (to milliliters)
    BAKING_UNITS = {
        'milliliters': 1,
        'milliliter': 1,
        'ml': 1,
        'liters': 1000,
        'liter': 1000,
        'l': 1000,
        'cups': 236.588,
        'cup': 236.588,
        'c': 236.588,
        'tablespoons': 14.7868,
        'tablespoon': 14.7868,
        'tbsp': 14.7868,
        'teaspoons': 4.92892,
        'teaspoon': 4.92892,
        'tsp': 4.92892,
        'fluid_ounces': 29.5735,
        'fluid_ounce': 29.5735,
        'fl_oz': 29.5735,
        'pints': 473.176,
        'pint': 473.176,
        'pt': 473.176,
        'quarts': 946.353,
        'quart': 946.353,
        'qt': 946.353,
        'gallons': 3785.41,
        'gallon': 3785.41,
        'gal': 3785.41
    }
    
    @classmethod
    def convert_time(cls, value, from_unit, to_unit):
        """Convert time between different units."""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in cls.TIME_UNITS:
            raise ValueError(f"Unknown time unit: {from_unit}")
        if to_unit not in cls.TIME_UNITS:
            raise ValueError(f"Unknown time unit: {to_unit}")
        
        # Convert to seconds first, then to target unit
        seconds = value * cls.TIME_UNITS[from_unit]
        result = seconds / cls.TIME_UNITS[to_unit]
        return result
    
    @classmethod
    def convert_weight(cls, value, from_unit, to_unit):
        """Convert weight between different units."""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in cls.WEIGHT_UNITS:
            raise ValueError(f"Unknown weight unit: {from_unit}")
        if to_unit not in cls.WEIGHT_UNITS:
            raise ValueError(f"Unknown weight unit: {to_unit}")
        
        # Convert to grams first, then to target unit
        grams = value * cls.WEIGHT_UNITS[from_unit]
        result = grams / cls.WEIGHT_UNITS[to_unit]
        return result
    
    @classmethod
    def convert_length(cls, value, from_unit, to_unit):
        """Convert length between different units."""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in cls.LENGTH_UNITS:
            raise ValueError(f"Unknown length unit: {from_unit}")
        if to_unit not in cls.LENGTH_UNITS:
            raise ValueError(f"Unknown length unit: {to_unit}")
        
        # Convert to meters first, then to target unit
        meters = value * cls.LENGTH_UNITS[from_unit]
        result = meters / cls.LENGTH_UNITS[to_unit]
        return result
    
    @classmethod
    def convert_baking(cls, value, from_unit, to_unit):
        """Convert baking/volume measurements between different units."""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in cls.BAKING_UNITS:
            raise ValueError(f"Unknown baking unit: {from_unit}")
        if to_unit not in cls.BAKING_UNITS:
            raise ValueError(f"Unknown baking unit: {to_unit}")
        
        # Convert to milliliters first, then to target unit
        milliliters = value * cls.BAKING_UNITS[from_unit]
        result = milliliters / cls.BAKING_UNITS[to_unit]
        return result
    
    @classmethod
    def detect_unit_type(cls, unit):
        """Detect which type of unit this is."""
        unit = unit.lower()
        
        if unit in cls.TIME_UNITS:
            return 'time'
        elif unit in cls.WEIGHT_UNITS:
            return 'weight'
        elif unit in cls.LENGTH_UNITS:
            return 'length'
        elif unit in cls.BAKING_UNITS:
            return 'baking'
        else:
            return None
    
    @classmethod
    def convert_auto(cls, value, from_unit, to_unit):
        """Automatically detect unit type and convert."""
        from_type = cls.detect_unit_type(from_unit)
        to_type = cls.detect_unit_type(to_unit)
        
        if from_type is None:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_type is None:
            raise ValueError(f"Unknown unit: {to_unit}")
        if from_type != to_type:
            raise ValueError(f"Cannot convert between {from_type} and {to_type} units")
        
        if from_type == 'time':
            return cls.convert_time(value, from_unit, to_unit)
        elif from_type == 'weight':
            return cls.convert_weight(value, from_unit, to_unit)
        elif from_type == 'length':
            return cls.convert_length(value, from_unit, to_unit)
        elif from_type == 'baking':
            return cls.convert_baking(value, from_unit, to_unit)
    
    @classmethod
    def show_all_conversions(cls, conversion_type, value, from_unit):
        """Show all possible conversions for a given value and unit."""
        from_unit = from_unit.lower()
        
        unit_maps = {
            'time': cls.TIME_UNITS,
            't': cls.TIME_UNITS,
            'weight': cls.WEIGHT_UNITS,
            'w': cls.WEIGHT_UNITS,
            'length': cls.LENGTH_UNITS,
            'l': cls.LENGTH_UNITS,
            'baking': cls.BAKING_UNITS,
            'b': cls.BAKING_UNITS
        }
        
        # Define primary units (no duplicates/aliases)
        primary_units = {
            'time': ['seconds', 'minutes', 'hours', 'days'],
            't': ['seconds', 'minutes', 'hours', 'days'],
            'weight': ['grams', 'kilograms', 'pounds', 'ounces'],
            'w': ['grams', 'kilograms', 'pounds', 'ounces'],
            'length': ['millimeters', 'centimeters', 'meters', 'kilometers', 'inches', 'feet', 'yards', 'miles'],
            'l': ['millimeters', 'centimeters', 'meters', 'kilometers', 'inches', 'feet', 'yards', 'miles'],
            'baking': ['milliliters', 'liters', 'cups', 'tablespoons', 'teaspoons', 'fluid_ounces', 'pints', 'quarts', 'gallons'],
            'b': ['milliliters', 'liters', 'cups', 'tablespoons', 'teaspoons', 'fluid_ounces', 'pints', 'quarts', 'gallons']
        }
        
        if conversion_type not in unit_maps:
            raise ValueError(f"Unknown conversion type: {conversion_type}")
        
        units = unit_maps[conversion_type]
        
        if from_unit not in units:
            raise ValueError(f"Unknown {conversion_type} unit: {from_unit}")
        
        print(f"\n{value} {from_unit} converts to:")
        print("─" * 35)
        
        # Get the primary units for this conversion type
        target_units = primary_units[conversion_type]
        
        for to_unit in target_units:
            # Skip if converting to same unit type (e.g., seconds to seconds)
            if (to_unit.lower() == from_unit or 
                (from_unit == 's' and to_unit == 'seconds') or
                (from_unit == 'seconds' and to_unit == 'seconds') or
                (from_unit == 'ml' and to_unit == 'milliliters') or
                (from_unit == 'milliliters' and to_unit == 'milliliters') or
                (from_unit == 'g' and to_unit == 'grams') or
                (from_unit == 'grams' and to_unit == 'grams') or
                (from_unit == 'm' and to_unit == 'meters') or
                (from_unit == 'meters' and to_unit == 'meters')):
                continue
            
            try:
                if conversion_type in ['time', 't']:
                    result = cls.convert_time(value, from_unit, to_unit)
                elif conversion_type in ['weight', 'w']:
                    result = cls.convert_weight(value, from_unit, to_unit)
                elif conversion_type in ['length', 'l']:
                    result = cls.convert_length(value, from_unit, to_unit)
                elif conversion_type in ['baking', 'b']:
                    result = cls.convert_baking(value, from_unit, to_unit)
                
                # Format the result nicely
                if result >= 1000000:
                    formatted_result = f"{result:,.0f}"
                elif result >= 1000:
                    formatted_result = f"{result:,.1f}".rstrip('0').rstrip('.')
                elif result >= 1:
                    formatted_result = f"{result:.3f}".rstrip('0').rstrip('.')
                elif result >= 0.001:
                    formatted_result = f"{result:.5f}".rstrip('0').rstrip('.')
                else:
                    formatted_result = f"{result:.6f}".rstrip('0').rstrip('.')
                
                # Handle singular/plural forms
                display_unit = to_unit
                if result == 1.0:
                    # Convert plural to singular for result of 1
                    if to_unit.endswith('s') and to_unit not in ['cups', 'inches', 'ounces']:
                        display_unit = to_unit[:-1]
                    elif to_unit == 'feet':
                        display_unit = 'foot'
                
                print(f"  {formatted_result} {display_unit}")
                
            except ValueError:
                continue


def install_service():
    """Install the converter as a system service/command."""
    current_file = Path(__file__).resolve()
    system = platform.system().lower()
    
    try:
        if system == "windows":
            # Windows: Add to PATH or copy to a PATH directory
            scripts_dir = Path.home() / "AppData" / "Local" / "Microsoft" / "WindowsApps"
            if not scripts_dir.exists():
                scripts_dir = Path.home() / "bin"
                scripts_dir.mkdir(exist_ok=True)
            
            target = scripts_dir / "converter.py"
            shutil.copy2(current_file, target)
            print(f"✓ Installed to {target}")
            print("Add the directory to your PATH if not already done.")
            
        elif system == "darwin":  # macOS
            # Install to /usr/local/bin
            target = Path("/usr/local/bin/converter")
            try:
                shutil.copy2(current_file, target)
                os.chmod(target, 0o755)
                print(f"✓ Installed to {target}")
            except PermissionError:
                print("Permission denied. Try running with sudo:")
                print(f"sudo python3 {current_file} --install")
                
        else:  # Linux and other Unix-like systems
            # Install to /usr/local/bin
            target = Path("/usr/local/bin/converter")
            try:
                shutil.copy2(current_file, target)
                os.chmod(target, 0o755)
                print(f"✓ Installed to {target}")
            except PermissionError:
                print("Permission denied. Try running with sudo:")
                print(f"sudo python3 {current_file} --install")
        
        print("Installation complete! You can now use 'converter' from anywhere.")
        
    except Exception as e:
        print(f"Installation failed: {e}")
        sys.exit(1)


def main():
    """Main function handling command-line arguments and execution."""
    
    # Handle installation first
    if len(sys.argv) == 2 and sys.argv[1] == "--install":
        install_service()
        return
    
    # Handle help
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help"]):
        print("""
Converter CLI - Convert time, weight, length, and baking units with ease

Usage:
  converter [--install]                     # Install as system command
  converter <value> <unit>                  # Show all conversions
  converter <value> <from_unit> <to_unit>   # Specific conversion
  
  Legacy format (still supported):
  converter <type> <value> <unit> [to_unit] # Type-specific conversion

Examples:
  converter 60 d                        # Show all time conversions for 60 days
  converter 60 s minutes                # Convert 60 seconds to minutes
  converter 1000 g                      # Show all weight conversions for 1000 grams
  converter 5.5 kg pounds               # Convert 5.5 kg to pounds
  converter 100 cm                      # Show all length conversions for 100 cm
  converter 5 feet inches               # Convert 5 feet to inches
  converter 250 ml                      # Show all baking conversions for 250 ml
  converter 2 cups ml                   # Convert 2 cups to milliliters

Auto-detected units:
  Time: seconds(s), minutes(m), hours(h), days(d)
  Weight: grams(g), kilograms(kg), pounds(lb), ounces(oz)
  Length: mm, cm, meters(m), km, inches(in), feet(ft), yards(yd), miles(mi)
  Baking: ml, liters(l), cups(c), tbsp, tsp, fl_oz, pints(pt), quarts(qt), gallons(gal)
        """)
        return
    
    args = sys.argv[1:]
    
    try:
        # Check if first argument is a legacy type command
        if args[0] in ["time", "t", "weight", "w", "length", "l", "baking", "b"]:
            # Legacy format: converter time 60 s [minutes]
            if len(args) < 3:
                print("Error: Legacy format requires at least 3 arguments")
                sys.exit(1)
            
            conversion_type = args[0]
            value = float(args[1])
            from_unit = args[2]
            to_unit = args[3] if len(args) > 3 else None
            
            if to_unit:
                # Specific conversion
                if conversion_type in ["time", "t"]:
                    result = Converter.convert_time(value, from_unit, to_unit)
                elif conversion_type in ["weight", "w"]:
                    result = Converter.convert_weight(value, from_unit, to_unit)
                elif conversion_type in ["length", "l"]:
                    result = Converter.convert_length(value, from_unit, to_unit)
                elif conversion_type in ["baking", "b"]:
                    result = Converter.convert_baking(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.6g} {to_unit}")
            else:
                # Show all conversions
                Converter.show_all_conversions(conversion_type, value, from_unit)
        
        else:
            # Auto-detection format: converter 60 s [minutes]
            if len(args) < 2:
                print("Error: Need at least value and unit")
                sys.exit(1)
            
            value = float(args[0])
            from_unit = args[1]
            to_unit = args[2] if len(args) > 2 else None
            
            if to_unit:
                # Specific conversion: converter 60 s minutes
                result = Converter.convert_auto(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.6g} {to_unit}")
            else:
                # Show all conversions: converter 60 s
                unit_type = Converter.detect_unit_type(from_unit)
                if unit_type is None:
                    raise ValueError(f"Unknown unit: {from_unit}")
                Converter.show_all_conversions(unit_type, value, from_unit)
                
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except IndexError:
        print("Error: Invalid arguments. Use -h for help.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
