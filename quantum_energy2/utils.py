import argparse
import configparser
import os.path
import sys

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'config.ini')

def parse_cli_arguments():
    parser = argparse.ArgumentParser(description='A script that estimates the energy of a quantum physical two body system by implementing gradient descent')
    parser.add_argument('-x0', type=float, default=1.0, metavar='x0',help='initial value for x', required=False)
    parser.add_argument('-a', type=float, default=1.0, metavar='a',help='initial value for a (sigma)', required=False)
    parser.add_argument('-b', type=float, default=1.0, metavar='b',help='initial value for b', required=False)
    parser.add_argument('-lr', type=float, default=1.0, metavar='learning rate', help='value for initial learning rate used in gradient descent', required=False)
    parser.add_argument('-i', '--max_iter', type=int, default=2000, metavar='max iterations',
    help='number of maximum iterations in gradient descent', required=False)
    parser.add_argument('-f', '--function', dest='func', choices=['func1', 'func2'], required=False,
                        help='Choose between the functions. Default: func1', default='func1')
    parser.add_argument('-p', '--plot', dest='plot', action='store_true', default=False,
                        help='Option for plotting the result', required=False)
    parser.add_argument('-np', '--num_particles', type=int, dest='num_particles', default = 1, help='number of particles in quantum system', choices=[1,2], required = False)
    # Forklaring: type=type parser konverterer til, metavar=dummy variabelnavn i help og feilmeldinger,
    # dest=variabelnavn for lagring

    args = parser.parse_args()
    print(args)
    return vars(args)

def parse_config_file():
    assert os.path.isfile(CONFIG_FILE)
    
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    x0 = config['ARGUMENTS'].getfloat('x0')
    a = config['ARGUMENTS'].getfloat('a')
    b = config['ARGUMENTS'].getfloat('b')
    lr = config['ARGUMENTS'].getfloat('lr')
    max_iter = config['ARGUMENTS'].getint('max_iter')
    plot = config['ARGUMENTS'].getboolean('plot')
    func = config['ARGUMENTS']['function']
    num_particles = config['ARGUMENTS'].getint('num_particles')

    args = {
        'x0':x0,
        'a':a, 
        'b':b, 
        'lr':lr, 
        'max_iter':max_iter, 
        'plot': plot,
        'func':func, 
        'num_particles':num_particles
        }
    return args



