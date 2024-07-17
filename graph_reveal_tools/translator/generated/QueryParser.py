# Generated from QueryParser.g4 by ANTLR 4.13.1
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
        4,1,17,38,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,3,1,22,8,1,1,1,1,1,3,1,26,
        8,1,1,1,3,1,29,8,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,
        8,0,2,1,0,5,8,1,0,9,17,36,0,10,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,
        6,33,1,0,0,0,8,35,1,0,0,0,10,15,3,2,1,0,11,12,5,3,0,0,12,14,3,2,
        1,0,13,11,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,
        1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,22,5,4,0,0,21,
        20,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,29,3,4,2,0,24,26,5,4,0,
        0,25,24,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,29,3,8,4,0,28,21,
        1,0,0,0,28,25,1,0,0,0,29,3,1,0,0,0,30,31,5,2,0,0,31,32,3,6,3,0,32,
        5,1,0,0,0,33,34,7,0,0,0,34,7,1,0,0,0,35,36,7,1,0,0,36,9,1,0,0,0,
        4,15,21,25,28
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
                     "'planar'", "'tree'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "INTEGER", "SEPERATOR", 
                      "NOT", "VERTEX", "EDGE", "BLOCK", "COMPONENT", "ACYCLIC", 
                      "BIPARTITE", "COMPLETE", "CONNECTED", "EULERIAN", 
                      "HAMILTONIAN", "NO_ISOLATED_V", "PLANAR", "TREE" ]

    RULE_query = 0
    RULE_expr = 1
    RULE_numEntityExpr = 2
    RULE_entity = 3
    RULE_boolProperty = 4

    ruleNames =  [ "query", "expr", "numEntityExpr", "entity", "boolProperty" ]

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
    EULERIAN=13
    HAMILTONIAN=14
    NO_ISOLATED_V=15
    PLANAR=16
    TREE=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




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

        def numEntityExpr(self):
            return self.getTypedRuleContext(QueryParser.NumEntityExprContext,0)


        def NOT(self):
            return self.getToken(QueryParser.NOT, 0)

        def boolProperty(self):
            return self.getTypedRuleContext(QueryParser.BoolPropertyContext,0)


        def getRuleIndex(self):
            return QueryParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = QueryParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 20
                    self.match(QueryParser.NOT)


                self.state = 23
                self.numEntityExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 24
                    self.match(QueryParser.NOT)


                self.state = 27
                self.boolProperty()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumEntityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(QueryParser.INTEGER, 0)

        def entity(self):
            return self.getTypedRuleContext(QueryParser.EntityContext,0)


        def getRuleIndex(self):
            return QueryParser.RULE_numEntityExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumEntityExpr" ):
                listener.enterNumEntityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumEntityExpr" ):
                listener.exitNumEntityExpr(self)




    def numEntityExpr(self):

        localctx = QueryParser.NumEntityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_numEntityExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(QueryParser.INTEGER)
            self.state = 31
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)




    def entity(self):

        localctx = QueryParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
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

        def EULERIAN(self):
            return self.getToken(QueryParser.EULERIAN, 0)

        def HAMILTONIAN(self):
            return self.getToken(QueryParser.HAMILTONIAN, 0)

        def NO_ISOLATED_V(self):
            return self.getToken(QueryParser.NO_ISOLATED_V, 0)

        def PLANAR(self):
            return self.getToken(QueryParser.PLANAR, 0)

        def TREE(self):
            return self.getToken(QueryParser.TREE, 0)

        def getRuleIndex(self):
            return QueryParser.RULE_boolProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolProperty" ):
                listener.enterBoolProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolProperty" ):
                listener.exitBoolProperty(self)




    def boolProperty(self):

        localctx = QueryParser.BoolPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_boolProperty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 261632) != 0)):
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





