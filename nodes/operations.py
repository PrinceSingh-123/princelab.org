from PyQt5.QtCore import *
from calc_conf import *
from calc_node_base import *
from nodeeditor.utils import dumpException


# My custom function
@register_node(OP_NODE_SQR)
class CalcNode_sqr(CalcNode):
    icon = "icons/add.png"
    op_code = OP_NODE_SQR
    op_title = "SQR"
    content_label = "**"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1,input2):    
        return input1 * input1

@register_node(OP_NODE_ADD)
class CalcNode_Add(CalcNode):
    icon = "icons/add.png"
    op_code = OP_NODE_ADD
    op_title = "Add"
    content_label = "+"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        return int(input1) + int(input2)

@register_node(OP_NODE_SUB)
class CalcNode_Sub(CalcNode):
    icon = "icons/sub.png"
    op_code = OP_NODE_SUB
    op_title = "Substract"
    content_label = "-"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        return int(input1) - int(input2)

@register_node(OP_NODE_MUL)
class CalcNode_Mul(CalcNode):
    icon = "icons/mul.png"
    op_code = OP_NODE_MUL
    op_title = "Multiply"
    content_label = "*"
    content_label_objname = "calc_node_mul"

    def evalOperation(self, input1, input2):
        print('foo')
        return int(input1) * int(input2)

@register_node(OP_NODE_DIV)
class CalcNode_Div(CalcNode):
    icon = "icons/divide.png"
    op_code = OP_NODE_DIV
    op_title = "Divide"
    content_label = "/"
    content_label_objname = "calc_node_div"

    def evalOperation(self, input1, input2):
        return int(input1) / int(input2)

# way how to register by function call
# register_node_now(OP_NODE_ADD, CalcNode_Add)