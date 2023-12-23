# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, too-few-public-methods, redefined-builtin

from __future__ import annotations
import argparse
import sys
from typing import Optional
from typing import List
from ply import lex
from ply import yacc

IN = "in"
ACCEPT = "A"
REJECT = "R"

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--debug', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.set_defaults(verbose=False, debug=False, part2=False)
args = parser.parse_args()

if args.debug:
    args.verbose = True

tokens = (
    'WORD',
    'XCOOL',
    'MUSICAL',
    'AERODYNAMIC',
    'SHINY',
    'GT',
    'EQ',
    'LT',
    'NUMBER',
    'COLON',
    'OPEN_BRACE',
    'CLOSE_BRACE',
    'COMMA',
    'NEWLINE',
)

reserved = {
    'x': 'XCOOL',
    'm': 'MUSICAL',
    'a': 'AERODYNAMIC',
    's': 'SHINY',
}

t_XCOOL = r'x'
t_MUSICAL = r'm'
t_AERODYNAMIC = r'a'
t_SHINY = r's'

t_GT = r'>'
t_EQ = r'='
t_LT = r'<'
t_COLON = r':'
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACE = r'\}'
t_COMMA = r','

GT = '>'
LT = '<'

def t_WORD(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value, 'WORD')
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


def t_error(t):
    raise ValueError(f"Invalid character: {t.value[0]}")


def p_file(p):
    'file : workflow_definition_list part_list'
    p[0] = File(p[1], p[2])


def p_workflow_definition_list_recursion(p):
    'workflow_definition_list : workflow_definition_list workflow_definition'
    p[0] = p[1] + [p[2]]


def p_workflow_definition_list_terminator(p):
    'workflow_definition_list : workflow_definition'
    p[0] = [p[1]]


def p_workflow_definition(p):
    'workflow_definition : workflow_name OPEN_BRACE rule_list CLOSE_BRACE NEWLINE'
    p[0] = Workflow(p[1], p[3])


def p_workflow_name(p):
    'workflow_name : WORD'
    p[0] = p[1]


def p_rule_list_recursion(p):
    'rule_list : rule_list COMMA rule'
    p[0] = p[1] + [p[3]]


def p_rule_list_terminator(p):
    'rule_list : rule'
    p[0] = [p[1]]


def p_rule_with_comparison(p):
    'rule : comparison COLON workflow_name'
    p[0] = Rule(p[3], p[1])


def p_rule_default(p):
    'rule : workflow_name'
    p[0] = Rule(p[1])


def p_comparison(p):
    'comparison : property compare_operator NUMBER'
    p[0] = Comparison(p[1], p[2], p[3])


def p_property_x(p):
    'property : XCOOL'
    p[0] = p[1]


def p_property_m(p):
    'property : MUSICAL'
    p[0] = p[1]


def p_property_a(p):
    'property : AERODYNAMIC'
    p[0] = p[1]


def p_property_s(p):
    'property : SHINY'
    p[0] = p[1]


def p_compare_operator_gt(p):
    'compare_operator : GT'
    p[0] = p[1]


def p_compare_operator_lt(p):
    'compare_operator : LT'
    p[0] = p[1]


def p_part_list_recursion(p):
    'part_list : part_list part'
    p[0] = p[1] + [p[2]]


def p_part_list_termination(p):
    'part_list : part'
    p[0] = [p[1]]


def p_part(p):
    'part : OPEN_BRACE rating_list CLOSE_BRACE NEWLINE'
    p[0] = Part(p[2])


def p_rating_list_recursion(p):
    "rating_list : rating_list COMMA rating"
    p[0] = p[1] + [p[3]]


def p_rating_list_termination(p):
    "rating_list : rating"
    p[0] = [p[1]]


def p_rating(p):
    "rating : property EQ NUMBER"
    p[0] = Rating(p[1], p[3])


def p_error(p):
    raise ValueError(
        f"Syntax error {p.type} '{p.value}' at line {p.lineno}, "
        f"column {find_column(p.lexer.lexdata, p)}")


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


class File:
    def __init__(self, workflows: List[Workflow], parts: List[Part]) -> None:
        self.workflows = workflows
        self.parts = parts


class Workflow:
    def __init__(self, name: str, rules: list[Rule]) -> None:
        self.name = name
        self.rules = rules

    def __str__(self) -> str:
        return f'{self.name}{{{",".join([str(rule) for rule in self.rules])}}}'

    def __repr__(self) -> str:
        return self.__str__()


class Rule:
    def __init__(self, workflow: str, comparison: Optional[Comparison] = None) -> None:
        self.workflow = workflow
        self.comparison = comparison

    def __str__(self) -> str:
        if self.comparison is None:
            return f'{self.workflow}'
        return f'{self.comparison}:{self.workflow}'

    def __repr__(self) -> str:
        return self.__str__()


class Comparison:
    def __init__(self, property: str, operator: str, value: int) -> None:
        self.property = property
        self.operator = operator
        self.value = value

    def __str__(self) -> str:
        return f'{self.property}{self.operator}{self.value}'

    def __repr__(self) -> str:
        return self.__str__()


class Part:
    def __init__(self, ratings: List[Rating]) -> None:
        self.ratings = ratings

    def __str__(self) -> str:
        return f'{{{",".join([str(rating) for rating in self.ratings])}}}'

    def __repr__(self) -> str:
        return self.__str__()


class Rating:
    def __init__(self, property: str, value: int) -> None:
        self.property = property
        self.value = value

    def __str__(self) -> str:
        return f'{self.property}={self.value}'

    def __repr__(self) -> str:
        return self.__str__()


class Engine:
    def __init__(self, workflows: List[Workflow]) -> None:
        self.workflows = {workflow.name: workflow for workflow in workflows}
    
    def accept(self, part: Part) -> bool:
        workflow = IN
        while workflow != ACCEPT and workflow != REJECT:
            workflow = self.process_workflow(part, workflow)
        return workflow == ACCEPT
    
    def process_workflow(self, part: Part, workflow_name: str) -> str:
        workflow = self.workflows[workflow_name]
        for rule in workflow.rules:
            if rule.comparison is None:
                return rule.workflow
            if self.process_comparison(part, rule.comparison):
                return rule.workflow
        return REJECT
    
    def process_comparison(self, part: Part, comparison: Comparison) -> bool:
        for rating in part.ratings:
            if rating.property == comparison.property:
                if comparison.operator == GT:
                    return rating.value > comparison.value
                if comparison.operator == LT:
                    return rating.value < comparison.value
                raise ValueError(f'Unknown operator {comparison.operator}')
        return False

lexer = lex.lex()
parser = yacc.yacc()
file = parser.parse(sys.stdin.read())
engine = Engine(file.workflows)

if not args.part2:
    accepted_parts = [part for part in file.parts if engine.accept(part)]
    ratings_total = sum([rating.value for part in accepted_parts for rating in part.ratings])
    print(ratings_total)
