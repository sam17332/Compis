// Generated from /Users/rsam/OneDrive/Documents/U/5Quinto/Semestre2/Compis/Decaf.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DecafLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, CLASS=3, PROGRAM=4, IF=5, ELSE=6, FOR=7, WHILE=8, RETURN=9, 
		BREAK=10, CONTINUE=11, BOOLEAN=12, CHAR=13, INT=14, STRING=15, VOID=16, 
		STRUCT=17, CALLOUT=18, SEMICOLON=19, LCURLY=20, RCURLY=21, LSQUARE=22, 
		RSQUARE=23, LROUND=24, RROUND=25, COMMA=26, QUOTES=27, APOSTROPHE=28, 
		ADD=29, SUB=30, MULTIPLY=31, DIVIDE=32, REMINDER=33, AND=34, OR=35, NOT=36, 
		GREATER_OP=37, LESS_OP=38, GREATER_eq_op=39, LESS_eq_op=40, EQUAL_OP=41, 
		ADD_eq_op=42, SUB_eq_op=43, EQUALITY_OP=44, UNEQUALITY_OP=45, POINT=46, 
		ID=47, ALPHA=48, DECIMAL_LITERAL=49, DIGIT=50, CHAR_LITERAL=51, ALPHA_NUM=52, 
		HEX_DIGIT=53, LINE_COMMENT=54, COMMENT=55, NEWLINE=56, WHITESPACE=57;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "CLASS", "PROGRAM", "IF", "ELSE", "FOR", "WHILE", "RETURN", 
			"BREAK", "CONTINUE", "BOOLEAN", "CHAR", "INT", "STRING", "VOID", "STRUCT", 
			"CALLOUT", "SEMICOLON", "LCURLY", "RCURLY", "LSQUARE", "RSQUARE", "LROUND", 
			"RROUND", "COMMA", "QUOTES", "APOSTROPHE", "ADD", "SUB", "MULTIPLY", 
			"DIVIDE", "REMINDER", "AND", "OR", "NOT", "GREATER_OP", "LESS_OP", "GREATER_eq_op", 
			"LESS_eq_op", "EQUAL_OP", "ADD_eq_op", "SUB_eq_op", "EQUALITY_OP", "UNEQUALITY_OP", 
			"POINT", "ID", "ALPHA", "DECIMAL_LITERAL", "DIGIT", "CHAR_LITERAL", "ALPHA_NUM", 
			"HEX_DIGIT", "LINE_COMMENT", "COMMENT", "NEWLINE", "WHITESPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'True'", "'False'", "'class'", "'Program'", "'if'", "'else'", 
			"'for'", "'while'", "'return'", "'break'", "'continue'", "'boolean'", 
			"'char'", "'int'", "'string'", "'void'", "'struct'", "'callout'", "';'", 
			"'{'", "'}'", "'['", "']'", "'('", "')'", "','", "'\"'", "'''", "'+'", 
			"'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", "'!'", "'>'", "'<'", "'>='", 
			"'<='", "'='", "'+='", "'-='", "'=='", "'!='", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "CLASS", "PROGRAM", "IF", "ELSE", "FOR", "WHILE", "RETURN", 
			"BREAK", "CONTINUE", "BOOLEAN", "CHAR", "INT", "STRING", "VOID", "STRUCT", 
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


	public DecafLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Decaf.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;\u0177\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3\2\3\2\3\2\3"+
		"\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3"+
		"\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3"+
		"\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3"+
		"&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3."+
		"\3.\3/\3/\3\60\3\60\7\60\u0125\n\60\f\60\16\60\u0128\13\60\3\61\3\61\3"+
		"\62\6\62\u012d\n\62\r\62\16\62\u012e\3\63\3\63\3\64\3\64\6\64\u0135\n"+
		"\64\r\64\16\64\u0136\3\64\3\64\3\64\3\64\6\64\u013d\n\64\r\64\16\64\u013e"+
		"\3\64\3\64\5\64\u0143\n\64\3\65\3\65\5\65\u0147\n\65\3\66\3\66\3\66\5"+
		"\66\u014c\n\66\3\67\3\67\3\67\3\67\7\67\u0152\n\67\f\67\16\67\u0155\13"+
		"\67\3\67\3\67\3\67\3\67\38\38\38\38\78\u015f\n8\f8\168\u0162\138\38\3"+
		"8\38\38\38\39\59\u016a\n9\39\39\69\u016e\n9\r9\169\u016f\39\39\3:\3:\3"+
		":\3:\4\u0153\u0160\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27"+
		"\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33"+
		"\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63"+
		"e\64g\65i\66k\67m8o9q:s;\3\2\7\5\2C\\aac|\3\2\62;\4\2ZZzz\5\2\62;CHch"+
		"\5\2\13\f\17\17\"\"\2\u0181\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3"+
		"\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2"+
		"\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37"+
		"\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3"+
		"\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2"+
		"\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C"+
		"\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2"+
		"\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2"+
		"\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i"+
		"\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3u\3\2"+
		"\2\2\5z\3\2\2\2\7\u0080\3\2\2\2\t\u0086\3\2\2\2\13\u008e\3\2\2\2\r\u0091"+
		"\3\2\2\2\17\u0096\3\2\2\2\21\u009a\3\2\2\2\23\u00a0\3\2\2\2\25\u00a7\3"+
		"\2\2\2\27\u00ad\3\2\2\2\31\u00b6\3\2\2\2\33\u00be\3\2\2\2\35\u00c3\3\2"+
		"\2\2\37\u00c7\3\2\2\2!\u00ce\3\2\2\2#\u00d3\3\2\2\2%\u00da\3\2\2\2\'\u00e2"+
		"\3\2\2\2)\u00e4\3\2\2\2+\u00e6\3\2\2\2-\u00e8\3\2\2\2/\u00ea\3\2\2\2\61"+
		"\u00ec\3\2\2\2\63\u00ee\3\2\2\2\65\u00f0\3\2\2\2\67\u00f2\3\2\2\29\u00f4"+
		"\3\2\2\2;\u00f6\3\2\2\2=\u00f8\3\2\2\2?\u00fa\3\2\2\2A\u00fc\3\2\2\2C"+
		"\u00fe\3\2\2\2E\u0100\3\2\2\2G\u0103\3\2\2\2I\u0106\3\2\2\2K\u0108\3\2"+
		"\2\2M\u010a\3\2\2\2O\u010c\3\2\2\2Q\u010f\3\2\2\2S\u0112\3\2\2\2U\u0114"+
		"\3\2\2\2W\u0117\3\2\2\2Y\u011a\3\2\2\2[\u011d\3\2\2\2]\u0120\3\2\2\2_"+
		"\u0122\3\2\2\2a\u0129\3\2\2\2c\u012c\3\2\2\2e\u0130\3\2\2\2g\u0142\3\2"+
		"\2\2i\u0146\3\2\2\2k\u0148\3\2\2\2m\u014d\3\2\2\2o\u015a\3\2\2\2q\u016d"+
		"\3\2\2\2s\u0173\3\2\2\2uv\7V\2\2vw\7t\2\2wx\7w\2\2xy\7g\2\2y\4\3\2\2\2"+
		"z{\7H\2\2{|\7c\2\2|}\7n\2\2}~\7u\2\2~\177\7g\2\2\177\6\3\2\2\2\u0080\u0081"+
		"\7e\2\2\u0081\u0082\7n\2\2\u0082\u0083\7c\2\2\u0083\u0084\7u\2\2\u0084"+
		"\u0085\7u\2\2\u0085\b\3\2\2\2\u0086\u0087\7R\2\2\u0087\u0088\7t\2\2\u0088"+
		"\u0089\7q\2\2\u0089\u008a\7i\2\2\u008a\u008b\7t\2\2\u008b\u008c\7c\2\2"+
		"\u008c\u008d\7o\2\2\u008d\n\3\2\2\2\u008e\u008f\7k\2\2\u008f\u0090\7h"+
		"\2\2\u0090\f\3\2\2\2\u0091\u0092\7g\2\2\u0092\u0093\7n\2\2\u0093\u0094"+
		"\7u\2\2\u0094\u0095\7g\2\2\u0095\16\3\2\2\2\u0096\u0097\7h\2\2\u0097\u0098"+
		"\7q\2\2\u0098\u0099\7t\2\2\u0099\20\3\2\2\2\u009a\u009b\7y\2\2\u009b\u009c"+
		"\7j\2\2\u009c\u009d\7k\2\2\u009d\u009e\7n\2\2\u009e\u009f\7g\2\2\u009f"+
		"\22\3\2\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7v\2\2\u00a3"+
		"\u00a4\7w\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7p\2\2\u00a6\24\3\2\2\2\u00a7"+
		"\u00a8\7d\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7c\2\2"+
		"\u00ab\u00ac\7m\2\2\u00ac\26\3\2\2\2\u00ad\u00ae\7e\2\2\u00ae\u00af\7"+
		"q\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3"+
		"\7p\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7g\2\2\u00b5\30\3\2\2\2\u00b6\u00b7"+
		"\7d\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7n\2\2\u00ba"+
		"\u00bb\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7p\2\2\u00bd\32\3\2\2\2\u00be"+
		"\u00bf\7e\2\2\u00bf\u00c0\7j\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7t\2\2"+
		"\u00c2\34\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7"+
		"v\2\2\u00c6\36\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca"+
		"\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7i\2\2\u00cd"+
		" \3\2\2\2\u00ce\u00cf\7x\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7k\2\2\u00d1"+
		"\u00d2\7f\2\2\u00d2\"\3\2\2\2\u00d3\u00d4\7u\2\2\u00d4\u00d5\7v\2\2\u00d5"+
		"\u00d6\7t\2\2\u00d6\u00d7\7w\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9\7v\2\2"+
		"\u00d9$\3\2\2\2\u00da\u00db\7e\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7n\2"+
		"\2\u00dd\u00de\7n\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1"+
		"\7v\2\2\u00e1&\3\2\2\2\u00e2\u00e3\7=\2\2\u00e3(\3\2\2\2\u00e4\u00e5\7"+
		"}\2\2\u00e5*\3\2\2\2\u00e6\u00e7\7\177\2\2\u00e7,\3\2\2\2\u00e8\u00e9"+
		"\7]\2\2\u00e9.\3\2\2\2\u00ea\u00eb\7_\2\2\u00eb\60\3\2\2\2\u00ec\u00ed"+
		"\7*\2\2\u00ed\62\3\2\2\2\u00ee\u00ef\7+\2\2\u00ef\64\3\2\2\2\u00f0\u00f1"+
		"\7.\2\2\u00f1\66\3\2\2\2\u00f2\u00f3\7$\2\2\u00f38\3\2\2\2\u00f4\u00f5"+
		"\7)\2\2\u00f5:\3\2\2\2\u00f6\u00f7\7-\2\2\u00f7<\3\2\2\2\u00f8\u00f9\7"+
		"/\2\2\u00f9>\3\2\2\2\u00fa\u00fb\7,\2\2\u00fb@\3\2\2\2\u00fc\u00fd\7\61"+
		"\2\2\u00fdB\3\2\2\2\u00fe\u00ff\7\'\2\2\u00ffD\3\2\2\2\u0100\u0101\7("+
		"\2\2\u0101\u0102\7(\2\2\u0102F\3\2\2\2\u0103\u0104\7~\2\2\u0104\u0105"+
		"\7~\2\2\u0105H\3\2\2\2\u0106\u0107\7#\2\2\u0107J\3\2\2\2\u0108\u0109\7"+
		"@\2\2\u0109L\3\2\2\2\u010a\u010b\7>\2\2\u010bN\3\2\2\2\u010c\u010d\7@"+
		"\2\2\u010d\u010e\7?\2\2\u010eP\3\2\2\2\u010f\u0110\7>\2\2\u0110\u0111"+
		"\7?\2\2\u0111R\3\2\2\2\u0112\u0113\7?\2\2\u0113T\3\2\2\2\u0114\u0115\7"+
		"-\2\2\u0115\u0116\7?\2\2\u0116V\3\2\2\2\u0117\u0118\7/\2\2\u0118\u0119"+
		"\7?\2\2\u0119X\3\2\2\2\u011a\u011b\7?\2\2\u011b\u011c\7?\2\2\u011cZ\3"+
		"\2\2\2\u011d\u011e\7#\2\2\u011e\u011f\7?\2\2\u011f\\\3\2\2\2\u0120\u0121"+
		"\7\60\2\2\u0121^\3\2\2\2\u0122\u0126\5a\61\2\u0123\u0125\5i\65\2\u0124"+
		"\u0123\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2"+
		"\2\2\u0127`\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\t\2\2\2\u012ab\3\2"+
		"\2\2\u012b\u012d\t\3\2\2\u012c\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e"+
		"\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012fd\3\2\2\2\u0130\u0131\t\3\2\2"+
		"\u0131f\3\2\2\2\u0132\u0134\7$\2\2\u0133\u0135\5i\65\2\u0134\u0133\3\2"+
		"\2\2\u0135\u0136\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137"+
		"\u0138\3\2\2\2\u0138\u0139\7$\2\2\u0139\u0143\3\2\2\2\u013a\u013c\59\35"+
		"\2\u013b\u013d\5i\65\2\u013c\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013c"+
		"\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\59\35\2\u0141"+
		"\u0143\3\2\2\2\u0142\u0132\3\2\2\2\u0142\u013a\3\2\2\2\u0143h\3\2\2\2"+
		"\u0144\u0147\5a\61\2\u0145\u0147\5e\63\2\u0146\u0144\3\2\2\2\u0146\u0145"+
		"\3\2\2\2\u0147j\3\2\2\2\u0148\u0149\7\62\2\2\u0149\u014b\t\4\2\2\u014a"+
		"\u014c\t\5\2\2\u014b\u014a\3\2\2\2\u014cl\3\2\2\2\u014d\u014e\7\61\2\2"+
		"\u014e\u014f\7\61\2\2\u014f\u0153\3\2\2\2\u0150\u0152\13\2\2\2\u0151\u0150"+
		"\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0154\3\2\2\2\u0153\u0151\3\2\2\2\u0154"+
		"\u0156\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u0157\7\f\2\2\u0157\u0158\3\2"+
		"\2\2\u0158\u0159\b\67\2\2\u0159n\3\2\2\2\u015a\u015b\7\61\2\2\u015b\u015c"+
		"\7,\2\2\u015c\u0160\3\2\2\2\u015d\u015f\13\2\2\2\u015e\u015d\3\2\2\2\u015f"+
		"\u0162\3\2\2\2\u0160\u0161\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0163\3\2"+
		"\2\2\u0162\u0160\3\2\2\2\u0163\u0164\7,\2\2\u0164\u0165\7\61\2\2\u0165"+
		"\u0166\3\2\2\2\u0166\u0167\b8\2\2\u0167p\3\2\2\2\u0168\u016a\7\17\2\2"+
		"\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016e"+
		"\7\f\2\2\u016c\u016e\7\17\2\2\u016d\u0169\3\2\2\2\u016d\u016c\3\2\2\2"+
		"\u016e\u016f\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171"+
		"\3\2\2\2\u0171\u0172\b9\2\2\u0172r\3\2\2\2\u0173\u0174\t\6\2\2\u0174\u0175"+
		"\3\2\2\2\u0175\u0176\b:\2\2\u0176t\3\2\2\2\17\2\u0126\u012e\u0136\u013e"+
		"\u0142\u0146\u014b\u0153\u0160\u0169\u016d\u016f\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}