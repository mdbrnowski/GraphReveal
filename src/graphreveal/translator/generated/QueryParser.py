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
        4,1,27,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,1,
        2,5,2,29,8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,42,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,62,8,4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,
        12,0,2,1,0,13,16,1,0,17,27,70,0,14,1,0,0,0,2,17,1,0,0,0,4,25,1,0,
        0,0,6,41,1,0,0,0,8,61,1,0,0,0,10,63,1,0,0,0,12,65,1,0,0,0,14,15,
        3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,22,3,4,2,0,18,19,5,4,0,0,19,
        21,3,4,2,0,20,18,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,
        0,23,3,1,0,0,0,24,22,1,0,0,0,25,30,3,6,3,0,26,27,5,3,0,0,27,29,3,
        6,3,0,28,26,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,
        5,1,0,0,0,32,30,1,0,0,0,33,42,3,8,4,0,34,42,3,12,6,0,35,36,5,7,0,
        0,36,42,3,6,3,0,37,38,5,5,0,0,38,39,3,2,1,0,39,40,5,6,0,0,40,42,
        1,0,0,0,41,33,1,0,0,0,41,34,1,0,0,0,41,35,1,0,0,0,41,37,1,0,0,0,
        42,7,1,0,0,0,43,44,5,2,0,0,44,62,3,10,5,0,45,46,5,8,0,0,46,47,5,
        2,0,0,47,62,3,10,5,0,48,49,5,9,0,0,49,50,5,2,0,0,50,62,3,10,5,0,
        51,52,5,10,0,0,52,53,5,2,0,0,53,62,3,10,5,0,54,55,5,11,0,0,55,56,
        5,2,0,0,56,62,3,10,5,0,57,58,5,2,0,0,58,59,5,12,0,0,59,60,5,2,0,
        0,60,62,3,10,5,0,61,43,1,0,0,0,61,45,1,0,0,0,61,48,1,0,0,0,61,51,
        1,0,0,0,61,54,1,0,0,0,61,57,1,0,0,0,62,9,1,0,0,0,63,64,7,0,0,0,64,
        11,1,0,0,0,65,66,7,1,0,0,66,13,1,0,0,0,4,22,30,41,61
    ]

class QueryParser ( Parser ):

    grammarFileName = "QueryParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'|'", "'('", "')'", "<INVALID>", "'<'", "'>'", "'<='", 
                     "'>='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'bipartite'", "'complete'", 
                     "'connected'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'planar'", "'regular'", "'tree'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "INTEGER", "AND", "OR", 
                      "LPAREN", "RPAREN", "NOT", "LESS", "GREATER", "LESS_OR_EQUAL", 
                      "GREATER_OR_EQUAL", "RANGE_OPERATOR", "VERTEX", "EDGE", 
                      "BLOCK", "COMPONENT", "ACYCLIC", "BIPARTITE", "COMPLETE", 
                      "CONNECTED", "CUBIC", "EULERIAN", "HAMILTONIAN", "NO_ISOLATED_V", 
                      "PLANAR", "REGULAR", "TREE" ]

    RULE_query = 0
    RULE_orExpr = 1
    RULE_andExpr = 2
    RULE_expr = 3
    RULE_entityProperty = 4
    RULE_entity = 5
    RULE_boolProperty = 6

    ruleNames =  [ "query", "orExpr", "andExpr", "expr", "entityProperty", 
                   "entity", "boolProperty" ]

    EOF = Token.EOF
    WHITESPACE=1
    INTEGER=2
    AND=3
    OR=4
    LPAREN=5
    RPAREN=6
    NOT=7
    LESS=8
    GREATER=9
    LESS_OR_EQUAL=10
    GREATER_OR_EQUAL=11
    RANGE_OPERATOR=12
    VERTEX=13
    EDGE=14
    BLOCK=15
    COMPONENT=16
    ACYCLIC=17
    BIPARTITE=18
    COMPLETE=19
    CONNECTED=20
    CUBIC=21
    EULERIAN=22
    HAMILTONIAN=23
    NO_ISOLATED_V=24
    PLANAR=25
    REGULAR=26
    TREE=27

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

        def orExpr(self):
            return self.getTypedRuleContext(QueryParser.OrExprContext,0)


        def EOF(self):
            return self.getToken(QueryParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.orExpr()
            self.state = 15
            self.match(QueryParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.AndExprContext)
            else:
                return self.getTypedRuleContext(QueryParser.AndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(QueryParser.OR)
            else:
                return self.getToken(QueryParser.OR, i)

        def getRuleIndex(self):
            return QueryParser.RULE_orExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = QueryParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.andExpr()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 18
                self.match(QueryParser.OR)
                self.state = 19
                self.andExpr()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.ExprContext)
            else:
                return self.getTypedRuleContext(QueryParser.ExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(QueryParser.AND)
            else:
                return self.getToken(QueryParser.AND, i)

        def getRuleIndex(self):
            return QueryParser.RULE_andExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = QueryParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.expr()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 26
                self.match(QueryParser.AND)
                self.state = 27
                self.expr()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        def expr(self):
            return self.getTypedRuleContext(QueryParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(QueryParser.LPAREN, 0)
        def orExpr(self):
            return self.getTypedRuleContext(QueryParser.OrExprContext,0)

        def RPAREN(self):
            return self.getToken(QueryParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = QueryParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 8, 9, 10, 11]:
                localctx = QueryParser.SimpleExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.entityProperty()
                pass
            elif token in [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]:
                localctx = QueryParser.SimpleExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.boolProperty()
                pass
            elif token in [7]:
                localctx = QueryParser.NotExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(QueryParser.NOT)
                self.state = 36
                self.expr()
                pass
            elif token in [5]:
                localctx = QueryParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.match(QueryParser.LPAREN)
                self.state = 38
                self.orExpr()
                self.state = 39
                self.match(QueryParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 8, self.RULE_entityProperty)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = QueryParser.NumEntityPropertyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(QueryParser.INTEGER)
                self.state = 44
                self.entity()
                pass

            elif la_ == 2:
                localctx = QueryParser.HalfOpenRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                localctx.op = self.match(QueryParser.LESS)
                self.state = 46
                self.match(QueryParser.INTEGER)
                self.state = 47
                self.entity()
                pass

            elif la_ == 3:
                localctx = QueryParser.HalfOpenRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                localctx.op = self.match(QueryParser.GREATER)
                self.state = 49
                self.match(QueryParser.INTEGER)
                self.state = 50
                self.entity()
                pass

            elif la_ == 4:
                localctx = QueryParser.HalfOpenRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                localctx.op = self.match(QueryParser.LESS_OR_EQUAL)
                self.state = 52
                self.match(QueryParser.INTEGER)
                self.state = 53
                self.entity()
                pass

            elif la_ == 5:
                localctx = QueryParser.HalfOpenRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                localctx.op = self.match(QueryParser.GREATER_OR_EQUAL)
                self.state = 55
                self.match(QueryParser.INTEGER)
                self.state = 56
                self.entity()
                pass

            elif la_ == 6:
                localctx = QueryParser.ClosedRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.match(QueryParser.INTEGER)
                self.state = 58
                self.match(QueryParser.RANGE_OPERATOR)
                self.state = 59
                self.match(QueryParser.INTEGER)
                self.state = 60
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
        self.enterRule(localctx, 10, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_boolProperty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 268304384) != 0)):
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





