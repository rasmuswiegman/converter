# Converter CLI

A cross-platform command-line utility for converting time and weight units. Works on macOS, Linux, and Windows.

## Installation

### Quick Start
```python
python3 converter.py --install
```

### Manual Installation
1. Download `converter.py`
2. Make it executable: `chmod +x converter.py` (Unix/Linux/macOS)
3. Run the install command above to add it to your system PATH

## Usage

```python
converter <type> <value> <from_unit> <to_unit>
```

### Time Conversions
```python
converter time 120 seconds minutes    # 120 seconds = 2 minutes
converter t 60 s                      # Show all time conversions for 60 seconds
converter time 2 hours sec            # 2 hours = 7200 seconds
```

### Weight Conversions
```python
converter weight 5.5 kg pounds        # 5.5 kg = 12.1254 pounds
converter w 1000 g                    # Show all weight conversions for 1000 grams
converter weight 16 oz pounds         # 16 oz = 1 pound
```

### Length Conversions
```python
converter length 100 cm meters        # 100 cm = 1 meters
converter l 5 feet                    # Show all length conversions for 5 feet
converter length 1 mile km            # 1 mile = 1.60934 km
```

### Baking/Volume Conversions
```python
converter baking 2 cups ml            # 2 cups = 473.176 ml
converter b 250 ml                    # Show all baking conversions for 250 ml
converter baking 3 tbsp tsp           # 3 tbsp = 9 tsp
```

## Supported Units

**Time:** seconds (s), minutes (m), hours (h), days (d)  
**Weight:** grams (g), kilograms (kg), pounds (lb), ounces (oz)  
**Length:** millimeters (mm), centimeters (cm), meters (m), kilometers (km), inches (in), feet (ft), yards (yd), miles (mi)  
**Baking:** milliliters (ml), liters (l), cups (c), tablespoons (tbsp), teaspoons (tsp), fluid ounces (fl_oz), pints (pt), quarts (qt), gallons (gal)

## Help

```python
converter -h                          # Show help
converter time -h                     # Show time conversion help
converter weight -h                   # Show weight conversion help
converter length -h                   # Show length conversion help
converter baking -h                   # Show baking conversion help
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

Open source - feel free to modify and distribute.
