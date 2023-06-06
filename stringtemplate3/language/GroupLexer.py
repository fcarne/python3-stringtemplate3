### $ANTLR 2.7.7 (2006-11-01): "group.g" -> "GroupLexer.py"$
### import antlr and other modules ..
from stringtemplate3 import antlr

### header action >>>
from .ASTExpr import *

### header action <<<
### preamble action >>>

### preamble action <<<
### >>>The Literals<<<
literals = {}
literals["default"] = 21
literals["group"] = 4
literals["implements"] = 7


### import antlr.Token
### >>>The Known Token Types <<<
SKIP = antlr.SKIP
INVALID_TYPE = antlr.INVALID_TYPE
EOF_TYPE = antlr.EOF_TYPE
EOF = antlr.EOF
NULL_TREE_LOOKAHEAD = antlr.NULL_TREE_LOOKAHEAD
MIN_USER_TYPE = antlr.MIN_USER_TYPE
LITERAL_group = 4
ID = 5
COLON = 6
LITERAL_implements = 7
COMMA = 8
SEMI = 9
AT = 10
DOT = 11
LPAREN = 12
RPAREN = 13
DEFINED_TO_BE = 14
STRING = 15
BIGSTRING = 16
ASSIGN = 17
ANONYMOUS_TEMPLATE = 18
LBRACK = 19
RBRACK = 20
LITERAL_default = 21
STAR = 22
PLUS = 23
OPTIONAL = 24
SL_COMMENT = 25
ML_COMMENT = 26
NL = 27
WS = 28


