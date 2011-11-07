import ast, sys

globals = { "classes" : {}, "vars" : {}, "methods" : {} }

# BUILDS UP THE REPRESENATION OF THE TREE
def Hack( node, scope ):
    if hasattr( node, "Hack" ):
        node.Hack( scope )
    else:
        print "AHH NODE", node, "Doesnt have HACK METHOD"

def HackMap( nodes, scope ):
    for node in nodes:
        Hack( node, scope )

def ModuleHack( self, scope ):
    HackMap( self.body, scope )

def ImportHack( self, scope ):
    for name in self.names:
        name.Variablize( scope )

def ImportFormHack( self, scope ):
    pass # NOT SURE WHAT TO DO..
    
def ClassHack( self, scope ):
    classScope = scope[ "classes" ][ self.name ] = { "classes" : {}, "vars" : {}, "methods" : {}, "lineno" : self.lineno, "doc" : ast.get_docstring( self ) }
    map( lambda node : Hack( node, classScope ), self.body )

def FunctionDefHack( self, scope ):
    newScope = scope["methods"][ self.name ] = { "lineno": self.lineno, "doc" : ast.get_docstring( self ), "classes" : {}, "methods" : {}, "vars": {} }
    for arg in self.args.args:
        arg.Variablize( newScope )
    if self.args.vararg:
        newScope[ "vars" ][ "*" + self.args.vararg ] = { "lineno": self.lineno, "classes" : {}, "methods" : {}, "vars" : {} }
    if self.args.kwarg:
        newScope[ "vars" ][ "**" + self.args.kwarg ] = { "lineno": self.lineno, "classes" : {}, "methods" : {}, "vars" : {} }

def AssignHack( self, scope ):
    for target in self.targets:
        target.Variablize( scope )

def IfHack( self, scope ):
    HackMap( self.body, scope )
    HackMap( self.orelse, scope )

# VARIABLIZES
def NameVariablize( self, scope ):
    scope[ "vars" ][ self.id ] = { "lineno": self.lineno, "classes" : {}, "methods" : {}, "vars" : {} }

def TupleVariablize( self, scope ):
    for name in self.elts:
        name.Variablize( scope )

def AttributeVariablize( self, scope ):
    scope[ "vars" ][ self.Id() ] = ""

def aliasVariablize( self, scope ):
    scope[ "vars" ][ self.name ] = self.asname if self.asname else ""

def NameId( self ):
    return self.id

def AttributeId( self ):
    return self.value.Id() + "." + self.attr

ast.Name.Id = NameId
ast.Attribute.Id = AttributeId

ast.Name.Variablize = NameVariablize
ast.Tuple.Variablize = TupleVariablize
ast.Attribute.Variablize = AttributeVariablize
ast.alias.Variablize = aliasVariablize

ast.Module.Hack = ModuleHack
ast.Import.Hack = ImportHack
ast.FunctionDef.Hack = FunctionDefHack
ast.ClassDef.Hack = ClassHack
ast.Assign.Hack = AssignHack
ast.If.Hack = IfHack
ast.Pass.Hack = ast.Assert.Hack = ast.Raise.Hack = ast.Print.Hack = ast.AugAssign.Hack = ast.Delete.Hack = ast.Expr.Hack = lambda self, scope: None

def printStr( d, indent=0 ):
    if type( d ) != dict:
        print "%s%s" % ( ' ' * indent * 5 , d )
    else:
        for key, val in d.items():
            print "%s{ %s : " % ( ' ' * indent * 5 , key )
            printStr( val, indent + 1)
            print "%s}" % ( ' ' * indent * 5 )


def HACK( text ):
    global globals
    try:
        Hack( ast.parse( text ), globals )
    except SyntaxError as s:
        return "Syntax Error : " + str( s )
    ret = globals
    globals = { "classes" : {}, "vars" : {}, "methods" : {} }
    return ret

'''
if __name__ == '__main__':
    if len( sys.argv ) > 1:
        printStr( HACK( "\n".join( open( sys.argv[-1] ).readlines() ) ) )
'''
