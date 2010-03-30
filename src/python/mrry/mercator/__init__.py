from optparse import OptionParser
import cherrypy

def set_port(port):
    cherrypy.config.update({'server.socket_port': port})

def set_config(filename):
    cherrypy.config.update(filename)

def main(default_role=None):
    
    parser = OptionParser()
    parser.add_option("-r", "--role", action="store", dest="role", help="Server role", metavar="ROLE", default=default_role)
    parser.add_option("-p", "--port", action="callback", callback=lambda w, x, y, z: set_port(y), type="int", help="Server port", metavar="PORT")
    parser.add_option("-c", "--config", action="callback", callback=lambda w, x, y, z: set_config(y), help="Configuration file", metavar="FILE")
    parser.add_option("-m", "--master", action="store", dest="master", help="Master URI", metavar="URI")
    (options, args) = parser.parse_args()

    if options.role == 'master':
        from mrry.mercator.master import master_main
        master_main(options)
    elif options.role == 'jobmanager':
        from mrry.mercator.jobmanager import jobmanager_main
        jobmanager_main(options)
    else:
        raise
    
if __name__ == '__main__':
    main()