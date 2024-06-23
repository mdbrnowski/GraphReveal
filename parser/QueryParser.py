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
        4,1,13,31,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,3,1,22,8,1,1,1,3,1,25,8,1,1,
        2,1,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,2,1,0,5,6,1,0,7,13,29,0,8,1,0,
        0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,28,1,0,0,0,8,13,3,2,1,0,9,10,5,3,
        0,0,10,12,3,2,1,0,11,9,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,
        1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,
        19,5,2,0,0,19,25,3,4,2,0,20,22,5,4,0,0,21,20,1,0,0,0,21,22,1,0,0,
        0,22,23,1,0,0,0,23,25,3,6,3,0,24,18,1,0,0,0,24,21,1,0,0,0,25,3,1,
        0,0,0,26,27,7,0,0,0,27,5,1,0,0,0,28,29,7,1,0,0,29,7,1,0,0,0,3,13,
        21,24
    ]

class QueryParser ( Parser ):

    grammarFileName = "QueryParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'acyclic'", 
                     "'bipartite'", "'complete'", "'connected'", "<INVALID>", 
                     "<INVALID>", "'planar'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "INTEGER", "SEPERATOR", 
                      "NOT", "VERTEX", "EDGE", "ACYCLIC", "BIPARTITE", "COMPLETE", 
                      "CONNECTED", "EULERIAN", "HAMILTONIAN", "PLANAR" ]

    RULE_query = 0
    RULE_expr = 1
    RULE_fundamental = 2
    RULE_boolProperty = 3

    ruleNames =  [ "query", "expr", "fundamental", "boolProperty" ]

    EOF = Token.EOF
    WHITESPACE=1
    INTEGER=2
    SEPERATOR=3
    NOT=4
    VERTEX=5
    EDGE=6
    ACYCLIC=7
    BIPARTITE=8
    COMPLETE=9
    CONNECTED=10
    EULERIAN=11
    HAMILTONIAN=12
    PLANAR=13

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
            self.state = 8
            self.expr()
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 9
                self.match(QueryParser.SEPERATOR)
                self.state = 10
                self.expr()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
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

        def INTEGER(self):
            return self.getToken(QueryParser.INTEGER, 0)

        def fundamental(self):
            return self.getTypedRuleContext(QueryParser.FundamentalContext,0)


        def boolProperty(self):
            return self.getTypedRuleContext(QueryParser.BoolPropertyContext,0)


        def NOT(self):
            return self.getToken(QueryParser.NOT, 0)

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
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(QueryParser.INTEGER)
                self.state = 19
                self.fundamental()
                pass
            elif token in [4, 7, 8, 9, 10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 20
                    self.match(QueryParser.NOT)


                self.state = 23
                self.boolProperty()
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


    class FundamentalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERTEX(self):
            return self.getToken(QueryParser.VERTEX, 0)

        def EDGE(self):
            return self.getToken(QueryParser.EDGE, 0)

        def getRuleIndex(self):
            return QueryParser.RULE_fundamental

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFundamental" ):
                listener.enterFundamental(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFundamental" ):
                listener.exitFundamental(self)




    def fundamental(self):

        localctx = QueryParser.FundamentalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fundamental)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
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

        def PLANAR(self):
            return self.getToken(QueryParser.PLANAR, 0)

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
        self.enterRule(localctx, 6, self.RULE_boolProperty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16256) != 0)):
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





