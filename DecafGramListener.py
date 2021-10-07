# Generated from DecafGram.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafGramParser import DecafGramParser
else:
    from DecafGramParser import DecafGramParser

# This class defines a complete listener for a parse tree produced by DecafGramParser.
class DecafGramListener(ParseTreeListener):

    # Enter a parse tree produced by DecafGramParser#program.
    def enterProgram(self, ctx:DecafGramParser.ProgramContext):
        pass

    # Exit a parse tree produced by DecafGramParser#program.
    def exitProgram(self, ctx:DecafGramParser.ProgramContext):
        pass


    # Enter a parse tree produced by DecafGramParser#declaration.
    def enterDeclaration(self, ctx:DecafGramParser.DeclarationContext):
        pass

    # Exit a parse tree produced by DecafGramParser#declaration.
    def exitDeclaration(self, ctx:DecafGramParser.DeclarationContext):
        pass


    # Enter a parse tree produced by DecafGramParser#vardeclr.
    def enterVardeclr(self, ctx:DecafGramParser.VardeclrContext):
        pass

    # Exit a parse tree produced by DecafGramParser#vardeclr.
    def exitVardeclr(self, ctx:DecafGramParser.VardeclrContext):
        pass


    # Enter a parse tree produced by DecafGramParser#field_declr.
    def enterField_declr(self, ctx:DecafGramParser.Field_declrContext):
        pass

    # Exit a parse tree produced by DecafGramParser#field_declr.
    def exitField_declr(self, ctx:DecafGramParser.Field_declrContext):
        pass


    # Enter a parse tree produced by DecafGramParser#array_id.
    def enterArray_id(self, ctx:DecafGramParser.Array_idContext):
        pass

    # Exit a parse tree produced by DecafGramParser#array_id.
    def exitArray_id(self, ctx:DecafGramParser.Array_idContext):
        pass


    # Enter a parse tree produced by DecafGramParser#field_var.
    def enterField_var(self, ctx:DecafGramParser.Field_varContext):
        pass

    # Exit a parse tree produced by DecafGramParser#field_var.
    def exitField_var(self, ctx:DecafGramParser.Field_varContext):
        pass


    # Enter a parse tree produced by DecafGramParser#var_id.
    def enterVar_id(self, ctx:DecafGramParser.Var_idContext):
        pass

    # Exit a parse tree produced by DecafGramParser#var_id.
    def exitVar_id(self, ctx:DecafGramParser.Var_idContext):
        pass


    # Enter a parse tree produced by DecafGramParser#struct_declr.
    def enterStruct_declr(self, ctx:DecafGramParser.Struct_declrContext):
        pass

    # Exit a parse tree produced by DecafGramParser#struct_declr.
    def exitStruct_declr(self, ctx:DecafGramParser.Struct_declrContext):
        pass


    # Enter a parse tree produced by DecafGramParser#method_declr.
    def enterMethod_declr(self, ctx:DecafGramParser.Method_declrContext):
        pass

    # Exit a parse tree produced by DecafGramParser#method_declr.
    def exitMethod_declr(self, ctx:DecafGramParser.Method_declrContext):
        pass


    # Enter a parse tree produced by DecafGramParser#return_type.
    def enterReturn_type(self, ctx:DecafGramParser.Return_typeContext):
        pass

    # Exit a parse tree produced by DecafGramParser#return_type.
    def exitReturn_type(self, ctx:DecafGramParser.Return_typeContext):
        pass


    # Enter a parse tree produced by DecafGramParser#block.
    def enterBlock(self, ctx:DecafGramParser.BlockContext):
        pass

    # Exit a parse tree produced by DecafGramParser#block.
    def exitBlock(self, ctx:DecafGramParser.BlockContext):
        pass


    # Enter a parse tree produced by DecafGramParser#statement_assign.
    def enterStatement_assign(self, ctx:DecafGramParser.Statement_assignContext):
        pass

    # Exit a parse tree produced by DecafGramParser#statement_assign.
    def exitStatement_assign(self, ctx:DecafGramParser.Statement_assignContext):
        pass


    # Enter a parse tree produced by DecafGramParser#statement_methodcall.
    def enterStatement_methodcall(self, ctx:DecafGramParser.Statement_methodcallContext):
        pass

    # Exit a parse tree produced by DecafGramParser#statement_methodcall.
    def exitStatement_methodcall(self, ctx:DecafGramParser.Statement_methodcallContext):
        pass


    # Enter a parse tree produced by DecafGramParser#statement_if.
    def enterStatement_if(self, ctx:DecafGramParser.Statement_ifContext):
        pass

    # Exit a parse tree produced by DecafGramParser#statement_if.
    def exitStatement_if(self, ctx:DecafGramParser.Statement_ifContext):
        pass


    # Enter a parse tree produced by DecafGramParser#statement_while.
    def enterStatement_while(self, ctx:DecafGramParser.Statement_whileContext):
        pass

    # Exit a parse tree produced by DecafGramParser#statement_while.
    def exitStatement_while(self, ctx:DecafGramParser.Statement_whileContext):
        pass


    # Enter a parse tree produced by DecafGramParser#statement_return.
    def enterStatement_return(self, ctx:DecafGramParser.Statement_returnContext):
        pass

    # Exit a parse tree produced by DecafGramParser#statement_return.
    def exitStatement_return(self, ctx:DecafGramParser.Statement_returnContext):
        pass


    # Enter a parse tree produced by DecafGramParser#statement_for.
    def enterStatement_for(self, ctx:DecafGramParser.Statement_forContext):
        pass

    # Exit a parse tree produced by DecafGramParser#statement_for.
    def exitStatement_for(self, ctx:DecafGramParser.Statement_forContext):
        pass


    # Enter a parse tree produced by DecafGramParser#statement_break.
    def enterStatement_break(self, ctx:DecafGramParser.Statement_breakContext):
        pass

    # Exit a parse tree produced by DecafGramParser#statement_break.
    def exitStatement_break(self, ctx:DecafGramParser.Statement_breakContext):
        pass


    # Enter a parse tree produced by DecafGramParser#method_call.
    def enterMethod_call(self, ctx:DecafGramParser.Method_callContext):
        pass

    # Exit a parse tree produced by DecafGramParser#method_call.
    def exitMethod_call(self, ctx:DecafGramParser.Method_callContext):
        pass


    # Enter a parse tree produced by DecafGramParser#expr_presedencia2.
    def enterExpr_presedencia2(self, ctx:DecafGramParser.Expr_presedencia2Context):
        pass

    # Exit a parse tree produced by DecafGramParser#expr_presedencia2.
    def exitExpr_presedencia2(self, ctx:DecafGramParser.Expr_presedencia2Context):
        pass


    # Enter a parse tree produced by DecafGramParser#expr_literal.
    def enterExpr_literal(self, ctx:DecafGramParser.Expr_literalContext):
        pass

    # Exit a parse tree produced by DecafGramParser#expr_literal.
    def exitExpr_literal(self, ctx:DecafGramParser.Expr_literalContext):
        pass


    # Enter a parse tree produced by DecafGramParser#expr_location.
    def enterExpr_location(self, ctx:DecafGramParser.Expr_locationContext):
        pass

    # Exit a parse tree produced by DecafGramParser#expr_location.
    def exitExpr_location(self, ctx:DecafGramParser.Expr_locationContext):
        pass


    # Enter a parse tree produced by DecafGramParser#expr_presedencia1.
    def enterExpr_presedencia1(self, ctx:DecafGramParser.Expr_presedencia1Context):
        pass

    # Exit a parse tree produced by DecafGramParser#expr_presedencia1.
    def exitExpr_presedencia1(self, ctx:DecafGramParser.Expr_presedencia1Context):
        pass


    # Enter a parse tree produced by DecafGramParser#expr_menos.
    def enterExpr_menos(self, ctx:DecafGramParser.Expr_menosContext):
        pass

    # Exit a parse tree produced by DecafGramParser#expr_menos.
    def exitExpr_menos(self, ctx:DecafGramParser.Expr_menosContext):
        pass


    # Enter a parse tree produced by DecafGramParser#expr_normal.
    def enterExpr_normal(self, ctx:DecafGramParser.Expr_normalContext):
        pass

    # Exit a parse tree produced by DecafGramParser#expr_normal.
    def exitExpr_normal(self, ctx:DecafGramParser.Expr_normalContext):
        pass


    # Enter a parse tree produced by DecafGramParser#expr_parentesis.
    def enterExpr_parentesis(self, ctx:DecafGramParser.Expr_parentesisContext):
        pass

    # Exit a parse tree produced by DecafGramParser#expr_parentesis.
    def exitExpr_parentesis(self, ctx:DecafGramParser.Expr_parentesisContext):
        pass


    # Enter a parse tree produced by DecafGramParser#expr_methodCall.
    def enterExpr_methodCall(self, ctx:DecafGramParser.Expr_methodCallContext):
        pass

    # Exit a parse tree produced by DecafGramParser#expr_methodCall.
    def exitExpr_methodCall(self, ctx:DecafGramParser.Expr_methodCallContext):
        pass


    # Enter a parse tree produced by DecafGramParser#expr_negacion.
    def enterExpr_negacion(self, ctx:DecafGramParser.Expr_negacionContext):
        pass

    # Exit a parse tree produced by DecafGramParser#expr_negacion.
    def exitExpr_negacion(self, ctx:DecafGramParser.Expr_negacionContext):
        pass


    # Enter a parse tree produced by DecafGramParser#location.
    def enterLocation(self, ctx:DecafGramParser.LocationContext):
        pass

    # Exit a parse tree produced by DecafGramParser#location.
    def exitLocation(self, ctx:DecafGramParser.LocationContext):
        pass


    # Enter a parse tree produced by DecafGramParser#int_literal.
    def enterInt_literal(self, ctx:DecafGramParser.Int_literalContext):
        pass

    # Exit a parse tree produced by DecafGramParser#int_literal.
    def exitInt_literal(self, ctx:DecafGramParser.Int_literalContext):
        pass


    # Enter a parse tree produced by DecafGramParser#char_literal.
    def enterChar_literal(self, ctx:DecafGramParser.Char_literalContext):
        pass

    # Exit a parse tree produced by DecafGramParser#char_literal.
    def exitChar_literal(self, ctx:DecafGramParser.Char_literalContext):
        pass


    # Enter a parse tree produced by DecafGramParser#bool_literal.
    def enterBool_literal(self, ctx:DecafGramParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by DecafGramParser#bool_literal.
    def exitBool_literal(self, ctx:DecafGramParser.Bool_literalContext):
        pass


    # Enter a parse tree produced by DecafGramParser#rel_op.
    def enterRel_op(self, ctx:DecafGramParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DecafGramParser#rel_op.
    def exitRel_op(self, ctx:DecafGramParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DecafGramParser#eq_op.
    def enterEq_op(self, ctx:DecafGramParser.Eq_opContext):
        pass

    # Exit a parse tree produced by DecafGramParser#eq_op.
    def exitEq_op(self, ctx:DecafGramParser.Eq_opContext):
        pass


    # Enter a parse tree produced by DecafGramParser#cond_op.
    def enterCond_op(self, ctx:DecafGramParser.Cond_opContext):
        pass

    # Exit a parse tree produced by DecafGramParser#cond_op.
    def exitCond_op(self, ctx:DecafGramParser.Cond_opContext):
        pass


    # Enter a parse tree produced by DecafGramParser#literal.
    def enterLiteral(self, ctx:DecafGramParser.LiteralContext):
        pass

    # Exit a parse tree produced by DecafGramParser#literal.
    def exitLiteral(self, ctx:DecafGramParser.LiteralContext):
        pass


    # Enter a parse tree produced by DecafGramParser#arith_op.
    def enterArith_op(self, ctx:DecafGramParser.Arith_opContext):
        pass

    # Exit a parse tree produced by DecafGramParser#arith_op.
    def exitArith_op(self, ctx:DecafGramParser.Arith_opContext):
        pass


    # Enter a parse tree produced by DecafGramParser#var_type.
    def enterVar_type(self, ctx:DecafGramParser.Var_typeContext):
        pass

    # Exit a parse tree produced by DecafGramParser#var_type.
    def exitVar_type(self, ctx:DecafGramParser.Var_typeContext):
        pass


    # Enter a parse tree produced by DecafGramParser#assign_op.
    def enterAssign_op(self, ctx:DecafGramParser.Assign_opContext):
        pass

    # Exit a parse tree produced by DecafGramParser#assign_op.
    def exitAssign_op(self, ctx:DecafGramParser.Assign_opContext):
        pass


    # Enter a parse tree produced by DecafGramParser#method_name.
    def enterMethod_name(self, ctx:DecafGramParser.Method_nameContext):
        pass

    # Exit a parse tree produced by DecafGramParser#method_name.
    def exitMethod_name(self, ctx:DecafGramParser.Method_nameContext):
        pass



del DecafGramParser