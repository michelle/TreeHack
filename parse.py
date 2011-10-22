import ast, sys
from operator import add

globals = { "classes" : {}, "variables" : {}, "functions" : {} }

def Hack( node, scope ):
    #if hasattr( node, "lineno" ):
    #    scope[ "lineno" ] = node.lineno
    node.Hack( scope )

def DocHack( node, scope ):
    return node.doc( scope ) if hasattr( self.body[0], "Doc" ) else ""

def ModuleHack( self, scope ):
    map( lambda node : Hack( node, scope ), self.body )

def ClassHack( self, scope ):
    classScope = scope[ "classes" ][ self.name ] = { "variables" : {}, "functions" : {}, "lineno" : self.lineno }
    if hasattr( self.body[0], "Doc" ):
        docString = self.body[0].Doc( classScope )
        map( lambda node : Hack( node, classScope ), self.body[1:] )
    else:
        docString = ""
        map( lambda node : Hack( node, classScope ), self.body )

def FunctionDefHack( self, scope ):
    newScope = scope["functions"][ self.name ] = { "lineno": self.lineno }
    self.body[0].Doc( newScope )

def ExprDoc( self, scope ):
    scope["doc"] = self.value.s or ""

def AssignHack( self, scope ):
    scope["variables"][ self.targets[0].id ] = { "lineno": self.lineno }

ast.Expr.Doc = ExprDoc
ast.Module.Hack = ModuleHack
ast.FunctionDef.Hack = FunctionDefHack
ast.ClassDef.Hack = ClassHack
ast.Assign.Hack = AssignHack

def printStr( d, indent=0 ):
    if type( d ) != dict:
        print "%s%s" % ( ' ' * indent * 5 , d )
    else:
        for key, val in d.items():
            print "%s{%s : " % ( ' ' * indent * 5 , key )
            printStr( val, indent + 1)
            print "%s}" % ( ' ' * indent * 5 )

if __name__=='__main__':
    fileCode = ''.join( open( sys.argv[ 1 ] ).readlines() )
    parsedObj = ast.parse( fileCode )
    Hack( parsedObj, globals )
    printStr( globals )
