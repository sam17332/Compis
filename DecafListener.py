# Generated from Decaf.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete listener for a parse tree produced by DecafParser.
class DecafListener(ParseTreeListener):

    # Enter a parse tree produced by DecafParser#program.
    def enterProgram(self, ctx:DecafParser.ProgramContext):
        pass

    # Exit a parse tree produced by DecafParser#program.
    def exitProgram(self, ctx:DecafParser.ProgramContext):
        pass


    # Enter a parse tree produced by DecafParser#declaration.
    def enterDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#declaration.
    def exitDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#vardeclr.
    def enterVardeclr(self, ctx:DecafParser.VardeclrContext):
        pass

    # Exit a parse tree produced by DecafParser#vardeclr.
    def exitVardeclr(self, ctx:DecafParser.VardeclrContext):
        pass


    # Enter a parse tree produced by DecafParser#field_declr.
    def enterField_declr(self, ctx:DecafParser.Field_declrContext):
        pass

    # Exit a parse tree produced by DecafParser#field_declr.
    def exitField_declr(self, ctx:DecafParser.Field_declrContext):
        pass


    # Enter a parse tree produced by DecafParser#array_id.
    def enterArray_id(self, ctx:DecafParser.Array_idContext):
        pass

    # Exit a parse tree produced by DecafParser#array_id.
    def exitArray_id(self, ctx:DecafParser.Array_idContext):
        pass


    # Enter a parse tree produced by DecafParser#field_var.
    def enterField_var(self, ctx:DecafParser.Field_varContext):
        pass

    # Exit a parse tree produced by DecafParser#field_var.
    def exitField_var(self, ctx:DecafParser.Field_varContext):
        pass


    # Enter a parse tree produced by DecafParser#var_id.
    def enterVar_id(self, ctx:DecafParser.Var_idContext):
        pass

    # Exit a parse tree produced by DecafParser#var_id.
    def exitVar_id(self, ctx:DecafParser.Var_idContext):
        pass


    # Enter a parse tree produced by DecafParser#struct_declr.
    def enterStruct_declr(self, ctx:DecafParser.Struct_declrContext):
        pass

    # Exit a parse tree produced by DecafParser#struct_declr.
    def exitStruct_declr(self, ctx:DecafParser.Struct_declrContext):
        pass


    # Enter a parse tree produced by DecafParser#method_declr.
    def enterMethod_declr(self, ctx:DecafParser.Method_declrContext):
        pass

    # Exit a parse tree produced by DecafParser#method_declr.
    def exitMethod_declr(self, ctx:DecafParser.Method_declrContext):
        pass


    # Enter a parse tree produced by DecafParser#return_type.
    def enterReturn_type(self, ctx:DecafParser.Return_typeContext):
        pass

    # Exit a parse tree produced by DecafParser#return_type.
    def exitReturn_type(self, ctx:DecafParser.Return_typeContext):
        pass


    # Enter a parse tree produced by DecafParser#block.
    def enterBlock(self, ctx:DecafParser.BlockContext):
        pass

    # Exit a parse tree produced by DecafParser#block.
    def exitBlock(self, ctx:DecafParser.BlockContext):
        pass


    # Enter a parse tree produced by DecafParser#statement.
    def enterStatement(self, ctx:DecafParser.StatementContext):
        pass

    # Exit a parse tree produced by DecafParser#statement.
    def exitStatement(self, ctx:DecafParser.StatementContext):
        pass


    # Enter a parse tree produced by DecafParser#method_call_inter.
    def enterMethod_call_inter(self, ctx:DecafParser.Method_call_interContext):
        pass

    # Exit a parse tree produced by DecafParser#method_call_inter.
    def exitMethod_call_inter(self, ctx:DecafParser.Method_call_interContext):
        pass


    # Enter a parse tree produced by DecafParser#method_call.
    def enterMethod_call(self, ctx:DecafParser.Method_callContext):
        pass

    # Exit a parse tree produced by DecafParser#method_call.
    def exitMethod_call(self, ctx:DecafParser.Method_callContext):
        pass


    # Enter a parse tree produced by DecafParser#expr.
    def enterExpr(self, ctx:DecafParser.ExprContext):
        pass

    # Exit a parse tree produced by DecafParser#expr.
    def exitExpr(self, ctx:DecafParser.ExprContext):
        pass


    # Enter a parse tree produced by DecafParser#literal.
    def enterLiteral(self, ctx:DecafParser.LiteralContext):
        pass

    # Exit a parse tree produced by DecafParser#literal.
    def exitLiteral(self, ctx:DecafParser.LiteralContext):
        pass


    # Enter a parse tree produced by DecafParser#location.
    def enterLocation(self, ctx:DecafParser.LocationContext):
        pass

    # Exit a parse tree produced by DecafParser#location.
    def exitLocation(self, ctx:DecafParser.LocationContext):
        pass


    # Enter a parse tree produced by DecafParser#callout_arg.
    def enterCallout_arg(self, ctx:DecafParser.Callout_argContext):
        pass

    # Exit a parse tree produced by DecafParser#callout_arg.
    def exitCallout_arg(self, ctx:DecafParser.Callout_argContext):
        pass


    # Enter a parse tree produced by DecafParser#int_literal.
    def enterInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#int_literal.
    def exitInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#string_literal.
    def enterString_literal(self, ctx:DecafParser.String_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#string_literal.
    def exitString_literal(self, ctx:DecafParser.String_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#bool_literal.
    def enterBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#bool_literal.
    def exitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#rel_op.
    def enterRel_op(self, ctx:DecafParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DecafParser#rel_op.
    def exitRel_op(self, ctx:DecafParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DecafParser#eq_op.
    def enterEq_op(self, ctx:DecafParser.Eq_opContext):
        pass

    # Exit a parse tree produced by DecafParser#eq_op.
    def exitEq_op(self, ctx:DecafParser.Eq_opContext):
        pass


    # Enter a parse tree produced by DecafParser#cond_op.
    def enterCond_op(self, ctx:DecafParser.Cond_opContext):
        pass

    # Exit a parse tree produced by DecafParser#cond_op.
    def exitCond_op(self, ctx:DecafParser.Cond_opContext):
        pass


    # Enter a parse tree produced by DecafParser#bin_op.
    def enterBin_op(self, ctx:DecafParser.Bin_opContext):
        pass

    # Exit a parse tree produced by DecafParser#bin_op.
    def exitBin_op(self, ctx:DecafParser.Bin_opContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op.
    def enterArith_op(self, ctx:DecafParser.Arith_opContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op.
    def exitArith_op(self, ctx:DecafParser.Arith_opContext):
        pass


    # Enter a parse tree produced by DecafParser#var_type.
    def enterVar_type(self, ctx:DecafParser.Var_typeContext):
        pass

    # Exit a parse tree produced by DecafParser#var_type.
    def exitVar_type(self, ctx:DecafParser.Var_typeContext):
        pass


    # Enter a parse tree produced by DecafParser#assign_op.
    def enterAssign_op(self, ctx:DecafParser.Assign_opContext):
        pass

    # Exit a parse tree produced by DecafParser#assign_op.
    def exitAssign_op(self, ctx:DecafParser.Assign_opContext):
        pass


    # Enter a parse tree produced by DecafParser#method_name.
    def enterMethod_name(self, ctx:DecafParser.Method_nameContext):
        pass

    # Exit a parse tree produced by DecafParser#method_name.
    def exitMethod_name(self, ctx:DecafParser.Method_nameContext):
        pass



del DecafParser