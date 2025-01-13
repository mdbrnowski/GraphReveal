# Generated from QueryParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,36,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,5,8,
        1,0,9,19,34,0,10,1,0,0,0,2,26,1,0,0,0,4,28,1,0,0,0,6,31,1,0,0,0,
        8,33,1,0,0,0,10,15,3,2,1,0,11,12,5,3,0,0,12,14,3,2,1,0,13,11,1,0,
        0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,15,
        1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,27,3,4,2,0,21,27,3,8,4,0,22,
        23,5,4,0,0,23,27,3,4,2,0,24,25,5,4,0,0,25,27,3,8,4,0,26,20,1,0,0,
        0,26,21,1,0,0,0,26,22,1,0,0,0,26,24,1,0,0,0,27,3,1,0,0,0,28,29,5,
        2,0,0,29,30,3,6,3,0,30,5,1,0,0,0,31,32,7,0,0,0,32,7,1,0,0,0,33,34,
        7,1,0,0,34,9,1,0,0,0,2,15,26
    ]

class QueryParser ( Parser ):

    grammarFileName = "QueryParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'bipartite'", "'complete'", 
                     "'connected'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'planar'", "'regular'", "'tree'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "INTEGER", "SEPERATOR", 
                      "NOT", "VERTEX", "EDGE", "BLOCK", "COMPONENT", "ACYCLIC", 
                      "BIPARTITE", "COMPLETE", "CONNECTED", "CUBIC", "EULERIAN", 
                      "HAMILTONIAN", "NO_ISOLATED_V", "PLANAR", "REGULAR", 
                      "TREE" ]

    RULE_query = 0
    RULE_expr = 1
    RULE_numEntityProperty = 2
    RULE_entity = 3
    RULE_boolProperty = 4

    ruleNames =  [ "query", "expr", "numEntityProperty", "entity", "boolProperty" ]

    EOF = Token.EOF
    WHITESPACE=1
    INTEGER=2
    SEPERATOR=3
    NOT=4
    VERTEX=5
    EDGE=6
    BLOCK=7
    COMPONENT=8
    ACYCLIC=9
    BIPARTITE=10
    COMPLETE=11
    CONNECTED=12
    CUBIC=13
    EULERIAN=14
    HAMILTONIAN=15
    NO_ISOLATED_V=16
    PLANAR=17
    REGULAR=18
    TREE=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.ExprContext)
            else:
                return self.getTypedRuleContext(QueryParser.ExprContext,i)


        def EOF(self):
            return self.getToken(QueryParser.EOF, 0)

        def SEPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(QueryParser.SEPERATOR)
            else:
                return self.getToken(QueryParser.SEPERATOR, i)

        def getRuleIndex(self):
            return QueryParser.RULE_query

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = QueryParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 11
                self.match(QueryParser.SEPERATOR)
                self.state = 12
                self.expr()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(QueryParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def numEntityProperty(self):
            return self.getTypedRuleContext(QueryParser.NumEntityPropertyContext,0)

        def boolProperty(self):
            return self.getTypedRuleContext(QueryParser.BoolPropertyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpr" ):
                return visitor.visitSimpleExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(QueryParser.NOT, 0)
        def numEntityProperty(self):
            return self.getTypedRuleContext(QueryParser.NumEntityPropertyContext,0)

        def boolProperty(self):
            return self.getTypedRuleContext(QueryParser.BoolPropertyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = QueryParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = QueryParser.SimpleExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.numEntityProperty()
                pass

            elif la_ == 2:
                localctx = QueryParser.SimpleExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.boolProperty()
                pass

            elif la_ == 3:
                localctx = QueryParser.NotExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(QueryParser.NOT)
                self.state = 23
                self.numEntityProperty()
                pass

            elif la_ == 4:
                localctx = QueryParser.NotExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(QueryParser.NOT)
                self.state = 25
                self.boolProperty()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumEntityPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(QueryParser.INTEGER, 0)

        def entity(self):
            return self.getTypedRuleContext(QueryParser.EntityContext,0)


        def getRuleIndex(self):
            return QueryParser.RULE_numEntityProperty

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumEntityProperty" ):
                return visitor.visitNumEntityProperty(self)
            else:
                return visitor.visitChildren(self)




    def numEntityProperty(self):

        localctx = QueryParser.NumEntityPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_numEntityProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(QueryParser.INTEGER)
            self.state = 29
            self.entity()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERTEX(self):
            return self.getToken(QueryParser.VERTEX, 0)

        def EDGE(self):
            return self.getToken(QueryParser.EDGE, 0)

        def BLOCK(self):
            return self.getToken(QueryParser.BLOCK, 0)

        def COMPONENT(self):
            return self.getToken(QueryParser.COMPONENT, 0)

        def getRuleIndex(self):
            return QueryParser.RULE_entity

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity" ):
                return visitor.visitEntity(self)
            else:
                return visitor.visitChildren(self)




    def entity(self):

        localctx = QueryParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACYCLIC(self):
            return self.getToken(QueryParser.ACYCLIC, 0)

        def BIPARTITE(self):
            return self.getToken(QueryParser.BIPARTITE, 0)

        def COMPLETE(self):
            return self.getToken(QueryParser.COMPLETE, 0)

        def CONNECTED(self):
            return self.getToken(QueryParser.CONNECTED, 0)

        def CUBIC(self):
            return self.getToken(QueryParser.CUBIC, 0)

        def EULERIAN(self):
            return self.getToken(QueryParser.EULERIAN, 0)

        def HAMILTONIAN(self):
            return self.getToken(QueryParser.HAMILTONIAN, 0)

        def NO_ISOLATED_V(self):
            return self.getToken(QueryParser.NO_ISOLATED_V, 0)

        def PLANAR(self):
            return self.getToken(QueryParser.PLANAR, 0)

        def REGULAR(self):
            return self.getToken(QueryParser.REGULAR, 0)

        def TREE(self):
            return self.getToken(QueryParser.TREE, 0)

        def getRuleIndex(self):
            return QueryParser.RULE_boolProperty

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolProperty" ):
                return visitor.visitBoolProperty(self)
            else:
                return visitor.visitChildren(self)




    def boolProperty(self):

        localctx = QueryParser.BoolPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_boolProperty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





