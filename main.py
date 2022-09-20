# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# opdracht 1

def greet(name, groet='Hello, <name>!'):
    groet = groet.replace('<name>', name)
    return groet

print(greet('Bob', 'Whats up <name>'))    

# opdracht 2

gravity = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6,
        }

def force(mass, body='earth'):
    return mass * gravity[body]

# opdracht 3

G = 6.674*10**-11

def pull(m1,m2,d):
    return G * ((m1*m2)/d**2)

print(pull(800,1500,3))    
