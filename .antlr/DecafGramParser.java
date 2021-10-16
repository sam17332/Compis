// Generated from /Users/rsam/OneDrive/Documents/U/5Quinto/Semestre2/Compis/DecafGram.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DecafGramParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, PROGRAM=2, IF=3, ELSE=4, FOR=5, WHILE=6, RETURN=7, BREAK=8, CONTINUE=9, 
		BOOLEAN=10, CHAR=11, INT=12, TRUE=13, FALSE=14, VOID=15, STRUCT=16, CALLOUT=17, 
		SEMICOLON=18, LCURLY=19, RCURLY=20, LSQUARE=21, RSQUARE=22, LROUND=23, 
		RROUND=24, COMMA=25, QUOTES=26, APOSTROPHE=27, ADD=28, SUB=29, MULTIPLY=30, 
		DIVIDE=31, REMINDER=32, AND=33, OR=34, NOT=35, GREATER_OP=36, LESS_OP=37, 
		GREATER_eq_op=38, LESS_eq_op=39, EQUAL_OP=40, ADD_eq_op=41, SUB_eq_op=42, 
		EQUALITY_OP=43, UNEQUALITY_OP=44, POINT=45, ID=46, ALPHA=47, DECIMAL_LITERAL=48, 
		DIGIT=49, CHAR_LITERAL=50, ALPHA_NUM=51, HEX_DIGIT=52, LINE_COMMENT=53, 
		COMMENT=54, NEWLINE=55, WHITESPACE=56;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_vardeclr = 2, RULE_field_declr = 3, 
		RULE_array_id = 4, RULE_field_var = 5, RULE_var_id = 6, RULE_struct_declr = 7, 
		RULE_method_declr = 8, RULE_return_type = 9, RULE_block = 10, RULE_statement = 11, 
		RULE_method_call = 12, RULE_expr = 13, RULE_location = 14, RULE_int_literal = 15, 
		RULE_char_literal = 16, RULE_bool_literal = 17, RULE_rel_op = 18, RULE_eq_op = 19, 
		RULE_cond_op = 20, RULE_literal = 21, RULE_arith_op = 22, RULE_var_type = 23, 
		RULE_assign_op = 24, RULE_method_name = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "vardeclr", "field_declr", "array_id", "field_var", 
			"var_id", "struct_declr", "method_declr", "return_type", "block", "statement", 
			"method_call", "expr", "location", "int_literal", "char_literal", "bool_literal", 
			"rel_op", "eq_op", "cond_op", "literal", "arith_op", "var_type", "assign_op", 
			"method_name"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'Program'", "'if'", "'else'", "'for'", "'while'", "'return'", 
			"'break'", "'continue'", "'boolean'", "'char'", "'int'", "'True'", "'False'", 
			"'void'", "'struct'", "'callout'", "';'", "'{'", "'}'", "'['", "']'", 
			"'('", "')'", "','", "'\"'", "'''", "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'&&'", "'||'", "'!'", "'>'", "'<'", "'>='", "'<='", "'='", "'+='", "'-='", 
			"'=='", "'!='", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "PROGRAM", "IF", "ELSE", "FOR", "WHILE", "RETURN", "BREAK", 
			"CONTINUE", "BOOLEAN", "CHAR", "INT", "TRUE", "FALSE", "VOID", "STRUCT", 
			"CALLOUT", "SEMICOLON", "LCURLY", "RCURLY", "LSQUARE", "RSQUARE", "LROUND", 
			"RROUND", "COMMA", "QUOTES", "APOSTROPHE", "ADD", "SUB", "MULTIPLY", 
			"DIVIDE", "REMINDER", "AND", "OR", "NOT", "GREATER_OP", "LESS_OP", "GREATER_eq_op", 
			"LESS_eq_op", "EQUAL_OP", "ADD_eq_op", "SUB_eq_op", "EQUALITY_OP", "UNEQUALITY_OP", 
			"POINT", "ID", "ALPHA", "DECIMAL_LITERAL", "DIGIT", "CHAR_LITERAL", "ALPHA_NUM", 
			"HEX_DIGIT", "LINE_COMMENT", "COMMENT", "NEWLINE", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "DecafGram.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DecafGramParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(DecafGramParser.CLASS, 0); }
		public TerminalNode PROGRAM() { return getToken(DecafGramParser.PROGRAM, 0); }
		public TerminalNode LCURLY() { return getToken(DecafGramParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(DecafGramParser.RCURLY, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			match(CLASS);
			setState(53);
			match(PROGRAM);
			setState(54);
			match(LCURLY);
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << CHAR) | (1L << INT) | (1L << VOID) | (1L << STRUCT))) != 0)) {
				{
				{
				setState(55);
				declaration();
				}
				}
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(61);
			match(RCURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public Struct_declrContext struct_declr() {
			return getRuleContext(Struct_declrContext.class,0);
		}
		public VardeclrContext vardeclr() {
			return getRuleContext(VardeclrContext.class,0);
		}
		public Method_declrContext method_declr() {
			return getRuleContext(Method_declrContext.class,0);
		}
		public Field_declrContext field_declr() {
			return getRuleContext(Field_declrContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(63);
				struct_declr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(64);
				vardeclr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(65);
				method_declr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(66);
				field_declr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardeclrContext extends ParserRuleContext {
		public TerminalNode SEMICOLON() { return getToken(DecafGramParser.SEMICOLON, 0); }
		public List<Var_typeContext> var_type() {
			return getRuleContexts(Var_typeContext.class);
		}
		public Var_typeContext var_type(int i) {
			return getRuleContext(Var_typeContext.class,i);
		}
		public List<Field_varContext> field_var() {
			return getRuleContexts(Field_varContext.class);
		}
		public Field_varContext field_var(int i) {
			return getRuleContext(Field_varContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(DecafGramParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DecafGramParser.COMMA, i);
		}
		public VardeclrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardeclr; }
	}

	public final VardeclrContext vardeclr() throws RecognitionException {
		VardeclrContext _localctx = new VardeclrContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vardeclr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(69);
			var_type();
			setState(70);
			field_var();
			}
			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(72);
				match(COMMA);
				setState(73);
				var_type();
				setState(74);
				field_var();
				}
				}
				setState(80);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(81);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Field_declrContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public List<Field_varContext> field_var() {
			return getRuleContexts(Field_varContext.class);
		}
		public Field_varContext field_var(int i) {
			return getRuleContext(Field_varContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(DecafGramParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(DecafGramParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DecafGramParser.COMMA, i);
		}
		public Field_declrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_declr; }
	}

	public final Field_declrContext field_declr() throws RecognitionException {
		Field_declrContext _localctx = new Field_declrContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_field_declr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			var_type();
			setState(84);
			field_var();
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(85);
				match(COMMA);
				setState(86);
				field_var();
				}
				}
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(92);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_idContext extends ParserRuleContext {
		public Array_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_id; }
	 
		public Array_idContext() { }
		public void copyFrom(Array_idContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Array_id_structContext extends Array_idContext {
		public TerminalNode ID() { return getToken(DecafGramParser.ID, 0); }
		public TerminalNode LSQUARE() { return getToken(DecafGramParser.LSQUARE, 0); }
		public TerminalNode RSQUARE() { return getToken(DecafGramParser.RSQUARE, 0); }
		public List<TerminalNode> POINT() { return getTokens(DecafGramParser.POINT); }
		public TerminalNode POINT(int i) {
			return getToken(DecafGramParser.POINT, i);
		}
		public List<LocationContext> location() {
			return getRuleContexts(LocationContext.class);
		}
		public LocationContext location(int i) {
			return getRuleContext(LocationContext.class,i);
		}
		public Int_literalContext int_literal() {
			return getRuleContext(Int_literalContext.class,0);
		}
		public Var_idContext var_id() {
			return getRuleContext(Var_idContext.class,0);
		}
		public Array_id_structContext(Array_idContext ctx) { copyFrom(ctx); }
	}
	public static class Array_id_varContext extends Array_idContext {
		public TerminalNode ID() { return getToken(DecafGramParser.ID, 0); }
		public TerminalNode LSQUARE() { return getToken(DecafGramParser.LSQUARE, 0); }
		public TerminalNode RSQUARE() { return getToken(DecafGramParser.RSQUARE, 0); }
		public Int_literalContext int_literal() {
			return getRuleContext(Int_literalContext.class,0);
		}
		public Var_idContext var_id() {
			return getRuleContext(Var_idContext.class,0);
		}
		public Array_id_varContext(Array_idContext ctx) { copyFrom(ctx); }
	}

	public final Array_idContext array_id() throws RecognitionException {
		Array_idContext _localctx = new Array_idContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_array_id);
		try {
			setState(115);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				_localctx = new Array_id_structContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				match(ID);
				setState(95);
				match(LSQUARE);
				setState(98);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case DECIMAL_LITERAL:
					{
					setState(96);
					int_literal();
					}
					break;
				case ID:
					{
					setState(97);
					var_id();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(100);
				match(RSQUARE);
				setState(101);
				match(POINT);
				setState(102);
				location();
				setState(105);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(103);
					match(POINT);
					setState(104);
					location();
					}
					break;
				}
				}
				break;
			case 2:
				_localctx = new Array_id_varContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(107);
				match(ID);
				setState(108);
				match(LSQUARE);
				setState(111);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case DECIMAL_LITERAL:
					{
					setState(109);
					int_literal();
					}
					break;
				case ID:
					{
					setState(110);
					var_id();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(113);
				match(RSQUARE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Field_varContext extends ParserRuleContext {
		public Var_idContext var_id() {
			return getRuleContext(Var_idContext.class,0);
		}
		public Array_idContext array_id() {
			return getRuleContext(Array_idContext.class,0);
		}
		public Field_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_var; }
	}

	public final Field_varContext field_var() throws RecognitionException {
		Field_varContext _localctx = new Field_varContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_field_var);
		try {
			setState(119);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(117);
				var_id();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(118);
				array_id();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_idContext extends ParserRuleContext {
		public Var_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_id; }
	 
		public Var_idContext() { }
		public void copyFrom(Var_idContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Var_id_varContext extends Var_idContext {
		public TerminalNode ID() { return getToken(DecafGramParser.ID, 0); }
		public Var_id_varContext(Var_idContext ctx) { copyFrom(ctx); }
	}
	public static class Var_id_structContext extends Var_idContext {
		public TerminalNode ID() { return getToken(DecafGramParser.ID, 0); }
		public List<TerminalNode> POINT() { return getTokens(DecafGramParser.POINT); }
		public TerminalNode POINT(int i) {
			return getToken(DecafGramParser.POINT, i);
		}
		public List<LocationContext> location() {
			return getRuleContexts(LocationContext.class);
		}
		public LocationContext location(int i) {
			return getRuleContext(LocationContext.class,i);
		}
		public Var_id_structContext(Var_idContext ctx) { copyFrom(ctx); }
	}

	public final Var_idContext var_id() throws RecognitionException {
		Var_idContext _localctx = new Var_idContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_var_id);
		try {
			setState(129);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				_localctx = new Var_id_structContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(121);
				match(ID);
				setState(122);
				match(POINT);
				setState(123);
				location();
				setState(126);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
				case 1:
					{
					setState(124);
					match(POINT);
					setState(125);
					location();
					}
					break;
				}
				}
				break;
			case 2:
				_localctx = new Var_id_varContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(128);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Struct_declrContext extends ParserRuleContext {
		public TerminalNode STRUCT() { return getToken(DecafGramParser.STRUCT, 0); }
		public TerminalNode ID() { return getToken(DecafGramParser.ID, 0); }
		public TerminalNode LCURLY() { return getToken(DecafGramParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(DecafGramParser.RCURLY, 0); }
		public TerminalNode SEMICOLON() { return getToken(DecafGramParser.SEMICOLON, 0); }
		public List<VardeclrContext> vardeclr() {
			return getRuleContexts(VardeclrContext.class);
		}
		public VardeclrContext vardeclr(int i) {
			return getRuleContext(VardeclrContext.class,i);
		}
		public Struct_declrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_declr; }
	}

	public final Struct_declrContext struct_declr() throws RecognitionException {
		Struct_declrContext _localctx = new Struct_declrContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_struct_declr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(STRUCT);
			setState(132);
			match(ID);
			setState(133);
			match(LCURLY);
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << CHAR) | (1L << INT) | (1L << STRUCT))) != 0)) {
				{
				{
				setState(134);
				vardeclr();
				}
				}
				setState(139);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(140);
			match(RCURLY);
			setState(141);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_declrContext extends ParserRuleContext {
		public Return_typeContext return_type() {
			return getRuleContext(Return_typeContext.class,0);
		}
		public Method_nameContext method_name() {
			return getRuleContext(Method_nameContext.class,0);
		}
		public TerminalNode LROUND() { return getToken(DecafGramParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(DecafGramParser.RROUND, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode VOID() { return getToken(DecafGramParser.VOID, 0); }
		public List<TerminalNode> COMMA() { return getTokens(DecafGramParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DecafGramParser.COMMA, i);
		}
		public List<Var_typeContext> var_type() {
			return getRuleContexts(Var_typeContext.class);
		}
		public Var_typeContext var_type(int i) {
			return getRuleContext(Var_typeContext.class,i);
		}
		public List<Var_idContext> var_id() {
			return getRuleContexts(Var_idContext.class);
		}
		public Var_idContext var_id(int i) {
			return getRuleContext(Var_idContext.class,i);
		}
		public Method_declrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_declr; }
	}

	public final Method_declrContext method_declr() throws RecognitionException {
		Method_declrContext _localctx = new Method_declrContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_method_declr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			return_type();
			setState(144);
			method_name();
			setState(145);
			match(LROUND);
			setState(161);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << CHAR) | (1L << INT) | (1L << VOID) | (1L << STRUCT))) != 0)) {
				{
				setState(150);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case BOOLEAN:
				case CHAR:
				case INT:
				case STRUCT:
					{
					{
					setState(146);
					var_type();
					setState(147);
					var_id();
					}
					}
					break;
				case VOID:
					{
					setState(149);
					match(VOID);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(152);
					match(COMMA);
					setState(153);
					var_type();
					setState(154);
					var_id();
					}
					}
					setState(160);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(163);
			match(RROUND);
			setState(164);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_typeContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public TerminalNode VOID() { return getToken(DecafGramParser.VOID, 0); }
		public Return_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_type; }
	}

	public final Return_typeContext return_type() throws RecognitionException {
		Return_typeContext _localctx = new Return_typeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_return_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
			case CHAR:
			case INT:
			case STRUCT:
				{
				setState(166);
				var_type();
				}
				break;
			case VOID:
				{
				setState(167);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LCURLY() { return getToken(DecafGramParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(DecafGramParser.RCURLY, 0); }
		public List<VardeclrContext> vardeclr() {
			return getRuleContexts(VardeclrContext.class);
		}
		public VardeclrContext vardeclr(int i) {
			return getRuleContext(VardeclrContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			match(LCURLY);
			setState(174);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << CHAR) | (1L << INT) | (1L << STRUCT))) != 0)) {
				{
				{
				setState(171);
				vardeclr();
				}
				}
				setState(176);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(180);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << FOR) | (1L << WHILE) | (1L << RETURN) | (1L << BREAK) | (1L << ID))) != 0)) {
				{
				{
				setState(177);
				statement();
				}
				}
				setState(182);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(183);
			match(RCURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Statement_breakContext extends StatementContext {
		public TerminalNode BREAK() { return getToken(DecafGramParser.BREAK, 0); }
		public TerminalNode SEMICOLON() { return getToken(DecafGramParser.SEMICOLON, 0); }
		public Statement_breakContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Statement_whileContext extends StatementContext {
		public TerminalNode WHILE() { return getToken(DecafGramParser.WHILE, 0); }
		public TerminalNode LROUND() { return getToken(DecafGramParser.LROUND, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RROUND() { return getToken(DecafGramParser.RROUND, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Statement_whileContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Statement_assignContext extends StatementContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public Assign_opContext assign_op() {
			return getRuleContext(Assign_opContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(DecafGramParser.SEMICOLON, 0); }
		public Statement_assignContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Statement_methodcallContext extends StatementContext {
		public Method_callContext method_call() {
			return getRuleContext(Method_callContext.class,0);
		}
		public Statement_methodcallContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Statement_returnContext extends StatementContext {
		public TerminalNode RETURN() { return getToken(DecafGramParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(DecafGramParser.SEMICOLON, 0); }
		public Statement_returnContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Statement_forContext extends StatementContext {
		public TerminalNode FOR() { return getToken(DecafGramParser.FOR, 0); }
		public List<Var_idContext> var_id() {
			return getRuleContexts(Var_idContext.class);
		}
		public Var_idContext var_id(int i) {
			return getRuleContext(Var_idContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(DecafGramParser.COMMA, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<Int_literalContext> int_literal() {
			return getRuleContexts(Int_literalContext.class);
		}
		public Int_literalContext int_literal(int i) {
			return getRuleContext(Int_literalContext.class,i);
		}
		public List<TerminalNode> EQUAL_OP() { return getTokens(DecafGramParser.EQUAL_OP); }
		public TerminalNode EQUAL_OP(int i) {
			return getToken(DecafGramParser.EQUAL_OP, i);
		}
		public Statement_forContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Statement_ifContext extends StatementContext {
		public TerminalNode IF() { return getToken(DecafGramParser.IF, 0); }
		public TerminalNode LROUND() { return getToken(DecafGramParser.LROUND, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RROUND() { return getToken(DecafGramParser.RROUND, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(DecafGramParser.ELSE, 0); }
		public Statement_ifContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_statement);
		int _la;
		try {
			setState(230);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				_localctx = new Statement_assignContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(185);
				location();
				setState(186);
				assign_op();
				setState(187);
				expr(0);
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(188);
					match(SEMICOLON);
					}
				}

				}
				break;
			case 2:
				_localctx = new Statement_methodcallContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(191);
				method_call();
				}
				break;
			case 3:
				_localctx = new Statement_ifContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(192);
				match(IF);
				setState(193);
				match(LROUND);
				setState(194);
				expr(0);
				setState(195);
				match(RROUND);
				setState(196);
				block();
				setState(199);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ELSE) {
					{
					setState(197);
					match(ELSE);
					setState(198);
					block();
					}
				}

				}
				break;
			case 4:
				_localctx = new Statement_whileContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(201);
				match(WHILE);
				setState(202);
				match(LROUND);
				setState(203);
				expr(0);
				setState(204);
				match(RROUND);
				setState(205);
				block();
				}
				break;
			case 5:
				_localctx = new Statement_returnContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(207);
				match(RETURN);
				setState(208);
				expr(0);
				setState(209);
				match(SEMICOLON);
				}
				break;
			case 6:
				_localctx = new Statement_forContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(211);
				match(FOR);
				setState(212);
				var_id();
				setState(215);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==EQUAL_OP) {
					{
					setState(213);
					match(EQUAL_OP);
					setState(214);
					int_literal();
					}
				}

				setState(217);
				match(COMMA);
				setState(224);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					{
					setState(218);
					var_id();
					setState(221);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==EQUAL_OP) {
						{
						setState(219);
						match(EQUAL_OP);
						setState(220);
						int_literal();
						}
					}

					}
					}
					break;
				case DECIMAL_LITERAL:
					{
					setState(223);
					int_literal();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(226);
				block();
				}
				break;
			case 7:
				_localctx = new Statement_breakContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(228);
				match(BREAK);
				setState(229);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_callContext extends ParserRuleContext {
		public Method_nameContext method_name() {
			return getRuleContext(Method_nameContext.class,0);
		}
		public TerminalNode LROUND() { return getToken(DecafGramParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(DecafGramParser.RROUND, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(DecafGramParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(DecafGramParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DecafGramParser.COMMA, i);
		}
		public Method_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_call; }
	}

	public final Method_callContext method_call() throws RecognitionException {
		Method_callContext _localctx = new Method_callContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_method_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			method_name();
			setState(233);
			match(LROUND);
			setState(242);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TRUE) | (1L << FALSE) | (1L << LROUND) | (1L << SUB) | (1L << NOT) | (1L << ID) | (1L << DECIMAL_LITERAL) | (1L << CHAR_LITERAL))) != 0)) {
				{
				setState(234);
				expr(0);
				setState(239);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(235);
					match(COMMA);
					setState(236);
					expr(0);
					}
					}
					setState(241);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(244);
			match(RROUND);
			setState(246);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				{
				setState(245);
				match(SEMICOLON);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Expr_presedencia2Context extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(DecafGramParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(DecafGramParser.SUB, 0); }
		public Expr_presedencia2Context(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_literalContext extends ExprContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public Expr_literalContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_locationContext extends ExprContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public Expr_locationContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_presedencia1Context extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MULTIPLY() { return getToken(DecafGramParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(DecafGramParser.DIVIDE, 0); }
		public TerminalNode REMINDER() { return getToken(DecafGramParser.REMINDER, 0); }
		public Expr_presedencia1Context(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_menosContext extends ExprContext {
		public TerminalNode SUB() { return getToken(DecafGramParser.SUB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Expr_menosContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_normalContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public Arith_opContext arith_op() {
			return getRuleContext(Arith_opContext.class,0);
		}
		public Rel_opContext rel_op() {
			return getRuleContext(Rel_opContext.class,0);
		}
		public Eq_opContext eq_op() {
			return getRuleContext(Eq_opContext.class,0);
		}
		public Cond_opContext cond_op() {
			return getRuleContext(Cond_opContext.class,0);
		}
		public Expr_normalContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_parentesisContext extends ExprContext {
		public TerminalNode LROUND() { return getToken(DecafGramParser.LROUND, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RROUND() { return getToken(DecafGramParser.RROUND, 0); }
		public Expr_parentesisContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_methodCallContext extends ExprContext {
		public Method_callContext method_call() {
			return getRuleContext(Method_callContext.class,0);
		}
		public Expr_methodCallContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_negacionContext extends ExprContext {
		public TerminalNode NOT() { return getToken(DecafGramParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Expr_negacionContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				_localctx = new Expr_literalContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(249);
				literal();
				}
				break;
			case 2:
				{
				_localctx = new Expr_locationContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(250);
				location();
				}
				break;
			case 3:
				{
				_localctx = new Expr_methodCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(251);
				method_call();
				}
				break;
			case 4:
				{
				_localctx = new Expr_menosContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(252);
				match(SUB);
				setState(253);
				expr(3);
				}
				break;
			case 5:
				{
				_localctx = new Expr_negacionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(254);
				match(NOT);
				setState(255);
				expr(2);
				}
				break;
			case 6:
				{
				_localctx = new Expr_parentesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(256);
				match(LROUND);
				setState(257);
				expr(0);
				setState(258);
				match(RROUND);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(279);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(277);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
					case 1:
						{
						_localctx = new Expr_presedencia1Context(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(262);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(263);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MULTIPLY) | (1L << DIVIDE) | (1L << REMINDER))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(264);
						expr(7);
						}
						break;
					case 2:
						{
						_localctx = new Expr_presedencia2Context(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(265);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(266);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(267);
						expr(6);
						}
						break;
					case 3:
						{
						_localctx = new Expr_normalContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(268);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(273);
						_errHandler.sync(this);
						switch (_input.LA(1)) {
						case ADD:
						case SUB:
						case MULTIPLY:
						case DIVIDE:
						case REMINDER:
							{
							setState(269);
							arith_op();
							}
							break;
						case GREATER_OP:
						case LESS_OP:
						case GREATER_eq_op:
						case LESS_eq_op:
							{
							setState(270);
							rel_op();
							}
							break;
						case EQUALITY_OP:
						case UNEQUALITY_OP:
							{
							setState(271);
							eq_op();
							}
							break;
						case AND:
						case OR:
							{
							setState(272);
							cond_op();
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(275);
						expr(5);
						}
						break;
					}
					} 
				}
				setState(281);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class LocationContext extends ParserRuleContext {
		public Var_idContext var_id() {
			return getRuleContext(Var_idContext.class,0);
		}
		public Array_idContext array_id() {
			return getRuleContext(Array_idContext.class,0);
		}
		public LocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_location; }
	}

	public final LocationContext location() throws RecognitionException {
		LocationContext _localctx = new LocationContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_location);
		try {
			setState(284);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(282);
				var_id();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(283);
				array_id();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Int_literalContext extends ParserRuleContext {
		public TerminalNode DECIMAL_LITERAL() { return getToken(DecafGramParser.DECIMAL_LITERAL, 0); }
		public Int_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_literal; }
	}

	public final Int_literalContext int_literal() throws RecognitionException {
		Int_literalContext _localctx = new Int_literalContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_int_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			match(DECIMAL_LITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Char_literalContext extends ParserRuleContext {
		public TerminalNode CHAR_LITERAL() { return getToken(DecafGramParser.CHAR_LITERAL, 0); }
		public Char_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_char_literal; }
	}

	public final Char_literalContext char_literal() throws RecognitionException {
		Char_literalContext _localctx = new Char_literalContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_char_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			match(CHAR_LITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Bool_literalContext extends ParserRuleContext {
		public TerminalNode TRUE() { return getToken(DecafGramParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(DecafGramParser.FALSE, 0); }
		public Bool_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_literal; }
	}

	public final Bool_literalContext bool_literal() throws RecognitionException {
		Bool_literalContext _localctx = new Bool_literalContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_bool_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			_la = _input.LA(1);
			if ( !(_la==TRUE || _la==FALSE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Rel_opContext extends ParserRuleContext {
		public TerminalNode GREATER_OP() { return getToken(DecafGramParser.GREATER_OP, 0); }
		public TerminalNode LESS_OP() { return getToken(DecafGramParser.LESS_OP, 0); }
		public TerminalNode LESS_eq_op() { return getToken(DecafGramParser.LESS_eq_op, 0); }
		public TerminalNode GREATER_eq_op() { return getToken(DecafGramParser.GREATER_eq_op, 0); }
		public Rel_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rel_op; }
	}

	public final Rel_opContext rel_op() throws RecognitionException {
		Rel_opContext _localctx = new Rel_opContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_rel_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GREATER_OP) | (1L << LESS_OP) | (1L << GREATER_eq_op) | (1L << LESS_eq_op))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Eq_opContext extends ParserRuleContext {
		public TerminalNode EQUALITY_OP() { return getToken(DecafGramParser.EQUALITY_OP, 0); }
		public TerminalNode UNEQUALITY_OP() { return getToken(DecafGramParser.UNEQUALITY_OP, 0); }
		public Eq_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eq_op; }
	}

	public final Eq_opContext eq_op() throws RecognitionException {
		Eq_opContext _localctx = new Eq_opContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_eq_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(294);
			_la = _input.LA(1);
			if ( !(_la==EQUALITY_OP || _la==UNEQUALITY_OP) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Cond_opContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(DecafGramParser.AND, 0); }
		public TerminalNode OR() { return getToken(DecafGramParser.OR, 0); }
		public Cond_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond_op; }
	}

	public final Cond_opContext cond_op() throws RecognitionException {
		Cond_opContext _localctx = new Cond_opContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_cond_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public Int_literalContext int_literal() {
			return getRuleContext(Int_literalContext.class,0);
		}
		public Char_literalContext char_literal() {
			return getRuleContext(Char_literalContext.class,0);
		}
		public Bool_literalContext bool_literal() {
			return getRuleContext(Bool_literalContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_literal);
		try {
			setState(301);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECIMAL_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(298);
				int_literal();
				}
				break;
			case CHAR_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(299);
				char_literal();
				}
				break;
			case TRUE:
			case FALSE:
				enterOuterAlt(_localctx, 3);
				{
				setState(300);
				bool_literal();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arith_opContext extends ParserRuleContext {
		public TerminalNode MULTIPLY() { return getToken(DecafGramParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(DecafGramParser.DIVIDE, 0); }
		public TerminalNode REMINDER() { return getToken(DecafGramParser.REMINDER, 0); }
		public TerminalNode ADD() { return getToken(DecafGramParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(DecafGramParser.SUB, 0); }
		public Arith_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op; }
	}

	public final Arith_opContext arith_op() throws RecognitionException {
		Arith_opContext _localctx = new Arith_opContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_arith_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADD) | (1L << SUB) | (1L << MULTIPLY) | (1L << DIVIDE) | (1L << REMINDER))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(DecafGramParser.INT, 0); }
		public TerminalNode CHAR() { return getToken(DecafGramParser.CHAR, 0); }
		public TerminalNode BOOLEAN() { return getToken(DecafGramParser.BOOLEAN, 0); }
		public TerminalNode STRUCT() { return getToken(DecafGramParser.STRUCT, 0); }
		public TerminalNode ID() { return getToken(DecafGramParser.ID, 0); }
		public Struct_declrContext struct_declr() {
			return getRuleContext(Struct_declrContext.class,0);
		}
		public Var_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_type; }
	}

	public final Var_typeContext var_type() throws RecognitionException {
		Var_typeContext _localctx = new Var_typeContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_var_type);
		try {
			setState(311);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(305);
				match(INT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(306);
				match(CHAR);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(307);
				match(BOOLEAN);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(308);
				match(STRUCT);
				setState(309);
				match(ID);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(310);
				struct_declr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_opContext extends ParserRuleContext {
		public TerminalNode EQUAL_OP() { return getToken(DecafGramParser.EQUAL_OP, 0); }
		public TerminalNode ADD_eq_op() { return getToken(DecafGramParser.ADD_eq_op, 0); }
		public TerminalNode SUB_eq_op() { return getToken(DecafGramParser.SUB_eq_op, 0); }
		public Assign_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_op; }
	}

	public final Assign_opContext assign_op() throws RecognitionException {
		Assign_opContext _localctx = new Assign_opContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_assign_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(313);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL_OP) | (1L << ADD_eq_op) | (1L << SUB_eq_op))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_nameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DecafGramParser.ID, 0); }
		public Method_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_name; }
	}

	public final Method_nameContext method_name() throws RecognitionException {
		Method_nameContext _localctx = new Method_nameContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_method_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 13:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		case 2:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:\u0140\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\7\2;\n\2\f\2\16\2>\13\2\3\2\3\2\3"+
		"\3\3\3\3\3\3\3\5\3F\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4O\n\4\f\4\16\4"+
		"R\13\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5Z\n\5\f\5\16\5]\13\5\3\5\3\5\3\6\3\6"+
		"\3\6\3\6\5\6e\n\6\3\6\3\6\3\6\3\6\3\6\5\6l\n\6\3\6\3\6\3\6\3\6\5\6r\n"+
		"\6\3\6\3\6\5\6v\n\6\3\7\3\7\5\7z\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u0081\n\b"+
		"\3\b\5\b\u0084\n\b\3\t\3\t\3\t\3\t\7\t\u008a\n\t\f\t\16\t\u008d\13\t\3"+
		"\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0099\n\n\3\n\3\n\3\n\3\n\7"+
		"\n\u009f\n\n\f\n\16\n\u00a2\13\n\5\n\u00a4\n\n\3\n\3\n\3\n\3\13\3\13\5"+
		"\13\u00ab\n\13\3\f\3\f\7\f\u00af\n\f\f\f\16\f\u00b2\13\f\3\f\7\f\u00b5"+
		"\n\f\f\f\16\f\u00b8\13\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00c0\n\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ca\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00da\n\r\3\r\3\r\3\r\3\r\5\r\u00e0\n\r\3"+
		"\r\5\r\u00e3\n\r\3\r\3\r\3\r\3\r\5\r\u00e9\n\r\3\16\3\16\3\16\3\16\3\16"+
		"\7\16\u00f0\n\16\f\16\16\16\u00f3\13\16\5\16\u00f5\n\16\3\16\3\16\5\16"+
		"\u00f9\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\5\17\u0107\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\5\17\u0114\n\17\3\17\3\17\7\17\u0118\n\17\f\17\16\17\u011b\13\17\3\20"+
		"\3\20\5\20\u011f\n\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25"+
		"\3\26\3\26\3\27\3\27\3\27\5\27\u0130\n\27\3\30\3\30\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\5\31\u013a\n\31\3\32\3\32\3\33\3\33\3\33\2\3\34\34\2\4\6\b"+
		"\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\2\n\3\2 \"\3\2\36\37"+
		"\3\2\17\20\3\2&)\3\2-.\3\2#$\3\2\36\"\3\2*,\2\u0159\2\66\3\2\2\2\4E\3"+
		"\2\2\2\6G\3\2\2\2\bU\3\2\2\2\nu\3\2\2\2\fy\3\2\2\2\16\u0083\3\2\2\2\20"+
		"\u0085\3\2\2\2\22\u0091\3\2\2\2\24\u00aa\3\2\2\2\26\u00ac\3\2\2\2\30\u00e8"+
		"\3\2\2\2\32\u00ea\3\2\2\2\34\u0106\3\2\2\2\36\u011e\3\2\2\2 \u0120\3\2"+
		"\2\2\"\u0122\3\2\2\2$\u0124\3\2\2\2&\u0126\3\2\2\2(\u0128\3\2\2\2*\u012a"+
		"\3\2\2\2,\u012f\3\2\2\2.\u0131\3\2\2\2\60\u0139\3\2\2\2\62\u013b\3\2\2"+
		"\2\64\u013d\3\2\2\2\66\67\7\3\2\2\678\7\4\2\28<\7\25\2\29;\5\4\3\2:9\3"+
		"\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=?\3\2\2\2><\3\2\2\2?@\7\26\2\2@\3"+
		"\3\2\2\2AF\5\20\t\2BF\5\6\4\2CF\5\22\n\2DF\5\b\5\2EA\3\2\2\2EB\3\2\2\2"+
		"EC\3\2\2\2ED\3\2\2\2F\5\3\2\2\2GH\5\60\31\2HI\5\f\7\2IP\3\2\2\2JK\7\33"+
		"\2\2KL\5\60\31\2LM\5\f\7\2MO\3\2\2\2NJ\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3"+
		"\2\2\2QS\3\2\2\2RP\3\2\2\2ST\7\24\2\2T\7\3\2\2\2UV\5\60\31\2V[\5\f\7\2"+
		"WX\7\33\2\2XZ\5\f\7\2YW\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3\2"+
		"\2\2][\3\2\2\2^_\7\24\2\2_\t\3\2\2\2`a\7\60\2\2ad\7\27\2\2be\5 \21\2c"+
		"e\5\16\b\2db\3\2\2\2dc\3\2\2\2ef\3\2\2\2fg\7\30\2\2gh\7/\2\2hk\5\36\20"+
		"\2ij\7/\2\2jl\5\36\20\2ki\3\2\2\2kl\3\2\2\2lv\3\2\2\2mn\7\60\2\2nq\7\27"+
		"\2\2or\5 \21\2pr\5\16\b\2qo\3\2\2\2qp\3\2\2\2rs\3\2\2\2st\7\30\2\2tv\3"+
		"\2\2\2u`\3\2\2\2um\3\2\2\2v\13\3\2\2\2wz\5\16\b\2xz\5\n\6\2yw\3\2\2\2"+
		"yx\3\2\2\2z\r\3\2\2\2{|\7\60\2\2|}\7/\2\2}\u0080\5\36\20\2~\177\7/\2\2"+
		"\177\u0081\5\36\20\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0084\3"+
		"\2\2\2\u0082\u0084\7\60\2\2\u0083{\3\2\2\2\u0083\u0082\3\2\2\2\u0084\17"+
		"\3\2\2\2\u0085\u0086\7\22\2\2\u0086\u0087\7\60\2\2\u0087\u008b\7\25\2"+
		"\2\u0088\u008a\5\6\4\2\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089"+
		"\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e"+
		"\u008f\7\26\2\2\u008f\u0090\7\24\2\2\u0090\21\3\2\2\2\u0091\u0092\5\24"+
		"\13\2\u0092\u0093\5\64\33\2\u0093\u00a3\7\31\2\2\u0094\u0095\5\60\31\2"+
		"\u0095\u0096\5\16\b\2\u0096\u0099\3\2\2\2\u0097\u0099\7\21\2\2\u0098\u0094"+
		"\3\2\2\2\u0098\u0097\3\2\2\2\u0099\u00a0\3\2\2\2\u009a\u009b\7\33\2\2"+
		"\u009b\u009c\5\60\31\2\u009c\u009d\5\16\b\2\u009d\u009f\3\2\2\2\u009e"+
		"\u009a\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2"+
		"\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u0098\3\2\2\2\u00a3"+
		"\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\7\32\2\2\u00a6\u00a7\5"+
		"\26\f\2\u00a7\23\3\2\2\2\u00a8\u00ab\5\60\31\2\u00a9\u00ab\7\21\2\2\u00aa"+
		"\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\25\3\2\2\2\u00ac\u00b0\7\25\2"+
		"\2\u00ad\u00af\5\6\4\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae"+
		"\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b6\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3"+
		"\u00b5\5\30\r\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3"+
		"\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9"+
		"\u00ba\7\26\2\2\u00ba\27\3\2\2\2\u00bb\u00bc\5\36\20\2\u00bc\u00bd\5\62"+
		"\32\2\u00bd\u00bf\5\34\17\2\u00be\u00c0\7\24\2\2\u00bf\u00be\3\2\2\2\u00bf"+
		"\u00c0\3\2\2\2\u00c0\u00e9\3\2\2\2\u00c1\u00e9\5\32\16\2\u00c2\u00c3\7"+
		"\5\2\2\u00c3\u00c4\7\31\2\2\u00c4\u00c5\5\34\17\2\u00c5\u00c6\7\32\2\2"+
		"\u00c6\u00c9\5\26\f\2\u00c7\u00c8\7\6\2\2\u00c8\u00ca\5\26\f\2\u00c9\u00c7"+
		"\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00e9\3\2\2\2\u00cb\u00cc\7\b\2\2\u00cc"+
		"\u00cd\7\31\2\2\u00cd\u00ce\5\34\17\2\u00ce\u00cf\7\32\2\2\u00cf\u00d0"+
		"\5\26\f\2\u00d0\u00e9\3\2\2\2\u00d1\u00d2\7\t\2\2\u00d2\u00d3\5\34\17"+
		"\2\u00d3\u00d4\7\24\2\2\u00d4\u00e9\3\2\2\2\u00d5\u00d6\7\7\2\2\u00d6"+
		"\u00d9\5\16\b\2\u00d7\u00d8\7*\2\2\u00d8\u00da\5 \21\2\u00d9\u00d7\3\2"+
		"\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00e2\7\33\2\2\u00dc"+
		"\u00df\5\16\b\2\u00dd\u00de\7*\2\2\u00de\u00e0\5 \21\2\u00df\u00dd\3\2"+
		"\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00e3\5 \21\2\u00e2"+
		"\u00dc\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\5\26"+
		"\f\2\u00e5\u00e9\3\2\2\2\u00e6\u00e7\7\n\2\2\u00e7\u00e9\7\24\2\2\u00e8"+
		"\u00bb\3\2\2\2\u00e8\u00c1\3\2\2\2\u00e8\u00c2\3\2\2\2\u00e8\u00cb\3\2"+
		"\2\2\u00e8\u00d1\3\2\2\2\u00e8\u00d5\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9"+
		"\31\3\2\2\2\u00ea\u00eb\5\64\33\2\u00eb\u00f4\7\31\2\2\u00ec\u00f1\5\34"+
		"\17\2\u00ed\u00ee\7\33\2\2\u00ee\u00f0\5\34\17\2\u00ef\u00ed\3\2\2\2\u00f0"+
		"\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f5\3\2"+
		"\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00ec\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5"+
		"\u00f6\3\2\2\2\u00f6\u00f8\7\32\2\2\u00f7\u00f9\7\24\2\2\u00f8\u00f7\3"+
		"\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\33\3\2\2\2\u00fa\u00fb\b\17\1\2\u00fb"+
		"\u0107\5,\27\2\u00fc\u0107\5\36\20\2\u00fd\u0107\5\32\16\2\u00fe\u00ff"+
		"\7\37\2\2\u00ff\u0107\5\34\17\5\u0100\u0101\7%\2\2\u0101\u0107\5\34\17"+
		"\4\u0102\u0103\7\31\2\2\u0103\u0104\5\34\17\2\u0104\u0105\7\32\2\2\u0105"+
		"\u0107\3\2\2\2\u0106\u00fa\3\2\2\2\u0106\u00fc\3\2\2\2\u0106\u00fd\3\2"+
		"\2\2\u0106\u00fe\3\2\2\2\u0106\u0100\3\2\2\2\u0106\u0102\3\2\2\2\u0107"+
		"\u0119\3\2\2\2\u0108\u0109\f\b\2\2\u0109\u010a\t\2\2\2\u010a\u0118\5\34"+
		"\17\t\u010b\u010c\f\7\2\2\u010c\u010d\t\3\2\2\u010d\u0118\5\34\17\b\u010e"+
		"\u0113\f\6\2\2\u010f\u0114\5.\30\2\u0110\u0114\5&\24\2\u0111\u0114\5("+
		"\25\2\u0112\u0114\5*\26\2\u0113\u010f\3\2\2\2\u0113\u0110\3\2\2\2\u0113"+
		"\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\5\34"+
		"\17\7\u0116\u0118\3\2\2\2\u0117\u0108\3\2\2\2\u0117\u010b\3\2\2\2\u0117"+
		"\u010e\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2"+
		"\2\2\u011a\35\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011f\5\16\b\2\u011d\u011f"+
		"\5\n\6\2\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f\37\3\2\2\2\u0120"+
		"\u0121\7\62\2\2\u0121!\3\2\2\2\u0122\u0123\7\64\2\2\u0123#\3\2\2\2\u0124"+
		"\u0125\t\4\2\2\u0125%\3\2\2\2\u0126\u0127\t\5\2\2\u0127\'\3\2\2\2\u0128"+
		"\u0129\t\6\2\2\u0129)\3\2\2\2\u012a\u012b\t\7\2\2\u012b+\3\2\2\2\u012c"+
		"\u0130\5 \21\2\u012d\u0130\5\"\22\2\u012e\u0130\5$\23\2\u012f\u012c\3"+
		"\2\2\2\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u0130-\3\2\2\2\u0131\u0132"+
		"\t\b\2\2\u0132/\3\2\2\2\u0133\u013a\7\16\2\2\u0134\u013a\7\r\2\2\u0135"+
		"\u013a\7\f\2\2\u0136\u0137\7\22\2\2\u0137\u013a\7\60\2\2\u0138\u013a\5"+
		"\20\t\2\u0139\u0133\3\2\2\2\u0139\u0134\3\2\2\2\u0139\u0135\3\2\2\2\u0139"+
		"\u0136\3\2\2\2\u0139\u0138\3\2\2\2\u013a\61\3\2\2\2\u013b\u013c\t\t\2"+
		"\2\u013c\63\3\2\2\2\u013d\u013e\7\60\2\2\u013e\65\3\2\2\2$<EP[dkquy\u0080"+
		"\u0083\u008b\u0098\u00a0\u00a3\u00aa\u00b0\u00b6\u00bf\u00c9\u00d9\u00df"+
		"\u00e2\u00e8\u00f1\u00f4\u00f8\u0106\u0113\u0117\u0119\u011e\u012f\u0139";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}