class Lexer(antlr.CharScanner):
    ### user action >>>
    ### user action <<<
    def __init__(self, *argv, **kwargs):
        antlr.CharScanner.__init__(self, *argv, **kwargs)
        self.caseSensitiveLiterals = True
        self.setCaseSensitive(True)
        self.literals = literals

    def nextToken(self):
        while True:
            try:  ### try again ..
                while True:
                    _token = None
                    _ttype = INVALID_TYPE
                    self.resetText()
                    try:  ## for char stream error handling
                        try:  ##for lexical error handling
                            la1 = self.LA(1)
                            if False:
                                pass
                            elif (
                                la1
                                and la1
                                in "ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz"
                            ):
                                self.mID(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in '"':
                                self.mSTRING(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "<":
                                self.mBIGSTRING(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "{":
                                self.mANONYMOUS_TEMPLATE(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "@":
                                self.mAT(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "(":
                                self.mLPAREN(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in ")":
                                self.mRPAREN(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "[":
                                self.mLBRACK(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "]":
                                self.mRBRACK(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in ",":
                                self.mCOMMA(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in ".":
                                self.mDOT(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in ";":
                                self.mSEMI(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "*":
                                self.mSTAR(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "+":
                                self.mPLUS(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "=":
                                self.mASSIGN(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "?":
                                self.mOPTIONAL(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in "\t\n\u000c\r ":
                                self.mWS(True)
                                theRetToken = self._returnToken
                            else:
                                if (self.LA(1) == ":") and (self.LA(2) == ":"):
                                    self.mDEFINED_TO_BE(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1) == "/") and (self.LA(2) == "/"):
                                    self.mSL_COMMENT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1) == "/") and (self.LA(2) == "*"):
                                    self.mML_COMMENT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1) == ":") and (True):
                                    self.mCOLON(True)
                                    theRetToken = self._returnToken
                                else:
                                    self.default(self.LA(1))

                            if not self._returnToken:
                                raise antlr.TryAgain  ### found SKIP token
                            ### return token to caller
                            return self._returnToken
                        ### handle lexical errors ....
                        except antlr.RecognitionException as e:
                            raise antlr.TokenStreamRecognitionException(e)
                    ### handle char stream errors ...
                    except antlr.CharStreamException as cse:
                        if isinstance(cse, antlr.CharStreamIOException):
                            raise antlr.TokenStreamIOException(cse.io)
                        else:
                            raise antlr.TokenStreamException(str(cse))
            except antlr.TryAgain:
                pass

    def mID(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ID
        _saveIndex = 0
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in "abcdefghijklmnopqrstuvwxyz":
            self.matchRange("a", "z")
        elif la1 and la1 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.matchRange("A", "Z")
        elif la1 and la1 in "_":
            self.match("_")
        else:
            self.raise_NoViableAlt(self.LA(1))

        while True:
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in "abcdefghijklmnopqrstuvwxyz":
                self.matchRange("a", "z")
            elif la1 and la1 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                self.matchRange("A", "Z")
            elif la1 and la1 in "0123456789":
                self.matchRange("0", "9")
            elif la1 and la1 in "-":
                self.match("-")
            elif la1 and la1 in "_":
                self.match("_")
            else:
                break

        ### option { testLiterals=true }
        _ttype = self.testLiteralsTable(_ttype)
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mSTRING(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = STRING
        _saveIndex = 0
        _saveIndex = self.text.length()
        self.match('"')
        self.text.setLength(_saveIndex)
        while True:
            if (self.LA(1) == "\\") and (self.LA(2) == '"'):
                _saveIndex = self.text.length()
                self.match("\\")
                self.text.setLength(_saveIndex)
                self.match('"')
            elif (self.LA(1) == "\\") and (_tokenSet_0.member(self.LA(2))):
                self.match("\\")
                self.matchNot('"')
            elif _tokenSet_1.member(self.LA(1)):
                self.matchNot('"')
            else:
                break

        _saveIndex = self.text.length()
        self.match('"')
        self.text.setLength(_saveIndex)
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mBIGSTRING(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BIGSTRING
        _saveIndex = 0
        _saveIndex = self.text.length()
        self.match("<<")
        self.text.setLength(_saveIndex)
        if (self.LA(1) == "\n" or self.LA(1) == "\r") and (
            self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe"
        ):
            _saveIndex = self.text.length()
            self.mNL(False)
            self.text.setLength(_saveIndex)
            self.newline()
        elif (self.LA(1) >= "\u0000" and self.LA(1) <= "\ufffe") and (
            self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe"
        ):
            pass
        else:
            self.raise_NoViableAlt(self.LA(1))

        while True:
            ###  nongreedy exit test
            if (self.LA(1) == ">") and (self.LA(2) == ">"):
                break
            if (
                (self.LA(1) == "\r")
                and (self.LA(2) == "\n")
                and (self.LA(3) == ">" and self.LA(4) == ">")
            ):
                _saveIndex = self.text.length()
                self.match("\r")
                self.text.setLength(_saveIndex)
                _saveIndex = self.text.length()
                self.match("\n")
                self.text.setLength(_saveIndex)
                self.newline()
            elif (
                (self.LA(1) == "\n")
                and (self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe")
                and (self.LA(2) == ">" and self.LA(3) == ">")
            ):
                _saveIndex = self.text.length()
                self.match("\n")
                self.text.setLength(_saveIndex)
                self.newline()
            elif (
                (self.LA(1) == "\r")
                and (self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe")
                and (self.LA(2) == ">" and self.LA(3) == ">")
            ):
                _saveIndex = self.text.length()
                self.match("\r")
                self.text.setLength(_saveIndex)
                self.newline()
            elif (self.LA(1) == "\n" or self.LA(1) == "\r") and (
                self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe"
            ):
                self.mNL(False)
                self.newline()
            elif (self.LA(1) == "\\") and (self.LA(2) == ">"):
                _saveIndex = self.text.length()
                self.match("\\")
                self.text.setLength(_saveIndex)
                self.match(">")
            elif (self.LA(1) >= "\u0000" and self.LA(1) <= "\ufffe") and (
                self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe"
            ):
                self.matchNot(antlr.EOF_CHAR)
            else:
                break

        _saveIndex = self.text.length()
        self.match(">>")
        self.text.setLength(_saveIndex)
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mNL(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = NL
        _saveIndex = 0
        if (self.LA(1) == "\r") and (self.LA(2) == "\n"):
            self.match("\r")
            self.match("\n")
        elif (self.LA(1) == "\r") and (True):
            self.match("\r")
        elif self.LA(1) == "\n":
            self.match("\n")
        else:
            self.raise_NoViableAlt(self.LA(1))

        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mANONYMOUS_TEMPLATE(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ANONYMOUS_TEMPLATE
        _saveIndex = 0
        args = None
        t = None
        _saveIndex = self.text.length()
        self.match("{")
        self.text.setLength(_saveIndex)
        while True:
            ###  nongreedy exit test
            if (self.LA(1) == "}") and (True):
                break
            if (self.LA(1) == "\n" or self.LA(1) == "\r") and (
                self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe"
            ):
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in "\r":
                    self.match("\r")
                elif la1 and la1 in "\n":
                    pass
                else:
                    self.raise_NoViableAlt(self.LA(1))

                self.match("\n")
                self.newline()
            elif (self.LA(1) == "\\") and (self.LA(2) == ">"):
                _saveIndex = self.text.length()
                self.match("\\")
                self.text.setLength(_saveIndex)
                self.match(">")
            elif (self.LA(1) >= "\u0000" and self.LA(1) <= "\ufffe") and (
                self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe"
            ):
                self.matchNot(antlr.EOF_CHAR)
            else:
                break

        _saveIndex = self.text.length()
        self.match("}")
        self.text.setLength(_saveIndex)
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mAT(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = AT
        _saveIndex = 0
        self.match("@")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mLPAREN(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LPAREN
        _saveIndex = 0
        self.match("(")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mRPAREN(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = RPAREN
        _saveIndex = 0
        self.match(")")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mLBRACK(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LBRACK
        _saveIndex = 0
        self.match("[")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mRBRACK(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = RBRACK
        _saveIndex = 0
        self.match("]")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mCOMMA(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = COMMA
        _saveIndex = 0
        self.match(",")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mDOT(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DOT
        _saveIndex = 0
        self.match(".")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mDEFINED_TO_BE(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DEFINED_TO_BE
        _saveIndex = 0
        self.match("::=")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mSEMI(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SEMI
        _saveIndex = 0
        self.match(";")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mCOLON(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = COLON
        _saveIndex = 0
        self.match(":")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mSTAR(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = STAR
        _saveIndex = 0
        self.match("*")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mPLUS(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = PLUS
        _saveIndex = 0
        self.match("+")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mASSIGN(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ASSIGN
        _saveIndex = 0
        self.match("=")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mOPTIONAL(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = OPTIONAL
        _saveIndex = 0
        self.match("?")
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mSL_COMMENT(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SL_COMMENT
        _saveIndex = 0
        self.match("//")
        while True:
            if _tokenSet_2.member(self.LA(1)):
                self.match(_tokenSet_2)
            else:
                break

        if self.LA(1) == "\n" or self.LA(1) == "\r":
            self.mNL(False)
        else:  ## <m4>
            pass

        _ttype = SKIP
        self.newline()
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mML_COMMENT(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ML_COMMENT
        _saveIndex = 0
        self.match("/*")
        while True:
            ###  nongreedy exit test
            if (self.LA(1) == "*") and (self.LA(2) == "/"):
                break
            if (self.LA(1) == "\n" or self.LA(1) == "\r") and (
                self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe"
            ):
                self.mNL(False)
                self.newline()
            elif (self.LA(1) >= "\u0000" and self.LA(1) <= "\ufffe") and (
                self.LA(2) >= "\u0000" and self.LA(2) <= "\ufffe"
            ):
                self.matchNot(antlr.EOF_CHAR)
            else:
                break

        self.match("*/")
        _ttype = SKIP
        self.set_return_token(_createToken, _token, _ttype, _begin)

    def mWS(self, _createToken):
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = WS
        _saveIndex = 0
        _cnt66 = 0
        while True:
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in " ":
                self.match(" ")
            elif la1 and la1 in "\t":
                self.match("\t")
            elif la1 and la1 in "\u000c":
                self.match("\f")
            elif la1 and la1 in "\n\r":
                self.mNL(False)
                self.newline()
            else:
                break

            _cnt66 += 1
        if _cnt66 < 1:
            self.raise_NoViableAlt(self.LA(1))
        _ttype = SKIP
        self.set_return_token(_createToken, _token, _ttype, _begin)


### generate bit set
def mk_tokenSet_0():
    data = [0] * 2048  ### init list
    data[0] = -17179869185
    for x in range(1, 1023):
        data[x] = -1
    data[1023] = 9223372036854775807
    return data


_tokenSet_0 = antlr.BitSet(mk_tokenSet_0())


### generate bit set
def mk_tokenSet_1():
    data = [0] * 2048  ### init list
    data[0] = -17179869185
    data[1] = -268435457
    for x in range(2, 1023):
        data[x] = -1
    data[1023] = 9223372036854775807
    return data


_tokenSet_1 = antlr.BitSet(mk_tokenSet_1())


### generate bit set
def mk_tokenSet_2():
    data = [0] * 2048  ### init list
    data[0] = -9217
    for x in range(1, 1023):
        data[x] = -1
    data[1023] = 9223372036854775807
    return data


_tokenSet_2 = antlr.BitSet(mk_tokenSet_2())

### __main__ header action >>>
if __name__ == "__main__":
    from stringtemplate3 import antlr

    from . import GroupLexer

    ### create lexer - shall read from stdin
    try:
        for token in GroupLexer.Lexer():
            print(token)

    except antlr.TokenStreamException as e:
        print("error: exception caught while lexing: ", e)
### __main__ header action <<<
