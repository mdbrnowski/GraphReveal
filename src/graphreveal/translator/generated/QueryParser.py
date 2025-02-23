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
        4,1,24,53,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,47,8,2,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,2,1,
        0,10,13,1,0,14,24,56,0,10,1,0,0,0,2,26,1,0,0,0,4,46,1,0,0,0,6,48,
        1,0,0,0,8,50,1,0,0,0,10,15,3,2,1,0,11,12,5,3,0,0,12,14,3,2,1,0,13,
        11,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,
        0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,27,3,4,2,0,21,27,3,
        8,4,0,22,23,5,4,0,0,23,27,3,4,2,0,24,25,5,4,0,0,25,27,3,8,4,0,26,
        20,1,0,0,0,26,21,1,0,0,0,26,22,1,0,0,0,26,24,1,0,0,0,27,3,1,0,0,
        0,28,29,5,2,0,0,29,47,3,6,3,0,30,31,5,5,0,0,31,32,5,2,0,0,32,47,
        3,6,3,0,33,34,5,6,0,0,34,35,5,2,0,0,35,47,3,6,3,0,36,37,5,7,0,0,
        37,38,5,2,0,0,38,47,3,6,3,0,39,40,5,8,0,0,40,41,5,2,0,0,41,47,3,
        6,3,0,42,43,5,2,0,0,43,44,5,9,0,0,44,45,5,2,0,0,45,47,3,6,3,0,46,
        28,1,0,0,0,46,30,1,0,0,0,46,33,1,0,0,0,46,36,1,0,0,0,46,39,1,0,0,
        0,46,42,1,0,0,0,47,5,1,0,0,0,48,49,7,0,0,0,49,7,1,0,0,0,50,51,7,
        1,0,0,51,9,1,0,0,0,3,15,26,46
    ]

class QueryParser ( Parser ):

    grammarFileName = "QueryParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<'", "'>'", "'<='", "'>='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'bipartite'", "'complete'", "'connected'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'planar'", "'regular'", "'tree'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "INTEGER", "SEPERATOR", 
                      "NOT", "LESS", "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", 
                      "RANGE_OPERATOR", "VERTEX", "EDGE", "BLOCK", "COMPONENT", 
                      "ACYCLIC", "BIPARTITE", "COMPLETE", "CONNECTED", "CUBIC", 
                      "EULERIAN", "HAMILTONIAN", "NO_ISOLATED_V", "PLANAR", 
                      "REGULAR", "TREE" ]

    RULE_query = 0
    RULE_expr = 1
    RULE_entityProperty = 2
    RULE_entity = 3
    RULE_boolProperty = 4

    ruleNames =  [ "query", "expr", "entityProperty", "entity", "boolProperty" ]

    EOF = Token.EOF
    WHITESPACE=1
    INTEGER=2
    SEPERATOR=3
    NOT=4
    LESS=5
    GREATER=6
    LESS_OR_EQUAL=7
    GREATER_OR_EQUAL=8
    RANGE_OPERATOR=9
    VERTEX=10
    EDGE=11
    BLOCK=12
    COMPONENT=13
    ACYCLIC=14
    BIPARTITE=15
    COMPLETE=16
    CONNECTED=17
    CUBIC=18
    EULERIAN=19
    HAMILTONIAN=20
    NO_ISOLATED_V=21
    PLANAR=22
    REGULAR=23
    TREE=24

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

        def entityProperty(self):
            return self.getTypedRuleContext(QueryParser.EntityPropertyContext,0)

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
        def entityProperty(self):
            return self.getTypedRuleContext(QueryParser.EntityPropertyContext,0)

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
                self.entityProperty()
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
                self.entityProperty()
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


    class EntityPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_entityProperty

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumEntityPropertyContext(EntityPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.EntityPropertyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(QueryParser.INTEGER, 0)
        def entity(self):
            return self.getTypedRuleContext(QueryParser.EntityContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumEntityProperty" ):
                return visitor.visitNumEntityProperty(self)
            else:
                return visitor.visitChildren(self)


    class HalfOpenRangeContext(EntityPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.EntityPropertyContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(QueryParser.INTEGER, 0)
        def entity(self):
            return self.getTypedRuleContext(QueryParser.EntityContext,0)

        def LESS(self):
            return self.getToken(QueryParser.LESS, 0)
        def GREATER(self):
            return self.getToken(QueryParser.GREATER, 0)
        def LESS_OR_EQUAL(self):
            return self.getToken(QueryParser.LESS_OR_EQUAL, 0)
        def GREATER_OR_EQUAL(self):
            return self.getToken(QueryParser.GREATER_OR_EQUAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHalfOpenRange" ):
                return visitor.visitHalfOpenRange(self)
            else:
                return visitor.visitChildren(self)


    class ClosedRangeContext(EntityPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.EntityPropertyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(QueryParser.INTEGER)
            else:
                return self.getToken(QueryParser.INTEGER, i)
        def RANGE_OPERATOR(self):
            return self.getToken(QueryParser.RANGE_OPERATOR, 0)
        def entity(self):
            return self.getTypedRuleContext(QueryParser.EntityContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosedRange" ):
                return visitor.visitClosedRange(self)
            else:
                return visitor.visitChildren(self)



    def entityProperty(self):

        localctx = QueryParser.EntityPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_entityProperty)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = QueryParser.NumEntityPropertyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(QueryParser.INTEGER)
                self.state = 29
                self.entity()
                pass

            elif la_ == 2:
                localctx = QueryParser.HalfOpenRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                localctx.op = self.match(QueryParser.LESS)
                self.state = 31
                self.match(QueryParser.INTEGER)
                self.state = 32
                self.entity()
                pass

            elif la_ == 3:
                localctx = QueryParser.HalfOpenRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                localctx.op = self.match(QueryParser.GREATER)
                self.state = 34
                self.match(QueryParser.INTEGER)
                self.state = 35
                self.entity()
                pass

            elif la_ == 4:
                localctx = QueryParser.HalfOpenRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                localctx.op = self.match(QueryParser.LESS_OR_EQUAL)
                self.state = 37
                self.match(QueryParser.INTEGER)
                self.state = 38
                self.entity()
                pass

            elif la_ == 5:
                localctx = QueryParser.HalfOpenRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                localctx.op = self.match(QueryParser.GREATER_OR_EQUAL)
                self.state = 40
                self.match(QueryParser.INTEGER)
                self.state = 41
                self.entity()
                pass

            elif la_ == 6:
                localctx = QueryParser.ClosedRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 42
                self.match(QueryParser.INTEGER)
                self.state = 43
                self.match(QueryParser.RANGE_OPERATOR)
                self.state = 44
                self.match(QueryParser.INTEGER)
                self.state = 45
                self.entity()
                pass


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
            self.state = 48
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
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
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33538048) != 0)):
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





