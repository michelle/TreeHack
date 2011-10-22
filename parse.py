import ast, sys
from operator import add

globals = {}

def Hack( node, scope ):
    if hasattr( node, "lineno" ):
        scope[ "lineno" ] = node.lineno
    node.Hack( scope )

def DocHack( node, scope ):
    return node.doc( scope ) if hasattr( self.body[0], "Doc" ) else ""

def ModuleHack( self, scope ):
    map( lambda node : Hack( node, scope ), self.body )

def ClassHack( self, scope ):
    classScope = scope[ self.name ] = {}
    if hasattr( self.body[0], "Doc" ):
        docString = self.body[0].Doc( classScope )
        map( lambda node : Hack( node, classScope ), self.body[1:] )
    else:
        docString = ""
        map( lambda node : Hack( node, classScope ), self.body )

def FunctionDefHack( self, scope ):
    newScope = scope[ self.name ] = {}
    self.body[0].Doc( newScope )

def ExprDoc( self, scope ):
    scope["doc"] = self.value.s or ""

ast.Expr.Doc = ExprDoc
ast.Module.Hack = ModuleHack
ast.FunctionDef.Hack = FunctionDefHack
ast.ClassDef.Hack = ClassHack

if __name__=='__main__':
    fileCode = ''.join( open( sys.argv[ 1 ] ).readlines() )
    parsedObj = ast.parse( fileCode )
    Hack( parsedObj, globals )
    print globals

