class BinaryTree:
    ''' This is a tree it is cool you know... '''

    def __init__( self, datum, left=None, right=None ):
        ''' This is the constructor for the Tree '''
          self.datum = datum
          self.left = left
          self.right = right

    def children( self ):
          ''' This returns the children as a list '''
          return [ self.left, self.right ]

    def right_child( self ):
          return self.right

    def left_child( self ):
          return self.left

def Print( tree ):
    """ I print treess.. isnt that obvious >.> """
      def helper( tree, indent ):
          print tree.datum
          helper( tree.left, indent + 1 )
          helper( tree.right, indent + 1 )
      helper( tree, 0 )

B = BinaryTree

Tree = B( 1, B( 2, B( 3 ), B( 1, B( 4 ) ) ), B( 4 ) )
Print( tree )
